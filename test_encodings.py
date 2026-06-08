#!/bin/env python3

import numpy as np

import Encodings as enc
import Dencodings as dec

test_vect = np.array([1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1])

def test_manchester():
    t, encoded_manchester = enc.Manchester(test_vect)
    decoded_manchester = dec.Manchester(encoded_manchester)

    assert np.array_equal(test_vect, decoded_manchester)
