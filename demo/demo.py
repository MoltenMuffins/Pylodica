import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pylodica

'''
For now we'll use this file to experiment with how we want
the pylodica API to work
'''

# There are several structures and sub-structures that
# make up a pylodica song. 
# Song > Bars > Notes, Beats

# A song is comprised of multiple bars that can be
# chained together or stacked on top of each other
# as we will demonstrate later. When instantiating a bar,
# we need to pass in a time signature as an argument

# time signatures consist of two numerals 'N/M'
# The numeral 'N' before the '/' indicates the note value that represents one beat 
# (the beat unit). This number is typically a power of 2.
# The numeral 'M' after the '/' indicates how many such beats (N) constitute a bar.
example_bar = pylodica.bar(time_sig='4/4')

# We can add notes or a stroke to a bar.

# If playing a note, we we pass in a key,
# the index of the note (relative to the time signature)
# and how many beats to play the note for
key = 1
index = 1
duration = 4
example_bar.note(key, index, duration)

# If playing a beat, we pass in an instrument
# and the index of the beat (relative to the time signature)
instrument = 'snare'
index = 2
example_bar.stroke(instrument, index)

# The main idea behind Pylodica is to provide
# a high-level interface for simpleaudio, allowing
# one to programatically generate songs

# Here's an example of building a drum beat in
# a 4/4 time signature using some conditional logic
drum_bar = pylodica.bar(time_sig='4/4')
for i in range(3):
    time = i+1
    drum_bar.stroke('hihat', time)

    # Snare on 2s and 4s
    if time % 2 == 0:
        drum_bar.stroke('snare', time)
    # Bass Drum on 1s and 3s:
    else:
        drum_bar.stroke('bassdrum', time)

# Now that we've built up our bars, we can use them to make
# more complicated musical structures. 
# bars can be layered on top of one another or chained together
# to make compounded bars. These work the same as regular bars

# Extend the drum beat by chaining multiple drum_bars together
drums = pylodica.chain([drum_bar] * 4)

bar3 = pylodica.stack([melody_bar, drum_bar])

# Play bar 1 after bar 2

