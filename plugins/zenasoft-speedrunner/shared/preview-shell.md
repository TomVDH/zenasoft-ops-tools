# The preview file

`{brand}-{slug}-preview.html` is the file the marketer opens to review a landing page.
The body file uses `var(--{p}-…)` tokens, and a plain browser cannot resolve them
without the brand's theme, so the body alone renders in black and white with unstyled
buttons. The preview wraps the same body in the brand's tokens and fonts, so colours,
type and buttons render as they will on the portal.

Two rules:

- The preview is a review copy. It is never pasted into HubSpot. Marketing Operations
  installs the body file.
- The body inside the preview is byte-for-byte the body file. Never edit one without
  the other. Rebuild the preview from the body after every change.

An email needs no preview. It carries inline styles and its own font link, so
`{brand}-{slug}-email.html` renders as it is.

## How to build it

1. Open `brands/{brand}/tokens.css`. Copy its `:root { … }` block whole, from `:root {`
   to the matching `}`. Do not edit a value.
2. Read `--{p}-font-headline` and `--{p}-font-body` in that block. Take every quoted
   family name. A family that is on Google Fonts goes into the font link below, once,
   with weights `400;500;600;700;800`. A family that is not on Google Fonts (for example
   `all-round-gothic`) is left out; the next family in the stack renders instead. Do not
   fetch fonts from anywhere else.
3. Write the template below to `output/{brand}-{slug}/{brand}-{slug}-preview.html`, with
   `{p}` replaced by the brand's prefix, the `:root` block in slot A, the font families in
   the link, and the body file's full contents in slot B.

## The template

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview: {Brand} {Page Name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={Family+One}:wght@400;500;600;700;800&family={Family+Two}:wght@400;500;600;700;800&display=swap">
<style>
/* A. the brand's tokens, copied whole from brands/{brand}/tokens.css */
:root {
  …
}

/* preview shim: what the theme provides on the portal, restated for a plain browser */
html { background: var(--{p}-bg); }
body {
  margin: 0;
  font-family: var(--{p}-font-body);
  font-size: var(--{p}-body-size);
  line-height: var(--{p}-body-lh);
  color: var(--{p}-ink);
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3, h4 { font-family: var(--{p}-font-headline); line-height: 1.15; margin: 0 0 0.5em; }
h1 { font-size: var(--{p}-h1-size); }
h2 { font-size: var(--{p}-h2-size); }
h3 { font-size: var(--{p}-h3-size); }
h4 { font-size: var(--{p}-h4-size); }
p { margin: 0 0 1em; }
img { max-width: 100%; height: auto; }
a { color: var(--{p}-accent-1); }

.button, .button--colourway {
  --fill: var(--{p}-btn-primary-bg);
  --ink: var(--{p}-btn-primary-text);
  display: inline-flex; align-items: center; justify-content: center;
  font-family: var(--{p}-font-body);
  font-size: var(--{p}-btn-font-size);
  font-weight: var(--{p}-btn-font-weight);
  line-height: 1; text-align: center; text-decoration: none; cursor: pointer;
  padding: var(--{p}-btn-pad-v) var(--{p}-btn-pad-h);
  border-radius: var(--{p}-btn-radius);
  background: var(--mode-bg, var(--fill));
  color: var(--mode-fg, var(--ink));
  border: 2px solid var(--mode-border, var(--fill));
}
.button:hover, .button:focus, .button--colourway:hover, .button--colourway:focus {
  background: var(--mode-bg-hover, var(--{p}-btn-primary-hover-bg));
  color: var(--mode-fg, var(--ink));
}
.button--cw-1 { --fill: var(--{p}-cw-1); --ink: var(--{p}-on-cw-1); }
.button--cw-2 { --fill: var(--{p}-cw-2, var(--{p}-accent-1)); --ink: var(--{p}-on-cw-2, var(--{p}-on-accent)); }
.button--cw-3 { --fill: var(--{p}-cw-3, var(--{p}-accent-1)); --ink: var(--{p}-on-cw-3, var(--{p}-on-accent)); }
.button--cw-4 { --fill: var(--{p}-cw-4, var(--{p}-accent-1)); --ink: var(--{p}-on-cw-4, var(--{p}-on-accent)); }
.button--cw-5 { --fill: var(--{p}-cw-5, var(--{p}-accent-1)); --ink: var(--{p}-on-cw-5, var(--{p}-on-accent)); }
.button--mode-outline { --mode-bg: transparent; --mode-fg: var(--fill); --mode-border: var(--fill); }

/* slots the body marks for Marketing Operations, shown as labelled boxes */
.zt-placeholder, .zt-hsform, .zt-scheduler {
  position: relative; min-height: 160px;
  border: 2px dashed var(--{p}-ink-muted);
  background: var(--{p}-bg-muted);
}
.zt-placeholder::after, .zt-hsform::after, .zt-scheduler::after {
  content: attr(data-placeholder);
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--{p}-font-body); font-size: 14px;
  color: var(--{p}-ink-muted); text-transform: uppercase; letter-spacing: 0.08em;
}
.zt-hsform::after { content: "form goes here"; }
.zt-scheduler::after { content: "booking calendar goes here"; }
</style>
</head>
<body>
<!-- B. the body file, pasted whole -->
…
</body>
</html>
```

The comments `A.` and `B.` are part of the preview only. The body file itself carries no
comments except placeholder markers.
