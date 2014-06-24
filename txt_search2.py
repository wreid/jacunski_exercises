import sys, gzip, csv
from sys import argv
from os.path import exists

def check_files(f1, f2):
	"""checks if the input and output files exist"""
	global open_type
	if exists(f1):
		print 'Input file exists'
	else:
		print 'Invalid input file'
		sys.exit()

	if exists(f2):
		print 'Output file exists. Overwrite (o), append (a), or quit (q)?'
		a = str(raw_input('> '))
		if a[0] == 'o' or a[0] == 'O':
			open_type = 'wb'
			return True
		elif a[0] == 'a' or a[0] == 'A':
			open_type = 'ab'
			return True	
		elif a[0] == 'q' or a[0] == 'Q':
			print 'Quitting program.'
			sys.exit()
		else:
			print 'Invalid input. Quitting program.'
			sys.exit()	
	else:
		open_type = 'wb'
		print 'Writing output file.'
		return True

def csv_loop(inp, out, delimiter, l, numbers):
	"""uses csv to read file and print appropriate lines"""
	rd = csv.reader(inp, delimiter=delimiter)
	wr = csv.writer(out, delimiter=delimiter)
	# loops through list of fields in the row, writes the [x] field
	for z in l:
		print z.upper()
		for row in rd:
			if any(z in s for s in row):
				# print 'true'
				wr.writerow([row[y] for y in numbers])
		# resets the csv reader to the top of the file to search for 
		# the next item in z
		inp.seek(0)

def main(argv):

	input_name, output_name, terms_file, header_length = argv[1:5]
	
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

	with open(terms_file, 'rb') as list_file:
		txt = list_file.read()
		terms = txt.splitlines()

	if check_files(input_name, output_name):
		with open(output_name, open_type) as output: 
			# checks if the file is compressed
			if input_name[-3:] == '.gz':
				with gzip.open(input_name, 'rb') as f:
					csv_loop(f, output, '\t', terms, x)

			else:
				with open(input_name, 'rb') as f:
					csv_loop(f, output, '\t', terms, x)
		print 'Completed.'

	else:
		print 'Failed.'
		sys.exit()

if __name__ == '__main__':
	main(sys.argv)