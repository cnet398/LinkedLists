from operator import itemgetter


class Node:
    def __init__(self, item, next):
        self.mItem = item
        self.mNext = next


class UUC:
    def __init__(self):
        self.mFirst = None

    def Size(self):
        count = 0
        current = self.mFirst
        while current:
            count += 1
            current = current.mNext
        return count

    def Insert(self, item):
        if self.Exists(item):
            return False
        self.mFirst = Node(item, self.mFirst)
        return True

    def Delete(self, item):
        if not self.Exists(item):
            return False
        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True
        current = self.mFirst
        while not current.mNext.mItem == item:
            current = current.mNext
        current.mNext = current.mNext.mNext
        return True

    def Exists(self, item):
        current = self.mFirst
        while current:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def Retrieve(self, item):
        if not self.Exists(item):
            return None
        current = self.mFirst
        while not (current.mItem == item):
            current = current.mNext
        return current.mItem

    def Traverse(self, callback, data):
        current = self.mFirst
        while current:
            callback(current.mItem, data)
            current = current.mNext

    def PrintName(s, data):
        data.age += int(s.mAge)