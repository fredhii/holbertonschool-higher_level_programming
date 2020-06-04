#!/usr/bin/python3
""" Read from standard input and prints statistics """

if __name__ == "__main__":
    import sys


    def print_stats(file_size, dict):
        """ Print statistics """
        print("File size: {}".format(file_size))
        for key in dict:
            if dict[key] != 0:
                print("{}: {}".format(key, dict[key]))


    """ ============================================= """
    """ Variables """
    """ ============================================= """
    file_size = 0
    count = 0
    dict = {'200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0}


    """ ============================================= """
    """ Read from line """
    """ ============================================= """
    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(file_size, dict)
                count = 1
            else:
                count += 1

            split_line = line.split()
            file_size += int(split_line[-1])

            if split_line[-2] in dict:
                dict[split_line[-2]] += 1
        print_stats(file_size, dict)
    except KeyboardInterrupt:
        print_stats(file_size, dict)
        raise
