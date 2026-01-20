# Gemini 2.0 Flash: Multimodal LLM with Streaming

*Source: [Simon Willison](https://simonwillison.net/2024/Dec/11/gemini-2/) - December 2024*

Google's Gemini 2.0 Flash is a multimodal LLM that's both more capable and 2x faster than Gemini 1.5 Pro.

## Key Capabilities

### Input/Output Modalities
- **Input**: Images, video, audio, documents (same as 1.5)
- **Output**: Text, images, audio (image/audio output coming early 2025)

### Code Execution
Can write and execute Python code as part of responses:

```bash
llm -m gemini-2.0-flash-exp -o code_execution 1 \
  'write and execute python to generate a 80x40 ascii art fractal'
```

Note: Code environment has no network access.

### Bounding Boxes / Spatial Understanding
Returns coordinates for objects within images. Can also do "3D bounding boxes."

Try it: [AI Studio Spatial Understanding demo](https://aistudio.google.com/)

### Streaming API (Sci-Fi Mode)
Two-way WebSocket stream: send audio/video, receive text/audio in real-time.

**Try it**: https://aistudio.google.com/live (works in Chrome, Mobile Safari)

**DIY Setup**:
```bash
git clone https://github.com/google-gemini/multimodal-live-api-web-console
cd multimodal-live-api-web-console
npm install
# Add GOOGLE_API_KEY to .env
npm start
```

## Using with LLM CLI

```bash
llm install -U llm-gemini
llm keys set gemini
llm -m gemini-2.0-flash-exp describe -a https://example.com/image.jpg
```

## Pricing
Not yet announced (free preview as of Dec 2024). Expected to be inexpensive based on Gemini 1.5 pricing.

## Comparison to OpenAI
OpenAI has WebSocket streaming API (DevDay 2024) but:
- Only handles audio (not video)
- Currently expensive

Gemini 2.0's live video + audio streaming is more capable.

## Upcoming Features
- Native image editing ("Turn this car into a convertible")
- Audio output with varied voices, accents, intonation

---

*See also: `llm-2024-year-review.md` for broader context*
