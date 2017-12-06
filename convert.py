#!/usr/bin/python3
import os
import sys
import re


def main():
    filename = ''
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if not os.path.exists(filename):
            print("Invalid file")
            print("Usage: ./convert.py <filename>")
            return 1
    
    else:
        print("Usage: ./convert.py <filename>")
        return 1

    data = []
    with open(filename) as f:
        headers = [f.readline().rstrip().split(',') for i in range(4)]
        cols = [''] * len(headers[0])
        for h in headers:
            for i in range(len(h)):
                cols[i] = cols[i] + h[i]
#        cols = cols[:2] + cols[7:10]
        print('\t', cols)
            
        line = f.readline().rstrip()
        row = line.split(",")
        data.append(row)

        num = 0
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
#                row = row[:2] + row[7:10]
                data.append(row)
                print(len(row), '\t', row)
                num += 1
            line = f.readline().rstrip()
    out = 'out.csv'
    with open(out, 'w+') as f:
        f.write(','.join(cols) + '\n')
        for r in data:
            f.write(','.join(r) + '\n')
    return 0
            
                


if __name__ == '__main__':
    main()
