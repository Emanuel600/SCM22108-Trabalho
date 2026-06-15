"""
@file: Dencodings.py
@brief: Decoding of generic line encodings
@description: Implementing line deecodings for audio signals, primarily bipolar
"""

import numpy as np
import Jit as jit

"""
@brief:      Decodes AMI signal
@param data: Trinary data read from line
@param Tb:   Bit time
@return:     A tuple containg time vector and decoded bit sequence
"""
@jit.configure(parallel=True)
def AMI(data, Tb=1):
    t = np.arange(0, len(data)*Tb, Tb)
    decoded_signal = np.zeros_like(t)
    for i in range(len(data)):
        bit = data[i]
        if bit!= 0:
            decoded_signal[i] = 1
        else:
            decoded_signal[i] = 0
    return t, decoded_signal


"""
@brief:      Decodes CMI signal
@param data: Trinary data read from line
@param Tb:   Bit time
@return:     A tuple containg time vector and decoded bit sequence
"""
@jit.configure(parallel=True)
def CMI(data, Tb=1):
    t = np.arange(0, (len(data)//2)*Tb, Tb)
    decoded_signal = np.zeros_like(t)
    for i in range(len(data)//2):
        id    = i*2
        hbit1 = data[id]
        hbit2 = data[id+1]
        bit   = hbit1==hbit2
        
        decoded_signal[i] = bit
    return t, decoded_signal


"""
@brief: Manchester decoding for a binary signal (IEEE 802.3 Standard)
@param data: Trinary data read from line
@param Tb: Bit duration
@return: A list containing the time array and the decoded signal array
"""
@jit.configure(parallel=True)
def Manchester(data, Tb=1):
    t = np.arange(0, (len(data)//2)*Tb, Tb)
    decoded_signal = np.zeros(len(data)//2)

    for i in range(len(decoded_signal)):
        idx = i*2
        val0 = data[idx]
        val1 = data[idx+1]

        if val0 == -1 and val1 == 1:
            decoded_signal[i] = 0
        else:
            decoded_signal[i] = 1

    return t, decoded_signal
