#! /usr/bin/env python3
def main():
    f = open('input.txt', 'r')
    lines = list(f)

    i = 0
    while i < len(lines) - 2:
        for test in lines[i + 1:]:
            j = 0
            mm_count = 0
            while j < len(test):
                if lines[i][j] != test[j]:
                    mm_count += 1
                    if mm_count > 1:
                        break
                j += 1

            if mm_count == 1:
                for x in range(len(lines[i])):
                    if lines[i][x] != test[x]:
                        print(lines[i][:x] + lines[i][x + 1:])

        i += 1


if __name__ == '__main__':
    main()
