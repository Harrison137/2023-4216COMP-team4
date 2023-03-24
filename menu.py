def option1():
    print("hello world")
def option2():
    print("hello world")

def options():
    print("[0] To leave")
    print("[1] Option 1")
    print("[2] Option 2")
    


while True:
    options()
    option = int(input())
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 0:
        break