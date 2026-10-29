# Design

## Overview
Archaeological/excavation aesthetic with a dark, atmospheric feel. Grid-based layout reminiscent of maps/surveys with monospace coordinates and artifact-like elements.

## Color Palette

### Core Colors (OKLCH)
```css
--background: oklch(0.205 0.009 85);      /* Deep brown-black */
--foreground: oklch(0.93 0.012 85);       /* Warm off-white */
--card: oklch(0.23 0.009 85);             /* Slightly lighter background */
--primary: oklch(0.73 0.15 75);           /* Warm amber/gold */
--primary-foreground: oklch(0.205 0.009 85); /* Dark text on gold */
--muted: oklch(0.27 0.012 85);           /* Subtle background */
--muted-foreground: oklch(0.7 0.013 85); /* Muted text */
--border: oklch(0.93 0.012 85 / 13%);   /* Subtle borders */
```

### Accent
- Primary accent: `#d9a95b` (warm gold/amber) - used for CTAs, links, emphasis
- Grid: `oklch(0.93 0.012 85 / 3%)` - subtle grid overlay

## Typography

### Font Families
- **Display/Headings**: `Space Grotesk` - Bold, geometric sans-serif with character
- **Body**: `Instrument Sans` - Clean, readable sans-serif
- **Monospace/Labels**: `JetBrains Mono` - Technical, coordinate-style labels

### Type Scale
- H1: `text-4xl sm:text-6xl` (clamp responsive)
- H2: `text-3xl md:text-4xl`
- H3: `text-xl`
- Body: `text-base md:text-lg`
- Small/Labels: `text-sm`, `label-mono` utility (0.72rem, uppercase, mono)

## Spacing
- Section padding: `py-16 md:py-24`
- Container: `max-w-5xl mx-auto px-6 md:px-10`
- Component gaps: `gap-6`, `gap-8`, `gap-10`

## Components

### Emblem
Diamond-shaped SVG with 'A' - the artifact/excavation symbol

### Marker
Coordinate-style labels: `N{n} | E{e}` in monospace, used to mark sections

### Cards
Bordered cards with subtle background, hover states with primary border

### Buttons
- Primary CTA style with gold background
- Ghost/icon buttons for navigation

## Layout
- Single column with max-width containers
- Grid overlays for texture
- Section-based vertical rhythm
- Border separators between major sections

## Imagery
Minimal - relies on typography, icons, and geometric elements. No stock photos needed.

## Motion
- Subtle rise animation on hero (`animate-rise`)
- Smooth scroll
- Hover transitions on cards and buttons
- Respects `prefers-reduced-motion`

## Voice in Design
Archaeological survey aesthetic - coordinates, specimens, excavation terminology, grid maps. Technical without feeling cold.

## Animated Quote Reel Series — Phase 2 (Thought-Provoking Quotes)

Design for extending the frame-by-frame animated reel treatment (delivered via
`instagram-posts/quote-wildfire-reel.html` + `generate-wildfire-reel.cjs` →
`reels/07-wildfire-animated-reel.mp4`) to the remaining thought-provoking quotes.

### Approved decisions

1. **Generator strategy**: bespoke HTML + generator per quote.
   - `instagram-posts/quote-<slug>.html` — standalone 9:16 reel page modeled on the
     wildfire reel (same `.reel` container, veil, grid, glow, embers, marker, lockup).
   - `instagram-posts/generate-<slug>-reel.cjs` — copy of the wildfire generator with
     `SOURCE` / `NAME` swapped; frames stepped via WAAPI `currentTime`, ffmpeg encode,
     thumbnail at t=3.6s.
2. **Motion language**: shared ember/gold treatment for all quotes — ignition glow,
   rising embers, staggered quote lines, coordinate marker, emblem + handle lockup,
   fade-out veil looping cleanly. Per-quote variation limited to text, accent word,
   kicker label, line count, and typography scale.

### Scope

All quotes in `thought-provoking-quotes.md` (post-wildfire). Proposed production order
follows the doc's "Best Performers" tier, then remaining quotes.

| Slug | Lines | Accent word | Kicker | Style note |
|---|---|---|---|---|
| create | 4 (stacked, bold) | CREATE | 008 — Create | Bold stacked text, minimal, gold accent on CREATE |
| sketchbook | 2 | — | 009 — Sketchbook | Typographic, editorial feel |
| references | 2 | — | 010 — References | Classic quote, punchy |
| messy-first | 2 | — | 011 — Messy First | Conversational, relatable |
| record | 2 | — | 012 — The Record | Vinyl culture |
| improvisation | 3 | — | 013 — Improvisation | Jazz/design craft |
| streets | 2 | — | 014 — Streets | Graffiti appreciation |
| craft | 3 | — | 015 — Craft | Philosophical, applies to all creative work |
| excavate | 3 | — | 016 — Excavate | Subtle brand tie-in, no pitch |
| taste | 3 | — | 017 — Taste | Very shareable |
| process | 3 | — | 018 — Process | Motivational, not cheesy |
| time | 2 | — | 019 — Time | Minimal, impactful |

### Output convention

`reels/NN-<slug>-animated-reel.mp4` + `reels/NN-<slug>-animated-reel-thumbnail.png`,
continuing the numeric sequence after `07-wildfire-animated-reel`.

### Next step

Write the implementation plan (per-quote content finalization → HTML → generator → render
→ encode → thumbnail → update `reels/README.md`).

