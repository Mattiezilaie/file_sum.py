# Author: Mahtab Zilaie
# Date: January 31 2020
# Description: file_sum takes the name of a file and calculates the sum of all numbers
# in the file. Then outputs the sum into a new file name sum.txt.


def file_sum(name):
    """function file_sum takes parameter name as the file name and calculates sum of
    all numbers in file then creates a new file with the name 'sum_file' """

    sum_total = 0                                   # sets new variable
    with open(name, 'r') as num_r:                  # opens file to read
        for line in num_r:                          # goes through every line in file

            try:
                num = float(line)                    # sets num to every line in file as a floating integer
                sum_total += num                     # adds every num in file to the sum_total variable
                with open('sum.txt', 'w') as outfile:
                    outfile.write(str(sum_total) + '\n')  # makes new file named sum.txt and prints of sum_total string

            except FileNotFoundError:
                print("The file was not found")


file_sum("num.txt")     # test
