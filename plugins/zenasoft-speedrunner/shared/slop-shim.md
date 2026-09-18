# Front-end visual slop: markers & tells

For landing pages and wireframes. **Visual only.** Nothing here about links, alt text,
console logs or placeholder copy, an in-build page has dead links and grey boxes by
design, that is not slop.

Severity: 🔴 near-certain tell · 🟠 context-dependent · 🟡 fine alone, damning in a pile

---

## 1. Colour

| | Tell | Looks like |
|---|---|---|
| 🔴 | The purple gradient | `linear-gradient(135deg,#667eea,#764ba2)` |
| 🔴 | Indigo to pink | `#6366f1` `#8b5cf6` `#a855f7` `#ec4899` |
| 🔴 | Every gradient is 135deg | angle chosen by habit, not by the layout |
| 🔴 | Gradient where flat would do | buttons, badges, icon tiles, section backgrounds |
| 🟠 | Gradient text headline | `background-clip:text` + transparent fill |
| 🟠 | Tailwind slate dark mode | `#0f172a` / `#1e293b` / `#334155` untouched |
| 🟠 | Muted text via `opacity` | `.7` on body copy instead of a real muted colour |
| 🟠 | Brand colour used at one saturation only | no tints/shades, so nothing recedes |
| 🟡 | `#333 / #666 / #f5f5f5 / #fafafa` | greys picked by reflex |
| 🟠 | Colour with no ratio discipline | brand colour on 30% of the page instead of ~5% |

**Fix:** tokens only, no raw hex in components. One accent, used sparingly. If a gradient
survives, it earns its angle.

## 2. Typography

| | Tell | Looks like |
|---|---|---|
| 🔴 | Inter and nothing else | `'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif` |
| 🔴 | Poppins / Montserrat headings | the "friendly SaaS" default |
| 🔴 | No pairing | one family, one voice, whole page |
| 🟠 | `clamp()` per element, no scale | `clamp(2rem,5vw,4rem)` with unrelated values everywhere |
| 🟠 | `letter-spacing:-.02em` on all headings | uniform negative tracking regardless of size |
| 🟠 | Two weights only | 700/800 display + 400 body, nothing between |
| 🟠 | Everything centred | `text-align:center` on every section |
| 🟡 | Line length unmanaged | body copy running the full 1200px |
| 🟠 | Same heading size for every section | no hierarchy between h2s that matter and ones that do not |

**Fix:** brand face, a real pairing, one type scale, track by size, keep measure ~65ch.

## 3. Shape, shadow, spacing

| | Tell | Looks like |
|---|---|---|
| 🔴 | Uniform 16px radius | `rounded-2xl` on cards, buttons, inputs, images alike |
| 🔴 | Radius soup | 8/10/12/16/20 mixed with no rule |
| 🔴 | Soft float shadow on everything | `0 10px 30px rgba(0,0,0,.1)` on every card |
| 🟠 | `shadow-2xl` untouched | Tailwind's default elevation stack |
| 🔴 | Glassmorphism | `backdrop-filter:blur()` + `rgba(255,255,255,.1)` + white hairline |
| 🟠 | Magic-number spacing | `padding:80px 20px`, `margin-bottom:60px` |
| 🟠 | Uniform section padding | every band the same height regardless of weight |
| 🟠 | `max-width:1200px;margin:0 auto` on everything | no container system, no full-bleed |
| 🟡 | Borders *and* shadows *and* fills | three separation devices doing one job |

**Fix:** 2-3 radii on a scale, controls are not surfaces. Separate with contrast or a border;
shadow only for real elevation. Spacing from a scale.

## 4. Motion

| | Tell | Looks like |
|---|---|---|
| 🔴 | `transition:all .3s ease` | catch-all, everywhere |
| 🔴 | Universal hover lift | `translateY(-5px)` on every card, clickable or not |
| 🟠 | `scale(1.05)` on every button | |
| 🟠 | Fade-up-on-scroll on every section | IntersectionObserver + `opacity:0;translateY(20px)` |
| 🟠 | Floating blurred orbs behind the hero | drifting gradient blobs |
| 🟠 | Marquee logo strip that never stops | |
| 🟡 | AOS / animate.css from CDN | |
| 🔴 | No `prefers-reduced-motion` guard | |

**Fix:** name the properties, vary duration with distance, animate one thing per screen.

## 5. Layout & composition

| | Tell | Looks like |
|---|---|---|
| 🔴 | The three-card grid | 3 equal cards, icon, title, two lines, always |
| 🔴 | Alternating white / grey-50 bands | `#fff` then `#f9fafb` then `#fff` down the page |
| 🔴 | The stock page order | hero, logo strip, 3 features, stat row, testimonial, pricing, FAQ, CTA band, footer |
| 🔴 | Perfect symmetry throughout | every section centred, every column equal |
| 🟠 | Full-bleed brand-colour CTA band before the footer | |
| 🟠 | The stat row | three big numbers, equal weight, no source |
| 🟠 | Testimonial cards in a 3-up grid | quote, avatar circle, name, title |
| 🟠 | Everything the same width | no narrow measure, no full-bleed, no offset |
| 🟠 | Hero: centred headline + sub + two buttons + screenshot below | |
| 🟡 | Uniform density | no breathing sections, no dense ones |
| 🟠 | Grid with no focal point | nothing on the page is bigger or louder than anything else |

**Fix:** order sections by what the page must prove. Break symmetry somewhere deliberate.
One clear focal point per screen.

## 6. Imagery & iconography

| | Tell | Looks like |
|---|---|---|
| 🔴 | Emoji as icons | 🚀 ✨ 💡 🔥 ⚡ 🎯 🛡️ in feature cards |
| 🔴 | Icon in a tinted circle | 48px circle, 10% brand tint, centred glyph, every card |
| 🟠 | Mixed icon families | Font Awesome + Heroicons + an SVG someone drew |
| 🟠 | Icons at inconsistent optical weight | 1.5px strokes next to filled glyphs |
| 🟠 | Generic stock photography | smiling team round a laptop |
| 🟠 | Screenshot floating with a shadow and a browser chrome frame | |
| 🟡 | Avatar circles that are all the same stock face set | |
| 🟠 | Decorative image doing no work | fills space, says nothing |

**Fix:** one icon family, one optical weight. Product imagery or nothing.

## 7. Wireframe-stage notes

Not slop while building (expected):
- grey boxes, `Lorem ipsum`, `href="#"`, unstyled buttons, missing assets

Still slop at wireframe stage:
- the stock section order (structure is the whole point of a wireframe)
- three equal cards as the default answer to every content group
- no focal point / no hierarchy: everything the same size
- centred everything

## 8. The combo test

Any one row can be innocent. **Slop is co-occurrence.** Count:

- [ ] Inter (or Poppins) and nothing else
- [ ] A purple/indigo gradient anywhere
- [ ] 16px radius on every surface
- [ ] Soft float shadow on every card
- [ ] `transition: all .3s`
- [ ] Emoji or tinted-circle icons in a 3-card grid
- [ ] Alternating white/grey bands
- [ ] Everything centred, perfectly symmetrical
- [ ] Hover lift on every card
- [ ] No focal point: nothing dominates

**0-2** fine · **3-5** templated, needs a pass · **6+** restart the art direction, do not patch it
