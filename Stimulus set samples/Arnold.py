import csv
import yaml
in_file = open('Arnold.csv', "rU")
picture_items = []


def convert_to_yaml(line,counter):
	#definitions
	fileNo = int(line[0])
	verbDescription = [line[5]]
	sentenceDescription = [line[15], line[16], line[17],line[18], line[19]]
	yamlfilename = line[6].split('.')[0] + '.yaml'
	picturefilename = line[6]
	agent = line[7]
	jointagent1 = line[8]
	jointagent2 = line[9]
	instrument = line[10]
	patient = line[11]
	theme = line[12]
	source = line[13]
	goal = line[14]
	StimType = line[2]
	GenderCond = line[3]
	CharGenderCond = line[4]
	ItemCond = line[1]

	#print(yamlfilename)

	picture_item = {}
	picture_item = {
		#dictionary
		'FileNo': fileNo,
		'PictureFilename': picturefilename,
		'verbDescription': verbDescription,
		'yamlFilename': yamlfilename,
		'SentenceDescription': sentenceDescription
	}

#condition loop
	pictureconditions = []
	possibleconditions = [StimType, GenderCond, CharGenderCond, ItemCond]
	conditiontype = ['StimType', 'Gender Condition', 
	'Char Gender Condition', 'Item Number']

	for i in xrange(0, len(possibleconditions)):
		conditionset = {conditiontype[i]: possibleconditions[i]}
		#else possibleconditions[i] == ['']:
			#conditionset = 'No Conditions'

		pictureconditions.append(conditionset)

	picture_item.update({'pictureconditions': pictureconditions})

#participant loop

	#if there is something in a cell, make a participant list
	#if there is nothing, don't do anything

	participantlist = []
	#more definitions of possibleroles and rolenames
	possibleroles = [agent, jointagent1, jointagent2, instrument, patient, theme, 
	source, goal]
	rolenames = ['Agent', 'Joint Agent', 'Joint Agent', 'Instrument',
	'Patient', 'Theme', 'Source', 'Goal']

	#if the role is not blank, carry on and make a list
	for i in xrange(0, len(possibleroles)): 
		#print(possibleroles[i])
		if possibleroles[i] != '':
			#print i
			newrole = {'Role': rolenames[i], 'ID': possibleroles[i]}
			#newrole is new dictionary
			participantlist.append(newrole)
	#print participantlist

#add the participants list to the yaml file ie picture_item list
	picture_item.update({'participantlist': participantlist})

	#print picture_item
	
	picture_items.append(picture_item)
	

try: 
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line, counter)

	for pi in picture_items:
		if(pi['yamlFilename']):
			out_file = open('Arnold_stimuli/' + pi['yamlFilename'], "w")
			out_file.write(yaml.dump(pi, default_flow_style=False, allow_unicode=True) )
			out_file.close()

finally:
	in_file.close()










	# if agent == 'The maid'
	# 	picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
	# 	{'ID':patient,'Role':'Patient'}]
	# if agent == 'The chef'
	# 	picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
	# 	{'ID':patient,'Role':'Patient'}]
	# if agent == 'The butler'
	# 	picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
	# 	{'ID':patient,'Role':'Patient'}]
	# 	picture_item['Instrument'] = ['Instrument':instrument]
	# if jointagent1 == 'The maid'
	# 	picture_item['Participants'] = [{'ID':jointagent1,'Role':'JointAgent'},
	# 	{'ID':jointagent2,'Role':'JointAgent'},{'ID':patient,'Role':'Patient'}]
	# if jointagent1 == 'The chef'
	# 	picture_item['Participants'] = [{'ID':jointagent1,'Role':'JointAgent'},
	# 	{'ID':jointagent2,'Role':'JointAgent'},{'ID':patient,'Role':'Patient'}]
	# if

	# picture_item['Participants'] = participantlist


