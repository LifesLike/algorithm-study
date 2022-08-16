import re


def sort_by_head(file):
    return re.split("[0-9]+", file.lower())[0]


def sort_by_num(file):
    return int(re.findall("[0-9]+", file)[0])


def solution(files):
    return sorted(files, key=lambda file: (sort_by_head(file), sort_by_num(file)))


if __name__ == '__main__':
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))
