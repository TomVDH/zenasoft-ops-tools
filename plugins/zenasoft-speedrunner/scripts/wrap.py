#!/usr/bin/env python3
"""wrap.py: package one Speedrunner run for Marketing Operations.

    python3 <plugin>/scripts/wrap.py output/<brand>-<slug>            # files, then zip
    python3 <plugin>/scripts/wrap.py output/<brand>-<slug> --no-zip   # files only

Reads the run folder and the brand's tokens.css. Writes the preview, PLACEHOLDERS.md,
FONTS.md and README.md. Refuses to zip without MANIFEST.md and the body file.
Stdlib only. Prints the zip path as its last line.
"""
import pathlib
import re
import sys
import zipfile

PLUGIN = pathlib.Path(__file__).resolve().parent.parent
BRANDS = PLUGIN / "brands"
SHELL = PLUGIN / "shared" / "preview-shell.md"


def die(msg):
    print("wrap: " + msg)
    sys.exit(2)


def brand_for(folder_name):
    """Longest brand slug that prefixes the run folder name."""
    slugs = sorted((d.name for d in BRANDS.iterdir() if (d / "tokens.css").exists()), key=len, reverse=True)
    for s in slugs:
        if folder_name == s or folder_name.startswith(s + "-"):
            return s
    return None


def root_block(tokens):
    m = re.search(r":root\s*\{", tokens)
    if not m:
        die("tokens.css has no :root block")
    depth, i = 0, m.start()
    for j in range(m.end() - 1, len(tokens)):
        depth += {"{": 1, "}": -1}.get(tokens[j], 0)
        if depth == 0:
            return tokens[i:j + 1]
    die("tokens.css :root block never closes")


def families(tokens, prefix):
    """Quoted family names from the font tokens. Google Fonts names carry a capital."""
    names = []
    for tok in ("font-headline", "font-body"):
        m = re.search(r"--%s-%s:\s*([^;]+);" % (prefix, tok), tokens)
        if m:
            names += re.findall(r"'([^']+)'", m.group(1))
    google, other = [], []
    for n in names:
        (google if re.search(r"[A-Z]", n) else other).append(n)
    return list(dict.fromkeys(google)), list(dict.fromkeys(other))


def font_link(google):
    fam = "&".join("family=%s:wght@400;500;600;700;800" % g.replace(" ", "+") for g in google)
    return "https://fonts.googleapis.com/css2?%s&display=swap" % fam


def build_preview(body, tokens, prefix, title, google):
    tpl = re.findall(r"```html\n(.*?)```", SHELL.read_text(encoding="utf-8"), re.S)
    if not tpl:
        die("shared/preview-shell.md has no html template")
    html = tpl[0]
    html = re.sub(r":root \{\n  …\n\}", lambda _: root_block(tokens), html, count=1)
    html = re.sub(r'href="https://fonts\.googleapis\.com/css2\?[^"]*"',
                  lambda _: 'href="%s"' % font_link(google), html, count=1)
    html = html.replace("<title>Preview: {Brand} {Page Name}</title>", "<title>Preview: %s</title>" % title)
    html = html.replace("{p}", prefix)
    html = re.sub(r"<!-- B\. the body file, pasted whole -->\n…", lambda _: "<!-- B. the body file, pasted whole -->\n" + body, html, count=1)
    return html


def placeholders(body):
    rows = re.findall(r"<!--\s*\[PLACEHOLDER:\s*([a-z0-9-]+)\]\s*(.*?)\s*-->", body)
    out = ["# Empty slots in this page", "",
           "Each slot shows as a dashed box in the preview. Marketing Operations fills it at install.", ""]
    if not rows:
        out.append("No empty image slots. Every image is in `assets/`.")
    else:
        out += ["| Slot | What goes there |", "|---|---|"]
        out += ["| `%s` | %s |" % (slug, desc) for slug, desc in rows]
    if 'class="zt-hsform"' in body:
        out += ["", "The form container (`zt-hsform`) is a slot too. Its fields are in MANIFEST.md."]
    if 'class="zt-scheduler"' in body:
        out += ["", "The booking calendar (`zt-scheduler`) is a slot. Its fields are in MANIFEST.md."]
    return "\n".join(out) + "\n"


def fonts_md(google, other, kind):
    out = ["# Fonts", ""]
    if kind == "page":
        out.append("The preview loads these from Google Fonts. On the portal the brand theme loads them; the body file adds no font link.")
    else:
        out.append("The email carries its own font link. Marketing Operations changes nothing here.")
    out.append("")
    for g in google:
        out.append("- %s: https://fonts.google.com/specimen/%s" % (g, g.replace(" ", "+")))
    if google:
        out += ["", "One link for all of them:", "", "    " + font_link(google)]
    for o in other:
        out += ["", "- %s is not on Google Fonts. The preview shows the next family in the stack; the portal theme loads the real one." % o]
    return "\n".join(out) + "\n"


def readme(review_file, kind):
    what = "page" if kind == "page" else "email"
    return ("1. Open `%s` in your browser to review the %s.\n"
            "2. When it is right, send the whole zip to Marketing Operations.\n"
            "3. Do not edit the %s file. Marketing Operations installs it as it is.\n"
            % (review_file, what, "body" if kind == "page" else "email"))


def main(argv):
    if not argv or argv[0].startswith("-"):
        die("usage: wrap.py output/<brand>-<slug> [--no-zip]")
    run = pathlib.Path(argv[0]).resolve()
    no_zip = "--no-zip" in argv
    if not run.is_dir():
        die("no run folder at %s" % run)
    name = run.name
    brand = brand_for(name)
    if not brand:
        die("run folder %s does not start with a brand slug in brands/" % name)
    tokens = (BRANDS / brand / "tokens.css").read_text(encoding="utf-8")
    m = re.search(r"PREFIX ON THE PORTAL: --([a-z0-9]+)-\*", tokens)
    if not m:
        die("tokens.css for %s carries no prefix line" % brand)
    prefix = m.group(1)

    body_files = sorted(run.glob("*-body.html"))
    email_files = sorted(run.glob("*-email.html"))
    if body_files and email_files:
        die("both a -body.html and an -email.html in %s; one run, one deliverable" % name)
    if not body_files and not email_files:
        die("no %s-body.html or %s-email.html in %s; build first" % (name, name, name))
    kind = "page" if body_files else "email"
    src = (body_files or email_files)[0]
    body = src.read_text(encoding="utf-8")
    google, other = families(tokens, prefix)

    (run / "assets").mkdir(exist_ok=True)
    (run / "fonts").mkdir(exist_ok=True)
    written = []
    if kind == "page":
        title = "%s %s" % (brand, name[len(brand) + 1:].replace("-", " "))
        preview = run / ("%s-preview.html" % name)
        preview.write_text(build_preview(body, tokens, prefix, title, google), encoding="utf-8")
        written.append(preview.name)
        review = preview.name
    else:
        review = src.name
    (run / "assets" / "PLACEHOLDERS.md").write_text(placeholders(body), encoding="utf-8")
    (run / "fonts" / "FONTS.md").write_text(fonts_md(google, other, kind), encoding="utf-8")
    (run / "README.md").write_text(readme(review, kind), encoding="utf-8")
    written += ["assets/PLACEHOLDERS.md", "fonts/FONTS.md", "README.md"]
    print("wrap: wrote " + ", ".join(written))

    if not (run / "MANIFEST.md").exists():
        print("wrap: MANIFEST.md is missing. Write it, then run wrap again.")
        sys.exit(1 if not no_zip else 0)
    if no_zip:
        print("wrap: files ready in %s (no zip requested)" % run.name)
        return

    zpath = run.parent / (name + ".zip")
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(run.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, f.relative_to(run.parent))
    count = len(zipfile.ZipFile(zpath).namelist())
    print("wrap: %d files zipped" % count)
    try:
        shown = zpath.relative_to(pathlib.Path.cwd())
    except ValueError:
        shown = zpath
    print(str(shown))


if __name__ == "__main__":
    main(sys.argv[1:])
