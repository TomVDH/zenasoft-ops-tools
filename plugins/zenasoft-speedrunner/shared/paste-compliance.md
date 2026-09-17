# Paste Compliance Rules

These are the rules a body.html must follow. Breaking any P1 rule means the page will
not work. P2 rules cause visual problems. P3+ are quality standards.

## P1: Will not work if broken

- **All colours via tokens.** Every colour must be a `var()` reference using the brand's
  own prefix (`--jd-*` for Jadian, `--wa-*` for WorkAware, `--df-*` for DeskFlex). No
  hex codes (`#ff6600`), no `rgb()`, no colour names. **Never `--zt-*`** — that prefix is
  for theme development and does not resolve on the portal, because this factory has no
  stamp step. Exception: inside `box-shadow` and `text-shadow`, raw colours are allowed.
- **No private token names.** Do not invent `--c-blue` or `--my-accent`. Only tokens
  from the brand's `tokens.css`.
- **Every token must resolve.** If a token is optional (not every brand defines it),
  add a fallback, and end the chain in a role every brand defines:
  `var(--jd-surface, var(--jd-bg))`. **Never a hex** — see "Fallback chains" below.

### Violation examples

**All colours via tokens**

Wrong:
```css
.zt-hero {
    background-color: #F4F6F8;
    color: #141D24;
    border-bottom: 1px solid #CCDAE0;
}
.zt-badge {
    background-color: rgb(254, 155, 0);
    color: white;
}
```

Right:
```css
.zt-hero {
    background-color: var(--{p}-bg-muted);
    color: var(--{p}-ink);
    border-bottom: 1px solid var(--{p}-border);
}
.zt-badge {
    background-color: var(--{p}-accent-1);
    color: var(--{p}-on-accent);
}
```

Exception — raw colours allowed inside shadow functions only:
```css
.zt-formcard {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);  /* OK */
}
```

**No private token names**

Wrong:
```css
:root {
    --c-brand: #0A4C70;
    --c-accent: #FE9B00;
    --my-padding: 30px;
}
.zt-hero { background: var(--c-brand); }
```

Right:
```css
/* No :root block. Use the brand's tokens directly. */
.zt-hero { background: var(--{p}-ground-dark); }
```

**Every token must resolve**

Wrong:
```css
.zt-card {
    background: var(--{p}-card-surface);  /* not every brand defines this */
}
```

Right:
```css
.zt-card {
    background: var(--{p}-card-bg, var(--{p}-surface, var(--{p}-bg)));
}
```

---

### Fallback chains: never a hex, always a token

Some roles are not defined by every brand. A bare `var()` on one of those drops the
**whole declaration**, so `background: var(--{p}-ground-dark)` paints nothing and the page
ground shows through.

So an optional role always carries a fallback, and **the chain terminates in a role every
brand defines**:

```css
background: var(--{p}-ground-dark, var(--{p}-footer-bg));
color:      var(--{p}-ink-on-dark, var(--{p}-footer-text));
```

**Never end a colour chain in a hex.** `var(--{p}-ink-on-dark, #fff)` looks like a safety
net and is the opposite: the hex only appears when the brand is missing the role, which is
exactly when a hardcoded colour is most likely to be wrong. Measured 2026-09-15: that
pattern put white text on a white page on 7 of 10 brands, because the background dropped
out while the hex kept the text white. Removing the hex would have left the text legible.

There is no usable literal fallback for a colour. A colour name and `rgb()` are banned too,
and `currentColor` is just the inherited value you already get by writing no fallback. A
token is the only correct answer.

Pair a ground with its own ink. If you fall back to `footer-bg`, fall back to
`footer-text` alongside it, never to a colour from somewhere else.

## P2: Causes visual problems

- **Container uses the brand's rail tokens.** `max-width: var(--{p}-max-width)` and
  `padding-inline: var(--{p}-section-pad-h)`. Never a literal number, and never a
  fallback value. This mirrors `_base`, which owns the rail and states it as tokens.
- **One container class.** Two containers with different widths create two rails.
- **Reset specificity.** Element resets (margin: 0 on headings) must use `:where()` so
  class-based spacing rules can override them.

### Violation examples

**Container uses the brand's rail tokens**

Wrong — a literal:
```css
.zt-container {
    max-width: 1100px;
    padding-inline: 24px;
}
```

Also wrong — a token carrying a fallback. The fallback is a number the theme never gave
you, and it silently wins whenever the token is missing:
```css
.zt-container {
    max-width: var(--{p}-max-width, 1200px);
    padding-inline: var(--{p}-section-pad-h, 30px);
}
```

Right:
```css
.zt-container {
    width: 100%;
    max-width: var(--{p}-max-width);
    margin: 0 auto;
    padding-inline: var(--{p}-section-pad-h);
}
```

The rail belongs to `_base`, which states it as tokens for every native section of every
brand and never as a number. The body is that same rail re-created after the Shell breaks
out, so it reads the same tokens. The value is compiled per brand from
`theme.spacing.max_content_width`, which is why SPEC-024 PC-INV-01 says a paste "can
never hardcode the rail correctly for any brand."

**One container class**

Wrong — two containers with different widths:
```css
.zt-container { max-width: var(--{p}-max-width); margin: 0 auto; }
.zt-narrow { max-width: 800px; margin: 0 auto; padding-inline: 24px; }
```

Right — constrain inner content, not the rail:
```css
.zt-container { width: 100%; max-width: var(--{p}-max-width); margin: 0 auto; padding-inline: var(--{p}-section-pad-h); }
.zt-section__head { max-width: 40em; }
```

**Reset specificity**

Wrong:
```css
h1, h2, h3, p, ul { margin: 0; }
/* Now .zt-section__title { margin-bottom: 12px; } must fight for specificity. */
```

Right:
```css
.zt-lp :where(h1, h2, h3, p, ul, figure, address, blockquote) { margin: 0; }
/* :where() has zero specificity, so any class-based rule overrides it. */
```

---

## Must NOT contain

- No `<header>`, `<nav>`, or `<footer>` at the top level. The Shell provides them.
- No `<script>` tags except the HubSpot form embed container.
- No `:root { }` redefinition. The theme owns `:root`.
- No `style="..."` inline attributes. All styling goes in the `<style>` block.
- No external stylesheet links. Everything is in the one file.

### Violation examples

**No top-level structural elements**

Wrong:
```html
<header class="zt-header">
    <nav>...</nav>
</header>
<div class="zt-lp">
    <!-- content -->
</div>
<footer>...</footer>
```

Right:
```html
<div class="zt-lp">
    <!-- content only — no header, nav, or footer -->
</div>
```

**No script tags**

Wrong:
```html
<script src="https://cdn.example.com/animation.js"></script>
<script>
    document.querySelectorAll('.card').forEach(el => {
        el.addEventListener('mouseover', () => el.classList.add('hover'));
    });
</script>
```

Right: no `<script>` tags at all. The form embed is a plain `<div>`:
```html
<div class="zt-hsform" id="zt-form-{slug}" data-zt-form="demo"></div>
```

The intake gate checks these (`PC-TRK-01`): a CTA anchor without `data-zt-cta`, a form
container without `data-zt-form` and its `id="zt-form-{slug}"`, or a value other than
`demo` or `contact`, fails the page at intake.

**No :root redefinition**

Wrong:
```css
:root {
    --{p}-accent-1: #ff6600;
    --custom-gap: 20px;
}
```

Right: do not include any `:root` block. The brand's theme defines every token value.

**No inline styles**

Wrong:
```html
<section style="background-color: var(--{p}-bg-muted); padding: 80px 0;">
    <div style="max-width: 1200px; margin: 0 auto;">
```

Right:
```html
<section class="zt-section zt-section--alt">
    <div class="zt-container">
```
```css
.zt-section--alt { background-color: var(--{p}-bg-muted); }
```

**No external stylesheet links**

Wrong:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Exo:wght@400;600;800">
<link rel="stylesheet" href="styles.css">
```

Right: no `<link>` tags. The brand's template already loads the fonts. All CSS lives in
the single `<style>` block at the top of the body file.

---

## Quality standards

- Band padding should use `var(--{p}-section-pad-v)` or a consistent fallback.
- Font sizes in `rem` where possible (not `px`).
- `prefers-reduced-motion` media query to disable animations.
- Visible focus states on interactive elements.
