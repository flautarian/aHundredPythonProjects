def add(*args):
    result = 0
    for num in args:
        result += num
    return result

def addKwargs(**kwargs):
    for key, value in kwargs.items():
        print (key + " - " + value)

print(add(1,2,3,4,5))

addKwargs(one="oneVal", two="twoVal", three="threeVal")