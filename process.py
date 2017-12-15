#!/usr/bin/python3
import os
import sys
import re
import numpy as np


def main():
    filename = ''
    if len(sys.argv) > 2:
        filename = sys.argv[2]

        if not os.path.exists(filename):
            print('Invalid file')
            print('Usage: ./process.py <command> <filename>')
            print('Commands:')
            print('\tprint - Prints formatted contents of csv')
            return 1
    else:
        print('Usage: ./process.py <command> <filename>')
        print('Commands:')
        print('\tprint - Prints formatted contents of csv')
        return 1

    data = []
    with open(filename) as f:
        cols = f.readline().rstrip().split(',')
        print(cols)
        line = f.readline().rstrip()
        row = line.split(',')
        data.append(row)

        while line != '':
            commas = 0
            '''if '$' in line:#re.search(r'(?:[^,\d]|^)(\d{1,3}(?:,\d{3})*)(?:[^,\d]|$)', line): #income
                for i in range(len(line)):
                    if line[i] == ",":
                        commas += 1
                        if commas == 2 or commas == 3:
                            line = line[:i] + '#' + line[i + 1:]
                line = re.sub(r'[#]', '', line)
            if re.sub(r'[,]', '', line) != '' and 'Source:' not in line:
                row = re.split(r'[,"]', line)
                row = row[:1] + row[7:10]
                data.append(row)
            line = f.readline().rstrip()'''
            row = line.split(',')
            data.append(row)
            line = f.readline().rstrip()

    category = ''
    categories = dict()
    for r in data:
        if r[0] not in categories:
            categories[r[0]] = [0, 0, 0]
        categories[r[0]][0] += float(r[2])  # rep
        categories[r[0]][1] += float(r[3])  # dem
        categories[r[0]][2] += float(r[4])  # ind

    print(categories)
    matrix = dict()
    for r in data:
        if r[0] not in matrix:
            matrix[r[0]] = [dict(), dict(), dict()]

        if categories[r[0]][0] == 0:
            matrix[r[0]][0][r[1]] = 0
        else:
            matrix[r[0]][0][r[1]] = float(r[2]) / categories[r[0]][0]

        if categories[r[0]][1] == 0:
            matrix[r[0]][1][r[1]] = 0
        else:
            matrix[r[0]][1][r[1]] = float(r[3]) / categories[r[0]][1]

        if categories[r[0]][2] == 0:
            matrix[r[0]][2][r[1]] = 0
        else:
            matrix[r[0]][2][r[1]] = float(r[4]) / categories[r[0]][2]

    return 0


if __name__ == '__main__':
    main()
