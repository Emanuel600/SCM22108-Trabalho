"""
@file: Encodings.py
@brief: Generic line encodings for audio signals
@description: Implementing line encodings for audio signals, primarily bipolar
"""

import numpy as np

"""
@brief: AMI encoding for a binary signal
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param fb: Bit frequency (inverse of bit duration)
@return: A tuple containing the time array and the encoded signal array
"""
def AMI(signal, Tb=1):
    t = np.arange(0, (len(signal))*Tb, Tb)
    encoded_signal = np.zeros_like(t)
    polarity = -1
    for i in range(len(signal)):
        if signal[i] == 1:
            polarity *= -1
            encoded_signal[i] = polarity
        else:
            encoded_signal[i] = 0
    return [t, encoded_signal]

"""
@brief: CMI encoding for a binary signal
@param signal: The binary signal to be encoded (array of 0s and 1s)
@param fb: Bit frequency (inverse of bit duration)
@return: A tuple containing the time array and the encoded signal array
"""
def CMI(signal, Tb=1):
    t = np.arange(0, (len(signal))*Tb, Tb/2)
    encoded_signal = np.zeros_like(t)
    polarity = -1
    for i in 2*np.array(range(len(signal))):
        if signal[i//2] == 1:
            polarity *= -1
            encoded_signal[i] = polarity
            encoded_signal[i+1] = polarity
        else:
            polarity *= -1
            encoded_signal[i] = polarity
            polarity *= -1
            encoded_signal[i+1] = polarity
    return [t, encoded_signal]


"""
@brief: Convert uint16 data to binary representation
@param data: An array of uint16 data to be converted
@return: A flattened array of binary bits representing the input data
"""
def uint16_to_binary(data):
    # Convert uint16 data to binary
    binary_data = np.unpackbits(data.astype(np.uint16).view(np.uint8))
    # Reshape to have one bit per row
    binary_data = binary_data.reshape(-1, 16)
    # Transpose to have bits in columns
    binary_data = binary_data.T
    # Flatten the array to get a single binary sequence
    return binary_data.flatten()