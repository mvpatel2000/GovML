#!/usr/bin/python3
import os
import sys
import re


class Category:
    def __init__(self, name, data, start, end): #name of category e.g. "Religion", data array, start and end indices in data array
        self.name = name
        self.dem = dict()
        self.rep = dict()
        self.ind = dict()
            
    def as_array(self):
        return list(self.dem, self.rep, self.ind)


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
        print(cols)
            
        line = f.readline()
        row = line.split(",")
        data.append(row)

        while line != "":
            row = line.split(",")
            data.append(row)
            line = f.readline()

    all_data = []

    last_category = ""
    categories = dict()
    category = 0
    for r in range(len(data)):
        if "  " not in data[r][1]:
            if data[r][0] != "" and data[r][1] != "" and data[r][-2] != "" and data[r][0].upper() == data[r][0]:
                last_category = data[r][0]
                if last_category not in categories:
                    categories[last_category] = category
                    #all_data.append([dict(), dict(), dict()]) #dem, rep, ind
                    category += 1
            
                
        #print(last_category)
    print(categories)   
    return 0
            
                
if __name__ == '__main__':
    main()
