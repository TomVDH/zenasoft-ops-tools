---
name: speedrun-wrap
description: Zip the finished page or email for Marketing Operations. Use when the marketer says done, asks for the files, or asks for the zip. Runs the Deliver step from /page-speedrun or /email-speedrun.
user-invocable: true
---

# ZenaSoft Speedrunner: wrap

Package the run the marketer has reviewed. Build nothing new here.

## Before you zip

1. Find the run folder: `output/{brand}-{slug}/`. One run per session, so there is one.
   None? Say: "Nothing is built yet. Type `/page-speedrun` or `/email-speedrun` first."
2. The marketer must have opened the review file and confirmed it. Not confirmed? Say:
   "Open `{brand}-{slug}-preview.html` (or the email file) in your browser and check it
   against your brief first. Say done and I zip it." Then stop.
3. Check that every file the run needs is in the folder. A page: `-body.html`,
   `-preview.html`, `assets/` with `PLACEHOLDERS.md`, `fonts/FONTS.md`, `MANIFEST.md`,
   `README.md`. An email: `-email.html` and the same folders and files, no preview.
   A file is missing? Write it now from the run, then continue.
4. The preview must match the body. Rebuild it from the body if the body changed after
   the last preview (see `shared/preview-shell.md`).

## Zip

Run the packager. The plugin folder is the one that holds `skills/`, `shared/`, `brands/`
and `scripts/`; Claude Code exposes it as `${CLAUDE_PLUGIN_ROOT}`:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/wrap.py" output/{brand}-{slug}
```

It rebuilds the preview and the small files, refuses without `MANIFEST.md`, zips with
Python alone, and prints the zip path. Done: tell the marketer. Only if `python3` is not
available, do it by hand, from the `output/` folder:

```
zip -r {brand}-{slug}.zip {brand}-{slug}
```

If `zip` is not found: `python3 -m zipfile -c {brand}-{slug}.zip {brand}-{slug}`
If neither runs (Windows PowerShell): `Compress-Archive -Path {brand}-{slug} -DestinationPath {brand}-{slug}.zip`

Print the zip path as the last line of your message, on its own line:
`output/{brand}-{slug}.zip`

## What to tell the marketer

> Your zip is ready: `output/{brand}-{slug}.zip`
>
> Send the whole zip to Marketing Operations with this note: "Here is a new {page or
> email} for {Brand}. MANIFEST.md inside has everything. Please install on staging first."

## No file system

If you cannot write files or run a command (claude.ai chat, the Chat tab in Claude
Desktop), say once:

> This chat cannot save files or make a zip. Claude Code and Cowork can. I can show you
> each file here to copy.

Then give the files one at a time, the body or email first, each in its own code block
with its filename above it.

Say "Marketing Operations", never a person's name. Say "plugin", never "agent".
