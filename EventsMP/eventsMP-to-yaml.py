import csv
import yaml

#This is gonna be a routine that turns rows of the complicatedly formatted CBMovies.csv into
#a set of metadata files (one per movie that actually exists, with the same name)

in_file  = open('EventsMP.csv', "rU")
items = []

#complete dictionary
def convert_to_yaml(line, counter):
    itemNo = counter
    intendedVerbDescription = [line[1]]
    intendedSentenceDescription = 'To add - a single sentence.'
    elicitedSentenceDescription = [line[5], line[6], line[7], line[8]]
    agent = line[3] 
    #pathdescription = line[2]
    yamlfilename = line[0].split('.')[0] + '.yaml'
    moviefilename = line[0]
    itemSet = line[4]
    movielength = 'lengthinseconds'
    size = [0,0] #The sizes for the movies are undefined...

    print(yamlfilename)

#print out into yaml
    item = {}
    item = {
        'ItemNo': itemNo,
        'ItemCondition': [itemSet, line[1], line[2]],
        'Length':movielength,
        'Size': 'TO ADD',
        'Color':'full color',
        'YamlFilename': yamlfilename,
        'MovieFilename': moviefilename,
        'ElicitedSentenceDescription':elicitedSentenceDescription,
        'IntendedSentenceDescription':intendedSentenceDescription,
        'IntendedVerbDescription':intendedVerbDescription,

        #sorting statements
        'NParticipants': 1,
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
        out_file = open('EventsMP yamls/' + mi['YamlFilename'], "w")
        out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
        out_file.close()


finally:
    in_file.close()
 
