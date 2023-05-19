import whisper
from pytube import YouTube

#Download a video from Youtube, get audio track 1 and transcribe
youtube_video_url = "https://www.youtube.com/watch?v=XXXXXXXX"
youtube_video_content = YouTube(youtube_video_url)

audio_streams = youtube_video_content.streams.filter(only_audio=True)
audio_stream = audio_streams[1]
audio_stream.download("")

model = whisper.load_model("base")
result = model.transcribe(str(audio_stream.default_filename), verbose=True)
print(result)

