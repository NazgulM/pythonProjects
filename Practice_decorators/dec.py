# def textFunction():
#      print("Result of this function: ")
#      print("Program has finished")

# def addTwoSum(a,b):
#     textFunction()
#     print(a+b)
    

# def multiply(a,b,c):
#     textFunction()
#     print(a*b*c)
    

# if __name__ == "__main__":
#     addTwoSum(5,8)
#     multiply(8,6,9)


# def textFunction():
#      print("Result of this function: ")
#      addTwoSum(10,12)
#      print("Program has finished")

# def addTwoSum(a,b):
#     print(a+b)
    

# def multiply(a,b,c):
#     print(a*b*c)
    

# if __name__ == "__main__":
#     textFunction()

# Decorators - functions that can add new functionality to another 
# function without changing the code

# def meat():
#      print("------TOMATO----")
#      print("@@@@@@SALAD@@@@")
#      print("======MEAT====")
#      print("@@@@@@SALAD@@@@")
#      print("~~~~~~TOMATO~~~~~~")

def bread(fun):
    def wrapper():
        print("~~~~~~~~~~~~~~~~~~~")
        fun()
        print("~~~~~~~~~~~~~~~~~~~")
    return wrapper

def tomato(fun):
    def wrapper():
        print("@@@@@@@@@@@@@@@@@@@@@")
        fun()
        print("@@@@@@@@@@@@@@@@@@@@@")
    return wrapper


def cucumber(fun):
    def wrapper():
        print("&&&&&&&&&&&&&&&&&&&&&&")
        fun()
        print("&&&&&&&&&&&&&&&&&&&&&&")
    return wrapper


def souce(fun):
    def wrapper():
        print("========KETCHUP=========")
        fun()
        print("=========CHEESE==========")
    return wrapper

@bread
@tomato
@cucumber
def meat():
    print("======MEAT=======")


@bread
@souce
def fish():
    print("======FISH=======")


@bread
@cucumber
def chicken():
    print("======CHICKEN=====")


def decoration_with_args(fun):
    def wrapper(*args, **kwargs):
        print(f"Welcome our Guest!\n Please introduce yourself.")
        fun(*args,**kwargs)

        print(f"Nice to meet you! {args[0]} {args[1]}! "
              f"Wish you good luck {args[3]}")
    return wrapper

@decoration_with_args
def showFullName(fName, sName,country, fkClub):
    print(f"My name is {fName} {sName}")

if __name__ == "__main__":
    # meat()
    # fish()
    # chicken()
    showFullName("Lionell", "Messi", "Argentina","PSG")