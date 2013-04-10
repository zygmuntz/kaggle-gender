'''
split a file into a given number of chunks randomly, by authors. 
Usage: chunk_by_authors.py <orig train file> <input file> <number of chunks>
input files with headers
no headers in output files
'''

import sys, random, os, csv

orig_train_file = sys.argv[1]
input_file = sys.argv[2]
num_chunks = int( sys.argv[3] )

try:
	seed = sys.argv[4]
except IndexError:
	seed = None
if seed:
	random.seed( seed )

basename = os.path.basename( input_file )
basename, ext = os.path.splitext( basename )

i_orig = open( orig_train_file )
orig_reader = csv.reader( i_orig )
i = open( input_file )

headers = orig_reader.next()
i.next()

os = {}
for n in range( num_chunks ):
	output_file = "%s_%s%s" % ( basename, n, ext )
	os[n] = open( output_file, 'wb' )
	# os[n].write( headers )

counter = 0
current_writer = None


for line in i:

	orig_line = orig_reader.next()
	writer = orig_line[0]
	
	if writer != current_writer:
		current_writer = writer
		n = random.randint( 0, num_chunks - 1 )

	os[n].write( line )
	
	counter += 1
	if counter % 100000 == 0:
		print counter
	

		
		
		
		
		
		
		