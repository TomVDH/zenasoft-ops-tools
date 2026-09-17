# Page Components

Proven HTML patterns for the Page Shell. Each component shows CSS then HTML. Copy both,
then replace every `--{p}-` with the brand's actual prefix (`--jd-`, `--wa-`, `--df-`).
`--{p}-` is not a real token and will not resolve.

For layouts not listed here, build from the brand's tokens and the container below.

---

## Placeholders

Every image, screenshot, or visual the admin will wire in later gets a placeholder.
The body never contains real images — only labelled slots.

```css
.zt-placeholder {
    background: var(--{p}-bg-muted);
    border: 1px dashed var(--{p}-border);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--{p}-text-muted);
    font-size: 0.8125rem;
    text-align: center;
    padding: 24px;
}
.zt-placeholder--16x9 { aspect-ratio: 16/9; }
.zt-placeholder--4x3 { aspect-ratio: 4/3; }
.zt-placeholder--1x1 { aspect-ratio: 1/1; }
.zt-placeholder--16x10 { aspect-ratio: 16/10; }
```

```html
<!-- [PLACEHOLDER: hero-image] Product dashboard screenshot, ~16:9 -->
<div class="zt-placeholder zt-placeholder--16x9" data-placeholder="hero-image">
  Product dashboard screenshot
</div>
```

Rules:
- Comment above: `<!-- [PLACEHOLDER: slug] description -->`
- Element: `class="zt-placeholder zt-placeholder--{ratio}"` + `data-placeholder="slug"`
- Use a ratio modifier class, never an inline `style` attribute
- These are the ONLY permitted HTML comments in the body

---

## Body Wrapper

Every body starts with this. Scopes all styles. Resets margins.

```css
.zt-lp {
    color: var(--{p}-ink);
    font-family: var(--{p}-font-body);
    font-size: var(--{p}-body-size);
    line-height: var(--{p}-body-lh);
    background: var(--{p}-surface, var(--{p}-bg));
    -webkit-font-smoothing: antialiased;
}
.zt-lp *, .zt-lp *::before, .zt-lp *::after { box-sizing: border-box; }
.zt-lp :where(h1, h2, h3, p, ul, figure, address, blockquote) { margin: 0; }
.zt-lp img, .zt-lp svg { display: block; max-width: 100%; }
.zt-lp h1, .zt-lp h2, .zt-lp h3 { font-family: var(--{p}-font-head); }
```

```html
<div class="zt-lp">
</div>
```

---

## Container

The content rail. Every section wraps its content in this. Uses the brand's own
tokens — never a literal number, never a fallback value.

```css
.zt-container {
    width: 100%;
    max-width: var(--{p}-max-width);
    margin: 0 auto;
    padding-inline: var(--{p}-section-pad-h);
}
```

---

## Section

A horizontal band of content. Sections carry their own vertical padding and are
separated by a hairline.

```css
.zt-section {
    padding: var(--{p}-section-pad-v) 0;
}
.zt-section + .zt-section {
    border-top: 1px solid var(--{p}-border);
}
.zt-section--alt {
    background-color: var(--{p}-bg-muted);
}
.zt-section--tint {
    background-color: var(--{p}-bg-secondary, var(--{p}-bg-muted));
}
.zt-section__head {
    max-width: 40em;
    margin-bottom: clamp(2rem, 4vw, 3.5rem);
}
.zt-section__title {
    font-size: clamp(1.55rem, 3vw, 2.1rem);
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -0.01em;
    text-wrap: balance;
    color: var(--{p}-ink);
}
.zt-section__intro {
    color: var(--{p}-text-muted);
    font-size: 1.1rem;
    margin-top: 14px;
}
```

---

## Split Hero (copy + image or form)

Two columns: copy on one side, a product screenshot or form card on the other.
The primary hero pattern for feature and lead-capture pages.

```css
.zt-hero {
    background: var(--{p}-bg-muted);
    border-bottom: 1px solid var(--{p}-border);
    padding: clamp(2.5rem, 6vw, 5rem) 0 clamp(2rem, 5vw, 4rem);
}
.zt-hero__grid {
    display: grid;
    grid-template-columns: 1.08fr 0.92fr;
    gap: clamp(2rem, 4vw, 3.25rem);
    align-items: center;
}
.zt-hero__eyebrow {
    display: inline-block;
    font-size: 0.8125rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--{p}-accent-ink, var(--{p}-accent-1));
    margin-bottom: 1rem;
}
.zt-hero__title {
    font-size: clamp(2rem, 4.4vw, 3rem);
    line-height: 1.12;
    font-weight: 800;
    letter-spacing: -0.015em;
    text-wrap: balance;
    color: var(--{p}-ink);
}
.zt-hero__lead {
    color: var(--{p}-text-muted);
    font-size: 1.18rem;
    margin-top: 1.25rem;
    max-width: 33em;
}
.zt-hero__actions {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 1.875rem;
}
.zt-hero__form-card {
    background: var(--{p}-card-bg, var(--{p}-bg));
    border: 1px solid var(--{p}-border);
    border-radius: var(--{p}-card-radius);
    padding: clamp(1.25rem, 2vw, 1.75rem);
}
.zt-hero__form-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--{p}-ink);
}
```

```html
<section class="zt-hero">
    <div class="zt-container zt-hero__grid">
        <div class="zt-hero__copy">
            <span class="zt-hero__eyebrow">New Feature</span>
            <h1 class="zt-hero__title">Headline here</h1>
            <p class="zt-hero__lead">Supporting text here.</p>
            <div class="zt-hero__actions">
                <a class="button button--colourway button--cw-1" href="#demo" data-zt-cta="demo">Book a Demo</a>
            </div>
        </div>
        <div class="zt-hero__media">
            <!-- [PLACEHOLDER: hero-image] Product screenshot, ~4:3 -->
            <div class="zt-placeholder zt-placeholder--4x3" data-placeholder="hero-image">
              Product screenshot
            </div>
        </div>
    </div>
</section>
```

For a form in the hero instead of an image, replace the media column:
```html
        <div class="zt-hero__media">
            <div class="zt-hero__form-card">
                <p class="zt-hero__form-title">Request a Demo</p>
                <div class="zt-hsform" id="zt-form-{slug}" data-zt-form="demo"></div>
            </div>
        </div>
```

---

## Cover Hero (full-width band with centred copy)

A bold, full-width coloured band with centred headline and CTA. Use for statement
pages, event registration, or when the page leads with presence over product.

```css
.zt-cover {
    background: var(--{p}-ground-dark, var(--{p}-footer-bg));
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
    padding: clamp(3.5rem, 8vw, 6.5rem) 0;
    text-align: center;
}
.zt-cover__inner {
    max-width: 40em;
    margin: 0 auto;
}
.zt-cover__title {
    font-size: clamp(2.2rem, 5vw, 3.5rem);
    line-height: 1.08;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-wrap: balance;
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
}
.zt-cover__lead {
    font-size: 1.18rem;
    line-height: 1.55;
    margin-top: 1.25rem;
    max-width: 38em;
    margin-inline: auto;
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
    opacity: 0.88;
}
.zt-cover__actions {
    margin-top: 2rem;
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
}
```

```html
<section class="zt-cover">
    <div class="zt-container">
        <div class="zt-cover__inner">
            <h1 class="zt-cover__title">Bold statement headline</h1>
            <p class="zt-cover__lead">Supporting text here.</p>
            <div class="zt-cover__actions">
                <a class="button button--colourway button--cw-1" href="#demo" data-zt-cta="demo">Book a Demo</a>
            </div>
        </div>
    </div>
</section>
```

---

## Feature Cards (icon + title + text)

A grid of 2–4 cards, each with an optional SVG icon. No shadows, no background fills
on the cards — differentiate with the icon and the heading, not with decoration.

```css
.zt-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(2rem, 4vw, 3rem);
}
.zt-card {
    max-width: 34ch;
}
.zt-card__icon {
    color: var(--{p}-accent-ink, var(--{p}-accent-1));
    margin-bottom: 1.125rem;
}
.zt-card__icon svg {
    display: block;
    width: 40px;
    height: 40px;
}
.zt-card__title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: var(--{p}-ink);
}
.zt-card__text {
    color: var(--{p}-text-muted);
    font-size: 1rem;
}
```

For 2 cards: `grid-template-columns: repeat(2, 1fr)`.
For 4 cards: `grid-template-columns: repeat(2, 1fr)` (2×2 grid, never 4 across).

---

## Feature Rows (alternating image + text)

Two-column rows with text on one side and a product screenshot on the other.
Alternate the image side every other row for visual rhythm.

```css
.zt-row {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: clamp(2rem, 4.5vw, 3.75rem);
    align-items: center;
    margin-bottom: clamp(3.25rem, 6vw, 5.25rem);
}
.zt-row:last-child { margin-bottom: 0; }
.zt-row--flip { grid-template-columns: 1.1fr 0.9fr; }
.zt-row--flip .zt-row__text { order: 2; }
.zt-row--flip .zt-row__media { order: 1; }
.zt-row__eyebrow {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--{p}-accent-ink, var(--{p}-accent-1));
    margin-bottom: 0.625rem;
}
.zt-row__heading {
    font-size: var(--{p}-h3-size);
    color: var(--{p}-accent-ink, var(--{p}-accent-1));
    margin: 0 0 0.5rem;
    line-height: 1.2;
}
.zt-row__body {
    font-size: var(--{p}-body-size);
    line-height: var(--{p}-body-lh);
    color: var(--{p}-ink);
}
.zt-row__media img {
    display: block;
    max-width: 100%;
    height: auto;
    border: 1px solid var(--{p}-border);
    border-radius: var(--{p}-card-radius);
    box-shadow: var(--{p}-shadow-md);
}
```

```html
<div class="zt-row">
    <div class="zt-row__text">
        <span class="zt-row__eyebrow">Feature Name</span>
        <h3 class="zt-row__heading">What it does</h3>
        <p class="zt-row__body">Description text here.</p>
    </div>
    <div class="zt-row__media">
        <!-- [PLACEHOLDER: feature-1-image] Dashboard view showing X, ~16:10 -->
        <div class="zt-placeholder zt-placeholder--16x10" data-placeholder="feature-1-image">
          Dashboard view showing X
        </div>
    </div>
</div>
<div class="zt-row zt-row--flip">
    <div class="zt-row__text">
        <span class="zt-row__eyebrow">Next Feature</span>
        <h3 class="zt-row__heading">What it does</h3>
        <p class="zt-row__body">Description text here.</p>
    </div>
    <div class="zt-row__media">
        <!-- [PLACEHOLDER: feature-2-image] Settings panel showing Y, ~16:10 -->
        <div class="zt-placeholder zt-placeholder--16x10" data-placeholder="feature-2-image">
          Settings panel showing Y
        </div>
    </div>
</div>
```

---

## Stats Row

Horizontal metric tiles — big numbers with labels. The copy provides the numbers.
Do not invent statistics.

```css
.zt-stats {
    display: flex;
    gap: clamp(2rem, 4vw, 3.5rem);
    flex-wrap: wrap;
}
.zt-stat {
    flex: 1;
    min-width: 10rem;
    text-align: center;
}
.zt-stat__number {
    font-family: var(--{p}-font-head);
    font-size: clamp(2.2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1;
    color: var(--{p}-accent-ink, var(--{p}-accent-1));
    font-variant-numeric: tabular-nums;
}
.zt-stat__label {
    font-size: 0.9375rem;
    color: var(--{p}-text-muted);
    margin-top: 0.5rem;
}
```

```html
<div class="zt-stats">
    <div class="zt-stat">
        <div class="zt-stat__number">30%</div>
        <div class="zt-stat__label">Reduction in unused floor space</div>
    </div>
    <div class="zt-stat">
        <div class="zt-stat__number">3 weeks</div>
        <div class="zt-stat__label">Average deployment time</div>
    </div>
    <div class="zt-stat">
        <div class="zt-stat__number">40 min</div>
        <div class="zt-stat__label">Saved per supervisor per day</div>
    </div>
</div>
```

---

## Quotes / Social Proof

Client quotes. The theme styles bare `<blockquote>` with white text (designed for
dark sections), so the body MUST set explicit `color` on every text element inside.
Never rely on colour inheritance through `<blockquote>`.

```css
.zt-quotes {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: clamp(2rem, 4vw, 2.5rem);
}
.zt-quote {
    border-left: 3px solid var(--{p}-accent-ink, var(--{p}-accent-1));
    padding-left: 1.5rem;
}
.zt-quote__text {
    font-size: 1.05rem;
    line-height: 1.6;
    color: var(--{p}-ink);
}
.zt-quote__attr {
    color: var(--{p}-text-muted);
    font-size: 0.9rem;
    margin-top: 0.875rem;
}
```

```html
<div class="zt-quotes">
    <blockquote class="zt-quote">
        <p class="zt-quote__text">"Quote text here."</p>
        <p class="zt-quote__attr">— Name, Title, Company</p>
    </blockquote>
    <blockquote class="zt-quote">
        <p class="zt-quote__text">"Quote text here."</p>
        <p class="zt-quote__attr">— Name, Title, Company</p>
    </blockquote>
</div>
```

---

## CTA Band

A dark full-width band at the bottom of the page. Centred copy with one button.

```css
.zt-cta {
    background: var(--{p}-ground-dark, var(--{p}-footer-bg));
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
    padding: var(--{p}-section-pad-v) 0;
    text-align: center;
}
.zt-cta__inner {
    max-width: 36em;
    margin: 0 auto;
}
.zt-cta__title {
    font-size: clamp(1.55rem, 3vw, 2.1rem);
    font-weight: 800;
    letter-spacing: -0.01em;
    text-wrap: balance;
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
}
.zt-cta__text {
    margin-top: 0.875rem;
    font-size: 1.05rem;
    line-height: 1.5;
    color: var(--{p}-ink-on-dark, var(--{p}-footer-text));
    opacity: 0.88;
}
.zt-cta__actions {
    margin-top: 1.75rem;
}
```

```html
<section class="zt-cta">
    <div class="zt-container">
        <div class="zt-cta__inner">
            <h2 class="zt-cta__title">Ready to get started?</h2>
            <p class="zt-cta__text">Supporting text here.</p>
            <div class="zt-cta__actions">
                <a class="button button--colourway button--cw-1" href="#demo" data-zt-cta="demo">Book a Demo</a>
            </div>
        </div>
    </div>
</section>
```

---

## Steps / How It Works

A vertical sequence of numbered steps. Use when the product has a clear workflow.

```css
.zt-steps {
    max-width: 38em;
}
.zt-step {
    display: grid;
    grid-template-columns: 3rem 1fr;
    gap: 1.25rem;
    padding-bottom: 2.5rem;
    position: relative;
}
.zt-step:last-child { padding-bottom: 0; }
.zt-step::before {
    content: '';
    position: absolute;
    left: calc(1.5rem - 1px);
    top: 3rem;
    bottom: 0;
    width: 2px;
    background: var(--{p}-border);
}
.zt-step:last-child::before { display: none; }
.zt-step__marker {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    background: var(--{p}-accent-ink, var(--{p}-accent-1));
    color: var(--{p}-on-accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1rem;
    flex-shrink: 0;
}
.zt-step__title {
    font-weight: 700;
    font-size: 1.15rem;
    margin-bottom: 0.375rem;
    color: var(--{p}-ink);
}
.zt-step__text {
    color: var(--{p}-text-muted);
}
```

```html
<div class="zt-steps">
    <div class="zt-step">
        <div class="zt-step__marker">1</div>
        <div>
            <h3 class="zt-step__title">Step title</h3>
            <p class="zt-step__text">Step description.</p>
        </div>
    </div>
    <div class="zt-step">
        <div class="zt-step__marker">2</div>
        <div>
            <h3 class="zt-step__title">Step title</h3>
            <p class="zt-step__text">Step description.</p>
        </div>
    </div>
    <div class="zt-step">
        <div class="zt-step__marker">3</div>
        <div>
            <h3 class="zt-step__title">Step title</h3>
            <p class="zt-step__text">Step description.</p>
        </div>
    </div>
</div>
```

---

---

---

## Tracking hooks — four attributes, always

Analytics has to recognise a CTA and a form on a page it has never seen. It cannot match
on button text, because the text is the marketer's copy and you are forbidden from
normalising it, so it differs on every page. It cannot match on the URL, because the page
is new.

So every page carries four stable hooks, and they are the contract:

| attribute | on what |
|---|---|
| `data-zt-cta="demo"` | a button that leads to a demo, a booking or a trial |
| `data-zt-cta="contact"` | a button that leads to contact, enquiry or support |
| `data-zt-form="demo"` | the wrapper of a demo or booking form |
| `data-zt-form="contact"` | the wrapper of a contact or enquiry form |

**On the `<a>` itself, never a wrapper.** When a person clicks a `<span>` inside the
anchor, the browser reports the span as the clicked element. The analytics selector
resolves descendants, but only if the attribute sits on the anchor.

**A data attribute, not a class.** The body uses the theme's button classes and defines no
button CSS, so a class belongs to the theme and gets renamed during a restyle. Tracking
would die silently, with no error. Nobody restyling a page touches a `data-*`.

**Use only these four values.** They are slugs from the intent registry, so each one
resolves to a campaign code downstream. An invented value resolves to nothing.

If a button or a form is genuinely neither — a case study link, a quote request, a
newsletter signup, an event registration — leave the hook **off entirely** and say so in
the manifest. A missing attribute reports nothing, which is true. A wrong one reports a
conversion that never happened, and the number looks plausible enough that nobody checks.

### Phone, email and the booking calendar carry no hook

- **`tel:` and `mailto:` links.** Analytics matches these natively on the URL, which
  already works on any page in any country. Leave them as plain links.
- **The booking calendar.** It loads in a frame the page cannot see into, so no attribute
  on the page can observe a booking. It is measured elsewhere.

Adding a hook to any of these three adds markup for nothing.

## Form and scheduler slot — the wireframe

A form and a booking calendar are both built by the admin in HubSpot, so the body ships a
container and nothing else. **Give that container a visible wireframe.** An empty `<div>`
has no height, so the marketer opens the file, sees a gap where their form should be, and
reports the page as broken.

The wireframe shows the field list the marketer asked for, as greyed rows. That is the one
thing only they can verify.

```html
<div class="zt-hsform" id="zt-form-{slug}" data-zt-form="demo">
    <div class="zt-slot">
        <p class="zt-slot__label">Demo request form</p>
        <p class="zt-slot__note">Your admin builds this in HubSpot</p>
        <div class="zt-slot__field">First name</div>
        <div class="zt-slot__field">Work email</div>
        <div class="zt-slot__field">Company</div>
        <div class="zt-slot__btn">Request demo</div>
    </div>
</div>
```

One row per field the marketer named. The last row is the submit button, labelled with
whatever they called it.

For a booking calendar the container changes and the contents do not:

```html
<div class="zt-scheduler" data-placeholder="scheduler">
    <div class="zt-slot">
        <p class="zt-slot__label">Booking calendar</p>
        <p class="zt-slot__note">Your admin builds this for {Brand}</p>
        <div class="zt-slot__field">First name</div>
        <div class="zt-slot__field">Work email</div>
        <div class="zt-slot__field">Company</div>
        <div class="zt-slot__btn">Book a time</div>
    </div>
</div>
```

The CSS is deliberately grey, not brand colours. It must read as unfinished at a glance so
nobody mistakes it for a working form:

```css
.zt-slot {
    border: 2px dashed var(--{p}-border);
    border-radius: var(--{p}-card-radius);
    background: var(--{p}-bg-muted);
    padding: 1.15rem 1rem;
}
.zt-slot__label {
    margin: 0 0 0.2rem;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--{p}-text-muted);
}
.zt-slot__note {
    margin: 0 0 0.85rem;
    font-size: 0.75rem;
    color: var(--{p}-text-muted);
}
.zt-slot__field {
    background: var(--{p}-bg);
    border: 1px solid var(--{p}-border);
    border-radius: 4px;
    padding: 0.6rem 0.65rem;
    margin-bottom: 0.5rem;
    font-size: 0.75rem;
    color: var(--{p}-text-muted);
}
.zt-slot__btn {
    background: var(--{p}-text-muted);
    border-radius: 5px;
    padding: 0.65rem;
    text-align: center;
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--{p}-bg);
}
```

Every token here is one that all brands define, so the slot renders on any brand. It is
the only place in the body where you may style something the theme would normally own, and
only because the admin deletes the whole block at install.

## Responsive

Add at the end of the `<style>` block. One breakpoint.

```css
@media (max-width: 767px) {
    .zt-hero__grid { grid-template-columns: 1fr; gap: 2.25rem; }
    .zt-hero__media { order: -1; }
    .zt-cards { grid-template-columns: 1fr; }
    .zt-quotes { grid-template-columns: 1fr; }
    .zt-row, .zt-row--flip { grid-template-columns: 1fr; }
    .zt-row__text, .zt-row--flip .zt-row__text { order: 1; }
    .zt-row__media, .zt-row--flip .zt-row__media { order: 2; }
    .zt-step { grid-template-columns: 2.5rem 1fr; }
    .zt-step__marker { width: 2.5rem; height: 2.5rem; font-size: 0.875rem; }
    .zt-step::before { left: calc(1.25rem - 1px); top: 2.5rem; }
    .zt-stats { flex-direction: column; align-items: center; }
}

/* Buttons stay as the theme renders them at every width. The body never
   styles .button or a colourway; a full-width mobile button is a theme decision. */

@media (prefers-reduced-motion: reduce) {
    .zt-lp * { transition: none !important; }
}
```

---

## Shell Adjustments

Add at the end. Handles the sticky header and hero spacing.

```css
.zt-lp .zt-hero, .zt-lp .zt-cover { padding-top: clamp(2rem, 5vw, 4.5rem); }
.zt-lp [id] { scroll-margin-top: 6rem; }
```
