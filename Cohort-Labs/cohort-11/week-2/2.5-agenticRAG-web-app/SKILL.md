---
description: Apply the Design System when designing or
  implementing UI. Use its typography, semantic colors, spacing, layout,
  radius, interaction, and visual consistency rules to keep interfaces
  precise, data-dense, accessible, and systematic.
name: design-system
---

# Design System

> Last extracted: 2026-05-13

------------------------------------------------------------------------

## Product Design Philosophy

The Design System follows a **precision-first, data-dense UI** philosophy. The
system is:

-   **Information-forward** --- every surface should earn its space; no
    decorative chrome
-   **Systematically scaled** --- all values come from a token-based
    scale, nothing is arbitrary
-   **Semantically layered** --- raw primitives (All Colors) map to
    semantic tokens (Token Colors) which map to components
-   **Accessible by default** --- color steps are chosen for sufficient
    contrast; primary text on white is near-black (#070A0E)
-   **Restrained** --- the default voice is greyscale; color is used
    purposefully to signal state, not style

------------------------------------------------------------------------

## Color System

### Architecture

The color system has two layers:

1.  **Primitive palette** (`All Colors/…`) --- raw 10-step scales, the
    source of truth
2.  **Semantic tokens** (`Token colors/…`) --- role-based aliases that
    map primitives to meaning

Always reference semantic tokens in UI code. Use raw primitives only
when defining token values.

------------------------------------------------------------------------

### Primitive Palette

Each color family runs a 10-step scale:
`900 → 800 → 700 → 600 → ★500 → 400 → 300 → 200 → 100 → 50` The `★` mark
on 500 indicates the **primary base** for that family.

#### Primary Blue (Brand Primary)

  Step   Hex
  ------ -----------
  900    `#082A5E`
  800    `#0A367B`
  700    `#0D469E`
  600    `#0044AE`
  ★500   `#115ACB`
  400    `#89B7FF`
  300    `#6196EA`
  200    `#92B7F0`
  100    `#B6CFF5`
  50     `#E7EFFC`

#### Grey (Neutral Foundation)

  Step   Hex
  ------ -----------
  ★900   `#070A0E`
  800    `#151719`
  700    `#25272B`
  600    `#2C2F32`
  500    `#4A4C4F`
  400    `#5E6062`
  300    `#8F9193`
  200    `#C1C2C3`
  100    `#DADADB`
  50     `#F0F0F1`
  25     `#FAFAFA`

> Grey has an extra `25` step (near-white surface) unique to this
> family.

#### Green (Success / Positive)

  Step   Hex
  ------ -----------
  900    `#084406`
  800    `#0A5908`
  700    `#0D720A`
  600    `#11930D`
  ★500   `#13A10E`
  400    `#42B43E`
  300    `#61C05E`
  200    `#92D490`
  100    `#B6E2B4`
  50     `#E7F6E7`

#### Red (Error / Danger / Destructive)

  Step   Hex
  ------ -----------
  900    `#581618`
  800    `#731D1F`
  700    `#942528`
  600    `#BE2F33`
  ★500   `#D13438`
  400    `#DA5D60`
  300    `#E0777A`
  200    `#EAA2A3`
  100    `#F1C0C1`
  50     `#FAEBEB`

#### Yellow (Warning / Attention)

  Step   Hex
  ------ -----------
  900    `#854D00`
  800    `#B36800`
  700    `#DB8000`
  600    `#FA9200`
  ★500   `#FFAA33`
  400    `#FFC16B`
  300    `#FFD294`
  200    `#FFE3BD`
  100    `#FFF2E0`
  50     `#FFF9F0`

#### Violet (Accent / Highlight)

  Step   Hex
  ------ -----------
  900    `#380070`
  800    `#5700AD`
  700    `#6600CC`
  600    `#7000E0`
  ★500   `#7F00FF`
  400    `#B870FF`
  300    `#D1A3FF`
  200    `#E3C7FF`
  100    `#F2E5FF`
  50     `#F7F0FF`

#### Orange (Secondary Accent)

  Step   Hex
  ------ -----------
  900    `#802400`
  800    `#B33300`
  700    `#D63D00`
  600    `#E63900`
  ★500   `#FF4405`
  400    `#FF956B`
  300    `#FFBA9E`
  200    `#FFD3C2`
  100    `#FFE9E0`
  50     `#FFF4F0`

------------------------------------------------------------------------

### Semantic Tokens

  ---------------------------------------------------------------------------------------------------------
  Token                                                     Value                   Usage
  --------------------------------------------------------- ----------------------- -----------------------
  `Token colors/Text/gray/text-gray-primary (900)`          `#070A0E`               Primary body text,
                                                                                    headings

  `Token colors/Text/gray/text-gray-secondary (500)`        `#4A4C4F`               Secondary/muted text,
                                                                                    captions, labels

  `Token colors/Background/gray/bg-white-primary (F-900)`   `#FFFFFF`               Primary page/card
                                                                                    background
  ---------------------------------------------------------------------------------------------------------

> Additional semantic tokens (borders, interactive states, surface
> layers) follow the same naming pattern:
> `Token colors/{category}/{subcategory}/{role}`.

------------------------------------------------------------------------

### Color Usage Rules

1.  **Text primary** → Grey 900 (`#070A0E`) on light backgrounds
2.  **Text secondary** → Grey 500 (`#4A4C4F`) for supporting copy,
    metadata, labels
3.  **Interactive / brand** → Primary Blue ★500 (`#115ACB`) for CTAs,
    links, focus rings
4.  **Success states** → Green ★500 (`#13A10E`) background tint: Green
    50
5.  **Error states** → Red ★500 (`#D13438`) background tint: Red 50
6.  **Warning states** → Yellow ★500 (`#FFAA33`) background tint: Yellow
    50
7.  **Surfaces** → White (`#FFFFFF`) for cards, modals; Grey 25
    (`#FAFAFA`) for page bg; Grey 50 (`#F0F0F1`) for subtle dividers
8.  **Never use raw primitive tokens in component code** --- always go
    through the semantic layer

------------------------------------------------------------------------

## Typography Hierarchy

**Font family:** `Inter Display` (all weights)

### Type Scale

  ---------------------------------------------------------------------------------------------------------------------------------
  Role          Size       Weight     Line Height       Letter Spacing        CSS
  ------------- ---------- ---------- ----------------- --------------------- -----------------------------------------------------
  H1            \~48px     700        \~56px            0                     *inferred*

  H2            \~36px     700        \~44px            0                     *inferred*

  H3            \~30px     600        \~38px            0                     *inferred*

  H4            \~28px     600        \~36px            0                     *inferred*

  **H5 /        **24px**   **500**    **32px**          **0**                 `font-size:24px; font-weight:500; line-height:32px`
  Medium**                                                                    

  **Paragraph   **16px**   **500**    **24px**          **0**                 `font-size:16px; font-weight:500; line-height:24px`
  Large /                                                                     
  Medium**                                                                    

  **Paragraph   **12px**   **400**    **18px**          **0**                 `font-size:12px; font-weight:400; line-height:18px`
  Small /                                                                     
  Regular**                                                                   
  ---------------------------------------------------------------------------------------------------------------------------------

> Rows marked *inferred* follow the geometric progression of confirmed
> steps. Verify against the typography page in Figma.

### Typography Rules

1.  **Section labels / category headings** → H5 Medium (24/32, weight
    500)
2.  **Body copy / list items / data labels** → Paragraph Large Medium
    (16/24, weight 500)
3.  **Captions / hex values / metadata** → Paragraph Small Regular
    (12/18, weight 400)
4.  **Color values in labels** always render in Grey 500; label names in
    Grey 900
5.  **No letter-spacing adjustments** --- system is letter-spacing: 0
    throughout
6.  **Line height is tight** --- ratio ≈ 1.3--1.5. Never add extra
    leading outside the type scale.

------------------------------------------------------------------------

## Spacing Rhythm

The spacing system is token-based on a **4px base unit**.

### Known Spacing Tokens

  Token                     Value
  ------------------------- ---------
  `Spacing/Spacing 0px`     `0px`
  `Spacing/Spacing 4px`     `4px`
  `Spacing/Spacing 96px`    `96px`
  `Spacing/Spacing 112px`   `112px`

### Inferred Scale (4px grid)

    4px   — micro gap (between color swatches, inline chips)
    8px   — small gap (label row stacking)
    12px  — component internal padding
    16px  — base unit (common padding, small gaps)
    24px  — section sub-grouping gap
    32px  — component-to-component gap
    40px  — section gap within a page zone
    48px  — large section padding
    64px  — inter-section spacing
    96px  — page vertical padding
    112px — page horizontal padding

### Spacing Rules

1.  **All spacing values must be multiples of 4px**
2.  **Page-level padding**: 112px horizontal, 96px vertical
3.  **Section gaps**: 40px between major content groups
4.  **Sub-section gaps**: 24px between labeled groups and their content
5.  **Item gaps**: 8px between label rows; 4px between color swatches
6.  **Inline gaps**: 2px for stacked text within a single label block

------------------------------------------------------------------------

## Border Radius Rules

> Border radius values are not explicitly documented in the extracted
> node. The following are inferred from the visual style and product
> tier (precision tools use subtle rounding).

  Context                               Radius
  ------------------------------------- ---------------------
  Cards / panels                        `8px`
  Buttons (default)                     `6px`
  Tags / badges                         `4px`
  Inputs                                `6px`
  Modals                                `12px`
  Color swatches (as seen in palette)   `0px` (flat/square)
  Avatars / image containers            `50%` (full circle)

> Verify against the component library pages in Figma. Default to `6px`
> when in doubt.

------------------------------------------------------------------------

## Layout Structure

### Page Canvas

    ┌────────────────────────────────────────────────────┐
    │  padding: 96px top/bottom, 112px left/right        │
    │  ┌──────────────────────────────────────────────┐  │
    │  │  Content area (full-width flex column)       │  │
    │  │  gap: 40px between major sections            │  │
    │  └──────────────────────────────────────────────┘  │
    └────────────────────────────────────────────────────┘

### Section Structure

Each content section follows:

    [Section Header — H5 Medium, full width]
      gap: 24px
    [Content grid — flex wrap, gap: 4px, items stretch to fill]

### Grid / Flex Patterns

-   **Content sections**: `flex-col`, `gap: 24px`, `width: 100%`
-   **Color/item grids**: `flex-wrap`, `gap: 4px`, each item
    `flex: 1 0 0`, `min-width: 1px`
-   **Label blocks**: `flex-col`, `gap: 2px`
-   **Top-level page**: `flex-col`, `gap: 40px`, `width: 100%`

### Responsive Behavior

The wrapping flex grid (`flex-wrap`) allows color swatches to reflow at
smaller widths. The `flex: 1 0 0` pattern ensures equal-width columns
that shrink uniformly.

------------------------------------------------------------------------

## Component Patterns

### Color Swatch Block (`_Color blank`)

    [Color swatch — h:60px, w:full, background = color value]
      gap: 8px
    [Label group]
      [Step number — Paragraph Large Medium, Grey 900]
      [Hex value — Paragraph Small Regular, Grey 500]

### Section Block

    [Section title — H5 Medium, Grey 900]
      gap: 24px
    [Swatch row — flex-wrap, gap:4px]
      [Color swatch block × 10]

### Reusable Pattern: Labeled Value Row

Used anywhere a value needs a name + sub-label (not just colors):

    [Primary label — 16px Medium, Grey 900]
    [Secondary value — 12px Regular, Grey 500]

Gap between rows: `2px`.

------------------------------------------------------------------------

## Interaction / Motion Language

> Motion is not explicitly defined in the extracted color guidance page.
> The following guidelines are inferred from the product tier and design
> philosophy.

### Principles

-   **Purposeful, not decorative** --- animation exists only to
    communicate state change or spatial relationship
-   **Fast** --- transitions ≤ 150ms for micro-interactions (hover,
    focus), ≤ 250ms for panel/modal transitions
-   **Easing** --- ease-out for elements entering the screen; ease-in
    for elements leaving; ease-in-out for position shifts

### Recommended Values

  Interaction                 Duration   Easing
  --------------------------- ---------- ---------------
  Button hover / focus ring   `100ms`    `ease-out`
  Input focus border          `100ms`    `ease-out`
  Dropdown / tooltip appear   `150ms`    `ease-out`
  Modal / sheet enter         `200ms`    `ease-out`
  Modal / sheet exit          `150ms`    `ease-in`
  Page transitions            `250ms`    `ease-in-out`
  Skeleton → content          `300ms`    `ease-in-out`

### State Colors (Motion-adjacent)

  State              Background tint   Border           Text
  ------------------ ----------------- ---------------- ------------
  Default            White / Grey 25   Grey 100         Grey 900
  Hover              Grey 50           Grey 200         Grey 900
  Focus              White             Blue 500 (2px)   Grey 900
  Active / Pressed   Grey 100          Grey 300         Grey 900
  Disabled           Grey 25           Grey 100         Grey 400
  Error              Red 50            Red 500          Red 700
  Success            Green 50          Green 500        Green 700
  Warning            Yellow 50         Yellow 500       Yellow 800

------------------------------------------------------------------------

## Visual Principles

1.  **Density over sprawl** --- pack information at comfortable density;
    white space is intentional, not default
2.  **Hierarchy through weight and size, not decoration** ---
    differentiate levels via font weight (400 vs 500) and size, not
    color or ornament
3.  **Color = signal** --- grey is the default; color communicates
    status, brand, or action
4.  **Flat depth** --- no gradients, no shadows by default; depth via
    background-color steps (Grey 25 → White)
5.  **Systematic consistency** --- if a value isn't in the token list,
    it doesn't belong in the UI

------------------------------------------------------------------------

## UI Consistency Rules

1.  **Use semantic tokens** --- never hardcode hex values in component
    styles; always reference `Token colors/…`
2.  **Type roles are fixed** --- don't mix type scale roles (e.g. don't
    use H5 for body copy)
3.  **Spacing must be on-grid** --- every gap, padding, and margin must
    be a multiple of 4px
4.  **Color families for status** --- Blue=brand/info, Green=success,
    Red=error/danger, Yellow=warning, Violet=accent, Orange=secondary
    accent
5.  **Grey 900 for primary text, Grey 500 for secondary** --- do not use
    other grey steps for body text
6.  **White for elevated surfaces, Grey 25 for page background, Grey 50
    for subtle dividers/hover**
7.  **Inter Display is the sole typeface** --- no mixing fonts
8.  **0 letter-spacing** --- do not add tracking unless explicitly
    specified in a style
9.  **Color swatches are square** (radius: 0) --- do not round
    swatch/palette UI elements
10. **Section titles use H5 (24px Medium)** --- not H4 or any other step

------------------------------------------------------------------------

## Reusable Patterns

### Semantic Status Badge

    background: [Color] 50
    border: 1px solid [Color] 200
    text: [Color] 700, Paragraph Small Medium
    border-radius: 4px
    padding: 2px 8px

Replace `[Color]` with Green/Red/Yellow/Blue based on status.

### Data Label Pair

``` html
<div style="display:flex; flex-direction:column; gap:2px;">
  <span style="font:500 16px/24px 'Inter Display'; color:#070A0E;">Label</span>
  <span style="font:400 12px/18px 'Inter Display'; color:#4A4C4F;">Sub-value</span>
</div>
```

### Section Block

``` html
<section style="display:flex; flex-direction:column; gap:24px; width:100%;">
  <h2 style="font:500 24px/32px 'Inter Display'; color:#070A0E; margin:0;">Section Title</h2>
  <!-- content -->
</section>
```

### Page Wrapper

``` html
<main style="
  padding: 96px 112px;
  display: flex;
  flex-direction: column;
  gap: 40px;
  background: #FFFFFF;
">
  <!-- sections -->
</main>
```

### Flex-Wrap Item Grid

``` html
<div style="display:flex; flex-wrap:wrap; gap:4px; align-items:flex-start; width:100%;">
  <!-- each item: flex: 1 0 0; min-width: 1px -->
</div>
```

------------------------------------------------------------------------

## Implementation Guidance

### CSS Custom Properties Setup

``` css
/* Primitives — define once, reference via semantic tokens */
:root {
  /* Grey */
  --color-grey-900: #070A0E;
  --color-grey-800: #151719;
  --color-grey-700: #25272B;
  --color-grey-600: #2C2F32;
  --color-grey-500: #4A4C4F;
  --color-grey-400: #5E6062;
  --color-grey-300: #8F9193;
  --color-grey-200: #C1C2C3;
  --color-grey-100: #DADADB;
  --color-grey-50:  #F0F0F1;
  --color-grey-25:  #FAFAFA;

  /* Blue */
  --color-blue-900: #082A5E;
  --color-blue-800: #0A367B;
  --color-blue-700: #0D469E;
  --color-blue-600: #0044AE;
  --color-blue-500: #115ACB;
  --color-blue-400: #89B7FF;
  --color-blue-300: #6196EA;
  --color-blue-200: #92B7F0;
  --color-blue-100: #B6CFF5;
  --color-blue-50:  #E7EFFC;

  /* Green */
  --color-green-900: #084406;
  --color-green-800: #0A5908;
  --color-green-700: #0D720A;
  --color-green-600: #11930D;
  --color-green-500: #13A10E;
  --color-green-400: #42B43E;
  --color-green-300: #61C05E;
  --color-green-200: #92D490;
  --color-green-100: #B6E2B4;
  --color-green-50:  #E7F6E7;

  /* Red */
  --color-red-900: #581618;
  --color-red-800: #731D1F;
  --color-red-700: #942528;
  --color-red-600: #BE2F33;
  --color-red-500: #D13438;
  --color-red-400: #DA5D60;
  --color-red-300: #E0777A;
  --color-red-200: #EAA2A3;
  --color-red-100: #F1C0C1;
  --color-red-50:  #FAEBEB;

  /* Yellow */
  --color-yellow-900: #854D00;
  --color-yellow-800: #B36800;
  --color-yellow-700: #DB8000;
  --color-yellow-600: #FA9200;
  --color-yellow-500: #FFAA33;
  --color-yellow-400: #FFC16B;
  --color-yellow-300: #FFD294;
  --color-yellow-200: #FFE3BD;
  --color-yellow-100: #FFF2E0;
  --color-yellow-50:  #FFF9F0;

  /* Violet */
  --color-violet-900: #380070;
  --color-violet-800: #5700AD;
  --color-violet-700: #6600CC;
  --color-violet-600: #7000E0;
  --color-violet-500: #7F00FF;
  --color-violet-400: #B870FF;
  --color-violet-300: #D1A3FF;
  --color-violet-200: #E3C7FF;
  --color-violet-100: #F2E5FF;
  --color-violet-50:  #F7F0FF;

  /* Orange */
  --color-orange-900: #802400;
  --color-orange-800: #B33300;
  --color-orange-700: #D63D00;
  --color-orange-600: #E63900;
  --color-orange-500: #FF4405;
  --color-orange-400: #FF956B;
  --color-orange-300: #FFBA9E;
  --color-orange-200: #FFD3C2;
  --color-orange-100: #FFE9E0;
  --color-orange-50:  #FFF4F0;

  /* Semantic tokens */
  --text-primary:   var(--color-grey-900);
  --text-secondary: var(--color-grey-500);
  --bg-primary:     #FFFFFF;
  --bg-surface:     var(--color-grey-25);
  --bg-subtle:      var(--color-grey-50);
  --brand:          var(--color-blue-500);

  /* Spacing */
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
  --space-28: 112px;
}
```

### Typography Classes

``` css
.type-h5 {
  font-family: 'Inter Display', sans-serif;
  font-size: 24px;
  font-weight: 500;
  line-height: 32px;
  letter-spacing: 0;
}

.type-body-lg {
  font-family: 'Inter Display', sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  letter-spacing: 0;
}

.type-body-sm {
  font-family: 'Inter Display', sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 18px;
  letter-spacing: 0;
}
```

### Figma Token Path Convention

When reading or writing to Figma: - Primitives:
`All Colors/{Family}/{Step}` e.g. `All Colors/Blue/★ 500` - Semantic:
`Token colors/{category}/{subcategory}/{role}`
e.g. `Token colors/Text/gray/text-gray-primary (900)` - Spacing:
`Spacing/Spacing {N}px` e.g. `Spacing/Spacing 4px` - Typography:
`Typography/{Role}/{Weight}` e.g. `Typography/H5/Medium`

------------------------------------------------------------------------

## Quick Reference Card

    FONT        Inter Display
    TEXT-1      #070A0E (Grey 900)
    TEXT-2      #4A4C4F (Grey 500)
    BG          #FFFFFF (White)
    SURFACE     #FAFAFA (Grey 25)
    SUBTLE      #F0F0F1 (Grey 50)
    BRAND       #115ACB (Primary Blue 500)
    SUCCESS     #13A10E (Green 500)
    ERROR       #D13438 (Red 500)
    WARNING     #FFAA33 (Yellow 500)
    ACCENT      #7F00FF (Violet 500)

    PAGE-PAD    112px H / 96px V
    SECTION-GAP 40px
    SUBSEC-GAP  24px
    ITEM-GAP    8px
    MICRO-GAP   4px

    RADIUS-SM   4px
    RADIUS-MD   6px
    RADIUS-LG   8px
    RADIUS-XL   12px
