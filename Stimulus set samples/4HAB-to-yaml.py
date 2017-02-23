import csv
import yaml
in_file = open('completion-4HAB.csv', "rU")
def convert_to_yaml(line,counter)
	itemNo = int(line[1])
	verbDescription = [line[2]]
	theme = [line[4]]
	goal = [line[5]]
	sentenceDescription = [line[6], line[7], line[8], line[9], line[10]]
	yamlfilename = line[3].split('.')[0] + '.yaml'
	moviefilename = line[3]
print(yamlfilename)
movieitem = {}
movieitem = {
	'ItemNo': itemNo,
	'MovieFilename': moviefilename,
	'sentenceDescription': sentenceDescription,
	'verbDescription': verbDescription,
	'ThemeGoal': ['Theme': theme, 'Goal': goal],
	'SentenceDescription': sentenceDescription
	}
	#now what?