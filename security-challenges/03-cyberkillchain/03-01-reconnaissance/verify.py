import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '9a566a54f5013e1073228ed0beb0b30f686794e6', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
