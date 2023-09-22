import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'c16f6bb6259c2d5a5a7589ebb722b2c2313fe026', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
