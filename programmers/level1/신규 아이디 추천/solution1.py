import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-zA-Z0-9.\-_]', "", new_id)
    new_id = re.sub('[.]+', ".", new_id)
    new_id = re.sub('^[.]|[.]$', "", new_id)

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


if __name__ == '__main__':
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))
