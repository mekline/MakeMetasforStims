import csv
import yaml
in_file = open('MPP.csv', "rU")
movie_items = []

def convert_to_yaml(line,counter):
	fileNo = int(line[0])
	fileName = line[1]
	yamlfilelist = fileName.split('.')[:-1]
	yamlfilename = '.'.join(yamlfilelist) + '.yaml'
	Means = line[2]
	Outcome = line[3]
	Novelverb = line[4]
	Domain = line[5]
	Agent = line[6]
	Patient = line[7]
	Instrument = line[8]
	GroundObject = line[9]
	SentenceDescription = [line[10], line[11], line[12], line[13], line[14]]

	#print(fileNo)

	movie_item = {
		'FileNo': fileNo,
		'moviefilename': fileName,
		'SentenceDescription': SentenceDescription,
		'yamlFilename': yamlfilename,
	}

	participantlist = []
	possibleroles = [Agent, Patient, Instrument, GroundObject]
	rolenames = ['Agent', 'Patient', 'Instrument', 'GroundObject']
	for i in xrange(0, len(possibleroles)):
		if possibleroles[i] != '':
			newrole = {rolenames[i]: possibleroles[i]}
			participantlist.append(newrole)

	movie_item.update({'participantlist': participantlist})

	conditionlist = []
	possibleconditions = [Means, Outcome, Novelverb, Domain]
	conditionlabel = ['Means', 'Outcome', 'Novelverb', 'Domain']
	for i in xrange(0,len(possibleconditions)):
		if possibleroles[i] != '':
			newcondition = {conditionlabel[i]: possibleconditions[i]}
			conditionlist.append(newcondition)
	movie_item.update({'conditionlist': conditionlist})

	movie_items.append(movie_item)

try:
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line, counter)

	for mi in movie_items:
		if(mi['yamlFilename']):
			out_file = open('MPP samples/' + mi['yamlFilename'], "w")
			out_file.write(yaml.dump(mi, default_flow_style=False, allow_unicode=True) )

finally:
	in_file.close()