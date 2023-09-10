import librosa
import matplotlib.pyplot as plt
import numpy as np

def plot_f0_from_wav(wav_file):
    y, sr = librosa.load(wav_file)
    f0, voiced_flag, voiced_probs = librosa.pyin(y,
                                                 fmin=librosa.note_to_hz('C2'),
                                                 fmax=librosa.note_to_hz('C7'))
    times = librosa.times_like(f0)

    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
    ax.set_title(f'pYIN fundamental frequency estimation [Average pitch: {np.round(np.nanmean(f0), 2)}]', pad=20)
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
    ax.legend(loc='upper right')

    plt.show()