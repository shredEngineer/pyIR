# Apply an impulse response (IR) signal to an audio signal. Accepts 44.1 kHz .wav files.

import sys
import warnings
import numpy as np
from scipy.io import wavfile
from scipy.signal import convolve

warnings.filterwarnings("ignore")

assert len(sys.argv) == 3, "Usage: pyIR ir.wav in.wav"

filename_IR = sys.argv[1]
filename_in = sys.argv[2]

print("* Loading IR: ", filename_IR)

# Read IR
samplerate_IR, data_IR = wavfile.read(filename_IR)
assert samplerate_IR == 44100

filename_out = filename_in[:-4] + "_cab.wav"

print("* Processing: ", filename_in, " -> ", filename_out)

# Read input
samplerate_in, data_in = wavfile.read(filename_in)
assert samplerate_in == 44100

data_in = data_in.astype(float)
data_IR = data_IR.astype(float)

# Convolve
data_out = convolve(data_in, data_IR)

# Normalize
data_out = np.int16(data_out / np.max(np.abs(data_out)) * 32767)

# Write output
wavfile.write(filename_out, 44100, data_out)
