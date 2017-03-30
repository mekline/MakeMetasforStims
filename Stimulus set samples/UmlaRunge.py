import csv
import yaml
in_file = open('UmlaRunge.csv', "rU")
movie_items = []

def convert_to_yaml(line,counter):
	itemNo = int(line[1])
	yamlfilename = line[2].split('.')[0] + '.yaml'
	movieFilename = line[2]
	Agent = line[3]
	Patient = line[4]
	Instrument = line[5]
	Theme = line[6]
	Source = line[7]
	Goal = line[8]
	sentenceDescription = [line[9], line[10], line[11], line[12], line[13]]
	
	print(yamlfilename)

	movie_item = {
		'ItemNo': itemNo,
		'movieFilename': movieFilename,
		'SentenceDescription': sentenceDescription,
		'yamlFilename': yamlfilename
	}

	participantlist = []
	possibleroles = [Agent, Patient, Instrument, Theme, Source, Goal]
	rolenames = ['Agent', 'Patient', 'Instrument', 'Theme', 'Source', 'Goal']

	for i in xrange(0, len(possibleroles)):
		if possibleroles[i] != ['']:
			newrole = {'ID': possibleroles[i], 'Role': rolenames[i]}
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
			out_file = open('UmlaRunge/' + mi['yamlFilename'], "w")
			out_file.write(yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
			out_file.close()

finally:
	in_file.close()