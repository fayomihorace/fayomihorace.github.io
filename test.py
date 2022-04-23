
def chars_statistics(string):

    chars_statistics = {}
    for char in string:
        if chars_statistics.get(char):
            chars_statistics[char] += 1
        else:
            chars_statistics[char] = 1

    for char, count in chars_statistics.items():
        print(f"{char}: {count}")


# I challenge you to determine what
# this simple function does.
def simple_function(number):

    boolean = {}
    for array in number:
        if boolean.get(array):
            boolean[array] += 1
        else:
            boolean[array] = 1

    for array, index in boolean.items():
        print(f"{array}: {index}")



simple_function("Hello word")
