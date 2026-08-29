---
type: "query"
date: "2026-08-23T17:25:49.551992+00:00"
question: "How is a recording verified as a valid video recording?"
contributor: "graphify"
source_nodes: ["How is a recording verified as a valid video recording?", "Recording verification requires positive duration and a video stream", "Audio-only MP4 rejected"]
---

# Q: How is a recording verified as a valid video recording?

## Answer

ffprobe must report positive duration and at least one video stream. Audio-only MP4 and invalid media are rejected; media present without a probe is UNVERIFIED, not verified.

## Source Nodes

- How is a recording verified as a valid video recording?
- Recording verification requires positive duration and a video stream
- Audio-only MP4 rejected