#!/bin/env python
#!/bin/env python3

import numpy as np

import Encodings as enc
import Decodings as dec

test_vect = np.array([1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1])


def test_AMI():
    t, encoded = enc.AMI(test_vect)
    t, decoded = dec.AMI(encoded)

    assert np.array_equal(test_vect, decoded)


def test_CMI():
    t, encoded = enc.CMI(test_vect)
    t, decoded = dec.CMI(encoded)

    assert np.array_equal(test_vect, decoded)


def test_manchester():
    t, encoded = enc.Manchester(test_vect)
    t, decoded = dec.Manchester(encoded)

    assert np.array_equal(test_vect, decoded)
