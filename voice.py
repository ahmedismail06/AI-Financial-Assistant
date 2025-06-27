import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

def to_voice(text:str):

    load_dotenv()

    elevenlabs = ElevenLabs(
      api_key= os.getenv("ELEVENLABS_API_KEY")
    )

    audio = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_flash_v2_5",
        output_format="mp3_44100_128",
    )

    play(audio)

