# PA4 session recordings

This directory is reserved for real, consented participant recordings. Do not create placeholder or fake MP4 files.

## Filename convention

Use anonymized participant IDs:

- `P01-session.mp4`
- `P02-session.mp4`
- `P03-session.mp4`
- `P04-session.mp4`
- `P05-session.mp4`

If a participant completes multiple sessions, append a documented date or session number without using a name.

## Verification rule

PASS only when each actual participant session has a corresponding verified recording that can be opened and matched to the consented session. A filename in a CSV is not proof that a recording exists. The current PA4 state has no recordings, so the recording requirement is `BLOCKED EXTERNALLY`.

The analysis gate accepts only an expected `.mp4` file that is present, at least 1 KiB, readable by `ffprobe`, has a positive duration, and has at least one `codec_type=video` stream. An audio-only MP4 is `RECORDING_INVALID_NO_VIDEO_STREAM`; a corrupt or text file renamed to `.mp4` is `RECORDING_INVALID_MEDIA`. A present file without a media probe is `RECORDING_PRESENT_UNVERIFIED` and never counts as verified. Keep the original recording immutable and retain the JSON probe result with the session audit.
