import csv
import yaml
in_file = open('Curtains.csv', "rU")
movie_items = []

def convert_to_yaml(line,counter):
	fileNo = int(line[0])
	filename = line[1]
	yamlfilename = line[1].split('.')[0] + '.yaml'
	patient = line[2]
	instrument = line[3]
	verb = line[4]
	sentenceDescription = [line[5], line[6], line[7], line[8], line[9]]

	movie_item = {}
	movie_item = {
	'FileNo': fileNo,
	'MovieFilename': filename,
	'verbDescription': verb,
	'yamlFilename': yamlfilename,
	'SentenceDescription': sentenceDescription
	}

	participantlist = []
	possibleroles = [patient, instrument]
	rolenames = ['Patient', 'Instrument']
	for i in xrange(0, len(possibleroles)):
		if possibleroles[i] != '':
			newrole = {'Role': rolenames[i], 'ID': possibleroles[i]}
			participantlist.append(newrole)

	movie_item.update({'participantlist': participantlist})

	movie_items.append(movie_item)

try: 
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line, counter)

	for mi in movie_items:
		if(mi['yamlFilename']):
			out_file = open('Curtains_stimuli_Ambridge/' + mi['yamlFilename'], "w")
			out_file.write(yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
			out_file.close()	

finally:
	in_file.close()