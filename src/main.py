import os
from voice_recorder import record_voice
from plot_fundamental import plot_f0_from_wav
from playsound import playsound

filename = 'output.wav'
use_recording = 'N'

while use_recording != 'y':
    play_recording = record_voice()

    if play_recording == 'y':
        playsound(filename)

        use_recording = input('\n\nUse this recording [y/N]: ')
    else:
        use_recording = 'y'

plot_f0_from_wav(filename)        