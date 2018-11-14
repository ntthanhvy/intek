#!/usr/bin/env python3

import os
import argparse
import hashlib
import datetime


# ---------------get arg----------
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('filename', nargs='?', type=argparse.FileType('wb'))
    return parser.parse_args()


# ------------lgit init----------------
'''This 'init' command will create a .lgit directory
contain 2 dir: objects, commits and snapshots
and 2 file index and config.
There will be a LOGNAME environment valriable that store in the config file
'''
def initialize_dir():
    os.mkdir('.lgit')
    os.mkdir('.lgit/objects')
    os.mkdir('.lgit/commits')
    os.mkdir('.lgit/snapshots')
    index = os.open('.lgit/index', os.O_RDWR | os.O_CREAT)
    config = os.open('.lgit/config', os.O_RDWR | os.O_CREAT)
    varname = os.environ['LOGNAME'].encode('utf-8')
    os.write(config, varname)
    os.close(index)
    os.close(config)
    return


# initialize_dir(get_args().command)


# -------------lgit add------------------------
def add_object(filename):
    # create object in objects dir
    name = filename.name
    path = os.path.abspath(name)
    fileRead = os.open(name, os.O_RDWR)
    fileContent = os.read(fileRead, os.stat(name).st_size)
    encodeContent = hashlib.sha1(fileContent).hexdigest()
    os.mkdir('.lgit/objects/' + encodeContent[:2])  # make dir
    path = '.lgit/objects/' + encodeContent[:2]
    objectName = os.open(path + '/' + encodeContent[3:], os.O_RDWR | os.O_CREAT)
    os.write(objectName, fileContent)  # write object content
    os.close(objectName)
    return

# ------------write index file------------
def add_index(filename):
    name = filename.name
    path = os.path.abspath(name)
    # get timestamp of the file
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    index = os.open('.lgit/index', os.O_RDWR)
    index_read = os.read(index, os.stat(index).st_size)
    # create a list to contain the info of the file
    index_lst = []
    index_lst.append(timestamp)
    # get the current hash code of file and after added has
    curf_hash = hashlib.sha1(index_read).hexdigest()
    addedf_hash = hashlib.sha1(index_read).hexdigest()
    index_lst.append(curf_hash)
    index_lst.append(addedf_hash)
    # because there isn't commit yet so there are 40 empty space
    index_lst.append(' ' * 40)
    # get the path of the file (basename or full path isn't clear yet)
    index_lst.append(os.path.basename(path) + '\n')
    # read from the begining of the index file
    os.lseek(index, 0, 1)
    # encode str in list into yte-like object and write it to inde file
    os.write(index, ' '.join(index_lst).encode())
    os.close(index)
    # print(index_lst)
    return

def main():
    args = get_args()
    if args.command == 'init':
        initialize_dir()
    if args.command == 'add':
        # add_object(args.filename)
        add_index(args.filename)


main()
