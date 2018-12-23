from sys import argv

# unpack argv  (taking script itself, and 3 other arguments while running python)
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third