import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '674379f134d55a4adbd61cdf640ce2df2d2f887c', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
