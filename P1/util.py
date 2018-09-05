# encoding:utf-8
__author__ = 'admin'

def lines(file):
    for line in file:
        yield line
    yield "\n"

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block=[]
"""
def creatGenerator(n):
    mylist = range(n)
    for i in mylist:
        print i
        return i*i

def creatTest(n):
    mylist = range(n)
    for i in mylist:
        print i
        yield i*i

if __name__ == "__main__":
    number = int(raw_input("input a number:"))
    creatGenerator(number)
    creatTest(number)
"""