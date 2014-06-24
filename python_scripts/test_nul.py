import gzip
if '\0' in gzip.open('biogrid_human.txt.gz'):
	print 'you have null bytes'
else:
	print 'you dont'