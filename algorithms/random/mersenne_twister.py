"""
    Mersenne Twister
    ----------------
    Generates high quality pseudo random integers with a long period.
    Used as the default random number generator for several
    languages (including Python).

    For a more technical overview, see the wikipedia entry.

    Pseudocode: http://en.wikipedia.org/wiki/Mersenne_twister
"""


class MersenneTwister:
    def __init__(self):
        self.state = []
        self.index = 0

    def seed(self, seed):
        """
        Initialize generator.

        :param seed: An integer value to seed the generator with
        """
        self.state = []
        self.index = 0
        self.state.append(seed)
        for i in range(1, 624):
            n = (0x6c078965 * (self.state[i-1] ^ (self.state[i-1] >> 30)) + i)
            n &= 0xffffffff
            self.state.append(n)

    def randint(self):
        """
        Extracts a random number.

        :rtype: A random integer
        """
        if self.index == 0:
            self.generate()

        y = self.state[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= y >> 18

        self.index = (self.index + 1) % 624
        return y

    def generate(self):
        """
        Generates 624 random numbers and stores in the state list.

        """
        for i in range(624):
            n = self.state[i] & 0x80000000
            n += self.state[(i+1) % 624] & 0x7fffffff
            self.state[i] = self.state[(i+397) % 624] ^ (n >> 1)
            if n % 2 != 0:
                self.state[i] ^= 0x9908b0df
