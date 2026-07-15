from app.voice.pipeline import VoicePipeline
from app.voice.wakeword.wake_word import WakeWordDetector
from app.voice.stt.speech_to_text import SpeechToText
from app.voice.tts.text_to_speech import TextToSpeech

pipeline = VoicePipeline(
    WakeWordDetector(),
    SpeechToText(),
    TextToSpeech(),
)

print(pipeline.status())