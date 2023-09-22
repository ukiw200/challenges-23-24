import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'f7fb1fbc91f33126a9ec16a2ec001c88cefe72ff', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
