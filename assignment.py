LinearQueue = []
LinearHead = -1
LinearTail = -1
for _ in range(8):
    LinearQueue.append("")


def LinearEnqueue(Name):
    global LinearHead, LinearTail
    if LinearTail == 7:
        return False
    if LinearHead == -1:
        LinearHead = 0
    LinearTail += 1
    LinearQueue[LinearTail] = Name
    return True


def LinearDequeue():
    global LinearHead
    if LinearHead == -1 or LinearHead > LinearTail:
        return ""
    name = LinearQueue[LinearHead]
    LinearHead += 1
    return name


def LinearCount():
    if LinearHead == -1 or LinearHead > LinearTail:
        return 0
    return LinearTail - LinearHead + 1


CircularQueue = []
CircularHead = -1
CircularTail = -1
NumberItems = 0
for _ in range(5):
    CircularQueue.append("")


def CircularEnqueue(Name):
    global CircularHead, CircularTail, NumberItems
    if NumberItems == 5:
        return False
    if NumberItems == 0:
        CircularHead = 0
        CircularTail = 0
    else:
        CircularTail += 1
        if CircularTail == 5:
            CircularTail = 0
    CircularQueue[CircularTail] = Name
    NumberItems += 1
    return True


def CircularDequeue():
    global CircularHead, CircularTail, NumberItems
    if NumberItems == 0:
        return ""
    name = CircularQueue[CircularHead]
    CircularHead += 1
    if CircularHead == 5:
        CircularHead = 0
    NumberItems -= 1
    if NumberItems == 0:
        CircularHead = -1
        CircularTail = -1
    return name


def GetItem(Position):
    if Position < 0 or Position >= NumberItems:
        return ""
    index = (CircularHead + Position) % 5
    return CircularQueue[index]


def Arrive(Name):
    if CircularEnqueue(Name):
        return "inside"
    if LinearEnqueue(Name):
        return "outside"
    return "full"


def Serve():
    served_customer = CircularDequeue()
    if served_customer == "":
        return ""
    next_customer = LinearDequeue()
    if next_customer != "":
        CircularEnqueue(next_customer)
    return served_customer
