from sys import argv
# from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()
# Combined from original functions:
# in_file = open(from_file)
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
# raw_input()

out_file = open(to_file).read()
# Combined from original functions:
# out_file = open(to_file)
# out_data = out_file.read()

print "Alright, all done."

# No longer needed:
# out_file.close()
# in_file.close()