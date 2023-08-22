import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '113fa6777c3616313eac59a0ef708c28d34d3727', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
