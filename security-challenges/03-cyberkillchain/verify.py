import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'fd37a11c625d87133c0e26a903e3260192a048d3', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
