def oooops(list):
    try:
        list[100] = "i"
    except IndexError:
        print("going beyond the boundaries")



oooops([1, 2])