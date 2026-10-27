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
