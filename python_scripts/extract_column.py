# Python script to extract a field from a text file

# Import arguments and gzip library for compressed files.
import sys
import gzip
from os.path  import exists
from sys import argv

# The 'header_length' argument is how long the header is, e.g., BioGrid files 
# have a header of 1, so using '1' for this argument would output a file
# without the first row. 

#Script arguments are as follows:

input_name, output_name, column_number, header_length = argv[1:]

# Checks that the files exist

def check_files(f1, f2):
	if exists(f1):
		print 'Input file exists'
	else:
		print 'Invalid input file file'
		return False

	if exists(f2):
		print 'Output file exists. Are you sure you want to overwrite the file?'
		a = str(raw_input('> '))
		if a[0] == 'y' or a[0] == 'Y':
			return True
		else:
			print 'Quitting program.'
			return False
	else:
		print 'New output file created.'
		return True

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

if check_files(input_name, output_name):
	with open(output_name, 'wb') as output_file:
		# Checks whether the file is compressed or not.
		if input_name[-2:] == 'gz':
		# If the file is compressed, uses gzip.open() to open the file.
			with gzip.open(input_name, 'rb') as input_file:
				# Runs over an initial for loop to skip over the file header
				i = 0
				for row in input_file:
					if i < h:
						i += 1
				# Splits the row string into the individual words in fields[]
					else:	
						fields = row.split('\t')
						output_file.write('%s\n' % fields[x])	
		else:
		# If the file isn't compressed, uses open() from Pythons standard library.
			with open(input_name, 'rb') as input_file:
				i = 0
				for row in input_file:
					if i < h:
						i += 1
				# Splits the row string into the individual words in fields[]
					else:	
						fields = row.split('\t')
						output_file.write('%s\n' % fields[x])	
	print 'Completed'
else:
	sys.exit()

