from app.voice.voice_manager import VoiceManager

voice = VoiceManager()

print(voice.status())

print(voice.enable())

print(voice.status())

print(voice.disable())

print(voice.status())