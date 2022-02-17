#!/usr/bin/python3

def main():
    test(1, 2, 3, 101, 102, 103, num1=1000, num2=2000, num3=3000)


def test(one, two, three, *args, **kwards):
    print(one, two, three, end=' ')
    print()
    for n in args: print(n)
    for key in kwards: print(key, kwards[key])


if __name__ == "__main__": main()
