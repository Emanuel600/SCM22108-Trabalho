"""
@file: Audio_Handler.py
@brief: Handling audio files and converting them to binary data
@description: This module provides functions to read WAV files,
                convert audio data to uint8 format,
                and then to binary representation for further processing or encoding.
"""

from scipy.io.wavfile import read
import numpy as np

"""
@brief: Convert uint8 data to binary representation
@param data: An array of uint8 data to be converted
@return: A flattened array of binary bits representing the input data
"""
def uint8_to_binary(data):
    # Convert uint8 data to binary
    binary_data = np.unpackbits(data.astype(np.uint8))
    # Reshape to have one bit per row
    binary_data = binary_data.reshape(-1, 8)
    # Transpose to have bits in columns
    binary_data = binary_data.T
    # Flatten the array to get a single binary sequence
    return binary_data.flatten()


"""
@brief: Convert wav file to uint8 data array
@param wav_filepath: The path to the WAV file
@return: An array of uint8 data reconstructed from the wav file
"""
def wav_to_uint8(wav_filepath):
    # Load the WAV file
    fs, data = read(wav_filepath)

    mp   = np.max(np.abs(data))
    data = data + mp
    data = (data / (2*mp)) * 255
    data = data.astype(np.uint8)

    return [fs, data]

"""
@brief: Convert a WAV file to binary data
@param wav_filepath: The path to the WAV file
@return: A tuple containing the sampling frequency and the binary data array
"""
def wav_to_binary(wav_filepath):
    fs, uint8_data = wav_to_uint8(wav_filepath)
    binary_data = uint8_to_binary(uint8_data)
    return [fs, binary_data]