import numpy as np
import simpleaudio

frequency = 220  # Our played note will be 440 Hz
fs = 8000  # 44100 samples per second
seconds = 0.5  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)
note = frequency * t * 2 * np.pi
print(note)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int8)

# Start playback
play_obj = simpleaudio.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()

bpm = 120
intro_melody = 'somefile.txt'
intro = Melody(intro_melody, bpm)
intro = 

for i in range(4):
    intro.play()

    if i == 4:
        