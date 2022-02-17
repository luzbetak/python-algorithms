#!/usr/bin/python3
import re


def domain():
    print("\n+" + "-" * 50)
    print("|    Domain")
    print("+" + "-" * 50)

    fh = open('links.dat')
    for line in fh:
        if re.search('(google|yahoo)', line):
            print(line, end='')


def protocol():
    print("\n+" + "-" * 50)
    print("|    Protocol")
    print("+" + "-" * 50)

    fh = open('links.dat')
    for line in fh:
        print(re.sub('https', 'http', line), end='')


def terms():
    print("\n+" + "-" * 50)
    print("|    Terms")
    print("+" + "-" * 50)

    fh = open('links.dat')
    for line in fh:
        match = re.search('games', line)
        if match:
            print(line.replace(match.group(), 'games'), end='')


def main():

    domain()
    protocol()
    terms()


if __name__ == "__main__":
    main()
