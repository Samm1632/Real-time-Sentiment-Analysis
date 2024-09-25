import analysis
import record
import convert
audio_file = "output.wav"
output_file = "output.txt"
chunk = 1024
channels = 1
rate = 44100
record_seconds = 10
recorded_file = record.record_audio(output_filename=audio_file, chunk=chunk, channels=channels, rate=rate, record_seconds=record_seconds)
transcribed_text = convert.record_and_transcribe(audio_file)
text_analyzer=analysis.sentiment_analyzer(transcribed_text)
if text_analyzer['neg'] > text_analyzer['pos'] and text_analyzer['neg'] > text_analyzer['neu']:
    print("The text_analyzer is negative.")
elif text_analyzer['pos'] > text_analyzer['neg'] and text_analyzer['pos'] > text_analyzer['neu']:
    print("The text_analyzer is positive.")
elif text_analyzer['neu'] > text_analyzer['neg'] and text_analyzer['neu'] > text_analyzer['pos']:
    print("The text_analyzer is neutral.")
else:
    print("The text_analyzer is mixed or unclear.")