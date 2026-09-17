# Email Components

Proven table patterns, taken from emails that shipped. Use these when they fit.

Replace the SCREAMING placeholders with the brand's values from the `EMAIL PALETTE`
block in `brands/{brand}/tokens.css`:

| placeholder | from the palette |
|---|---|
| `HEADING_FONT` / `BODY_FONT` | `heading-font` / `body-font` |
| `INK` | `ink` |
| `PAGE_GROUND` | `page-ground` |
| `BUTTON_BG` / `BUTTON_TEXT` | `button-bg` / `button-text` |
| `FOOTER_BG` / `FOOTER_TEXT` | `footer-bg` / `footer-text` |

Four more appear in the snippets and are NOT palette values:

| placeholder | replace with |
|---|---|
| `BRAND_FONT` | the family name from `heading-font`, without quotes (`Exo`, `Inter`); for a two-font brand, `family=Heading&family=Body` |
| `BRAND_NAME` | the brand's display name from `shared/BRANDS.md` |
| `BUTTON_URL` | the CTA's URL from the brief. Unknown? `##CTA_LINK##`, in **both** copies (VML and anchor) |
| `PORTAL_URL` | an image's File Manager URL. Unknown? `##IMAGE_<SLUG>##`, and list it under the manifest's fills |

A `BUTTON_URL` or `PORTAL_URL` left in the file is a failure at intake. A `##FILL##` is
not; it is a named question for Ops.

Read `email-rules.md` first — especially **the extraction contract**. The Body and
Footer marker comments in the Skeleton are required, not decoration.

---

## Skeleton

Copy this whole thing first, then fill the three regions.

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml"
      xmlns:v="urn:schemas-microsoft-com:vml"
      xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="format-detection" content="telephone=no">
  <meta name="x-apple-disable-message-reformatting">
  <title>Email subject line</title>

  <!--[if mso]>
  <xml>
    <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
  </xml>
  <![endif]-->

  <!--[if !mso]><!-->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=BRAND_FONT:wght@400;500;600;700&amp;display=swap">
  <!--<![endif]-->

  <!--[if mso]>
  <style>
    * { font-family: Arial, Helvetica, sans-serif !important; }
  </style>
  <![endif]-->

  <style>
    table, td { mso-line-height-rule: exactly; border-collapse: collapse;
                mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    body { margin: 0; padding: 0; width: 100% !important; }
    img  { border: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; }

    @media only screen and (max-width: 600px) {
      .container { width: 100% !important; max-width: 100% !important; }
      .pad       { padding-left: 24px !important; padding-right: 24px !important; }
      .btn-table { width: 100% !important; }
      .btn-link  { display: block !important; width: 100% !important;
                   box-sizing: border-box !important; text-align: center !important; }
    }
  </style>
</head>

<body style="margin:0; padding:0; background-color:PAGE_GROUND;">

  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all;
              font-size:1px; line-height:1px; color:PAGE_GROUND;">
    Preview text here, under 100 characters.
  </div>

  <!--[if mso]>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center">
  <![endif]-->

  <table role="presentation" id="backgroundTable" width="100%" cellpadding="0" cellspacing="0"
         border="0" style="background-color:PAGE_GROUND;">
    <tr>
      <td align="center" style="padding:24px 12px;">

        <!--[if mso]>
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td>
        <![endif]-->

        <table role="presentation" id="templateContainer" width="600" cellpadding="0"
               cellspacing="0" border="0" class="container"
               style="width:100%; max-width:600px; background-color:#FFFFFF;
                      font-family:BODY_FONT;">

          LETTERHEAD ROWS GO HERE

          <!-- ===== Body ===== -->

          CONTENT ROWS GO HERE

          <!-- ===== Footer ===== -->

          FOOTER ROWS GO HERE

        </table>

        <!--[if mso]>
        </td></tr></table>
        <![endif]-->

      </td>
    </tr>
  </table>

  <!--[if mso]>
  </td></tr></table>
  <![endif]-->

</body>
</html>
```

---

## Letterhead

Above the Body marker. The Shell replaces this at install, so keep it simple.

```html
<tr>
  <td align="left" class="pad" style="padding:32px 40px 24px 40px;">
    <img src="##PORTAL_LOGO##" width="184" height="44" alt="BRAND_NAME"
         style="display:block; width:184px; max-width:184px; height:auto; border:0; outline:none;">
  </td>
</tr>
<tr>
  <td height="3" style="height:3px; line-height:3px; font-size:3px; background-color:BUTTON_BG;">&nbsp;</td>
</tr>
```

The accent rule reads `button-bg`, not a separate accent role — that is what the
Shell does, so matching it keeps the preview honest.

---

## Headline

Optional. Many service emails open straight into the greeting instead.

```html
<tr>
  <td class="pad" align="left" style="padding:32px 40px 0 40px;">
    <p style="margin:0; font-family:HEADING_FONT; font-size:26px; font-weight:700;
              line-height:1.25; mso-line-height-rule:exactly; color:INK;">
      Headline goes here
    </p>
  </td>
</tr>
```

---

## Body text

One `<td>`, one `<p>` per paragraph, margin between them.

```html
<tr>
  <td class="pad" style="padding:36px 40px 0 40px;">
    <p style="margin:0 0 16px 0; font-family:BODY_FONT; font-size:16px; font-weight:400;
              line-height:1.6; mso-line-height-rule:exactly; color:INK;">
      First paragraph.
    </p>
    <p style="margin:0 0 28px 0; font-family:BODY_FONT; font-size:16px; font-weight:400;
              line-height:1.6; mso-line-height-rule:exactly; color:INK;">
      Last paragraph before the button carries the larger bottom margin.
    </p>
  </td>
</tr>
```

A greeting is its own row, so the cutter can lift it into the Shell's greeting field:

```html
<tr>
  <td class="pad" style="padding:36px 40px 0 40px;">
    <p style="margin:0 0 16px 0; font-family:BODY_FONT; font-size:16px; line-height:1.6;
              mso-line-height-rule:exactly; color:INK;">
      Hi {{ personalization_token('contact.firstname', 'there') }},
    </p>
  </td>
</tr>
```

---

## Primary button

The URL appears **twice**. Change both.

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

Set the VML `width` to roughly the rendered button width in pixels. Outlook does not
measure text, so a wrong width truncates or pads the label.

---

## Ghost button

Transparent fill, visible border. No VML — an unfilled `v:roundrect` renders as a
hairline box in Outlook, so let Outlook have the square-cornered `<a>`.

```html
<a href="BUTTON_URL"
   style="display:inline-block; padding:12px 30px; font-family:HEADING_FONT;
          font-size:15px; font-weight:600; color:INK; text-decoration:none;
          background-color:transparent; border:2px solid INK;">Button label</a>
```

---

## Image row

```html
<tr>
  <td align="center" class="pad" style="padding:24px 40px 8px 40px;">
    <img src="PORTAL_URL" width="520" height="292" alt="Description"
         style="display:block; width:520px; max-width:100%; height:auto;
                border:0; outline:none; margin:0 auto;">
  </td>
</tr>
```

When the real image is not available yet, use a solid placeholder — **a table, not a
flex div**:

```html
<tr>
  <td align="center" class="pad" style="padding:24px 40px 8px 40px;">
    <table role="presentation" width="520" cellpadding="0" cellspacing="0" border="0"
           style="width:100%; max-width:520px; background-color:PAGE_GROUND;">
      <tr>
        <td align="center" height="260"
            style="height:260px; font-family:BODY_FONT; font-size:14px; color:INK;">
          Product screenshot
        </td>
      </tr>
    </table>
  </td>
</tr>
```

Name the image in the handoff note so the admin knows what to wire in.

---

## Signature

Keep it one row with `<br>` between the lines, and put the placeholders in. The
cutter recognises `##SENDER_` and lifts the three lines into the Shell's signature
fields.

```html
<tr>
  <td class="pad" style="padding:0 40px 40px 40px;">
    <p style="margin:0; font-family:BODY_FONT; font-size:15px; line-height:1.6;
              mso-line-height-rule:exactly; color:INK;">
      <span style="font-weight:600;">##SENDER_NAME##</span><br>
      ##SENDER_TITLE##<br>
      ##SENDER_PHONE##
    </p>
  </td>
</tr>
```

---

## Divider

```html
<tr>
  <td class="pad" style="padding:8px 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td style="height:1px; line-height:1px; font-size:1px; background-color:FOOTER_BG;">&nbsp;</td>
      </tr>
    </table>
  </td>
</tr>
```

---

## Spacer

```html
<tr>
  <td style="height:32px; line-height:32px; font-size:0;">&nbsp;</td>
</tr>
```

`line-height` and `font-size` are both needed. Without them Outlook gives the row a
minimum text height and the gap grows.

---

## Footer

Below the Footer marker. The Shell replaces this and writes the real tokens, so this
copy is for the marketer's preview only.

```html
<tr>
  <td class="pad" align="center" style="padding:28px 40px; background-color:FOOTER_BG;">
    <p style="margin:0 0 12px 0; font-family:HEADING_FONT; font-size:14px;
              font-weight:700; color:FOOTER_TEXT;">
      BRAND_NAME
    </p>
    <p style="margin:0 0 12px 0; font-family:BODY_FONT; font-size:12px; line-height:1.7;
              mso-line-height-rule:exactly; color:FOOTER_TEXT;">
      [Company Name] &middot; [Street Address] &middot; [City, State ZIP]
    </p>
    <p style="margin:0; font-family:BODY_FONT; font-size:12px; line-height:1.7;
              mso-line-height-rule:exactly; color:FOOTER_TEXT;">
      <a href="#" style="color:FOOTER_TEXT; text-decoration:underline;">Unsubscribe</a>
      &nbsp;|&nbsp;
      <a href="#" style="color:FOOTER_TEXT; text-decoration:underline;">View in browser</a>
    </p>
  </td>
</tr>
```

Leave the links as `#`. The real `{{ unsubscribe_link }}` and `{{ view_as_page_url }}`
belong to the Shell, and a token above the Footer marker is a gate failure.
