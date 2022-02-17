def main():
    try:
        for line in readfile('file.dat'):
            print(line.strip())
    except IOError as e:
        print(e)
    except ValueError as e:
        print(e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readline()
    else:
        raise ValueError('Filename must end with .txt')


if __name__ == "__main__":
    main()
