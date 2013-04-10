'prepare a training file from train.csv and train_answers.csv'

import sys, csv

output_file = sys.argv[1]

input_file = 'data/orig/train.csv'
answers_file = 'data/orig/train_answers.csv'

# mapping author -> gender

writers = {}
reader = csv.reader( open( answers_file ))
headers = reader.next()

for line in reader:
	writer_id, gender = line
	writers[writer_id] = gender
	
###

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ))

# prep headers
headers = reader.next()
headers = headers[2:]
headers.insert( 0, 'gender' )
writer.writerow( headers )

for line in reader:
	
	if line[2] == 'Arabic':
		line[2] = 0
	else:
		line[2] = 1
		
	writer_id = line[0]
	gender = writers[writer_id]

	line = line[2:]
	line.insert( 0, gender )
	
	writer.writerow( line )
	
	