first= "testlido"
second= "more more"
third= "other names random"

#choice= 0

queue=[]

def addQueue(name):
    queue.append(name)
    print(queue)

def dropQueue():
    temp= queue.pop(0)
    print(queue)

addQueue(first)
addQueue(second)
addQueue(third)

dropQueue()
dropQueue()
dropQueue()