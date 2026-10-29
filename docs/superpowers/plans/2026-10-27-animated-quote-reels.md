# Animated Quote Reels Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render frame-by-frame animated 9:16 MP4 reels (with thumbnails) for every remaining thought-provoking quote, extending the wildfire reel treatment.

**Architecture:** Bespoke `quote-<slug>.html` + `generate-<slug>-reel.cjs` pair per quote, each modeled on `instagram-posts/quote-wildfire-reel.html` and `instagram-posts/generate-wildfire-reel.cjs`. Frames are stepped through the Web Animations API (`currentTime`), captured via clipped screenshot, encoded with ffmpeg libx264.

**Tech Stack:** Node.js scripts (`puppeteer-core`, `child_process`), ffmpeg (bundled imageio-ffmpeg binary or `FFMPEG_BIN`), headless Edge, H.264 via libx264.

**Spec:** `social-media/DESIGN.md` → section "Animated Quote Reel Series — Phase 2 (Thought-Provoking Quotes)"

## Global Constraints

- Per-reel output spec: 1080×1920, 30 fps, ~7 s (210 frames), H.264 High profile, yuv420p, CRF 15, preset slow, `x264-params aq-mode=3:aq-strength=1.1`, `+faststart`; thumbnail captured at settled frame (t = 3.6 s).
- Shared motion language is fixed and must not be reinvented per quote: radial ignition glow, rising embers, staggered quote lines, coordinate marker, emblem + handle lockup, fade-out veil looping cleanly to first frame, `prefers-reduced-motion` fallback.
- Per-quote variation is limited to: quote text/lines, accent word, kicker label, line count, typography scale.
- Each new generator is a copy of `generate-wildfire-reel.cjs` with only `SOURCE`, `NAME`, and `FRAMES_DIR` changed.
- No force pushes / history rewrites (Lovable-connected repo).

## Review Focus

- Headless font loading (Space Grotesk / Instrument Sans / JetBrains Mono) falling back incorrectly in the render environment.
- Per-line animation delays for 2- and 3-line quotes (wildfire only encoded 4-line stagger).
- ffmpeg binary resolution in the render environment (`FFMPEG_BIN` / imageio-ffmpeg fallback).
- Thumbnail frame: must be the fully-settled frame (t = 3.6 s), not an in-flight frame.

---

## Tasks

### Task 1: Render the "CREATE" animated reel (08) end-to-end

**Files:**
- Create: `instagram-posts/quote-create.html`
- Create: `instagram-posts/generate-create-reel.cjs`

**Interfaces:**
- Consumes: approved design ("Bold stacked text, minimal, gold accent on CREATE") + Quote 1 content from `thought-provoking-quotes.md`.
- Produces: `reels/08-create-animated-reel.mp4` + `reels/08-create-animated-reel-thumbnail.png`.

- [ ] **Step 1: Write `generate-create-reel.cjs`**
  - Copy of `generate-wildfire-reel.cjs` with `SOURCE = .../quote-create.html`, `NAME = '08-create-animated-reel'`, `FRAMES_DIR = os.tmpdir()/opencode-create-reel-frames`.
- [ ] **Step 2: Write `quote-create.html`**
  - Bold stacked "CREATE" lines from Quote 1 (`thought-provoking-quotes.md`: "CREATE before you're ready." / "CREATE before it's perfect." / "CREATE because you have to."), gold accent on CREATE, kicker `008 — Create`.
- [ ] **Step 3: Render** — `node generate-create-reel.cjs` from `instagram-posts`.
- [ ] **Step 4: Verify** — `reels/08-create-animated-reel.mp4` exists; ffprobe shows 1080×1920, ~30 fps, ~7 s; `reels/08-create-animated-reel-thumbnail.png` exists.
- [ ] **Step 5: Commit**

### Task 2: Render the "Sketchbook" animated reel (09) end-to-end

**Files:**
- Create: `instagram-posts/quote-sketchbook.html`
- Create: `instagram-posts/generate-sketchbook-reel.cjs`

**Interfaces:** Consumes: Quote 2 content + editorial style note. Produces: `reels/09-sketchbook-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-sketchbook-reel.cjs`** — copy with SOURCE=`quote-sketchbook.html`, NAME=`09-sketchbook-animated-reel`.
- [ ] **Step 2: Write `quote-sketchbook.html`** — lines: "A sketchbook is not a portfolio." / "It's a graveyard of ideas" / "and a laboratory for the next one."; editorial feel (no gold accent emphasis, cream text), kicker `009 — Sketchbook`.
- [ ] **Step 3: Render** — `node generate-sketchbook-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe dims/fps/duration OK.
- [ ] **Step 5: Commit**

### Task 3: Render the "References" animated reel (10) end-to-end

**Files:**
- Create: `instagram-posts/quote-references.html`
- Create: `instagram-posts/generate-references-reel.cjs`

**Interfaces:** Consumes: Quote 3 content + "classic quote, punchy". Produces: `reels/010-references-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-references-reel.cjs`** — copy with SOURCE=`quote-references.html`, NAME=`010-references-animated-reel`.
- [ ] **Step 2: Write `quote-references.html`** — lines: "Good artists borrow." / "Great artists steal with intent."; no accent emphasis, cream text, kicker `010 — References`.
- [ ] **Step 3: Render** — `node generate-references-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 4: Render the "Messy First" animated reel (11) end-to-end

**Files:**
- Create: `instagram-posts/quote-messy-first.html`
- Create: `instagram-posts/generate-messy-first-reel.cjs`

**Interfaces:** Consumes: Quote 4 content + "conversational, relatable". Produces: `reels/011-messy-first-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-messy-first-reel.cjs`** — copy with SOURCE=`quote-messy-first.html`, NAME=`011-messy-first-animated-reel`.
- [ ] **Step 2: Write `quote-messy-first.html`** — lines: "The first mark is always ugly." / "The hundredth starts to look like you."; conversational tone, cream text, kicker `011 — Messy First`.
- [ ] **Step 3: Render** — `node generate-messy-first-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 5: Render the "The Record" animated reel (12) end-to-end

**Files:**
- Create: `instagram-posts/quote-record.html`
- Create: `instagram-posts/generate-record-reel.cjs`

**Interfaces:** Consumes: Quote 5 content + "vinyl culture". Produces: `reels/012-record-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-record-reel.cjs`** — copy with SOURCE=`quote-record.html`, NAME=`012-record-animated-reel`.
- [ ] **Step 2: Write `quote-record.html`** — lines: "Some ideas start with a pencil." / "Mine start with the needle drop."; vinyl-flavored treatment (typography scale), kicker `012 — The Record`.
- [ ] **Step 3: Render** — `node generate-record-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 6: Render the "Improvisation" animated reel (13) end-to-end

**Files:**
- Create: `instagram-posts/quote-improvisation.html`
- Create: `instagram-posts/generate-improvisation-reel.cjs`

**Interfaces:** Consumes: Quote 6 content + "jazz/design craft". Produces: `reels/013-improvisation-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-improvisation-reel.cjs`** — copy with SOURCE=`quote-improvisation.html`, NAME=`013-improvisation-animated-reel`.
- [ ] **Step 2: Write `quote-improvisation.html`** — lines: "Jazz taught me more about design" / "than any textbook ever could." / "Listen. React. Adjust."; jazz treatment, kicker `013 — Improvisation`.
- [ ] **Step 3: Render** — `node generate-improvisation-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 7: Render the "Streets" animated reel (14) end-to-end

**Files:**
- Create: `instagram-posts/quote-streets.html`
- Create: `instagram-posts/generate-streets-reel.cjs`

**Interfaces:** Consumes: Quote 7 content + "graffiti appreciation". Produces: `reels/014-streets-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-streets-reel.cjs`** — copy with SOURCE=`quote-streets.html`, NAME=`014-streets-animated-reel`.
- [ ] **Step 2: Write `quote-streets.html`** — lines: "The best typography" / "has been on walls" / "long before it was on screens."; graffiti-flavored typography, kicker `014 — Streets`.
- [ ] **Step 3: Render** — `node generate-streets-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 8: Render the "Craft" animated reel (15) end-to-end

**Files:**
- Create: `instagram-posts/quote-craft.html`
- Create: `instagram-posts/generate-craft-reel.cjs`

**Interfaces:** Consumes: Quote 8 content + "philosophical, applies to all creative work". Produces: `reels/015-craft-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-craft-reel.cjs`** — copy with SOURCE=`quote-craft.html`, NAME=`015-craft-animated-reel`.
- [ ] **Step 2: Write `quote-craft.html`** — lines: "Craft is care" / "repeated long enough" / "to become instinct."; philosophical tone, kicker `015 — Craft`.
- [ ] **Step 3: Render** — `node generate-craft-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 9: Render the "Excavate" animated reel (16) end-to-end

**Files:**
- Create: `instagram-posts/quote-excavate.html`
- Create: `instagram-posts/generate-excavate-reel.cjs`

**Interfaces:** Consumes: Quote 9 content + "subtly ties to brand without pitching". Produces: `reels/016-excavate-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-excavate-reel.cjs`** — copy with SOURCE=`quote-excavate.html`, NAME=`016-excavate-animated-reel`.
- [ ] **Step 2: Write `quote-excavate.html`** — lines: "Most things worth keeping" / "are already there." / "You just have to look harder."; subtle-brand treatment, kicker `016 — Excavate`.
- [ ] **Step 3: Render** — `node generate-excavate-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 10: Render the "Taste" animated reel (17) end-to-end

**Files:**
- Create: `instagram-posts/quote-taste.html`
- Create: `instagram-posts/generate-taste-reel.cjs`

**Interfaces:** Consumes: Quote 10 content + "very shareable". Produces: `reels/017-taste-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-taste-reel.cjs`** — copy with SOURCE=`quote-taste.html`, NAME=`017-taste-animated-reel`.
- [ ] **Step 2: Write `quote-taste.html`** — lines: "Taste is knowing" / "what to keep" / "and having the discipline" / "to leave the rest."; kicker `017 — Taste`.
- [ ] **Step 3: Render** — `node generate-taste-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 11: Render the "Process" animated reel (18) end-to-end

**Files:**
- Create: `instagram-posts/quote-process.html`
- Create: `instagram-posts/generate-process-reel.cjs`

**Interfaces:** Consumes: Quote 11 content + "motivational without being cheesy". Produces: `reels/018-process-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-process-reel.cjs`** — copy with SOURCE=`quote-process.html`, NAME=`018-process-animated-reel`.
- [ ] **Step 2: Write `quote-process.html`** — lines: "The work you do" / "when no one's watching" / "is the work people notice."; kicker `018 — Process`.
- [ ] **Step 3: Render** — `node generate-process-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 12: Render the "Time" animated reel (19) end-to-end

**Files:**
- Create: `instagram-posts/quote-time.html`
- Create: `instagram-posts/generate-time-reel.cjs`

**Interfaces:** Consumes: Quote 12 content + "minimal, impactful". Produces: `reels/019-time-animated-reel.mp4` + thumbnail.

- [ ] **Step 1: Write `generate-time-reel.cjs`** — copy with SOURCE=`quote-time.html`, NAME=`019-time-animated-reel`.
- [ ] **Step 2: Write `quote-time.html`** — lines: "Speed is a skill." / "Restraint is mastery."; minimal treatment, kicker `019 — Time`.
- [ ] **Step 3: Render** — `node generate-time-reel.cjs`.
- [ ] **Step 4: Verify** — files exist; ffprobe OK.
- [ ] **Step 5: Commit**

### Task 13: Update reels README and run final sweep

**Files:**
- Modify: `social-media/reels/README.md`

- [ ] **Step 1: Update `social-media/reels/README.md`** — add the 12 new animated reels to the "Animated Quote Reels" list with their re-render commands.
- [ ] **Step 2: Final sweep** — confirm all 13 frame-by-frame animated reels present (07 + 08–019), thumbnails present, no leftover frame dirs.

---

## Self-Review

1. **Spec coverage:** every approved decision (bespoke generators, shared motion, per-quote variation limits) maps to Tasks 1–12; spec output format maps to Step 4 of each task; spec scope (all quotes post-wildfire) maps to Tasks 1–12 covering the 12 quotes.
2. **Step scan:** each task's steps are one action with checkable results; commit steps included; no vague steps.
3. **Type consistency:** generator names/slugs follow `NN-<slug>-animated-reel` convention consistently.
4. **Review Focus:** covered — font fallback, per-line stagger, ffmpeg resolution, thumbnail timing.
5. **Proportion:** plan ~ tasks × small step sets; acceptable given creative deliverables.

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-10-27-animated-quote-reels.md`. Please review the plan. Which execution approach would you prefer?

- **Subagent-driven** - A fresh subagent implements each task and a fresh reviewer checks it before the next one starts, then a whole-branch review at the end.
- **Native** - I implement every task myself in this session, then one fresh reviewer on the most capable model checks the whole branch.

For this plan I recommend **subagent-driven**, because the tasks are largely independent (each quote's pipeline is self-contained) but share the wildfire pattern, and independent failures should not compound in one context.

Does the plan capture what you want, and which approach should we use?
