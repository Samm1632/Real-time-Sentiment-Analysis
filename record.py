import pyaudio
import wave
def record_audio(output_filename, chunk, channels, rate, record_seconds):
  p = pyaudio.PyAudio()
  format=pyaudio.paInt16
  try:
      stream = p.open(format=format,
          channels=channels,
          rate=rate,
          input=True,
          frames_per_buffer=chunk)
      print("* recording")
      frames = []
      for i in range(0, int(rate / chunk * record_seconds)):
          data = stream.read(chunk)
          frames.append(data)
      print("* done recording")
      stream.stop_stream()
      stream.close()
      p.terminate()
      wf = wave.open(output_filename, 'wb')
      wf.setnchannels(channels)
      wf.setsampwidth(p.get_sample_size(format))
      wf.setframerate(rate)
      wf.writeframes(b''.join(frames))
      wf.close()
      return output_filename  
  except Exception as e:
      print(f"Error recording audio: {e}")
      return None  