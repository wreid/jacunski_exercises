import sys, gzip, csv
from sys import argv
from os.path import exists

input_name, output_name, gene, header_length = sys.argv[1:5]

print header_length

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

def csv_loop(inp, out, delimiter):
	"""uses csv to read file and print appropriate lines"""
	rd = csv.reader(inp, delimiter=delimiter)
	wr = csv.writer(out, delimiter=delimiter)
	# loops through list of fields in the row, writes the [x] field
	for rows in rd:
		if gene in rows:
			wr.writerow([rows[y] for y in x])


# sanitizes inputs

x = []
for number in sys.argv[5:]:
	try:
		number = int(number)
		x.append(number)
	except TypeError:
		print 'Column number must be an integer'
		sys.exit()

try:
	h = int(header_length)
except TypeError:
	print 'Header length must be an integer'
	sys.exit()

def main(argv):

	if check_files(input_name, output_name):
		with open(output_name, 'wb') as output: 
			# checks if the file is compressed
			if input_name[-3:] == '.gz':
				with gzip.open(input_name, 'rb') as f:
					csv_loop(f, output, '\t')

			else:
				with open(input_name, 'rb') as f:
					csv_loop(f, output, '\t')
		print 'Completed.'

	else:
		print 'Failed.'
		sys.exit()

if __name__ == '__main__':
	main(sys.argv[1:])