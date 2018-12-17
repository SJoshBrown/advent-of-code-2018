#! /usr/bin/env python3
def main():
    frequency = 0
    found_frequencies = set()
    found_frequencies.add(frequency)

    f = open('input.txt', 'r')

    changes = []
    for line in f:
        changes.append(int(line.strip('\n')))

    while True:
        for c in changes:
            frequency += c

            if frequency in found_frequencies:
                print(frequency)
                return

            found_frequencies.add(frequency)


if __name__ == '__main__':
    main()
