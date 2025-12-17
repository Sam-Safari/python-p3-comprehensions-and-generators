#!/usr/bin/env python3

def return_evens(num_list):
    """Return a list of the even integers from the iterable `num_list`.

    Uses a list comprehension to collect numbers where n % 2 == 0.
    Works with any iterable of integers (range, list, tuple, etc.).
    """
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    """Return a new list with an exclamation mark appended to each sentence.

    Uses a list comprehension to concatenate '!' to each string from
    `sentence_list`. If the input is empty, returns an empty list.
    """
    return [s + "!" for s in sentence_list]