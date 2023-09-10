import sounddevice as sd
from scipy.io.wavfile import write
from time import sleep

# Constants
fs = 44100  # Sample rate
seconds = 10  # Duration of recording
filename = 'output.wav'

def record_voice():
    print('======================================')
    print('\nPlease speak loudly and clearly while we record your voice for 10 seconds,'
          '\nyou can either improvise or use the provided text.')

    input('\n\n(Press any button to start)\n')

    print('======================================')

    print("\nI am currently testing my voice,\nmy favorite color is blue,\nthe sky is sunny,"
          "\nmy voice is loud and clear,\nI'm using a proper mic,\nmy environment is quiet.\n\n")

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

    for i in range(seconds):
        progressbar = f"[{'=' * (i + 1)}{' ' * (seconds - i - 1)}]"
        print(f"{progressbar} Remaining seconds: {seconds - i - 1}s", end=' \r')
        sleep(1)

    print(f"{progressbar} Remaining seconds: {seconds - i - 1}s DONE!", end=' \r')
    sd.stop()

    write(filename, fs, myrecording)  # Save as WAV file

    return input('\n\nPlay the recorded sound [y/N]: ')