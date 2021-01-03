# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
            pass

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print('Success')
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
