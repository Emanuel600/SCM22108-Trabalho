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