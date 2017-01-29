from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study drill! Trying out raw_input w/ argv
fourth = raw_input("What should the fourth variable be? ")
print "The fourth variable is %r " % fourth