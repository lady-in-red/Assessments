"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""
# this took 6 hours because I got stuck on maths.


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # create empty set, parse over list, add, and return sorted set
    without_duplicates = set()
    for word in words:
        without_duplicates.add(word)
    return sorted(without_duplicates)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # change both lists into sets, find intersection, return sorted
    items1 = set(items1)
    items2 = set(items2)
    find_unique_common_items = items1 & items2
    return sorted(find_unique_common_items)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # the math on this one stumped me for a while. 
    # Kept getting duplicates
    # Finally added line 113, solved problem! Still not sure why
    # it kept skipping 2.


    # set numbers, empty list,
    pairs = set()
    # check = []
    # numbers = set(numbers)
    numbers = list(set(numbers))
    for number in numbers:
        if number >= 0:
            if (-1 * number) in numbers:
                pair = (number, (-1 * number))
                pairs.add(pair)
                # numbers.remove(number)
            #numbers.remove(-number)

    # add pair of 0s if in list
    return pairs

    ## This passed 3/4 tests. not sure why fail 1?
    # for number in numbers:
    #     if 0 in numbers:
    #         pairs.add((0, 0))
    #     if number and (number * -1) in numbers:
    #         zero_pair = (number, (number * -1))
    #         pairs.add(zero_pair)
    #         numbers.remove(number)
    #         numbers.remove(number * -1)

    ## this + if 0 statement had duplicates
    # for number in numbers:
    #     # set varibale to check against
    #     check = number
    #     # loop over numbers again, checking for opposition
    #     for number in numbers:
    #         # add tuple if == 0
    #         if check + number == 0:
    #             pair = (check, number)
    #             pairs.add(pair)


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    letter_count = {}
    characters = phrase.replace(' ', '')
    # make characters all lower, add to dictionary with occurance
    for character in characters:
        character = character.lower()
        letter_count[character] = letter_count.get(character, 0) + 1

    # empty lists to move things around in
    pair_list = []
    hold_letter = []
    # add all pairs to list as value, key
    for letter, value in letter_count.items():
        pair_list.append((value, letter))
    # sort list so highest occurance is last
    sorted_pairs = sorted(pair_list)
    # for items in list, if value is equal to last, append
    for num, let in sorted_pairs:
        if num == sorted_pairs[-1][0]:
            hold_letter.append(let)

    return hold_letter


    ## how I was trying before:
    # for i in range(len(sorted_pairs)):
    #     if sorted_pairs[i] == sorted_pairs[-1]:
    #         hold_letter.append((sorted_pairs[i]))
    # # add letter to list
    # for num, let in hold_letter:
    #     highest_occuring.append(let)

    # place_holder_count = 0
    # hold_letter = []
    # place_holder_count = 0
    # for letter, l_count in sorted(letter_count.items()):
    #     if l_count > place_holder_count:
    #         place_holder_count = l_count
    #         hold_letter.append(letter)
    # for letter, l_count in sorted(letter_count.items()):
    #     if l_count == place_holder_count:
    #         hold_letter.append(letter)

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
