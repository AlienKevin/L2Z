from typing import List


def load_vocab(name: str) -> List[str]:
    with open("{}.txt".format(name), "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]
