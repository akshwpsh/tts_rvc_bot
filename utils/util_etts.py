import edge_tts
import asyncio

path = "./tts_output/edge_output.mp3"
example_text = "테스트 문장입니다."


async def test_etts(text):
    communicate = edge_tts.Communicate(text, "ko-KR-SunHiNeural")
    await communicate.save(path)

async def get_etts(text, channel):
    ch_path = f"utils/tts_output/{channel}_output.mp3"
    communicate = edge_tts.Communicate(text, "ko-KR-SunHiNeural")
    await communicate.save(ch_path)
