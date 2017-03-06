import csv
import yaml
in_file = open('Arnold.csv', "rU")
picture_items = []

#dictionary
def convert_to_yaml(line,counter):
	itemNo = int(line[1])
	verbDescription = [line[5]]
	sentenceDescription = [line[15], line[16], line[17],line[18], line[19]]
	yamlfilename = line[6].split('.')[0] + '.yaml'
	picturefilename = [line[6]]
	agent = [line[7]]
	jointagent1 = [line[8]]
	jointagent2 = [line[9]]
	instrument = [line[10]]
	patient = [line[11]]
	theme = [line[12]]
	source = [line[13]]
	goal = [line[14]]

	print(yamlfilename)

#yamlfilename
	picture_item = {}
	picture_item = {
		'ItemNo': itemNo,
		'PictureFilename': picturefilename,
		'verbDescription': verbDescription
	}
#if there is something in a cell, make a participant list
#if there is nothing, don't do anything
	participantlist = {}
	possibleroles = [agent, jointagent1, jointagent2, instrument, patient, theme, source, goal]
	rolenames = ['Agent', 'Joint Agent', 'Joint Agent', 'Instrument', 'Patient', 'Theme', 'Source']

#if the role is not blank, carry on and make a list
	for i in xrange(possibleroles): 
		if possibleroles[i] != '':
			participantlist.append({'ID':possibleroles[i],'Role': rolenames[i]})

#add the participants list to the yaml file ie picture_item list
	picture_item.append(participantlist)
	picture_items.append(picture_item)
	picture_item.update({'yamlFilename': yamlfilename})

try: 
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line,counter)

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


