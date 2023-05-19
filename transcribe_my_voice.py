import whisper

model = whisper.load_model("medium")

result = model.transcribe("my_voice_italian.m4a", verbose=True)
print(result)

# Base Model
# Detected language: Italian
# [00:00.000 --> 00:07.160]  Ciao! Il mio nome è Marco e vivo all'ondro.
# [00:07.160 --> 00:11.400]  E tu chi sei?

# Medium Model
# Detected language: Italian
# [00:00.000 --> 00:09.600]  Ciao, il mio nome è Marco e vivo a Londra. E tu chi sei?
