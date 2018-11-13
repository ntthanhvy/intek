#!/usr/bin/env python3

import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='put command')
    parser.add_argument('-m', help='commit content')
    args = parser.parse_args()
    command = args.command
    return command


class MyDirectory:
    def __init__(self):
        # DO: if files/directories aren't there:
        self.create_lgit()
        # DO: if files/directories are there:
        # Do: Update?
        pass

    def create_lgit(self):
        # The command lgit init will create the directory structure.
        self.create_objects()
        self.create_commits()
        self.create_snapshots()
        self.createf_index()
        self.createf_config()
        pass

    def create_objects(self):
        # a directory objects will store the files you lgit add
        pass

    def create_snapshots(self):
        # a directory snapshots will store the actual file listings
        pass

    def create_commits(self):
        # a directory commits will store the commit objects:
        # those are not the actual file listings but some information about the commit (author, date & commit message)
        pass

    def createf_index(self):
        # a file index will host the staging area & other information
        pass

    def createf_config(self):
        # a file config will store the name of the author, initialised from the environment variable LOGNAME
        pass

    def update(self):
        # update the file base on command if files/dirs are already created
        pass


class Commands:
    def __init__(self):
        self.directory = MyDirectory()

    def do_command(self, command):
        return getattr(self, str(command))()

    def init(self):
        # lgit init:
        # initialises version control in the current directory
        # (until this has been done, any lgit command should return a fatal error) --IMPORTANT
        print('init')

    def add(self):
        # lgit add: stages changes, should work with files and recursively with directories
        print('add')

    def rm(self):
        # lgit rm: removes a file from the working directory and the index
        print('remove')

    def config(self):
        # lgit config --author: sets a user for authoring the commits
        print('config --author')

    def commit(self):
        # lgit commit -m: creates a commit with the changes currently staged
        # (if the config file is empty, this should not be possible!)
        print('commit -m')

    def status(self):
        # lgit status:
        # updates the index with the content of the working directory and displays the status of tracked/untracked files
        print('status')

    def ls(self):
        # lgit ls-files: lists all the files currently tracked in the index, relative to the current directory
        print('ls-file')

    def log(self):
        # lgit log: shows the commit history
        print('log')


def main():
    # DON'T FIX THIS
    command = get_arguments()
    Commands().do_command(command)


if __name__ == '__main__':
    main()