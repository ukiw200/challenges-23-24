import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = sha1(file.read().strip().encode('utf-8')).hexdigest()

    assert solution == 'eee72e0a6878717ec45080756dc78e25d010f884', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
