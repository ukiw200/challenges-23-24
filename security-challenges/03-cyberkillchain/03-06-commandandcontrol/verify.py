import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == '67026c2823da833a6faf9a2117723f871db76e9e', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
