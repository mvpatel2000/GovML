#!/usr/bin/python3
import os
import sys
import re
import numpy as np


def build_categories(data):
    categories = dict()
    for r in data:
        if r[0] not in categories:
            categories[r[0]] = [0, 0, 0]
        categories[r[0]][0] += float(r[2])  # rep
        categories[r[0]][1] += float(r[3])  # dem
        categories[r[0]][2] += float(r[4])  # ind
    return categories


def build_matrix(data, categories):
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
    return matrix


def print_matrix(matrix):
    for k in matrix.keys():
        print(k)
        print(' Rep:')
        for t in matrix[k][0].keys():
            print('\t{0:100s} {1:5f}'.format(t, matrix[k][0][t]))
        print(' Dem:')
        for t in matrix[k][1].keys():
            print('\t{0:100s} {1:5f}'.format(t, matrix[k][1][t]))
        print(' Ind:')
        for t in matrix[k][2].keys():
            print('\t{0:100s} {1:5f}'.format(t, matrix[k][2][t]))
        print()


def main():
    filename = ''
    command = ''
    if len(sys.argv) > 2:
        filename = sys.argv[2]

        if not os.path.exists(filename):
            print('Invalid file')
            print('Usage: ./process.py <command> <filename>')
            print('Commands:')
            print('\tprint - Prints formatted contents of csv')
            return 1
        command = sys.argv[1]
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
            row = line.split(',')
            data.append(row)
            line = f.readline().rstrip()

    categories = build_categories(data)
    matrix = build_matrix(data, categories)

    if command == 'print':
        print(categories)
        print_matrix(matrix)

    return 0


if __name__ == '__main__':
    main()
