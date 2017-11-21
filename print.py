#!/usr/bin/python3
import os
import sys
import re


def main():
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if not os.path.exists(filename):
            print("Invalid file")
            print("Usage: ./process.py <filename>")
            return 1
    
    else:
        print("Usage: ./process.py <filename>")
        return 1

    data = []
    num = 1
    with open(filename) as f:
        headers = []
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        cols = [""] * len(headers[0])
        for h in headers:
            for i in range(len(h)):
                cols[i] = cols[i] + h[i]
        print(str(num) + " " + str(cols))
            
        num += 1
        line = f.readline()
        row = line.split(",")
        data.append(row)

        while line != "":
            row = line.split(",")
            data.append(row)
            line = f.readline()
            print(str(num) + " " + str(row))
            num += 1
    return 0
            
                


if __name__ == '__main__':
    main()
