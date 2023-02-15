
class LinkedList:

    def __init__(self, data):


class Node:

    def __init__(self, data) -> None:
        self.data = data  # self.data holds whatever the specific node holds in memory
        self.next = None  # self.next is a reference to the next node in the LL

    def __repr__(self) -> str:
        return self.data  # returns a string representation of the nodes contents
