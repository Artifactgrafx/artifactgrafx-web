# Artifact Grafx Reels

Organized like slydz-ig-content structure.

## Content

### Static Quote Reels
- 01-your-brand-is-real-reel.mp4
- 02-excavate-polish-bring-reel.mp4
- 03-one-conversation-reel.mp4
- 04-wildfire-reel.mp4
- 05-dig-ideas-reel.mp4
- 06-streets-to-studio-reel.mp4

### Animated Quote Reels
- 04-wildfire-animated-reel.mp4
- 05-dig-ideas-animated-reel.mp4
- 07-wildfire-animated-reel.mp4

`04-` and `05-` are pans over the animated square PNG. `07-` is different — it is
rendered frame-by-frame from `instagram-posts/quote-wildfire-reel.html`, a native
1080×1920 layout carrying the real CSS motion timeline: staggered quote lines,
ignition glow behind "wildfire", rising embers, a centered emblem + handle lockup,
and a fade-out that loops cleanly back to the first frame.

Re-render it with:

```
cd instagram-posts
node generate-wildfire-reel.cjs
```

Frames are stepped through the Web Animations API rather than screen-recorded, so
timing is exact and the output is reproducible.

All reels are 1080×1920 (vertical 9:16) optimized for Instagram Reels.
Thumbnails are included for each reel.
