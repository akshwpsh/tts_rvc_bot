from gtts import gTTS
import asyncio

path = "./tts_output/google_output.mp3"
example_text = "테스트 문장입니다."


async def test_gtts(text):
    tts = gTTS(text=text, lang='ko')
    await tts.save(path)


async def get_gtts(text, channel):
    ch_path = f"utils/tts_output/{channel}_output.mp3"
    tts = gTTS(text=text, lang='ko')
    await tts.save(ch_path)

