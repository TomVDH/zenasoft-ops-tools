# Email Rules

The technical constraints for email HTML. The agent reads this file; the marketer
does not need to.

Every rule here was measured on a real send or a real install. Nothing is inferred
from general email-HTML advice.

## Where your file ends up

You build **one standalone HTML document**. It opens in a browser, which is how the
marketer reviews it.

It is then cut down and poured into the brand's **Email Shell** — a HubSpot email
template that already owns `<html>`, `<head>`, the 600px container, the letterhead,
the footer and the legal tokens. The cut is done on the admin's side by
`email-body-extract.py`; you never run it.

This matters for two reasons:

1. **Your header and footer are thrown away.** Build them anyway — the marketer
   previews the whole document — but nothing the email needs may live only there.
2. **Your content rows must be cuttable.** The contract below is not a style
   preference. A file that breaks it cannot be installed at all.

## The extraction contract

Five requirements. Miss any one and the cutter refuses the file.

1. **Two marker comments, in this order.** They are how the cutter finds your content:

   ```html
   <!-- ===== Body ===== -->
   ...your content rows...
   <!-- ===== Footer ===== -->
   ```

   Write them exactly: `<!--`, space, five or more `=`, space, the word, space,
   five or more `=`, space, `-->`. Case does not matter.

2. **Everything between the markers is `<tr>` elements.** The first thing after the
   Body marker must be `<tr`. No wrapper `<div>`, no stray text, no `<table>` at the
   top level of the cut.

3. **No forbidden tags inside the cut.** No `<html>`, `<head>`, `<body>`, `<style>`,
   `<script>` or `<link>` between the markers, and no `data:image/` anywhere in it.
   Comments are fine in the cut — a `<!-- ===== CTA button ===== -->` that helps a
   human read the file is welcome, and MSO conditionals are required.

4. **A hidden preview-text div, first thing after `<body>`.** See "Preview text".

5. **Your `<head>`, letterhead and footer sit outside the markers.** The letterhead
   goes above the Body marker; the footer goes below the Footer marker.

## How email differs from a landing page

| Landing page | Email |
|---|---|
| CSS custom properties (`var(--{p}-*)`) | Literal hex values — Outlook strips `var()` |
| `<style>` block at the top | Inline `style=""` on every element |
| CSS grid and flexbox | `<table role="presentation">` for all layout |
| Container: the brand's rail token | Container: 600px, plus an Outlook width wrapper |
| Google Fonts loaded by the theme | A `<link>` inside `<!--[if !mso]><!-->` |
| One breakpoint at 767px | One breakpoint at 600px |
| `prefers-reduced-motion` | No motion at all — clients ignore animation |
| No HTML comments | Two marker comments, required |

## Structure

```
<!DOCTYPE html>
<html lang="en" xmlns:v="…vml" xmlns:o="…office">
<head>
  Meta tags · MSO document settings · MSO font pin · <style> reset + @media
</head>
<body style="margin:0; padding:0; background-color:{page-ground};">
  Hidden preview-text div
  <!--[if mso]> wrapper table <![endif]-->
  #backgroundTable (100% width, page ground)
    #templateContainer (600px, white)
      Letterhead rows (logo, accent rule)
      <!-- ===== Body ===== -->
      Content rows
      <!-- ===== Footer ===== -->
      Footer rows
</body>
</html>
```

Start from the **Skeleton** in `email-components.md`. Do not assemble your own.

## Container: 600px needs an Outlook wrapper

`max-width: 600px; width: 100%` alone **renders full-width in Outlook** — Outlook
ignores `max-width`. The container needs a fixed-width MSO wrapper table around it:

```html
<!--[if mso]><table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0"><tr><td><![endif]-->
<table role="presentation" id="templateContainer" cellspacing="0" cellpadding="0" border="0"
       width="600" style="max-width:600px; width:100%; background-color:#FFFFFF;">
  …
</table>
<!--[if mso]></td></tr></table><![endif]-->
```

**No `border-radius` and no `overflow:hidden` on the container.** Outlook clips
rounded corners on the outer table and the result looks broken.

Content padding is 40px each side, giving 520px of usable width.

## Colours: the brand's EMAIL PALETTE

Read `brands/{brand}/tokens.css` and find the **`EMAIL PALETTE`** block in its header.
It gives you literal hex values by role, already resolved for that brand:

| role | used for |
|---|---|
| `button-bg` / `button-text` | the CTA button, and the letterhead rule |
| `footer-bg` / `footer-text` | the footer band |
| `page-ground` | the area behind the container |
| `ink` | body copy and headings |
| `heading-font` / `body-font` | the two font stacks, ready to paste |

Use those hex values directly. **Never `var()`** — email clients ignore custom
properties, and the declaration is dropped entirely.

Case does not matter. The gate lowercases both sides, so `#FE9B00` and `#fe9b00` are the
same colour to it. Pick one and be consistent within a file.

Do not derive a colour, tint a colour, or pick one that is not in the block. If the
design needs a role the block does not carry, say so and ask.

## Typography

Use the brand's stacks from the `EMAIL PALETTE` block. They already end in
`Arial, Helvetica, sans-serif`.

Load the web font with a `<link>` inside an MSO-negative conditional, **not**
`@import`:

```html
<!--[if !mso]><!-->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&amp;display=swap">
<!--<![endif]-->
```

Then pin Outlook to Arial. Without this pin **Outlook falls back to Times**, not to
Arial — the system fallback in your stack is not enough, because Outlook resolves the
first name it does not recognise to its own default serif:

```html
<!--[if mso]>
<style>
  * { font-family: Arial, Helvetica, sans-serif !important; }
</style>
<![endif]-->
```

Set `font-family` inline on every text element as well. Do not rely on inheritance.

## Line height

Outlook inflates line-height unless told not to. Two places, both required:

```css
table, td { mso-line-height-rule: exactly; }
```

and inline on every paragraph:

```html
<p style="margin:0 0 16px 0; font-size:16px; line-height:1.6; mso-line-height-rule:exactly; …">
```

## Buttons

A button is a **table**, not a bare `<a>`. The `<td>` carries the fill and the
corner radius; the `<a>` sits inside it. This is what lets the button go full-width
on a phone — a bare `<a>` cannot.

```html
<tr>
  <td align="left" class="pad" style="padding:0 40px 32px 40px;">
    <!--[if mso]>
    <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"
                 href="BUTTON_URL" style="height:46px; v-text-anchor:middle; width:250px;"
                 arcsize="9%" fillcolor="BUTTON_BG" stroke="f">
      <w:anchorlock/>
      <center style="color:BUTTON_TEXT; font-family:Arial,sans-serif; font-size:16px; font-weight:bold;">Button label</center>
    </v:roundrect>
    <![endif]-->
    <!--[if !mso]><!-->
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" class="btn-table">
      <tr>
        <td align="center" style="border-radius:4px; background-color:BUTTON_BG;">
          <a href="BUTTON_URL" class="btn-link"
             style="display:inline-block; padding:14px 32px; font-family:HEADING_FONT;
                    font-size:16px; font-weight:600; color:BUTTON_TEXT; text-decoration:none;">Button label</a>
        </td>
      </tr>
    </table>
    <!--<![endif]-->
  </td>
</tr>
```

**The URL appears twice — once in the VML, once in the `<a>`.** Change both together.
A mismatch gives every Outlook reader a button that goes somewhere else, and nothing
in a normal preview shows it.

`arcsize="9%"` and `stroke="f"`. Do not add a `strokeweight` to a filled button;
Outlook draws the stroke as a second, offset edge.

**Sizing the VML.** Outlook does not measure text, so the `width` is yours to state and a
wrong one truncates or pads the label. At 16px the rule is:

    width = (characters in the label x 8.5) + 68, rounded up to the nearest 10

"Open the check-in board" is 23 characters, so 23 x 8.5 = 196, plus 68 = 264, round to
270. Height stays 46px. The label is the only thing this depends on, so recompute it
whenever the label changes.

## Images

- Max width 520px (600px container minus 80px of padding).
- **`width` AND `height` attributes**, both required — Outlook reserves space from
  the attributes, not from CSS.
- Inline `display:block; border:0; outline:none; text-decoration:none;` plus
  `width`, `max-width` and `height:auto`.
- `alt` text on every image. Many clients block images by default.
- **PNG or JPG only. No SVG** — Outlook does not render it.
- **No `data:image/` base64.** Gmail and Outlook block embedded images on a real
  send, so a base64 logo previews fine out of a ZIP and then disappears in the inbox.
- Hosted images come from the brand's official assets on the target portal's File
  Manager, under `/saas/{brand}/logos/`. Never re-cut a logo, and never point a
  production email at a staging URL.
- **If you do not have the logo URL, use `##PORTAL_LOGO##` as the `src`** and list it
  with the other fills. It is a fill like any other, not a placeholder box. Never draw a
  grey rectangle where the logo goes.

```html
<img src="PORTAL_URL" width="184" height="44" alt="Brand name"
     style="display:block; width:184px; max-width:184px; height:auto; border:0; outline:none;">
```

## Subject line

An email document has no slot for the subject: HubSpot holds it as a property, not as
markup. Put it in `<title>` so the file is identifiable, and state it in the manifest so
the admin does not retype it from the brief.

## Preview text

The line the inbox shows next to the subject. **First element after `<body>`**, and
the cutter looks for it there:

```html
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all;
            font-size:1px; line-height:1px; color:PAGE_GROUND;">
  Your preview text here — keep it under 100 characters.
</div>
```

Keep `display:none` and `mso-hide:all` in the style attribute. Those are what make it
findable as well as invisible.

## Responsive

One breakpoint at 600px, in a non-inlined `<style>` block:

```css
@media only screen and (max-width: 600px) {
  .container { width: 100% !important; max-width: 100% !important; }
  .pad       { padding-left: 24px !important; padding-right: 24px !important; }
  .btn-table { width: 100% !important; }
  .btn-link  { display: block !important; width: 100% !important;
               box-sizing: border-box !important; text-align: center !important; }
}
```

**These classes do not exist inside the Email Shell.** The Shell defines its own
(`{prefix}-pad` and the rest) and its media query is at 620px. So:

- In your standalone document the classes work, and the marketer's browser preview
  is correct.
- Rows that end up in the Shell's letter fields lose every class and style anyway —
  the Shell owns typography there.
- Rows that end up in the Shell's raw slot keep the classes but **find no rules**, so
  they lose the mobile padding reduction.

Therefore: **every row carries usable inline padding on its own.** Treat the media
query as an improvement for the standalone preview, never as the only thing keeping a
row readable on a phone.

## MSO document settings

Required in `<head>`:

```html
<!--[if mso]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
```

## Head reset block

```css
table, td { mso-line-height-rule: exactly; border-collapse: collapse; }
table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
body { margin: 0; padding: 0; width: 100% !important; }
img  { border: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; }
```

Plus `<meta name="format-detection" content="telephone=no">` in `<head>`, so iOS does
not turn every number into a blue phone link.

## Tokens, by target

HubSpot tokens are HubL. Which ones you write depends on who owns that part of the
email.

**You write these** — personalization, inside your content rows:

```
{{ personalization_token('contact.firstname', 'there') }}
```

That is the **only** form that works. The bare `{{ contact.firstname }}` renders, but
it has no fallback, so a contact with no first name gets an empty greeting. Always
give a fallback, and make it read naturally in the sentence.

The tokens you may use, all in that form, all with a fallback:

| token | typical fallback | use |
|---|---|---|
| `contact.firstname` | `there` | greeting |
| `contact.lastname` | ` ` (empty) | formal greeting, with firstname |
| `contact.company` | `your team` | body |
| `contact.jobtitle` | `your role` | body, sparingly |
| `contact.email` | ` ` (empty) | "this was sent to" lines only |

Nothing else. A token for the sender (owner name, phone) is NOT a body token: the
signature is filled by Ops from the brief (`##SENDER_NAME##` and the rest), because
the Shell's signature fields are plain text. If the brief asks for a token not in
this table, put it under `## Notes for Ops` in the manifest and use the fallback text.

**The Shell writes these — do not put them in your content rows:**

- `{{ unsubscribe_link }}`, `{{ preferences_link }}`
- `{{ view_as_page_url }}`
- `{{ site_settings.company_name }}` and the address fields

They belong to the footer, and the footer is the Shell's. Put them in your standalone
document's own footer if you like — that sits below the Footer marker and is
discarded — but never above it.

## Placeholders

Two conventions, and they are not interchangeable.

**`##NAME##` for text and URLs** that a human fills in later:

```
##SENDER_NAME##   ##SENDER_TITLE##   ##SENDER_PHONE##   ##CONSULTATION_LINK##
```

Use screaming snake case between double hashes. List every one you used in the
handoff note. An unresolved `##…##` in an `href` is a gate failure, so it must be
visible.

**`[PLACEHOLDER: slug]` for images only**, as the marker comment above the element.
Put it outside the Body/Footer markers when you can, so the admin finds every asset in
one place. Inside the cut it is allowed: comments survive the cut (contract rule 3).

The brand logo is not a placeholder. It is `##PORTAL_LOGO##`, a normal fill, because a
logo has a real URL that someone can supply.

## Must NOT contain

- No `var()` custom properties — clients drop the whole declaration.
- No `<style>` block as the only source of styles. Every visible element carries
  inline `style=""` with at least `font-family` and `color`.
- No CSS grid, no flexbox. Tables only.
- No `<div>` for structural layout. A `<div>` between two `<tr>`s is invalid table
  markup and Outlook renders it unpredictably.
- No JavaScript.
- No SVG in `<img>`.
- No `data:image/` base64 images.
- No CSS `background-image` — Outlook ignores it.
- No gradients — Outlook renders them as a flat fill.
- No web font as the only font.
- No `position`, `float` or `z-index`.
- No `border-radius` on the outer container.
- No CSS animation or transition.
- No `<!-- Hero Section -->`-style decoration outside the cut. Section markers
  inside the cut are fine; see the extraction contract.
