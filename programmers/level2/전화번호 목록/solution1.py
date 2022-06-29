class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, key):
        cur_node = self.head

        for ch in key:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            cur_node = cur_node.children[ch]

        cur_node.data = key

    def isstartswith(self, key):
        cur_node = self.head

        for ch in key:
            if ch in cur_node.children:
                cur_node = cur_node.children[ch]
                if cur_node.data:
                    return True
            else:
                return False

        return True


def solution(phone_book):
    trie = Trie()
    trie.insert(phone_book[0])

    for phone_num in phone_book[1:]:
        if trie.isstartswith(phone_num):
            return False
        trie.insert(phone_num)

    return True


if __name__ == '__main__':
    phone_book = ["12","123","1235","567","88"]
    print(solution(phone_book))
