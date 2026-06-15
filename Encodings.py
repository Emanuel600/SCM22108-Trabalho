"""
@file: Encodings.py
@brief: Generic line encodings for audio signals
@description: Implementing line encodings for audio signals, primarily bipolar
"""

import numpy as np
import Jit as jit

"""
@brief: AMI encoding for a binary signal
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param fb: Bit frequency (inverse of bit duration)
@return: A tuple containing the time array and the encoded signal array
"""
@jit.configure(parallel=True)
def AMI(signal, Tb=1):
    t = np.arange(0, len(signal)*Tb, Tb)
    encoded_signal = np.zeros_like(t)
    polarity = -1
    for i in range(len(signal)):
        if signal[i] == 1:
            polarity *= -1
            encoded_signal[i] = polarity
        else:
            encoded_signal[i] = 0
    return t, encoded_signal

"""
@brief: CMI encoding for a binary signal
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param fb: Bit frequency (inverse of bit duration)
@return: A tuple containing the time array and the encoded signal array
"""
@jit.configure(parallel=True)
def CMI(signal, Tb=1):
    t = np.arange(0, len(signal)*Tb, Tb/2)
    encoded_signal = np.zeros_like(t)
    polarity = -1
    for i in range(len(signal)):
        idx = 2 * i
        if signal[i] == 1:
            polarity *= -1
            encoded_signal[idx] = polarity
            encoded_signal[idx+1] = polarity
        else:
            polarity *= -1
            encoded_signal[idx] = polarity
            polarity *= -1
            encoded_signal[idx+1] = polarity
    return t, encoded_signal

"""
@brief: Manchester encoding for a binary signal (IEEE 802.3 Standard)
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param Tb: Bit duration
@return: A list containing the time array and the encoded signal array
"""
@jit.configure(parallel=True)
def Manchester(signal, Tb=1):
    t = np.arange(0, len(signal) * Tb, Tb / 2)
    encoded_signal = np.zeros_like(t)

    for i in range(len(signal)):
        idx = 2 * i
        if signal[i] == 0:
            # Low to high
            encoded_signal[idx] = -1
            encoded_signal[idx+1] = 1
        else:
            # High to low
            encoded_signal[idx] = 1
            encoded_signal[idx+1] = -1

    return t, encoded_signal
