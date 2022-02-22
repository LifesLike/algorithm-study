import sys

user_input = sys.stdin.readline().strip()

words = []
stack = []
tag = False

for ch in user_input:
    if ch == '<':
        if stack:
            words.extend(stack[::-1])
            stack.clear()
        words.append(ch)
        tag = True
    elif ch == '>':
        words.append(ch)
        tag = False
    elif tag:
        words.append(ch)
    elif ch != ' ':
        stack.append(ch)
    elif ch == ' ':
        words.extend(stack[::-1])
        words.append(" ")
        stack.clear()

if stack:
    words.extend(stack[::-1])

print("".join(map(str, words)))
