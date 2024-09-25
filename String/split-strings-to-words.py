# Parse String into Words

def parse_string(line):
    words = line.split()
    array = []
    for word in words:
        # array.append(word.strip('\n\r\t'))
        array.append(word)

    for element in array:
        print(element)


# --------------------------------------------------------#
a = 'String Parsing Transformation'
print('String: {}'.format(a))
print("-" * 50)

my_str = '''\
Kevin
Thomas
Luzbetak
'''

parse_string(my_str)
print(type(my_str))

print("-" * 50)
parse_string("kevin thomas luzbetak")
