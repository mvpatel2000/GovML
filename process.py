#!/usr/bin/python3
import os
import sys
import re


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
            line = f.readline().rstrip()
            '''
            row = line.split(',')
            data.append(row)
            line = f.readline().rstrip()
            
    category = ''
    categories = dict()
    r = 0
    for r in data:
        print(r)
        if r[0] in categories:
            rep = r[2]
            dem = r[3]
            ind = r[4]
            #categories[r[0]].append()
    '''while r < len(data):
        #if "  " not in data[r][1]:
            #if data[r][0] != '' and data[r][1] != '' and data[r][-2] != '' and data[r][0].upper() == data[r][0]:
        if data[r][0] != '':
            category = data[r][0]
            if category not in categories:
                sr = r
                sub = data[r + 1][0]
                while sub == '':
                    sub = data[sr][0]
                    sr += 1
                categories[category] = ((r, sr), dict(), dict(), dict())
                print(category)
                print(categories[category])
                print(sr)
                #all_data.append([dict(), dict(), dict()]) #dem, rep, ind
        else:
            if '\t' in data[r][1]:
                print("subcategory")
        r += 1
            
    '''         
        #print(last_category)
    print(categories)   
    return 0
            
                
if __name__ == '__main__':
    main()
