import csv
import yaml
in_file = open('Fausey.csv', "rU")
movie_items = []

def convert_to_yaml(line,counter):
	fileNo = int(line[0])
	Itemcond = line[1]
	ChangeCond = line[2]
	VerbDescription = line[3]
	fileName = line[4]
	yamlFilename = line[4].split('.')[0] + '.yaml'
	Agent = line[5]
	Instrument = line[6]
	Patient = line[7]
	SentenceDescription = [line[8], line[9], line[10], line[11], line[12]]

	movie_item = {}
	movie_item = {
	'FileNo': fileNo,
#Is the verb a condition too?
	'VerbDescription': VerbDescription,
	'yamlFilename': yamlFilename,
	'SentenceDescription': SentenceDescription
	}

	participantlist = []
	possibleparticipants = [Agent, Instrument, Patient]
	possibleroles = ['Agent', 'Instrument', 'Patient']

	for i in xrange(0, len(possibleparticipants)):
		if possibleparticipants != '':
			newrole = {'Role': possibleroles[i], 'ID': possibleparticipants[i]}
			participantlist.append(newrole)

	movie_item.update({'participantlist': participantlist})

	movieconditions = []
	possibleconditions = [Itemcond, ChangeCond]
	conditiontype = ['Item Condition', 'Change Condition']

	for i in xrange(0, len(possibleconditions)):
		conditionset = {conditiontype[i]: possibleconditions[i]}

		movieconditions.append(conditionset)

	movie_item.update({'movieconditions': movieconditions})

	movie_items.append(movie_item)

try: 
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line, counter)

	for mi in movie_items:
		if(mi['yamlFilename']):
			out_file = open('Fausey_ExampleVideos/' + mi['yamlFilename'], "w")
			out_file.write(yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
			out_file.close()

finally:
	in_file.close()


