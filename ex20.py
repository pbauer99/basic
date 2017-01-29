from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),       # Added "," to stop empty lines btw
                                          # "current_line"s seen below
current_file = open(input_file)

print "First, let's print the whole file: \n"

print_all(current_file)

print "Now, let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: \n"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1           # Can be reduced, x = x + y -> x += y
print_a_line(current_line, current_file)

current_line += 1                         # See above, same line, new form
print_a_line(current_line, current_file)