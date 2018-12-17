#! /usr/bin/env python3
def main():
    frequency = 0

    f = open('input.txt', 'r')
    for line in f:
        frequency += (int(line.strip('\n')))

    print(frequency)


if __name__ == '__main__':
    main()
