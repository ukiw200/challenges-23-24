import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'a60eb0ab04a573d8744fc384312d4dda141f9afb', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
