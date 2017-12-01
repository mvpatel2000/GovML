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
            print("Usage: ./print.py <filename>")
            return 1
    
    else:
        print("Usage: ./print.py <filename>")
        return 1

    data = []
    with open(filename) as f:
        headers = []
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        headers.append(f.readline().split(","))
        cols = [''] * len(headers[0])
        for h in headers:
            for i in range(len(h)):
                cols[i] = cols[i] + h[i]
        print(cols)
            
        line = f.readline().rstrip()
        row = line.split(",")
        data.append(row)

        while line != '':
            commas = 0
            if '$' in line:#re.search(r'(?:[^,\d]|^)(\d{1,3}(?:,\d{3})*)(?:[^,\d]|$)', line): #income
                for i in range(len(line)):
                    if line[i] == ",":
                        commas += 1
                        if commas == 2 or commas == 3:
                            line = line[:i] + '#' + line[i + 1:]
                line = re.sub(r'[#]', '', line)
            if re.sub(r'[,]', '', line) != '' and 'Source:' not in line:
                row = re.split(r'[,"]', line)
                data.append(row)
                print(row)
            line = f.readline().rstrip()

    return 0
            
                


if __name__ == '__main__':
    main()
