import csv
import yaml
in_file = open('completion-4HAB.csv', "rU")
movie_items = []

#dictionary
def convert_to_yaml(line,counter):
	itemNo = int(line[1])
	verbDescription = [line[2]]
	theme = [line[4]]
	goal = [line[5]]
	sentenceDescription = [line[6], line[7], line[8], line[9], line[10]]
	yamlfilename = line[3].split('.')[0] + '.yaml'
	moviefilename = line[3]

	print(yamlfilename)

#yamlformula
	movie_item = {}
	movie_item = {
		'ItemNo': itemNo,
		'MovieFilename': moviefilename,
		'verbDescription': verbDescription,
		'ThemeGoal': [{'Theme': theme,'Goal': goal}],
		'SentenceDescription': sentenceDescription
	}

	movie_item.update({'yamlFilename': yamlfilename})
	movie_items.append(movie_item)

	

try: 
	reader = csv.reader(in_file)
	next(reader)
	for counter, line in enumerate(reader):
		convert_to_yaml(line, counter)

	for mi in movie_items:
		if(mi['yamlFilename']):
			out_file = open('completion-4HAB/' + mi['yamlFilename'], "w")
			out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
			out_file.close()

finally:
	in_file.close()