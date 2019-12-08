import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import numpy as np
import note_frequencies

class Bar(object):
    def __init__(self, time_sig: tuple):
        beats_per_bar = time_sig[0]
        note_value = time_sig[1]
        self.index_range = beats_per_bar * (note_value / 4)
        print('max index {}'.format(self.index_range+1))
        self.wave_array = None

    def note(self, key, index, duration):
        print(key, index, duration)

    def stroke(self, instrument, index):
        print(instrument, index)


class Song(object):
    SAMPLING_FREQUENCY = 8000

    def __init__(self, bpm, note_duration=0.2, wave=np.sin):
        self._bpm = bpm
        self._wave = wave
        T = note_duration
        self.t = np.linspace(0, T, T * self.SAMPLING_FREQUENCY, False)
    
    def _note_write(frequency):
        fs = 44100  # 44100 samples per second
        seconds = 1  # Note duration of 3 seconds
        # Generate a 440 Hz sine wave
        note = self._wave(frequency * t * 2 * np.pi)
        # Ensure that highest value is in 16-bit range
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        # Convert to 16-bit data
        audio = audio.astype(np.int8)
        return audio
    
    def play(self):
        play_obj = simpleaudio.play_buffer(audio, 1, 2, self.SAMPLING_FREQUENCY)

    def note_maker(self, note):
        frequency = note_frequencies.NOTE_DICT[note]
        array = self._wave(frequency * self.t * 2 * np.pi)
        return array

class Rythmn(object):
    def __init__(self, bpm):
        self._bpm = bpm

if __name__ == "__main__":
    sang = Song(bpm=120)
    print(sang.note_maker(1))
