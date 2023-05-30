def find_sum_text(fun):
    def wrapper(someList):
        textToWrite = "All elements of list"
        with open("task1.txt", "w") as f:
            for i in someList:
                textToWrite +=f'\n{i}'
            
            textToWrite +='\n'
            textToWrite += '-' * 50
            textToWrite += '\nSum of all numbers from list: \n'
            textToWrite += '-' * 50
            textToWrite += f'\n{sum(someList)}\n'
            textToWrite += '-' * 50
            f.write(textToWrite)

        print("Saved to file")
    return wrapper

@find_sum_text
def showList(someList):
    return someList


if __name__=="__main__":
    showList([12,43,34,54,6])