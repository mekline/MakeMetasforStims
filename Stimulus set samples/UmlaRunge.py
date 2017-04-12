import csv
import yaml
in_file = open('UmlaRunge.csv', "rU")
movie_items = []

def convert_to_yaml(line,counter):
	itemNo = int(line[0])
	#make groupNo a condition
	groupNo = int(line[1])
	yamlfilename = line[2].split('.')[0] + '.yaml'
	movieFilename = line[2]
	Agent = line[3]
	Patient = line[4]
	Instrument = line[5]
	Theme = line[6]
	Source = line[7]
	Goal = line[8]
	sentenceDescription = [line[9], line[10], line[11], line[12], line[13]]
	#versionletter and versionlabel are conditions
	versionletter = line[14]
	versionlabel = line[15]
	
	print(yamlfilename)

	movie_item = {
		'ItemNo': itemNo,
		#'GroupNo': groupNo,
		'movieFilename': movieFilename,
		'SentenceDescription': sentenceDescription,
		'yamlFilename': yamlfilename#,
		#'VersionLabel': versionlabel
	}

	conditionlist = []
	possibleconditions = [versionletter, versionlabel, groupNo]
	conditionlabel = ['Version', 'Movie Set', 'Group Number']
	for i in xrange(0, len(possibleconditions)):
		if possibleconditions[i] != '':
			newcondition = {conditionlabel[i]: possibleconditions[i]}
			conditionlist.append(newcondition)

	movie_item.update({'conditionlist': conditionlist})

	#versionletterAB = versionletter
	#if versionletterAB != '':
	#	movie_item.update({'VersionLetter': versionletterAB})

	participantlist = []
	possibleroles = [Agent, Patient, Instrument, Theme, Source, Goal]
	rolenames = ['Agent', 'Patient', 'Instrument', 'Theme', 'Source', 'Goal']

	for i in xrange(0, len(possibleroles)):
		if possibleroles[i] != '':
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