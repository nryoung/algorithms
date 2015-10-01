import unittest

from algorithms.random import mersenne_twister


class TestMersenneTwister(unittest.TestCase):
    """
    Tests Mersenne Twister values for several seeds comparing against
    expected values from C++ STL's Mersenne Twister implementation
    """

    def test_mersenne_twister(self):
        mt = mersenne_twister.MersenneTwister()

        # Test seed 1
        mt.seed(1)
        self.expected = [
            1791095845, 4282876139, 3093770124,
            4005303368, 491263, 550290313, 1298508491,
            4290846341, 630311759, 1013994432
        ]
        self.results = []
        for i in range(10):
            self.results.append(mt.randint())
        self.assertEqual(self.expected, self.results)

        # Test seed 42
        mt.seed(42)
        self.expected = [
            1608637542, 3421126067, 4083286876,
            787846414, 3143890026, 3348747335,
            2571218620, 2563451924, 670094950, 1914837113
        ]
        self.results = []
        for i in range(10):
            self.results.append(mt.randint())
        self.assertEqual(self.expected, self.results)

        # Test seed 2147483647
        mt.seed(2147483647)
        self.expected = [
            1689602031, 3831148394, 2820341149,
            2744746572, 370616153, 3004629480,
            4141996784, 3942456616, 2667712047, 1179284407
        ]
        self.results = []
        for i in range(10):
            self.results.append(mt.randint())
        self.assertEqual(self.expected, self.results)

        # Test seed -1
        # Hex is used to force 32-bit -1
        mt.seed(0xffffffff)
        self.expected = [419326371, 479346978, 3918654476,
                         2416749639, 3388880820, 2260532800,
                         3350089942, 3309765114, 77050329, 1217888032]
        self.results = []
        for i in range(10):
            self.results.append(mt.randint())
        self.assertEqual(self.expected, self.results)
