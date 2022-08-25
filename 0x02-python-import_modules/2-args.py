#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    count = len(argv) - 1
    if count > 1:
        print("{} arguments:".format(count))
    elif count == 0:
        print("0 arguments.")

    for i in range(count):
        if count == 1:
            print("1 argument:")
        print("{}: {}".format(i + 1, argv[i + 1]))
