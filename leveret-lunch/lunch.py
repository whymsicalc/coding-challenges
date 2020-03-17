"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # figure out where to start
    start_row = []
    start_col = []
    if nrows % 2 == 0:
        start_row += [int(nrows/2) - 1]
        start_row += [int(nrows/2)]
    else:
        start_row += [int(nrows/2)]

    if ncols % 2 == 0:
        start_col += [int(ncols/2) - 1]
        start_col += [int(ncols/2)]
    else:
        start_col += [int(ncols/2)]

    start = []
    start_count = 0
    for idx1 in start_row:
        for idx2 in start_col:
            if garden[idx1][idx2] > start_count:
                start_count = garden[idx1][idx2]
                start = [idx1, idx2]

    # create count = number in starting spot
    carrots = 0
    if start:
        carrots = garden[start[0]][start[1]]
    # number in starting spot becomes 0 since items all eaten
        garden[start[0]][start[1]] = 0

    # eat carrots (looks at the neighbors in WNES order and finds the highest carrot count)
        next_loc = []
        next_count = 0
        while True:
            row = [start[0], start[0]-1, start[0], start[0]+1]
            col = [start[1]-1, start[1], start[1]+1, start[1]]
            for idx in range(4):
                if -1 < row[idx] < nrows and -1 < col[idx] < ncols:
                    if garden[row[idx]][col[idx]] > next_count:
                        next_count = garden[row[idx]][col[idx]]
                        next_loc = [row[idx], col[idx]]
            if next_count == 0:
                break
            else:
                carrots += garden[next_loc[0]][next_loc[1]]
                garden[next_loc[0]][next_loc[1]] = 0
                start = next_loc
                next_loc = []
                next_count = 0

    # if wnes = 0
    return carrots


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
