# Python script to extract a field from a text file

# Import arguments and gzip library for compressed files.
from sys import argv
import sys
import gzip


# The 'header_length' argument is how long the header is, e.g., BioGrid files 
# have a header of 1, so using '1' for this argument would output a file
# without the first row. 

#Script arguments are as follows:

script, input_name, output_name, column_number, header_length = argv

# Arguments are converted to ints for use in range() and fields[] below.
try:
	x = int(column_number)
except TypeError:
	print 'Column number must be an integer'
	sys.exit()

try:	
	h = int(header_length)
except TypeError:
	print 'Header length must be an integer'
	sys.exit()


with open(output_name, 'w') as output_file:
	# Checks whether the file is compressed or not.
	with gzip.open(input_name, 'rb') as input_file:
		# Assigns text of the file to the 'txt' var.
		for r in input_file:
			row = r.split()
			output_file.write('%s\n' % row[x])
