#! /usr/bin/env python3
def main():
    two_count = 0
    three_count = 0

    f = open('input.txt', 'r')

    for line in f:
        c_count = [0] * 26
        for c in line:
            if c == '\n':
                break
            c_count[ord(c) - ord('a')] += 1

        found_two = False
        found_three = False

        for count in c_count:
            if not found_two and count == 2:
                found_two = True
                two_count += 1
            if not found_three and count == 3:
                found_three = True
                three_count += 1
        print(two_count * three_count)


if __name__ == '__main__':
    main()
