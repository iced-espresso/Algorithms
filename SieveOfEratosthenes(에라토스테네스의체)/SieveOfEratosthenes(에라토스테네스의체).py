import math
import random

def era1(n:int):
    visitCnt=0
    isPrime = [False if i % 2 == 0 else True for i in range(0,n+1)]
    sqrtn = int(math.sqrt(n) + 1)
    for i in range(3, sqrtn ,2):
        for mul in range(i*i, n+1, i):
            isPrime[mul] = False
            visitCnt += 1

    # print("1: " + str(visitCnt))
    primeList = [x for x in range(2,n+1) if isPrime[x]]
    primetext = ""
    
    for x in primeList:
        primetext += str(x) + " "
    return primetext

class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data
        return

    def remove(self):
        if self.prev != None:
            self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node:Node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node:Node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        node.remove()
    
    def toList(self):
        myList = []
        curr = self.head
        while curr != None:
            myList.append(curr.data)
            curr = curr.next
        return myList

def era2(n:int):
    myLinkedList = DLinkedList()
    myLinkedList.append(Node(2))
    for i in range(3, n+1, 2):
        myLinkedList.append(Node(i))

    visitCnt = 0
    sqrtNum = int(math.sqrt(n) + 1)
    ref = myLinkedList.head
    while ref != None:
        refNum = ref.data
        curr = ref.next
        if refNum > sqrtNum:
            break
        while curr != None:
            visitCnt += 1
            if curr.data % refNum == 0:
                myLinkedList.remove(curr)
            curr = curr.next
        ref = ref.next

    myList = myLinkedList.toList()
    # print("2: " + str(visitCnt))
    primetext = ""
    
    for x in myList:
        primetext += str(x) + " "
    # print("end")
    return primetext
    

f = open("prime.txt", "r")
line = f.readline()

for i in range(1000):
    rnd = random.randrange(3,104831)
    myprime = era1(rnd)
    if myprime not in line:
        print("era1 error")

    # myprime2 = era2(rnd)
    # if myprime2 not in line:
    #     print("era2 error")

print("done")

f.close()
