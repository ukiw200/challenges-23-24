import os
from hashlib import sha1


def verify():
    assert os.path.exists('solution.txt'), 'FAIL: solution.txt does not exist'

    with open('solution.txt') as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest(
    ) == '66918b524219ea3ae22e98bfd330ed920691a26a', 'FAIL: incorrect solution'

    solution2Path = os.path.join('challenge-1', 'solution.txt')
    assert os.path.exists(
        solution2Path), 'FAIL: solution.txt does not exist'

    with open(solution2Path) as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest(
    ) == '8f5ed5c56512c61e4b70aeb084b5040773cd4a35', 'FAIL: incorrect solution'

    print("SUCCESS: challenge completed.")
    return True


verify()
