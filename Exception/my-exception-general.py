# Exception handling

def main():
    try:
        fh = open('dummy-file.txt')
    except IOError as e:
        print(e)
    else:
        for line in fh: print(line.strip())


if __name__ == "__main__":
    main()
