# Page Shell Rules

These are the technical constraints for the HTML body. The agent reads this file; the
marketer does not need to.

## Read this first: which workflow you are in

There are two ways a body reaches a HubSpot page, and they have OPPOSITE token rules.
Confusing them is the single most common way a page ships broken.

| | Page Factory (you are here) | Theme-dev page-bodies |
|---|---|---|
| Who writes it | This agent, for a marketer | A developer, from a vibe-coded drop |
| Token prefix | The brand's own: `--wa-*`, `--jd-*` | `--zt-*`, brand-neutral |
| Stamp step | **None.** Output IS the paste | `stamp-page-body.py` rewrites the prefix |
| Buttons | The theme's `.button` classes | Its own local `.zt-btn` CSS |

Everything below describes the Page Factory column. If you find yourself reading a
`hubspot-cms/page-bodies/*` file for a pattern, remember it is written in the other
column's rules and its `--zt-*` tokens are correct THERE and wrong HERE.

## What the Shell template provides

The HubSpot page template already includes:
- The brand's header (with logo and navigation)
- The brand's footer (with links and copyright)
- The brand's colour and typography CSS (the brand-prefixed tokens, e.g. `--wa-*`)
- The brand's button system (`.button`, `.button--colourway`, `.button--cw-<n>`)
- The page's `<head>`, favicon, and tracking scripts

## What the body must provide

Everything between the header and the footer:
- Its own `<style>` block with all layout CSS
- Its own container, built from the brand's rail tokens (see below)
- Its own band padding: `var(--{p}-section-pad-v)`
- Its own responsive breakpoints (one step at 767px)

## Container

The body content sits inside a container class. It uses **the brand's own rail tokens**:

```css
.zt-container {
    width: 100%;
    max-width: var(--{p}-max-width);
    margin: 0 auto;
    padding-inline: var(--{p}-section-pad-h);
}
```

**Never write a literal width or gutter.** Not `1100px`, not `1200px`, not `24px`. And no
fallback value either: `var(--wa-max-width, 1200px)` invents a number the theme did not
give you. Every brand defines both tokens.

This is the rule `_base` already applies to every native section of every brand
(`css/objects/_containers-dnd.css`):

```css
.content-wrapper { max-width: var(--zt-max-width); padding-inline: var(--zt-section-pad-h); }
```

`_base` owns the rail and states it as tokens, never as numbers. Your container is that
same rail, re-created after the Shell breaks out to full width, so it uses the same
tokens in the brand's prefix. **We bring what our engine provides, we do not override it.**

A literal could not be right anyway: the value compiles per brand from
`theme.spacing.max_content_width`. SPEC-024 states it as PC-INV-01, "A paste can never
hardcode the rail correctly for any brand."

## The Shell HTML module

The body is pasted into a HubSpot module called `_shell-html`. This module breaks out
to full viewport width using negative margins. That is why the body needs its own
container: the DnD wrapper's container has been bypassed.

## Buttons

**The body defines no button CSS at all.** Use the theme's classes on `<a>` elements.

A button is `class="button"` plus a colourway:

```html
<a class="button button--colourway button--cw-1" href="#demo">Book a Demo</a>
```

**Which colourways and modes your brand has is listed at the top of your
`brands/<brand>/tokens.css`.** That listing is generated from the brand's live theme, so
it is current for your brand and says nothing about any other. Use what it names. If you
need a second button and it lists only one colourway, make the second action a plain text
link rather than inventing a style.

Do not use a class the listing does not name. In particular `button--secondary` is not
part of the system.

Do not write `.zt-btn`, `.zt-btn--primary`, or any custom button class. Hand-written
button CSS cannot replicate the theme's colourway fallback chain, and it loses the hover
specificity fight against the theme's generic `a:hover` rule, which is how a page ends
up with underlined buttons on hover.

The buttons will look unstyled in a local browser preview, because the theme CSS is not
loaded there. That is expected. The portal is the target, not the preview.

## Forms

If the page has a form, place the container only:
```html
<div class="zt-hsform" id="zt-form-{slug}" data-zt-form="demo"></div>
```
The form itself is configured in HubSpot by your Ops person, not in the HTML, and the embed snippet
and attribution injection are added at install time. The body just provides the target.

## Token prefix

Write CSS with the **brand's own prefix**, `--wa-*` for WorkAware, `--jd-*` for Jadian,
`--df-*` for DeskFlex. Read the brand's `tokens.css` for the correct prefix, and trust
the token names in that file over the comment at the top of it.

**Do not use `--zt-*`.** The `--zt-*` prefix is for theme development, where a stamp tool
rewrites it. The Page Factory has no stamp step: your output is pasted exactly as
written, so a `--zt-*` token resolves to nothing and the declaration is dropped. A page
that looks fine in preview can lose every colour on the portal this way.
