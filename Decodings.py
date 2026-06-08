"""
@file: Dencodings.py
@brief: Decoding of generic line encodings
@description: Implementing line deecodings for audio signals, primarily bipolar
"""

import numpy as np

"""
@brief:      Decodes AMI signal
@param data: Trinary data read from line
@param Tb:   Bit time
@return:     A tuple containg time vector and decoded bit sequence
"""
def AMI(data, Tb=1):
    t = np.arange(0, len(data)*Tb, Tb)
    decoded_signal = np.zeros_like(t)
    for i in range(len(data)):
        bit = data[i]
        if bit!= 0:
            decoded_signal[i] = 1
        else:
            decoded_signal[i] = 0
    return [t, decoded_signal]


"""
@brief:      Decodes CMI signal
@param data: Trinary data read from line
@param Tb:   Bit time
@return:     A tuple containg time vector and decoded bit sequence
"""
def CMI(data, Tb=1):
    t = np.arange(0, (len(data)//2)*Tb, Tb)
    decoded_signal = np.zeros_like(t)
    for i in range(len(data)//2):
        id    = i*2
        hbit1 = data[id]
        hbit2 = data[id+1]
        bit   = hbit1==hbit2
        
        decoded_signal[i] = bit
    return [t, decoded_signal]


"""
@brief: Manchester dencoding for a binary signal (IEEE 802.3 Standard)
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param Tb: Bit duration
@return: A list containing the time array and the encoded signal array
"""
def Manchester(signal):
    decoded_signal = np.zeros(len(signal)//2)

    for i in range(len(decoded_signal)):
        idx = i*2
        val0 = signal[idx]
        val1 = signal[idx+1]

        if val0 == -1 and val1 == 1:
            decoded_signal[i] = 0
        else:
            decoded_signal[i] = 1

    return decoded_signal
