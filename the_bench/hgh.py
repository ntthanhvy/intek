#!/usr/bin/env python3
import json
import sys


def load_query():
    with open(str(sys.argv[1]), "r") as f:
        query = json.load(f)
    return query


def check(query, data, pos):
    op = query['op']
    left = query['left']
    right = query['right']
    for x in pos.keys():
        if x in left:
            value = data[pos[x]]
            break
    if "first_letter" in left:
        value = value[0]
    if op == '=':
        if left != 'age':
            return value == right
        else:
            return value == int(right)
    elif op == '>':
        if left != 'age':
            return value > right
        else:
            return value > int(right)
    elif op == '<':
        if left != 'age':
            return value < right
        else:
            return value < int(right)
    elif op == '!=':
        if left != 'age':
            return value != right
        else:
            return value != int(right)


def output(result):
    for i in result:
        for x in i:
            for y in range(len(x)):
                if y != len(x) - 1:
                    print(str(x[y]) + ', ', end='')
                else:
                    print(str(x[y]))


def output2(result):
    for x in result:
        for y in range(len(x)):
            if y != len(x) - 1:
                print(str(x[y]) + ', ', end='')
            else:
                print(x[y])


def main():
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    query = load_query()
    if type(query)  == type([]):
        lines = sys.stdin.readlines()
        result = []
        subresult = []
        flag = 1
        for line in lines:
            line = line.split(",")
            line[3] = int(line[3])
            line[5] = line[5][:len(line[5]) - 1]
            for x in range(len(query)):
                result.append([])
                subresult.append({})
                flag = 1
                if "where_and" in query[x].keys():
                    for y in query[x]['where_and']:
                        if check(y, line, pos) is False:
                            flag = 0
                            break
                elif "where_or" in query[x].keys():
                    flag = 0
                    for y in query[x]['where_or']:
                        if check(y, line, pos) is True:
                            flag = 1
                            break
                if flag == 1:
                    list = []
                    for y in query[x]['select'].split(", "):
                        list.append(line[pos[y]])
                    if 'order' in query[x].keys():
                        if line[pos[query[x]['order']]] not in subresult[x].keys():
                            subresult[x][line[pos[query[x]['order']]]] = [list]
                        else:
                            subresult[x][line[pos[query[x]['order']]]].append(list)
                    else:
                        result[x].append(list)
        for x in range(len(query)):
            if 'order' in query[x].keys():
                for y in sorted(subresult[x].keys()):
                    for z in subresult[x][y]:
                        result[x].append(z)
        output(result)
    else:
        result = []
        subresult = {}
        line = sys.stdin.readline()
        while line != "":
            line = line.split(",")
            line[3] = int(line[3])
            line[5] =  line[5][:len(line[5]) - 1]
            if "where_and" in query.keys():
                flag = 1
                for x in query['where_and']:
                    if check(x, line, pos) is False:
                        flag = 0
                        break
            elif "where_or" in query.keys():
                flag = 0
                for x in query['where_or']:
                    if check(x, line, pos) is True:
                        flag = 1
                        break
            if flag == 1:
                list = []
                for x in query['select'].split(", "):
                    list.append(line[pos[x]])
                if 'order' in query.keys():
                    subresult[line[pos[query['order']]]] = list
                else:
                    result.append(list)
            line = sys.stdin.readline()
        if 'order' in query.keys():
            for x in sorted(subresult.keys()):
                result.append(subresult[x])
        output2(result)


main()
