def oooops(list):
        list[100] = "i"

def oooops(list):
    try:
        list[100] = "i"
    except IndexError:
        print("The list is out of bounds")
