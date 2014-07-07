import sys
import gzip
import csv
import codecs
from sys import argv
from os.path import exists

input_name, output_name, column_number, header_length = argv[1:]

def check_files(f1, f2):
	"""checks if the input and output files exist"""
	if exists(f1):
		print 'Input file exists'
	else:
		print 'Invalid input file file'
		sys.exit()

	if exists(f2):
		print 'Output file exists. Overwrite the file?'
		a = str(raw_input('> '))
		if a[0] == 'y' or a[0] == 'Y':
			return True
		else:
			print 'Quitting program.'
			sys.exit()	
	else:
		print 'Writing output file.'
		return True

# sanitizes inputs
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
	with open(output_name, 'wb') as output: 
		# checks if the file is compressed
		if input_name[-3:] == '.gz':
			with gzip.open(input_name, 'rb') as f:
				rd = csv.reader(f)
				wr = csv.writer(output)
				# loops through list of fields in the row, writes the [x] field
				i = 0
				for columns in rd:
					if i < h:
						i += 1
					else:
						wr.writerow([columns[x]])

		else:
			with open(input_name, 'rb') as f:
				rd = csv.reader(f)
				wr = csv.writer(output)
				i = 0
				for columns in rd:
					if i < h:
						i += 1
					else:	
						wr.writerow([columns[x]])
	print 'Completed.'
else:
	print 'Failed.'
	sys.exit()