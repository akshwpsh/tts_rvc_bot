from rvc_python.infer import infer_file


def get_rvc(tts, channel):
    path = f"utils/tts_output/{channel}_output.mp3"
    pitch = 3
    if tts == "etts":
        pitch = 3
    elif tts == "gtts":
        pitch = 13

    result = infer_file(
        input_path=path,
        model_path="utils/models/voice_Milk_500e.pth",
        index_path="utils/models/index/voice_Milk.index",  # Optional: specify path to index file if available
        device="cpu:0",  # Use cpu or cuda
        f0method="rmvpe",  # Choose between 'harvest', 'crepe', 'rmvpe', 'pm'
        f0up_key=pitch,  # ptich up key
        opt_path=f"utils/rvc_output/{channel}_output.wav",  # Output file path
        index_rate=0.75,
        filter_radius=3,
        resample_sr=0,  # Set to desired sample rate or 0 for no resampling.
        rms_mix_rate=1,
        protect=0,
        version="v2"
    )
    return result
