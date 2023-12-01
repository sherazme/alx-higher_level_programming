#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(sys.argv)

    num = 0
    for i in range(1, argc):
        num += int(argv[i])

    print(num)
