import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(file.read().strip().lower().encode("utf-8")).hexdigest()

    assert (
        solution == "6f5db9a52ab0685548f52d44dc9708b164cc4e1e"
    ), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
