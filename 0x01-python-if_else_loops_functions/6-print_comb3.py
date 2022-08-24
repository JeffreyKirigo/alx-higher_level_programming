#!/usr/bin/python3
for num in range(0,10):
    for sec_num in range(num + 1,10):
        if num != sec_num and num != 8 and sec_num != 9:
            print("{}{}".format(num, sec_num), end=", ")
        else:
            print("{}{}".format(num, sec_num))
