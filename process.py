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
        headers = [f.readline().rstrip().split(',') for i in range(4)]
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
            line = f.readline().rstrip()

    category = ''
    categories = dict()
    for r in range(len(data)):
        #if "  " not in data[r][1]:
            #if data[r][0] != '' and data[r][1] != '' and data[r][-2] != '' and data[r][0].upper() == data[r][0]:
        if data[r][0] != '':
            category = data[r][0]
            if category not in categories:
                sub = ''
                sr = r
                while sub == '':
                    sr += 1
                    sub = data[sr][0]
                categories[category] = ((r, sr), dict(), dict(), dict())
                print(category)
                print(categories[category])
                #all_data.append([dict(), dict(), dict()]) #dem, rep, ind
        else:
            if '\t' in data[r][1]:
                print("subcategory")
            
                
        #print(last_category)
    print(categories)   
    return 0
            
                
if __name__ == '__main__':
    main()
