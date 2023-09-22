import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'e4ea0399070e864444a33dc7ddcc70329bb3f72e', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
