---
name: teamon-native-media-and-files
description: Choose native workspace, Read/vision, media-provider, connector, and delivery rails without asking for unnecessary keys. Use when the user sends images, replied Telegram photos, documents, audio/voice, or asks for generated/downloaded files and the right rail is not obvious.
---

# TeamON Native Media And Files

Choose native workspace, Read/vision, media-provider, connector, and delivery rails without asking for unnecessary keys.

## When to use
Use when the user sends images, replied Telegram photos, documents, audio/voice, or asks for generated/downloaded files and the right rail is not obvious.

## Steps
1. For DOCUMENTS and IMAGES use native Read/vision first: a sent photo or explicitly replied Telegram photo arrives as inline SDK image input, and a Telegram document is dropped in workspace inbox/ where Read renders PDF/DOCX/spreadsheets and reads text in images.
2. Do not build OCR/vision providers just because media.inspect_image, media.ocr, or media.read_document provider cards are blocked; those are fallback rails for stored/exotic artifacts after native reading fails.
3. Use a media provider only for AUDIO transcription (STT) and VOICE output (TTS). The make-ready path is a local MCP/STT/TTS extension in the capsule that writes workspace/media-providers.json as a JSON array of {kind, url, name}; loopback URLs only.
4. Do not model STT/TTS as a generic HTTP connector: integration.http_request cannot upload inbound audio bytes, and media.transcribe/media.synthesize do not read capsule connector manifests.
5. For local or public no-secret work use native workspace tools such as shell, files, and WebFetch. Use connector/integration rails for saved credentials, business API policy, repeatable App integrations, or evidence-bound external side effects.
6. Bound setup, not legitimate use: author a connector/skill/extension once, then use it. Do not loop re-authoring after a failed attempt; fix one concrete 4xx from the response body at most.
7. For APIs that return a JSON URL for a binary artifact, call integration.http_request for the real request, fetch the binary with response_mode="artifact", then deliver with gateway.send_artifact.
8. Never claim the media/file/transcript/message reached the user from setup alone; require end-result evidence such as gateway.send_artifact, media_transcript_ready, integration.web_search results, or integration.http_request 2xx for the real request.

## Success evidence
- native Read/vision result, media_transcript_ready/media_speech_ready, integration result, or gateway delivery evidence from the claimed rail.
- If blocked, the reply names the single missing access/artifact/provider without raw refs or internal codes.
