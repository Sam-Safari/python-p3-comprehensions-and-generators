#!/usr/bin/env python3

from lib.list_comprehension import return_evens, make_exclamation

# Replicate the tests from lib/testing/lib_test.py so we can run without pytest

def main():
    # TestReturnEvens
    num_list = range(1,10,2)
    assert return_evens(num_list) == [], "Expected empty list when no evens"

    num_list = range(10)
    assert return_evens(num_list) == [0, 2, 4, 6, 8], "Evens from 0..9"

    # TestMakeExclamation
    assert make_exclamation([]) == [], "Empty input should return empty list"

    sentence_list = [
        "I like computers",
        "I require coffee",
        "Live long and prosper",
    ]
    expected = [
        "I like computers!",
        "I require coffee!",
        "Live long and prosper!",
    ]
    assert make_exclamation(sentence_list) == expected, "Should append exclamation marks"

    print("All tests passed (replicated without pytest).")

if __name__ == '__main__':
    main()
