""" 
	knuth.py
	Implementation of the Fisher-Yates/Knuth shuffle
	
	Pre: Takes any list, unshuffled
	Post: Returns list shuffled randomly

	Time Complexity: n
	Space Complexity: n

	Pseudocode: http://en.wikipedia.org/wiki/Fisher%E1%80%93Yates_shuffle

"""
import random


def shuffle(li):
	random.seed()
	for i in xrange(len(li) - 1, 0, -1):
		j = random.randint(0, i)
		li[i], li[j] = li[j], li[i]
	return li
