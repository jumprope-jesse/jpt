---
type: link
source: notion
url: https://blog.untrod.com/2023/11/robot-dad.html
notion_type: Product Website
tags: 
created: 2023-11-27T16:13:00.000Z
---

# Robot Dad - Untrod

## AI Summary (from Notion)
- Project Overview: Development of "Robot Dad," an AI-driven assistant designed to answer children's science questions using voice cloning and AI technology.
- Motivation: Created as a response to unsatisfactory answers from existing voice assistants like Alexa, aiming to provide more engaging and contextual replies for children.
- Technology Used:
- Voice cloning from Eleven Labs to create a realistic dad-like voice.
- Integration of speech-to-text and AI response services (ChatGPT) to facilitate interaction.
- Local processing for wake word detection and speech recognition.
- User Interaction: Designed for children, allowing them to ask follow-up questions and receive contextual answers, enhancing learning experiences.
- Technical Insights:
- A few dozen lines of code combine various AI services for effective functioning.
- Challenges include limitations in speech-to-text accuracy and the need for a suitable local text-to-speech model.
- Visualization: Added a speech visualization feature to make interactions more engaging for kids.
- Code Accessibility: The code for Robot Dad is provided, requiring API keys for various services for implementation.
- Takeaway: Emphasizes the potential for AI to enhance educational interactions with children by making information more accessible and engaging.

## Content (from Notion)

Tired of Alexa's feeble "here's what I found on wikianswerspam.com" responses to my eight-year-old son's science questions, I whipped up Robot Dad during my Thanksgiving break. He now runs in the background of our family computer.

Robot Dad sounds like real dad, thanks to voice cloning from Eleven Labs (very easy; I rambled about Formula 1 into a new MacOS Voice Memo for about sixty seconds, uploaded it, and voila), and answers appropriately for an eight-year-old, while deflecting prank requests -- though I suspect prompt injection will soon be second nature to this generation.

Here's my son, Dash, interacting with Robot Dad.

The delays are real, and the speech-to-text is only so-so, but it manages to be just good enough to clear the "provides value" bar. Robot Dad can inject context from the previous question into the prompt Dash could follow up with "Robot Dad, tell me more about it" and ChatGPT would know what to do.

A few dozen lines of code glues together different AI services, for a remarkable result. The wakeword and speech-to-text happen locally, while the AI response (ChatGPT) and text-to-speech are via HTTP. It's trivial to move the LLM bit to a local Llama2 instance, but I haven't found a satisfactory text-to-speech model that can do voice cloning locally.

I also made a quick speech visualization (turns out kids are not very engaged reading console log messages) that of course ended up providing more entertainment value than the ENTIRE MODERN MIRACLE OF ARTIFICIAL INTELLIGENCE. Code for the visualization is in this gist.

Code for Robot Dad is below. You will need API keys for Picovoice (and a wakeword), Eleven Labs, and OpenAI. You can pick a pre-existing Eleven Labs voice or clone your own.

```plain text
import os, json, threading, time
import pvporcupine, pvcheetah
from pvrecorder import PvRecorder
from elevenlabs import voices, generate, play, stream
import openai

ENDPOINT_DURATION_SECONDS = 2 # 'Quiet' seconds indicating the end of audio capture
VOICE = 'Dad' # Via Eleven Labs
AUDIO_DEVICE_NAME = 'MacBook Pro Microphone'
AUDIO_DEVICE = PvRecorder.get_available_devices().index(AUDIO_DEVICE_NAME)
OPENAI_MODEL = 'gpt-3.5-turbo-1106'

BASE_PROMPT = """You are Robot Dad, and will be speaking with one of my children,
trying to be a helpful parent. You explain things at a level appropriate for
an eight-year-old.

You are encouraging and helpful, but won't tolerate any inappropriate requests
or attempts at pranks or jokes. If you you are asked or told anything
inappropriate, you gently say "nice try - but Robot Dad isn't falling for that!"

If you don't know how to reply, simply say "I'm just Robot Dad, not real dad -
so I'm afraid I can't help you with that".

You usually answer in no more than 4 sentences - kids do not have long attention
spans - but you can provide longer answers if it's clearly needed.
"""

PREV_CTX_PROMPT = """

The last request and response you received is below. The next request may or may
not be a continuation of this conversation.

Previous request:
%s

Previous response:
%s
"""

PREV_CTX_TIMEOUT = 60 # seconds

keyword_paths=['%s/wakewords/Robot-Dad.ppn' % ROOT]

porcupine_key = os.environ.get("PORCUPINE_API_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")

porcupine = pvporcupine.create(
    access_key=porcupine_key,
    keyword_paths=keyword_paths)

cheetah = pvcheetah.create(
    access_key=porcupine_key,
    endpoint_duration_sec=ENDPOINT_DURATION_SECONDS,
    enable_automatic_punctuation=True)

recorder = PvRecorder(
    frame_length=porcupine.frame_length,
    device_index=AUDIO_DEVICE)

break_audio = generate(text="Got it! Robot Dad is thinking...", voice=VOICE)
alert_audio = generate(text="What's up kiddo?", voice=VOICE)

def llm_req(prompt, txt):
    messages= [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f'Here is what the child has said: {txt}'}
    ]

    resp = openai.ChatCompletion.create(
      model=OPENAI_MODEL,
      messages=messages
    )
    return resp['choices'][0]['message']['content']


# Speech-to-text using Picovoice's Cheetah
def capture_input():
    transcript = ''
    while True:
        partial_transcript, is_endpoint = cheetah.process(recorder.read())
        transcript += partial_transcript
        if is_endpoint:
            transcript += cheetah.flush()
            break
    return transcript


def play_async(audio):
    audio_thread = threading.Thread(target=play, args=(audio,))
    audio_thread.start()


def main():
    keywords = get_wakewords()

    print('Listening...')

    recorder.start()

    prev_request = ''
    prev_response = ''
    last_wake_time = None

    try:
        while True:
            pcm = recorder.read()
            result = porcupine.process(pcm)

            if result >= 0:
                print('Detected Robot Dad')
                play_async(alert_audio)

                prompt = BASE_PROMPT
                current_time = time.time()
                if last_wake_time and current_time - last_wake_time < PREV_CTX_TIMEOUT:
                    prompt += PREV_CTX_PROMPT % (prev_request, prev_response)
                last_wake_time = current_time

                transcript = capture_input()
                print('Heard request: %s' % transcript)
                prev_request = transcript

                play_async(break_audio)

                resp = llm_req(prompt, transcript)
                print('Answering: %s' % resp)
                prev_response = resp

                resp_audio = generate(text=resp, voice=VOICE, stream=True)
                stream(resp_audio)
    except KeyboardInterrupt:
        pass

    recorder.stop()
    print('Stopped.')
main()

```

### Like what you read? Join the newsletter and get updated when there's something new.


