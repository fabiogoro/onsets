import argparse
import numpy as np
import librosa

def audio_to_midi_melodia(infile, fs):
    y, sr = librosa.load(infile, sr=fs, mono=True)
    onset_env = librosa.onset.onset_strength(y=y, sr=fs, aggregate=np.median, fmax=1000, n_mels=13)
    times = librosa.onset.onset_detect(y, fs, units='time', onset_envelope=onset_env, backtrack=True, wait=4, delta=0.001, pre_max=3, post_max=3, pre_avg=3, post_avg=3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Path to input audio file.")
    parser.add_argument("-r", type=int, default=8000, help="Input audio samplerate (Default 44100).")
    args = parser.parse_args()

    audio_to_midi_melodia(args.infile, args.r)
