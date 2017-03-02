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
		'PictureFilename': picturefilename
		'verbDescription': verbDescription
	}

	if agent == 'The maid'
		picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
		{'ID':patient,'Role':'Patient'}]
	if agent == 'The chef'
		picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
		{'ID':patient,'Role':'Patient'}]
	if agent == 'The butler'
		picture_item['Participants'] = [{'ID':agent,'Role':'Agent'},
		{'ID':patient,'Role':'Patient'}]
		picture_item['Instrument'] = ['Instrument':instrument]
	if jointagent1 == 'The maid'
		picture_item['Participants'] = [{'ID':jointagent1,'Role':'JointAgent'},
		{'ID':jointagent2,'Role':'JointAgent'},{'ID':patient,'Role':'Patient'}]
	if jointagent1 == 'The chef'
		picture_item['Participants'] = [{'ID':jointagent1,'Role':'JointAgent'},
		{'ID':jointagent2,'Role':'JointAgent'},{'ID':patient,'Role':'Patient'}]
	if



