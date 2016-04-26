import csv
import yaml

#This is gonna be a routine that turns rows of the complicatedly formatted CBMovies.csv into
#a set of metadata files (one per movie that actually exists, with the same name)

in_file  = open('EventsMP.csv', "rU")
items = []

def convert_to_yaml(line, counter):
    itemNo = counter
    primaryVerbDescription = line[1]
    primarySentenceDescription = 'To add - a single sentence.'
    verboseDescription = ['TO ADD', 'Multiple items']

    movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined...
    fileName = line[0].split('.')[0]
    itemSet = line[4]


    item = {}
    item = {
        'Filename': fileName + '.yml',
        'ItemNo': itemNo,
        'ItemCondition': [itemSet, line[1], line[2]],
        'Length':movielength,
        'Size': 'TO ADD',
        'Color':'full color',
        'PrimaryVerbDescription':primaryVerbDescription,
        'PrimarySentenceDescription':primarySentenceDescription,
        'VerboseDescription': verboseDescription,
        'NParticipants': 2,
        'Participants': [{'ID':line[3],'Role':'Agent','isAnimate':1}]

    }


    items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)


    #Read out movie files
    for mi in items:
        out_file = open('EventsMP yamls/' + mi['Filename'], "w")
        out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
        out_file.close()


finally:
    in_file.close()
 
