import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '1df5c848cdedbe6a39c36f052f9142b027543475', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
