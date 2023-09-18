import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '158df1a554b7d1f39cacea5f48c29d7ce3787dab', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
