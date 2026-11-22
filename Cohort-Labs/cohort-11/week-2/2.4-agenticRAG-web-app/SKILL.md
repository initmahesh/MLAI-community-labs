---
name: design-system
description: Design and build premium, production-quality frontend interfaces (SaaS, AI workspaces, document and chat apps) on top of an existing backend. Use when redesigning or implementing UI. Inspect the existing app and its API integration first, preserve every backend contract exactly, restructure the layout and components (not just the colors), apply a token-based design system with a distinctive visual identity, build responsive layouts and polished states, then validate the real rendered UI against the original screenshot. When the user supplies a reference screenshot as the design target, recreate it faithfully (layout, proportions, palette, hierarchy) using the app's real data, and compare the running app against it until the differences are gone.
---

# Design System: Premium Frontend Skill

> Version 2.1. Extends the original token system (palette, 4px grid, Inter
> type) into a full product-design and delivery workflow. v2.1 adds the
> **structural redesign mandate**: recoloring the old layout is a failed
> redesign (Section 3), and the document-workspace and AI-copilot patterns
> (Sections 7 and 9) that make a redesign visibly different. v2.2 adds
> **reference-driven redesign** (Section 15): when the user supplies a
> target screenshot, it is the specification, recreated with real data and
> verified by comparing the running app against it.

You are not applying a theme. You are acting as a senior product designer
and frontend engineer who has been handed a working app with a working
backend and asked to make the frontend look and feel like a real
commercial product, without breaking anything underneath it.

---

## 1. The Prime Directive: The Integration Boundary Is Frozen

Most frontend redesigns that go wrong go wrong here. Before any visual
work, treat the following as read-only.

**Never, under any circumstances:**

- Modify backend code, workflows (n8n, Zapier, serverless functions), or
  infrastructure.
- Change webhook or API URLs, HTTP methods, headers, or auth.
- Change request payload structure: JSON keys, `FormData` field names,
  binary vs. multipart encoding, query parameters.
- Change how responses are parsed or what shape the UI assumes.
- Replace or bypass the real backend with mocks, hardcoded answers or
  fake delays in shipped code.
- Add another AI provider, SDK or backend service.
- Remove an existing feature. Redesign it, do not delete it.
- Invent data the backend did not return (see Section 8).

**The rule of thumb:** the network tab before and after the redesign must
show the same requests with the same payloads. Only the pixels change.

If something about the integration is unclear, **investigate it** (read the
code, read the workflow JSON, watch the network tab). Never guess and never
"clean it up".

Where UI work genuinely requires touching code that sits next to an
integration (for example moving an upload handler into a new component),
move the logic verbatim, keep identical URL strings, field names and parse
logic, and prove it with the diff check in Section 11.

---

## 2. The Four-Phase Workflow

Do not skip phases. Do not start Phase 3 before finishing Phase 1.

### Phase 1: Inspect (read before you write)

1. Read this entire skill. If the user supplied a reference screenshot,
   study it now and start the reference inventory (Section 15.1).
2. Map the frontend: framework, build tooling, entry files, component or
   file structure, styling approach, state management.
3. Locate and **write down** every integration point:
   - Every `fetch` / `XMLHttpRequest` / SDK call: URL, method, headers,
     body shape, field names.
   - Upload implementation (how the binary is sent, which field name).
   - Chat implementation (request payload, how the user message and any
     session or context is attached).
   - Response parsing (which fields are read, how errors and malformed
     responses are handled, how citations or reasoning are extracted).
   - Existing state: what is tracked (file loaded, indexing, messages,
     busy flag) and which transitions the UI depends on.
4. If a backend workflow or API spec exists (for example an n8n JSON),
   read it for context only: node names, webhook paths, response
   fields. Do not edit it.
5. Run the app as it is today. Take baseline screenshots. Capture the
   baseline network requests (URL, payload, response) for each feature.
6. Write a **structural inventory of the baseline**: how many regions
   there are and how they are arranged and proportioned, what the
   navigation is, what the document toolbar and page navigation look
   like, how messages, citations and reasoning are composed, what the
   empty state contains. Phase 4 compares the result against this list.
7. Produce a **preservation list**: every feature and integration that
   must still work at the end (for a document app typically: upload,
   embedded viewer, thumbnails, page navigation, zoom, question
   answering, in-session conversation, citations, evidence excerpts,
   reasoning, every webhook).

### Phase 2: Design (decide before you build)

1. Write the **identity statement** (Section 3).
2. Choose the semantic tokens you will use (Section 5). Define them once.
3. Decide the **new composition** (Section 7.1; when the user supplied a
   reference screenshot the composition is the reference's, see Section
   15) and write a
   region-by-region **structural difference list** against the baseline
   inventory: what moves, what is merged or split, what is new, what
   changes proportion. If that list is short, or only mentions color,
   type, shadow or radius, the design is not ready (see the
   structural-difference test in Section 3).
4. Sketch the layout at four widths (Section 7) before writing CSS.
5. List every state each screen can be in (Section 9) and decide how
   each one looks.
6. Identify what the backend actually returns, since that determines what
   the UI may show (Section 8).

### Phase 3: Implement

1. Add tokens first, components second, screens last.
2. Build reusable components (button, input, badge, file card, message,
   source chip, toast, skeleton) before assembling screens.
3. Keep integration code untouched or moved verbatim.
4. Commit logically: tokens, components, layout, states, polish.

### Phase 4: Validate (see Section 11)

The work is not done when the code compiles. It is done when the real
rendered UI at four viewport widths has been inspected, the preservation
list passes, the structural-difference test (Section 3) passes against
the baseline screenshot, and the visual QA checklist is clean. Iterate
until it feels professionally designed.

---

## 3. Product Design Thinking

### Think about the user's job, not the component list

Ask what the user is trying to accomplish and what they are anxious about.
For a contract-review user: "Is this answer real, and where in my
document does it come from?" For a data-tool user: "Can I trust these
numbers?" Design hierarchy around that anxiety. In AI products, **trust
signals (sources, status, honest loading and error states) are core
features, not decoration.**

### Write the identity statement first

Before choosing a single color, write one sentence:

> "A [adjective] [domain] workspace that feels [two qualities], with one
> signature detail: [signature]."

Example: "A calm, precise legal workspace that feels trustworthy and fast,
with one signature detail: a deep ink header and a single warm accent
reserved for primary actions and citations."

The signature detail is what makes the product feel designed rather than
templated. Choose **one** and apply it consistently (a header treatment, an
accent used only for citations, a distinctive empty-state illustration, a
particular type pairing). One strong move beats five weak ones.

### Redesign the structure, not just the skin

The most common failed redesign keeps the old layout, the old component
arrangement and the old proportions, and only swaps the palette, font,
radius and shadows. A user who asked for a redesign and gets this will
(rightly) say "nothing changed". Treat a reskin as a defect.

**What counts as a structural change, and what does not:**

| Counts | Does not count |
|---|---|
| Regions rearranged, added, merged or removed (for example a navigation rail, a thumbnail rail, a document header) | New colors |
| Changed proportions (document becomes dominant, assistant gets a fixed comfortable width) | New font or font sizes |
| Different component composition (answer / evidence / sources / reasoning as separate blocks instead of one bubble) | New border radius |
| Different navigation model and toolbar organization | New shadows or gradients |
| New empty and onboarding composition | Icon swaps |
| Reworked small-screen layout (not a shrunken desktop layout) | Spacing tweaks inside the same boxes |

**The structural-difference test (run it in Phase 2 and again in Phase 4):**
put the baseline screenshot and the new screenshot side by side and
squint until only the region boundaries remain. If the two outlines
match, the redesign fails, however good the new palette looks. The new UI
must differ visibly in all of these: overall composition, navigation,
document workspace, document toolbar, page thumbnails, assistant layout,
answer presentation, citation component, input/composer, empty state and
responsive behavior.

**Make independent design decisions.** (The exception: a reference
screenshot the user explicitly supplies as the design target *is* the
specification; see Section 15.) A previous mockup, an earlier
attempt or the existing layout is input, not a specification. Do not
reproduce it. Choose the composition that best serves the user's job, even
if it differs from all of them, and be able to say why.

**Prefer product-grade composition over generic cards.** Think of how
the best document tools are put together: a slim navigation shell, a
document that dominates the screen with its own header and toolbar, and a
side-by-side copilot that reads like part of the product, not like a
second embedded widget.

### Take inspiration, not screenshots

Study the craft of Linear (density, keyboard focus, restraint), Stripe
(typographic hierarchy, trust), Vercel (contrast, monochrome confidence),
Notion (calm document surfaces). Extract principles. Do not copy layouts,
logos, or distinctive visual assets.

### Hierarchy through contrast and structure, not boxes

The most common amateur tell is **a white rounded card around everything**.
Prefer:

- Full-height **panes** separated by a single 1px border, instead of
  floating cards with gaps.
- Background steps (page, surface, sunken) to show structure.
- Cards only for things that are genuinely discrete objects (a file, a
  source, a message), not for layout regions.
- Typography weight and size to separate levels before reaching for color
  or ornament.

### Density is a feature

Professional tools are comfortably dense. Whitespace is intentional, not
a default. Avoid huge empty regions: when a pane is empty, the empty state
should teach or invite action (Section 9), not float a tiny icon in a
void.

---

## 4. Anti-Patterns (the "generic AI dashboard" checklist)

Reject these on sight (unless a user-supplied reference screenshot
deliberately uses one, such as pill chips or a soft background wash: then
the reference wins, see Section 15):

| Avoid | Do instead |
|---|---|
| White card around every region | Panes, dividers, background steps |
| Large radius on everything (16px+) | 4/6/8px system; 12px only for overlays and the composer |
| Random gradients, mesh blobs, glow | Flat surfaces; one purposeful accent |
| Glassmorphism / blur backdrops | Solid surfaces with 1px borders |
| Four identical stat cards across the top | Show only data that exists, in the layout it deserves |
| Oversized headings (40px+) inside the app UI | 20px page title, 16px section title |
| Browser-default inputs, buttons, scrollbars | Fully styled controls with all states |
| Decorative icons and emoji as ornament | Icons only when they aid scanning or recognition |
| Placeholder lorem / fake metrics to fill space | Honest empty states |
| Centered tiny content in a giant empty panel | Fill the space with guidance, or restructure the layout |
| Color used as decoration | Color = signal (brand, status, action) |
| Animation everywhere | Motion only for state change and spatial continuity |
| Same two-column layout, new colors | Re-compose the regions (Section 7.1) and pass the structural-difference test (Section 3) |
| A raw PDF plugin dropped into a box | Document header, designed toolbar, thumbnail rail, reading canvas (Section 9.2.1) |
| Generic chatbot bubbles for every message | A question row plus a structured answer block (Section 9.3) |
| One giant bubble holding answer, citations and reasoning | Separate answer, evidence, sources and reasoning blocks |
| Large citation cards stacked down the thread | Compact expandable evidence rows |
| Navigation items for features that do not exist | Only real destinations and actions (Section 8) |

---

## 5. Design Tokens

All visual values come from tokens. Components reference **semantic**
tokens only. Never hardcode a hex value in component styles.

### 5.1 Primitive palette (preserved from v1)

Each family runs `900 → 50`. `★` marks the base step.

| Step | Blue (brand) | Grey (neutral) | Green | Red | Yellow | Violet | Orange |
|---|---|---|---|---|---|---|---|
| 900 | `#082A5E` | ★ `#070A0E` | `#084406` | `#581618` | `#854D00` | `#380070` | `#802400` |
| 800 | `#0A367B` | `#151719` | `#0A5908` | `#731D1F` | `#B36800` | `#5700AD` | `#B33300` |
| 700 | `#0D469E` | `#25272B` | `#0D720A` | `#942528` | `#DB8000` | `#6600CC` | `#D63D00` |
| 600 | `#0044AE` | `#2C2F32` | `#11930D` | `#BE2F33` | `#FA9200` | `#7000E0` | `#E63900` |
| 500 | ★ `#115ACB` | `#4A4C4F` | ★ `#13A10E` | ★ `#D13438` | ★ `#FFAA33` | ★ `#7F00FF` | ★ `#FF4405` |
| 400 | `#89B7FF` | `#5E6062` | `#42B43E` | `#DA5D60` | `#FFC16B` | `#B870FF` | `#FF956B` |
| 300 | `#6196EA` | `#8F9193` | `#61C05E` | `#E0777A` | `#FFD294` | `#D1A3FF` | `#FFBA9E` |
| 200 | `#92B7F0` | `#C1C2C3` | `#92D490` | `#EAA2A3` | `#FFE3BD` | `#E3C7FF` | `#FFD3C2` |
| 100 | `#B6CFF5` | `#DADADB` | `#B6E2B4` | `#F1C0C1` | `#FFF2E0` | `#F2E5FF` | `#FFE9E0` |
| 50 | `#E7EFFC` | `#F0F0F1` | `#E7F6E7` | `#FAEBEB` | `#FFF9F0` | `#F7F0FF` | `#FFF4F0` |

Grey also has a `25` step: `#FAFAFA` (near-white page surface).

Primitives are the source of truth. Define them once; never reference
them from components.

### 5.2 Semantic tokens (extended in v2)

```css
:root {
  /* Surfaces */
  --bg-app:        var(--grey-25);    /* page background */
  --bg-surface:    #FFFFFF;           /* panes, message bubbles, inputs */
  --bg-sunken:     var(--grey-50);    /* wells, hover rows, code, tracks */
  --bg-inverse:    var(--grey-900);   /* dark chrome, tooltips */
  --bg-shell:      var(--blue-900);   /* optional branded header */

  /* Text */
  --text-primary:   var(--grey-900);  /* headings, body */
  --text-secondary: var(--grey-500);  /* supporting copy, metadata */
  --text-tertiary:  var(--grey-400);  /* placeholders, timestamps */
  --text-disabled:  var(--grey-300);  /* NOT for readable text (fails AA) */
  --text-inverse:   #FFFFFF;
  --text-link:      var(--blue-500);

  /* Borders */
  --border-subtle:  var(--grey-100);  /* dividers inside a surface */
  --border-default: var(--grey-200);  /* inputs, cards */
  --border-strong:  var(--grey-300);  /* hover on inputs */
  --border-focus:   var(--blue-500);

  /* Brand / interactive */
  --brand:          var(--blue-500);
  --brand-hover:    var(--blue-600);
  --brand-active:   var(--blue-700);
  --brand-subtle:   var(--blue-50);   /* selected, user bubble, hover wash */
  --brand-border:   var(--blue-200);

  /* Status: bg / border / text per family */
  --success-bg: var(--green-50);  --success-border: var(--green-200);  --success-text: var(--green-700);
  --danger-bg:  var(--red-50);    --danger-border:  var(--red-200);    --danger-text:  var(--red-700);
  --warning-bg: var(--yellow-50); --warning-border: var(--yellow-200); --warning-text: var(--yellow-800);
  --info-bg:    var(--blue-50);   --info-border:    var(--blue-200);   --info-text:    var(--blue-700);

  /* Accent: the signature detail (pick ONE use, see Section 3) */
  --accent:         var(--orange-500);
  --accent-subtle:  var(--orange-50);
}
```

Primitives are declared as `--grey-900`, `--blue-500`, etc. from the
table above. Dark mode, if required, is implemented by redefining the
**semantic** layer under `@media (prefers-color-scheme: dark)` and a
`[data-theme="dark"]` override. Components never change.

### 5.3 Typography

**Family:** `Inter` (use `Inter Display` for 20px and above if available),
fallback `system-ui, -apple-system, "Segoe UI", sans-serif`. Load with
`font-display: swap`. Monospace (`ui-monospace, "SF Mono", Menlo`) only for
clause references, IDs and code.

```css
:root {
  --font-sans: "Inter", "Inter Display", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, monospace;
}
```

Enable `font-variant-numeric: tabular-nums` wherever numbers must align
(file sizes, progress, counts, timestamps).

The scale is tuned for **application UI**, not marketing pages:

| Role | Size / Line | Weight | Use |
|---|---|---|---|
| Display | 32 / 40 | 600 | Marketing or empty-hero only; never inside working panes |
| Page title | 20 / 28 | 600 | One per screen |
| Section title | 16 / 24 | 600 | Pane and panel headings |
| Body | 14 / 22 | 400 | Chat messages, descriptions (use 15/24 for long-form reading) |
| Body strong | 14 / 22 | 500 | Names, emphasis, table headers |
| Label | 13 / 20 | 500 | Buttons, form labels, tabs |
| Caption | 12 / 18 | 400 | Metadata, timestamps, helper text |
| Overline | 11 / 16 | 600 | Optional small caps label; the only place letter-spacing (+0.04em) is allowed |

Rules:

1. One typeface family. Hierarchy comes from size and weight (400 / 500 /
   600), not from mixing fonts or colors.
2. Letter-spacing is 0 everywhere except Overline.
3. Max line length for reading text: about 70 characters (`max-width: 68ch`
   or a 720px message column).
4. Primary text is Grey 900, secondary is Grey 500, tertiary is Grey 400.
   Grey 300 and lighter never carry readable text.
5. Never set body text below 14px in chat or document UIs. Inputs are at
   least 16px on mobile to prevent iOS zoom-on-focus.

### 5.4 Spacing (4px base unit)

```css
:root {
  --space-1: 4px;   --space-2: 8px;   --space-3: 12px;  --space-4: 16px;
  --space-5: 20px;  --space-6: 24px;  --space-8: 32px;  --space-10: 40px;
  --space-12: 48px; --space-16: 64px;
}
```

Every gap, padding and margin is a multiple of 4px. Typical use:

- 4px: icon-to-text, badge padding block
- 8px: between related controls, message internals
- 12px: component padding (dense), gap between messages in a group
- 16px: standard pane padding, form field gap
- 24px: between sections within a pane
- 32px+: between major regions (rare inside an app shell)

Page-level padding scales down with the viewport (see Section 7). The
v1 rule of 112px horizontal / 96px vertical is for static presentation
pages only and must **not** be used inside an application shell.

### 5.5 Radius

| Context | Radius |
|---|---|
| Badges, chips, tags, small controls | `4px` |
| Buttons, inputs, menu items | `6px` |
| Cards, file cards, source cards, panes | `8px` |
| Composer, popovers, modals, sheets | `12px` |
| Avatars, spinner, status dots | `50%` |

Default to `6px` when in doubt. Do not exceed 12px anywhere except
circular elements (reference mode, Section 15.4, may raise cards to 16px
and use full-pill chips and buttons). Nested radii: inner radius = outer radius minus the
padding (when padding is small).

### 5.6 Elevation

Depth is created by **1px borders first, soft shadow second**.

```css
:root {
  --shadow-xs: 0 1px 2px rgba(7, 10, 14, 0.06);
  --shadow-sm: 0 1px 3px rgba(7, 10, 14, 0.08), 0 1px 2px rgba(7, 10, 14, 0.04);
  --shadow-md: 0 4px 12px rgba(7, 10, 14, 0.08);
  --shadow-lg: 0 12px 32px rgba(7, 10, 14, 0.14);
}
```

| Level | Use |
|---|---|
| none + border | Panes, inputs, resting cards |
| `--shadow-xs` | Buttons (primary), message bubbles (optional) |
| `--shadow-sm` | Hovered cards, sticky headers on scroll |
| `--shadow-md` | Dropdowns, composer when focused, toasts |
| `--shadow-lg` | Modals, mobile sheets |

No colored glows. No stacked heavy shadows. If a screenshot looks "puffy",
remove shadows until it does not.

### 5.7 Motion

| Interaction | Duration | Easing |
|---|---|---|
| Hover, focus ring, button press | 100ms | ease-out |
| Dropdown, tooltip, toast enter | 150ms | ease-out |
| Panel, sheet, modal enter | 200ms | ease-out |
| Panel, sheet, modal exit | 150ms | ease-in |
| Skeleton to content | 200ms | ease-in-out |

Animate only `opacity` and `transform`. Always honor reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
```

### 5.8 Icons

Use **one** icon set (for example Lucide or Phosphor) at a consistent
stroke width (1.5 or 1.75px) and consistent sizes (16px inline, 20px
standalone, 24px empty state). Icons inherit `currentColor`. Icon-only
buttons need an accessible name (`aria-label`) and a tooltip. Do not mix
filled and outline sets. Never use emoji as UI icons.

---

## 6. Interaction States (every interactive element)

Every control implements **all** of these. A control missing a state is
unfinished.

| State | Treatment |
|---|---|
| Default | Defined surface, border and text |
| Hover | One step darker or `--bg-sunken`; cursor pointer for actions |
| Focus-visible | 2px `--border-focus` ring with 2px offset; never remove outline without replacement |
| Active / pressed | One step darker again; optional `translateY(0.5px)` |
| Disabled | `--bg-sunken`, `--text-disabled`, `cursor: not-allowed`, `aria-disabled` |
| Loading | Inline spinner, label retained or replaced, width does not jump |
| Error | `--danger-border`, helper text in `--danger-text`, `aria-invalid` |
| Success | `--success-*` tokens, used briefly, not permanently |

Use `:focus-visible`, not `:focus`, so mouse users do not see rings.

---

## 7. Layout and Responsiveness

### 7.1 Application shell: three zones

A document-intelligence app is three zones, not "a PDF card and a chat
card":

```
┌─────┬──────────────────────────────────────────┬─────────────────┐
│  A  │ B  Document header: name · status · acts │ C  Assistant    │
│ nav │ B  Toolbar: page n/N · zoom · fit · …    │    header       │
│     ├────────┬─────────────────────────────────┤    Thread       │
│     │ thumbs │ Reading canvas (dominant)       │    (scrolls)    │
│     │ rail   │                                 │    Composer     │
└─────┴────────┴─────────────────────────────────┴─────────────────┘
```

**Zone A: navigation and application shell.** Either a slim 48 to 56px
left rail (icon buttons with tooltips and `aria-label`s) or a 48 to 56px
top bar. Contains the brand mark and wordmark, a clear workspace
hierarchy (Workspace › Document name), and document actions that really
exist in the app (Upload, Replace, Remove, Open in new tab). Navigation
entries must point at real destinations (see Section 8); a nav item for a
feature the app does not have is invented capability.

**Zone B: document workspace (primary).** The document is the focus.
Stack: document header, toolbar, then thumbnail rail plus reading
canvas (details in Section 9.2.1). At ≥ 1280px the document zone gets
the majority of the width (about 55 to 65%). Use the available space
intelligently: no outer gutters around the canvas, no wasted bands.

**Zone C: AI assistant workspace.** A copilot of a comfortable, bounded
width (about 360 to 440px, for example `clamp(360px, 32vw, 440px)`),
full height, with its own header, scrolling thread and docked composer.
It must feel like part of the product, not a second embedded card.

Reference grid (a starting point, not a mandate):

```css
.shell { display: grid; height: 100dvh; min-height: 0;
  grid-template-columns: 56px minmax(0, 1fr) clamp(360px, 32vw, 440px); }
.doc-zone { display: grid; grid-template-rows: auto auto minmax(0, 1fr); min-width: 0; min-height: 0; }
.doc-body { display: grid; grid-template-columns: 112px minmax(0, 1fr); min-height: 0; }
```

When the user supplied a reference screenshot, its composition replaces
this default (Section 15). Otherwise you may choose a different
arrangement (for example a top bar instead of a
rail, a collapsible assistant, a resizable divider) **if it gives a better
experience and passes the structural-difference test** (Section 3). You
may not fall back to "header plus two equal cards".

General rules:

- Use `height: 100dvh` (not `vh`) with the zones scrolling
  independently. The page itself does not scroll.
- Zones are full-height panes separated by single 1px borders (no gap, no
  outer cards).
- Branding is a small mark plus wordmark, not a banner.
- Constrain readable columns (messages, forms) to about 720px, or to the
  assistant's own width, and center them where there is spare room. Never
  stretch chat lines across 1400px.

### 7.2 Breakpoints

| Range | Layout |
|---|---|
| ≥ 1280px (desktop) | Three zones: nav rail, document workspace with thumbnail rail, assistant. Document dominant |
| 1024 to 1279px (laptop) | Same zones, assistant at its minimum width, thumbnail rail narrower or collapsed to icons, tighter padding (16px) |
| 768 to 1023px (tablet) | Nav becomes a top bar. Thumbnail rail becomes a toggleable drawer. Assistant becomes a slide-over panel or a collapsible side panel; the document stays the base layer |
| < 768px (mobile) | **Single pane at a time** with a segmented control (Document / Assistant); thumbnails open in a sheet; composer docked to the bottom with `env(safe-area-inset-bottom)`; document opens full-screen |

Rules for small screens: do not simply shrink the desktop layout. Rethink
it:

- Replace side-by-side panes with a tab or segmented switcher, a bottom
  sheet, or a full-screen document viewer with a back button.
- Touch targets are at least 44 x 44px.
- Use `dvh`, handle the on-screen keyboard (composer stays visible), and
  avoid fixed elements that cover content.
- Hide secondary metadata behind a disclosure, never behind clipped text.
- Test long filenames (truncate with ellipsis in the middle or end,
  full name in `title`/tooltip).

### 7.3 Responsive checklist

- No horizontal page scroll at 320px width.
- Text wraps, never overflows its container (`min-width: 0` on flex
  children, `overflow-wrap: anywhere` for long tokens).
- Document preview (PDF `<iframe>`/`<embed>`/viewer) has a visible
  fallback ("Open in new tab" / download link) when embedding is not
  supported, which is common on mobile Safari.

---

## 8. Data Honesty: Never Invent Capability

The UI may only present what the existing frontend and backend actually
provide. This is a hard rule, and a trust issue in AI products.

1. **No fake data.** No placeholder stats, fabricated clause counts,
   made-up risk scores, invented page numbers, fake confidence values.
   If a number or label is not in real data, it does not appear.
2. **No fake progress.** `fetch` does not expose upload progress.
   Without real progress events (for example `XMLHttpRequest.upload.onprogress`
   that the existing code already uses), show an **indeterminate**
   indicator, never a percentage animation that is not tied to real
   events. Backend processing (embedding, indexing) is indeterminate
   unless the backend reports progress.
3. **No fake steps.** Do not display "Analyzing clauses... Checking risk..."
   unless the frontend genuinely knows those steps occurred. A generic
   "Searching the contract..." is acceptable only if it accurately
   describes the request in flight.
4. **Conditional UI.** Citations, reasoning and metadata sections render
   **only when the response contains them**. When absent, the layout
   collapses cleanly without empty headings or "N/A" placeholders.
5. **Insights come from real data.** "Contract insights" are derived from
   what is already available: file name, size, type, upload and index
   status, and fields present in actual AI responses. If there is nothing
   more, say less. Do not pad.
6. **Suggested questions are real input.** Suggestion chips are
   frontend-authored prompts that are sent through the *exact same*
   chat path as typed messages. Keep them generic to the document type,
   and do not imply the backend has pre-computed answers.
7. **Don't overclaim.** Reasoning from a model is presented as "Model
   reasoning", not as verified analysis. AI answers carry an
   unobtrusive "AI-generated, verify against the source" note somewhere
   persistent (footer of composer or help text), not on every message.
8. **Never hardcode responses** to make a screenshot look good.
9. **Navigation and actions are real.** Every nav item, toolbar button and
   menu entry maps to something the app already does. No dead links to
   "Dashboard", "History", "Settings" or "Share" unless they exist. An
   action the viewer library cannot perform is not shown.
10. **Conversation history means this session's thread.** Show the
    messages the app already keeps. Do not add a saved-conversations list,
    history the app does not keep or persistence it does not have. Stamping a
    message with the client time when it is created or received is honest and
    fine.
11. **Citation navigation is conditional.** A citation is clickable (jumps
    the PDF to a page) only if the response carries a real page number
    **and** the existing viewer integration can navigate to it. Otherwise
    show the page number as plain text. Never imply navigation works when it
    does not, and never invent a page, section title or excerpt.
12. **Reference elements without backing data.** When a reference
    screenshot shows something the app cannot back (a notification dot, a
    "Sample Contract" tab, "up to 10MB", "Trusted by professionals"), follow
    the mapping rules in Section 15.3: reproduce the visual slot, never the
    fiction.

---

## 9. Component and State Specifications

For each component below, design and implement every listed state.

### 9.1 Shell and navigation (Zone A)

Brand mark (SVG, not an emoji) plus wordmark, a workspace hierarchy
(Workspace › current document, truncated), and document actions that
exist in the app. Implemented as a 48 to 56px rail or top bar (Section
7.1) with `--border-subtle` separation (or `--bg-shell` with
`--text-inverse` if the identity statement calls for a dark shell).
Small status indicator (for example "Ready" / "Indexing") **only when the
app tracks that state**. Icon-only controls have tooltips and
`aria-label`s; the current location is marked with `aria-current`. Use
`<header>` / `<nav>` landmarks.

### 9.2 Document workspace and upload

**Empty (no file): a real starting experience, not an empty webpage.**
Compose the empty state as the product's front door:

- **Product introduction:** one-line value statement ("Ask questions about
  a contract and see exactly where the answer comes from") and, at most,
  2 or 3 short capability lines that are true of the existing app.
- **Upload area:** a drag-and-drop zone sized to the pane (not a tiny icon
  floating in a void). Dashed 1.5px `--border-default`, `--bg-sunken` fill,
  8px radius, 24px icon, title ("Upload a contract"), helper text
  ("Drag a PDF here or browse"), primary "Choose PDF" button.
- **Instructions and supported-file info:** numbered 1-2-3 steps
  (Upload, wait for indexing, ask) and the constraints the existing
  implementation really enforces (accepted type, size limit *only if*
  enforced or documented). No invented limits.
- **Suggested questions** appear once a document is ready (Section 9.3),
  not before, because they cannot be asked without a document.
- Keyboard accessible: the zone is a focusable button or label wrapping a
  real `<input type="file" accept="application/pdf">`. The upload handler
  and request are unchanged.

**Drag-over:** border becomes `--brand`, fill `--brand-subtle`, helper text
changes to "Drop to upload".

**Client-side validation error:** wrong file type, empty file, or multiple
files. Show an inline `--danger-*` message and keep the zone usable.

**Uploading / processing:** a file card replaces the zone's content (or
sits above the viewer) showing file name, size, and an
indeterminate bar with an honest label ("Uploading…" then "Indexing
contract…", matching the existing flow). Disable the chat composer while
the existing app logic disables it. **Do not change when it is enabled or
disabled.**

**Ready:** file card with name (truncated), size in KB/MB (tabular
numerals), a success badge ("Indexed"), and actions: Open in new tab,
Replace, Remove, preserving all existing actions. Below it, the document
preview.

**Error:** `--danger-*` banner with the reason (if available), and a clear
recovery action ("Try again" / "Upload a different file").

**File card** layout: 40px file-type tile (icon on `--bg-sunken`), name
(Body strong, single line truncated), meta line (Caption, secondary:
`PDF · 87 KB`), status badge, then actions as ghost icon buttons with
tooltips.

**Preview:** fills the remaining pane height, neutral `--bg-sunken`
backdrop around the PDF, no extra card chrome, and a fallback link.

### 9.2.1 PDF viewer chrome (document header, toolbar, thumbnails, canvas)

A generic embedded PDF plugin dropped into a box is the tell of an
unfinished product. Build the interface *around* the existing PDF
integration. **Do not replace, fork or break the existing PDF rendering
library or its controls.**

- **Document header (48 to 56px):** 40px file-type tile, file name (Body
  strong, one line, truncated, full name in `title`), meta line (Caption:
  `PDF · 87 KB · 12 pages`, page count only if the viewer reports it),
  status badge, and ghost icon actions (Open in new tab, Replace, Remove).
  Real file info only.
- **Toolbar (40 to 44px, below the header):** grouped with 1px separators.
  Page navigation (previous / next and a `3 / 12` page indicator; make the
  number a jump input if the library supports go-to-page), zoom (out,
  in, a percentage control or menu, fit width, fit page), and any further
  controls the library already exposes (rotate, download, search). Ghost 32px
  icon buttons with tooltips; keyboard shortcuts are shown only if they
  actually work. Drive controls through the library's public API or
  options. If a control cannot be driven programmatically (for example an
  opaque iframe/embed), keep the native control and restyle only the
  surroundings; do not fake it.
- **Thumbnail rail:** a compact vertical rail (about 88 to 120px wide) on the
  document's left edge. Page number under each thumbnail; **active page**
  clearly marked (2px `--brand` border, brand-colored number at weight 600);
  the active thumbnail scrolls into view as the page changes; click jumps
  to the page; arrow-key navigation (`role="listbox"` or equivalent); lazy
  rendering for long documents; collapsible, and a drawer or sheet on
  small screens.
- **Reading canvas:** `--bg-sunken` backdrop, pages centered with a 1px
  border and `--shadow-xs`, fit-to-width by default, no card inside a card,
  no duplicate headers, no double scrollbars. Hide or restyle the library's
  default toolbar only through its supported options or CSS hooks. After any
  layout change, re-fit on container resize (`ResizeObserver`).
- **After every layout change, verify** that pages still render, zoom
  works, page navigation and thumbnails stay in sync, and nothing is
  clipped. Keep the fallback link (Open in new tab) for browsers that do not
  embed PDFs.

### 9.3 Chat / AI assistant (document copilot)

The assistant should feel like an intelligent document copilot, not a
generic chatbot widget. Hierarchy and structure do the work.

**Pane header:** title ("Assistant" / "Ask about this contract") and, only
if real, a small context chip showing the active document.

**Empty state:** the highest-value place for guidance. A concise
heading, one line of explanation, and a set of **suggested questions**
(3 to 5, as a vertical list of full-width tertiary buttons or a wrapped
chip row) shown when a document is ready and no conversation exists yet.
Clicking a chip sends that text through the normal send path. Before a
document is loaded, the empty state explains the next step (upload) and
the composer is disabled with an explanatory placeholder.

**Turn structure (question, then answer):**

- Layout: the assistant's column (max 720px), 24px between turns, 8px within a turn.
- **Question:** visually lighter than the answer: a compact row (for
  example right-aligned `--brand-subtle` with a 4px corner toward the
  sender, or a left-aligned Body-strong line with a small "You" label).
  Pick one pattern; make it clearly distinct from the answer.
- **Answer:** *not* a chat bubble. A borderless, document-like response
  block at the full column width (Body 15/24 for long-form), with a small
  assistant mark. Paragraphs, lists and emphasis are formatted for
  reading; whitespace is intentional.
- Hover/focus actions (copy, retry on error) never permanent clutter.
  Copy is purely client-side. No action that needs new backend behavior.
- Auto-scroll to the newest message *unless* the user has scrolled up;
  then show a "Jump to latest" button.

**Answer hierarchy.** Render the response as separate blocks, in this order,
divided by spacing and 1px rules rather than nested boxes. Each block
appears **only when the response contains that data** (Section 8):

1. **Answer:** the main response text, most visually prominent.
2. **Supporting evidence:** the key excerpt(s), quoted style (2px
   `--accent` or `--brand-border` left rule, 13/20, clamped to about 4
   lines with "Show more"), only when the response has distinct evidence
   fields.
3. **Sources / citations:** compact expandable rows (below).
4. **Reasoning:** collapsed disclosure (below).

Never render answer, evidence, citations and reasoning as one enormous
message bubble.

**Rendering AI text safely and well:**

- Render paragraphs, lists, bold/italic, inline code and tables with proper
  spacing (`p + p` 8px, list indent 20px, tables with 1px borders and
  sticky-less simple styling).
- **Never** insert untrusted AI or user text with `innerHTML` unsanitized.
  Use `textContent`, a framework's escaped binding, or a vetted sanitizer
  alongside any Markdown renderer. Links open with `rel="noopener noreferrer"`.
- If the existing code already renders responses a certain way, keep the
  *parsing* identical and only improve presentation and escaping.

**Citations and sources (when present in the response):**

Citations are the main trust feature, and the usual failure is giving
them too much vertical space. Design them as **compact, expandable
evidence components**:

- Inline numbered markers (`[1]`) styled as small `4px`-radius chips in
  `--accent-subtle` or `--brand-subtle` with `--*-text` color, if the
  response format supports locating them. Otherwise list sources after the
  answer.
- A "Sources (N)" group beneath the answer. **Collapsed row**: a single
  32 to 40px line with the index chip, the section title (truncated), a
  page badge (`p. 4`) and a chevron. A full group of collapsed sources
  should take a small fraction of the viewport height. Use a real
  `<button aria-expanded>` for the row; one or two sources may start
  expanded, more than two start collapsed.
- **Expanded row**: the source excerpt (13/20, quote style, clamped with
  "Show more"), plus whatever reference information the response carries
  (clause or section number in `--font-mono`, document name). Show
  **exactly the fields the response contains** (section title, page number,
  excerpt, reference) and nothing invented. A missing field simply leaves
  its slot out.
- **Source navigation:** a "Go to page 4" action (or a clickable page
  badge) that moves the PDF to that page **only if** the response has a real
  page number *and* the existing viewer integration can navigate to it
  (Section 8, item 11). Otherwise the page number is plain text, not a fake
  link. When navigation works, highlight the active page in the thumbnail
  rail.

**Reasoning (only when present):** a collapsed "Show reasoning" disclosure
(`<details>`-style, keyboard accessible) labeled as model reasoning, in
`--text-secondary`, visually subordinate to the answer. Never expanded by
default. When expanded it stays readable: 13/20 to 14/22, measured line
length, preserved paragraphs and lists, a clamped height with scroll
rather than a wall of text that pushes the thread away.

**Loading / typing:** after send, immediately show the question, then an
answer-shaped placeholder (a short line plus two or three shimmering
lines, or a three-dot indicator) with an honest label ("Searching the
contract…" only if that is what the request is doing). Respect reduced
motion (static dots). Disable duplicate sends while busy exactly as the
existing code does.

**Error:** a distinct `--danger-*` message block inline in the thread
("Something went wrong. Try again.") with a **Retry** action that
re-sends the *same* payload through the existing path. The user's text is
never lost, and the draft is restored in the composer if the app logic
supports it. Do not expose raw stack traces; a collapsible "Details" with
the actual error message is acceptable.

**Composer:**

- 12px radius, 1px `--border-default`, `--bg-surface`, `--shadow-xs`;
  on focus-within: `--border-focus` ring and `--shadow-md`.
- Auto-growing textarea (1 to ~6 lines) or input, `Enter` sends,
  `Shift+Enter` newlines, placeholder explains state.
- Input hierarchy: the text area is dominant; the send button sits inside
  the composer at the bottom right, and a quiet hint line ("Enter to send
  · Shift+Enter for a new line") appears with the disclaimer.
- Send button: icon + label on desktop, icon on mobile; disabled when
  empty or busy; loading spinner while in flight. Disabled state of the
  whole composer (no document yet, or busy) has an explanatory placeholder.
- While the conversation is empty and a document is ready, suggested
  questions sit above the composer or fill the thread's empty state.
- Docked to the bottom of the assistant zone; on mobile it respects
  `env(safe-area-inset-bottom)` and stays visible with the keyboard open.
- Persistent footnote (Caption, secondary): short AI disclaimer.

### 9.4 Contract / document insights

Only when real data exists. Present as a compact, labeled property list
(label in Caption secondary, value in Body) inside the document pane
header or a collapsible details section. Examples of legitimate
content: file name, size, type, index status, and anything the real
responses expose. Not a grid of decorative stat cards. If no extra data
exists, omit the section entirely.

### 9.5 Buttons

| Variant | Use | Style |
|---|---|---|
| Primary | One per view region | `--brand` bg, `--text-inverse`, `--shadow-xs`, hover `--brand-hover` |
| Secondary | Common actions | `--bg-surface`, 1px `--border-default`, hover `--bg-sunken` |
| Ghost | Toolbar, icon buttons | Transparent, hover `--bg-sunken` |
| Destructive | Remove / delete | `--danger-text` on ghost, or `--red-500` solid in confirm dialogs only |

Height 32px (dense), 36px (default), 44px (touch). Padding 12 to 16px,
radius 6px, Label type. Icon + text gap 8px.

### 9.6 Inputs

36px height (44px on touch), 6px radius, 1px `--border-default`,
`--bg-surface`, placeholder `--text-tertiary`, hover `--border-strong`,
focus `--border-focus` + 2px ring `rgba(17, 90, 203, 0.2)`. Visible label
or an `aria-label`; helper and error text beneath at Caption size.

### 9.7 Status badge

```css
.badge { display: inline-flex; align-items: center; gap: 4px;
  padding: 2px 8px; border-radius: 4px; border: 1px solid;
  font: 500 12px/18px var(--font-sans); }
.badge--success { background: var(--success-bg); border-color: var(--success-border); color: var(--success-text); }
```

Same recipe for danger, warning, info. Pair color with an icon or text,
never color alone.

### 9.8 Toasts, banners, dialogs

- **Banner:** inline, persistent, `--*-bg` with `--*-border`, icon, message,
  optional action. For upload and ingestion results.
- **Toast:** transient (4s), bottom-center or bottom-right, `--shadow-md`,
  `role="status"` (or `alert` for errors). Never the only place a critical
  error appears.
- **Dialog:** 12px radius, `--shadow-lg`, focus trapped, `Esc` closes,
  focus returns to the trigger. Use for destructive confirmation only.

### 9.9 Skeletons

Prefer skeletons shaped like the final content (lines, a file card) over
spinners for anything that takes > 300ms and has a predictable shape.
Shimmer with `--bg-sunken` to `--bg-app`, 1.4s, disabled for reduced motion.

---

## 10. Accessibility (non-negotiable)

1. **Contrast:** body text at least 4.5:1, large text and UI borders at least
   3:1. Grey 900 on white and Grey 500 on white pass; Grey 300 on white does
   not (decorative use only).
2. **Keyboard:** everything operable by keyboard in a logical tab order;
   visible `:focus-visible` rings; no focus traps outside dialogs.
3. **Semantics:** real `<button>`, `<a>`, `<label>`, `<input>`, headings in
   order, landmarks (`header`, `main`, `nav`).
4. **Live regions:** the message list is `role="log"` with
   `aria-live="polite"`; status changes (indexing, errors) are announced via
   `role="status"` / `role="alert"`.
5. **Names:** icon-only buttons have `aria-label`; images have `alt` (or
   `alt=""` if decorative).
6. **Touch:** 44px targets on touch devices; no hover-only functionality.
7. **Color is never the only signal:** status uses an icon or text as well.
8. **Motion:** honor `prefers-reduced-motion`.
9. **Zoom:** layout survives 200% zoom and text-only scaling.

---

## 11. Validation (the work is not done until this passes)

### 11.1 Preserve the integration: prove it, don't assume it

1. **Diff the integration code.** Before and after, compare every
   `fetch`/`XMLHttpRequest` call:

   ```bash
   git diff -U0 -- '*.js' '*.ts' '*.tsx' '*.jsx' '*.html' | grep -nE "fetch|XMLHttpRequest|FormData|webhook|http"
   ```

   Any changed URL string, method, header, field name or parse path is a
   defect unless the user explicitly approved it.
2. **Compare network traffic.** With the app running, capture requests for
   each action in the **preservation list** (Section 2, Phase 1) before
   and after. URL, method, headers, body (including `FormData` field
   names and the binary file) and response handling must match.
3. **Exercise every feature against the real backend** when it is
   reachable:
   - Upload a real PDF: confirm the upload request hits the original
     URL with the same binary payload and field name.
   - Ask a **contract-specific** question and a **general** question:
     confirm both return and render correctly.
   - Confirm responses are parsed correctly and citations/reasoning
     render from the real response.
   - Trigger error handling (browser DevTools offline mode or a blocked
     request; do **not** edit URLs): confirm loading and error states.
   - Remove / replace / re-upload flows still work.
4. If the backend is not reachable (for example a test webhook not
   listening), say so explicitly in the report. Do not substitute mocks in
   shipped code; a throwaway test harness is acceptable only if it is
   clearly separate, never committed, and disclosed.

### 11.2 Inspect the real rendered UI

Run the app and look at it. Reading CSS is not validation.

1. Take screenshots at **1440, 1024, 768 and 390px** widths for each of
   these states: empty, file uploading, indexing, ready, chat empty, chat
   with messages, chat loading, chat error, and a long-filename case.
2. Check the console for errors and warnings; fix all.
3. Compare with the baseline screenshots from Phase 1: the new UI must be
   **significantly** better, not just different.
4. Run an automated accessibility pass if tooling is available
   (axe/Lighthouse) and fix serious findings.
5. Exercise the flows in the real rendered app, not only in code: upload a
   real PDF and confirm it renders; use the toolbar, thumbnails, page
   navigation and zoom; submit a question and confirm the answer renders
   with its hierarchy; expand and collapse citations; expand reasoning;
   click a citation and check whether it navigates (only if supported);
   resize through all four widths.

### 11.2.1 Structural comparison against the baseline

A new screenshot is part of the deliverable, and it is compared with the
original one.

1. Capture the "after" screenshot in the same state as each baseline
   screenshot (empty, ready, answered).
2. Place before and after side by side and fill in this table in your
   report:

   | Aspect | Baseline | New | Structurally different? |
   |---|---|---|---|
   | Overall composition | | | |
   | Navigation | | | |
   | Document workspace | | | |
   | PDF toolbar | | | |
   | Thumbnail navigation | | | |
   | Assistant layout | | | |
   | Answer presentation | | | |
   | Citation component | | | |
   | Input / composer | | | |
   | Empty state | | | |
   | Responsive behavior | | | |

3. **Fail condition:** if the overall outline still resembles the
   baseline, or most rows answer "no" or only cite color, type, shadow or
   radius, the redesign is incomplete. Return to Phase 2 and change the
   composition, not the paint.
4. Measure, do not guess: for example the collapsed Sources group should
   occupy a small share of the viewport, and the document zone should be
   the largest zone at ≥ 1280px.

### 11.2.2 Reference comparison (when a reference screenshot exists)

Follow Section 15.5: reproduce the reference's state with real data, take
a screenshot of the running app, compare it against the reference
region by region, fix every unexplained difference, and repeat. The
reference comparison replaces the 11.2.1 baseline table when the user's
target is a screenshot rather than "make it different".

### 11.3 Visual QA checklist

- [ ] If a reference exists: the running app matches it in layout, proportions, spacing, palette and hierarchy; every remaining difference is listed and justified (15.5)
- [ ] Side-by-side with the baseline, the composition is clearly different (11.2.1)
- [ ] Three zones are recognizable: shell/navigation, document workspace, assistant
- [ ] PDF has its own header, toolbar and thumbnail rail; active page is obvious
- [ ] Answers show a hierarchy (answer, evidence, sources, reasoning), not one big bubble
- [ ] Citations are compact, expandable and show only real fields
- [ ] One clear primary action per region; hierarchy readable at a glance
- [ ] Everything on the 4px grid; no stray odd gaps
- [ ] Alignment: edges, baselines and icon/text centers line up
- [ ] No giant empty areas; empty states guide the user
- [ ] Not "white cards everywhere": panes and background steps used
- [ ] Radii consistent with Section 5.5; nothing over 12px
- [ ] Shadows subtle; no glow, no heavy gradients
- [ ] One typeface, sizes only from the scale; no oversized headings
- [ ] All interactive states present (hover, focus-visible, disabled, loading, error)
- [ ] Long text, long filenames and long AI answers do not break layout
- [ ] No horizontal scroll at 320px; touch targets at least 44px on mobile
- [ ] Dark/light consistent if dark mode exists
- [ ] The identity statement is recognizable in the result

### 11.4 Iterate

If any item fails, fix it and re-screenshot. Repeat until the checklist is
clean and the result genuinely feels like a commercial product.

### 11.5 Report honestly

The final message to the user states:

- Files changed (frontend only), and confirmation that integration code
  is unchanged (cite the diff check).
- What was verified against the real backend and what could **not** be
  verified, and why.
- If a reference screenshot was supplied: the reference-vs-actual
  comparison, the remaining differences and why each remains (for example
  "no notifications feature, so the bell is inert and has no unread dot").
- The before/after structural comparison table (11.2.1) and the paths of
  the baseline and new screenshots, plus anything that still resembles the
  baseline and why.
- Any decision where the response data limited the design (for example "no
  page numbers in citations, so sources are not clickable").
- Remaining known issues. Do not claim success on anything you did not
  test.

---

## 12. Frontend Code Quality

- Match the project's existing stack. Do not introduce a framework or
  heavy dependency for styling alone. Prefer CSS custom properties and, if
  the project uses one, its existing component conventions.
- One tokens file (`tokens.css`, or a `:root` block at the top of the
  stylesheet). Components consume semantic tokens only.
- Small, reusable components with clear props or class contracts; no
  duplicated style blocks.
- Name by role (`.message--assistant`, `.file-card`), not by appearance
  (`.blue-box`). A BEM-like or utility-consistent approach, applied
  uniformly.
- Keep **presentation and integration separate**: styling and markup in
  components, request/parse logic in clearly identified functions that you
  leave untouched.
- No inline styles except for dynamic values; no `!important` except the
  reduced-motion rule.
- Remove dead CSS you replaced; leave no commented-out experiments.
- Comments explain *why*, especially anywhere integration code sits
  nearby ("Do not change: contract with the n8n webhook").

---

## 13. Reusable Snippets

### Page shell

```html
<div class="app">
  <nav class="shell-nav" aria-label="Workspace">…</nav>            <!-- Zone A -->
  <main class="workspace">
    <section class="pane pane--document" aria-label="Document">     <!-- Zone B -->
      <header class="doc-header">…</header>
      <div class="doc-toolbar" role="toolbar" aria-label="Document controls">…</div>
      <div class="doc-body">
        <aside class="thumb-rail" aria-label="Pages">…</aside>
        <div class="canvas">…existing PDF viewer…</div>
      </div>
    </section>
    <section class="pane pane--assistant" aria-label="Assistant">…</section> <!-- Zone C -->
  </main>
</div>
```

```css
.app { display: grid; height: 100dvh; min-height: 0;
  grid-template-columns: 56px minmax(0, 1fr);
  background: var(--bg-app); color: var(--text-primary); font: 400 14px/22px var(--font-sans); }
.workspace { display: grid; min-width: 0; min-height: 0;
  grid-template-columns: minmax(0, 1fr) clamp(360px, 32vw, 440px); }
.pane { display: flex; flex-direction: column; min-width: 0; min-height: 0;
  background: var(--bg-surface); }
.pane + .pane { border-left: 1px solid var(--border-subtle); }
.doc-body { display: grid; flex: 1; min-height: 0; grid-template-columns: 112px minmax(0, 1fr); }
.canvas { min-width: 0; overflow: auto; background: var(--bg-sunken); }

@media (max-width: 1023px) {          /* tablet: nav becomes a top bar, thumbs a drawer */
  .app { grid-template-columns: minmax(0, 1fr); grid-template-rows: 48px minmax(0, 1fr); }
  .doc-body { grid-template-columns: minmax(0, 1fr); }
}
@media (max-width: 767px) {           /* mobile: one zone at a time */
  .workspace { grid-template-columns: minmax(0, 1fr); }
  .pane[hidden] { display: none; } /* toggled by a Document / Assistant switcher */
}
```

### Focus ring

```css
:focus-visible { outline: 2px solid var(--border-focus); outline-offset: 2px; }
```

### Labeled value pair

```html
<div class="meta"><span class="meta__label">Size</span><span class="meta__value">87 KB</span></div>
```

```css
.meta { display: flex; flex-direction: column; gap: 2px; }
.meta__label { font: 400 12px/18px var(--font-sans); color: var(--text-secondary); }
.meta__value { font: 500 14px/22px var(--font-sans); color: var(--text-primary); font-variant-numeric: tabular-nums; }
```

---

## 14. Worked Example: AI Document Q&A (Contract Review)

Backend (fixed, do not touch): PDF upload and ingestion webhook,
chat webhook with intent routing, query rewriting, retrieval and answer
generation, with citations and reasoning in the JSON response.

Frontend result:

- **Zone A (shell):** 56px navigation rail (or top bar) with brand mark,
  product name, Workspace › document-name hierarchy, and the real document
  actions (Upload, Replace, Remove), plus a status badge driven by the
  app's real indexing state.
- **Zone B (document, dominant):** empty = a front-door composition with a
  one-line product introduction, a large drop zone, 1-2-3 instructions and
  "PDF only" guidance. Loaded = a document header (name, size, "Indexed"
  badge, Open / Replace / Remove), a toolbar (page n/N, zoom, fit), a
  compact thumbnail rail with an obvious active page, and a reading canvas
  holding the existing PDF viewer with a new-tab fallback. Uploading and
  indexing use an honest indeterminate indicator.
- **Zone C (assistant copilot):** bounded 360 to 440px width. Empty state
  with 3 to 5 suggested contract questions sent through the normal chat
  request. Each turn is a light question row plus a document-like answer
  block, followed by compact expandable Sources rows (section title, page,
  excerpt; "Go to page" only if the viewer can navigate) and a collapsed
  "Show reasoning", all only when the response contains them. Answer-shaped
  loading placeholder; inline error with Retry; composer with Enter-to-send,
  keyboard hint and an AI disclaimer footnote.
- **Mobile:** Document / Assistant segmented control, full-screen document
  viewer, thumbnails in a sheet, docked composer.
- **Proof of redesign:** the before/after table (11.2.1) shows structural
  differences in every row, not just new colors.
- **Unchanged:** both webhook URLs, the binary `data` upload field, the
  chat message payload, and every response-parsing path.

---

## 15. Reference-Driven Redesign (the user supplies a target screenshot)

When the user attaches a screenshot and asks the UI to match it, the
screenshot is the **primary design specification**. "Match" means
*recreate*: the same composition, proportions, spacing rhythm, hierarchy
and palette, not "take inspiration". Where the reference conflicts with
this skill's defaults (radius, gradients, page-title size, shell), **the
reference wins**.

What never yields to a reference: the integration boundary (Section 1),
data honesty (Section 8) and accessibility (Section 10).

### 15.1 Reference inventory (Phase 1 and 2)

Before writing code, decompose the screenshot into a table. Estimate
measurements from the image, then verify them after building (15.5):

| Slot | What the reference shows | Real data source in our app | Treatment (render / inert / omit) |
|---|---|---|---|

Include: every region and its share of the viewport (sidebar width, column
split, header height), every component, the gaps between regions, type
sizes (estimated from cap heights against a known element), the palette
(sample real hex values and map each to a token), radii, shadows and icon
style. The "Real data source" column is mandatory: a slot with no real
source gets an honest treatment from 15.3, decided now, not at the end.

### 15.2 Slots versus content (the hardcoding rule)

Everything written in the screenshot is **sample content** (file names,
sizes, answers, percentages, times, the example questions). Recreate the
*slot and its styling*, then fill it from real application data:

- File name, size and status from the actual file and the app's real
  upload and indexing state.
- Answer text, bold emphasis, sources and citations from the actual
  response, through the existing parsing.
- Message times stamped client-side when a message is created or received.
- Never paste the reference's sample contract, file, answer or numbers into
  the code, not even as a fallback or a placeholder.

### 15.3 Reference elements the app cannot back

Reproduce the visual slot so the layout and proportions match, but do not
fake behavior or claims:

| Reference element | Rule |
|---|---|
| Sidebar: Home, History, Settings | Render all three in the reference style. Home goes to the main workspace view. If History or Settings have no real screen, render them `aria-disabled` with a "Coming soon" tooltip, no navigation, no fake pages |
| Sidebar promo card ("Smarter Contract Analysis with AI", "Learn More") | Keep the card. Copy must be true statements about what this app does. Show "Learn More" only if it has a real destination or opens a real disclosure; otherwise omit the button |
| Notification bell with a red dot, profile avatar | Keep the controls for layout fidelity but inert (`aria-disabled`, tooltip "Not available yet"). No unread dot, since it implies unread items. A neutral user glyph, never an invented initial or name |
| "Upload Document" and "Sample Contract" tabs | Tabs stay. Replace the second with the real **Document** tab (the existing PDF viewer with thumbnails, zoom and page navigation, enabled once a file is loaded). Do not add a sample contract unless the app really has one |
| "Supports PDF files up to 10MB" | State the accepted type. State a size limit only if the existing code enforces or documents one |
| Security and trust strip ("Your data is secure and private", "Trusted by professionals") | Keep the band and its three-item layout. Fill it with statements the app can stand behind (for example "PDF files only", "Answers cite the contract", "Ask in plain language"). Do not claim security, privacy or trust that the project does not document |
| Uploaded file row with a green "Uploaded" pill | Real file name and size; the pill reflects the real state: Uploading, Indexing, Indexed or Error |
| Assistant status pill ("Ready to help") | Driven by real state: Ready, Indexing…, Thinking…, "Upload a contract first". Never a static "Ready" |
| Paperclip in the composer | Wire it to the existing upload input (same handler) with a tooltip such as "Upload or replace contract (PDF)". If that is not equivalent, omit it |
| Suggested-question pills | Generic, frontend-authored prompts sent through the normal chat path. They may also sit under the thread as follow-ups, without claiming to be derived from the last answer |
| "View in Document →" on a source | Only with a real page number and a viewer that can navigate to it. Otherwise a plain "Source" row with the page as text |
| Read receipts (✓✓) and similar delivery marks | Omit; the app has no delivery state |

### 15.4 Visual direction in the reference

**Palette.** Dark navy shell, royal blue as the action color, white
surfaces, a subtle lavender wash. Treat these hex values as estimates;
re-sample them from the screenshot, then define them once as tokens and
keep components on semantic tokens only:

```css
:root {
  --navy-950: #0A1A44;               /* sidebar (optionally a faint vertical gradient to #081538) */
  --bg-shell: var(--navy-950);
  --brand: #2347D6;                  /* buttons, links, active tab, send */
  --brand-hover: #1B38B5;
  --lavender-50:  #F4F5FF;           /* app background wash */
  --lavender-100: #E9ECFF;           /* user bubble, chips, strip band */
  --lavender-200: #D9DEFF;           /* chip and dashed-zone borders */
  --shadow-card: 0 8px 24px rgba(35, 71, 214, 0.08);   /* soft, blue-tinted */
}
```

Verify contrast (white on `--brand`, secondary text on lavender) as in
Section 10.

**Radius and depth (reference override of 5.5 and 5.6).** Cards 16px.
Chips, pills and the primary button fully rounded (`999px`). Composer 16px,
send button 12px. Avatars circular. Soft tinted shadows on cards. One
decorative background is allowed: a very soft lavender radial wash behind
the header (and, optionally, a faint static line graphic at the foot of the
sidebar). No other gradients, no glow, no animation on decoration.

**Typography.** Inter. The reference's page title is large: about
32 to 36px / 40, weight 600 to 700, with a 15/24 secondary description
beneath (this overrides the 20px page title; apply it to this one title
only). Card titles 18 to 24px, body 14 to 15px.

**Composition at a desktop viewport (about 1440px wide).**

- **Sidebar:** full height, about 232 to 240px (≈ 12.5% of the width),
  navy. Brand lockup at the top (40px mark plus two-line wordmark). Nav
  items 44px high, 10px radius, white-ish text; the active item has a
  `rgba(255,255,255,0.10)` fill. A promo card pinned to the bottom (16px
  radius, 6% white fill, 1px 10% white border, sparkle icon, 14px / 600
  title, 12 to 13px copy at about 70% white, outlined pill button).
- **Main area:** lavender wash background, 24 to 32px outer padding.
- **Header:** the large title and description on the left; bell and avatar
  (40px circles) on the right.
- **Workspace row:** two white cards with a 16px gap, split about **44% /
  56%** (for example `grid-template-columns: minmax(0, 0.8fr) minmax(0, 1fr)`),
  equal height, filling the space under the header.
- **Left card (document workspace):** tab row (icon plus label, 15px / 500;
  the active tab is `--brand` with a 2px underline), then the upload zone:
  1.5px dashed `--lavender-200` border, 12 to 16px radius, light lavender
  fill, a centered SVG illustration (a document with a circular upload
  badge, about 120px), title "Upload Your Contract" (24/32, 600), helper
  line with a brand-colored "click to browse", a small meta line with an info
  icon, and a pill primary button with an upload icon. Beneath the zone, the
  file row (PDF tile, name in 600, size in tabular numerals, status pill),
  and below that the three-item strip on a `--lavender-100` band with 1px
  dividers.
- **Document tab:** the existing PDF viewer inside the card, using the
  chrome from Section 9.2.1 (toolbar above, thumbnail rail beside the
  canvas). The tab may be selected automatically once the file is ready.
- **Right card (assistant):** header with a 48px navy circular avatar (brand
  mark), title 18/24 / 600, subtitle 14 secondary, and the status pill on
  the right (green dot on a green-50 pill); a 1px divider; the thread; a row
  of suggested pills; the composer.
- **Messages:** user messages right-aligned in a `--lavender-100` bubble
  (16px radius, small circular user avatar at the right, 12px time beneath).
  Assistant messages left-aligned with a 40px navy avatar, a white bubble
  with a 1px border and soft shadow, the answer with emphasis rendered from
  the response, a 1px divider, then a compact **Source** row (document icon,
  "Source", and the "View in Document →" pill only when real, per 15.3).
  Expanded sources show the real excerpt as in Section 9.3. Reasoning stays
  a collapsed disclosure beneath.
- **Suggested pills:** fully rounded, `--lavender-100` fill, 1px
  `--lavender-200` border, 14px text, brand border on hover and a visible
  focus ring.
- **Composer:** 16px-radius white field with a 1px border and soft shadow;
  paperclip on the left, text input, and a 44px `--brand` (or navy) send
  button with a paper-plane icon on the right. All states from Section 6
  (disabled, busy, focus) and Enter / Shift+Enter behavior from 9.3.

**Responsive.**

| Range | Layout |
|---|---|
| ≥ 1280px | As above |
| 1024 to 1279px | Sidebar collapses to a 72px icon rail (promo card hidden); the two cards keep the split |
| 768 to 1023px | Sidebar becomes a top bar with a menu button; the workspace row becomes a Document / Assistant segmented switcher over a single card |
| < 768px | Single card at a time; the title shrinks to about 24px; the composer docks to the bottom with the safe-area inset; the sidebar is a drawer; touch targets ≥ 44px |

Do not just shrink the desktop layout (Section 7.2).

### 15.5 Compare the running app against the reference

This step is mandatory and is not finished until the differences are gone.

1. Run the app against the real backend. Set the browser viewport to the
   reference's aspect ratio (about 16:9, for example 1440 x 810).
2. Reproduce the reference's state with real data: upload a real PDF, ask a
   real question, and let a real answer with sources arrive, so the screenshot
   contains the sidebar, header, upload zone with a file row, the strip, a
   user message, an answer with a source row, the suggested pills and the
   composer.
3. Take the screenshot. Place it next to the reference (or overlay it at 50%
   opacity if tooling allows). Fill in a table: region, reference, actual,
   difference. Cover sidebar (width, color, promo card), header, tab row,
   drop zone, illustration, file row, strip, assistant header and status,
   bubbles, source row, pills, composer, spacing and proportions.
4. Measure instead of guessing, with `getBoundingClientRect()`: sidebar share
   of the width (≈ 12.5%), left card share of the workspace row (≈ 44%),
   card gaps, title size, radii and colors.
5. Fix every difference that is not a deliberate deviation. A deviation is
   legitimate only for data honesty (15.2, 15.3) or accessibility, and each
   must be listed in the final report with its reason.
6. Re-screenshot and repeat until the table is clean. Then check 1024, 768
   and 390px (15.4 responsive) and confirm the network requests are
   unchanged from the baseline (Section 11.1).
7. Report what matches, what intentionally differs and why, and anything you
   could not verify.

---

## Quick Reference Card

```
IDENTITY     One sentence + one signature detail
FONT         Inter (Inter Display ≥ 20px), 400 / 500 / 600
TEXT         #070A0E primary · #4A4C4F secondary · #5E6062 tertiary
SURFACES     #FAFAFA app · #FFFFFF surface · #F0F0F1 sunken
BORDERS      #DADADB subtle · #C1C2C3 default · #8F9193 strong
BRAND        #115ACB (hover #0044AE, subtle #E7EFFC)
STATUS       Green #13A10E · Red #D13438 · Yellow #FFAA33 · Violet #7F00FF · Orange #FF4405

TYPE         32/40 · 20/28 · 16/24 · 14/22 · 13/20 · 12/18 · 11/16
SPACE        4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64
RADIUS       4 badge · 6 control · 8 card/pane · 12 overlay/composer
SHADOW       xs · sm · md · lg (borders first)
MOTION       100 hover · 150 popover · 200 panel · ease-out in / ease-in out

LAYOUT       3 zones: nav/shell · document workspace (header, toolbar, thumbs, canvas) · copilot
ANSWER       answer → evidence → sources (compact, expandable) → reasoning (collapsed)
BREAKPOINTS  ≥1280 desktop · 1024 laptop · 768 tablet · <768 mobile (single pane)
TOUCH        44px targets · 16px+ inputs · dvh · safe-area insets

ORDER        Inspect → Design → Implement → Validate (rendered, 4 widths)
RULE ZERO    The network tab must look identical before and after
RULE ONE     A recolor of the old layout is not a redesign: pass the before/after structural test
REFERENCE    A supplied screenshot is the spec: recreate slots, fill them with real data, compare the running app, iterate
```
