'like split, but take writers from the original file into account'
'input file with headers, output files without headers'

import csv
import sys
import random

orig_train_file = sys.argv[1]
input_file = sys.argv[2]
output_file1 = sys.argv[3]
output_file2 = sys.argv[4]

try:
	P = float( sys.argv[5] )
except IndexError:
	P = 0.9
	
try:
	seed = sys.argv[6]
except IndexError:
	seed = None
	
print "P = %s" % ( P )

if seed:
	random.seed( seed )

i_orig = open( orig_train_file )
i = open( input_file )
o1 = open( output_file1, 'wb' )
o2 = open( output_file2, 'wb' )

orig_reader = csv.reader( i_orig )
reader = csv.reader( i )
writer1 = csv.writer( o1 )
writer2 = csv.writer( o2 )

headers = reader.next()
orig_reader.next()
#writer1.writerow( headers )
#writer2.writerow( headers )

counter = 0
current_writer = None

for line in reader:

	orig_line = orig_reader.next()
	writer = orig_line[0]

	if writer != current_writer:

		current_writer = writer
		r = random.random()
		if r > P:
			w = writer2
		else:
			w = writer1
	
	w.writerow( line )

	counter += 1
	if counter % 100000 == 0:
		print counter
	

		
		
		
		
		
		
		