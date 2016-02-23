#!/usr/bin/env python

import sys
import re
import time
import subprocess


def process_list():
    command = subprocess.Popen(["ps", "ax"], stdout=subprocess.PIPE)
    if command.wait() != 0:
        raise Exception("command ps didn't work!")
    return command.stdout


def find_pid(row):
    match = re.match("^\s*(\d+)", row)
    return int(match.groups()[0])


class Logger(object):

    know_pids = []

    def log(self, row):
        pid = find_pid(row)
        if pid not in self.know_pids:
            self.know_pids.append(pid)
            print row.strip()


def main():
    pattern = sys.argv[1]
    l = Logger()

    while True:
        for row in process_list():
            if pattern in row:
                l.log(row)
        time.sleep(1)


if __name__ == "__main__":
    main()
