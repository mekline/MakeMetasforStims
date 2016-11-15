import csv
import yaml

# This is gonna be a routine that turns rows of the complicatedly formatted
# CBMovies.csv into a set of metadata files (one per movie that actually
# exists, with the same name)

in_file  = open('CBMovies_longform.csv', "rU")
movie_items = []
audio_items = []

#Complete dictionary
def convert_to_yaml(line, counter):
    itemNo = int(line[1])
    intendedVerbDescription = [line[4]]
    intendedSentenceDescription = 'not given'
    elicitedSentenceDescription = [line[13], line[14], line[15], line[16], line[17]]
    agent = line[6]
    patient = line[8]
    instrument = line[7]
    yamlfilename = line[5].split('.')[0] + '.yaml'
    moviefilename = line[5]
    changecondition = line[2]
    instrumentcondition = line[3]
    

    print(yamlfilename)

    try:
        movielength = 'lengthinseconds'
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined right now...
   
#print out into yaml
    movie_item = {}
    movie_item = {
        'ItemNo':itemNo,
        'ItemCondition': [changecondition, instrumentcondition],
        'Length':movielength,
        'Size': 'TO ADD',
        'Color':'full color',
        'MovieFilename':moviefilename,
        'ElicitedSentenceDescription': elicitedSentenceDescription,
        'IntendedSentenceDescription':intendedSentenceDescription,
        'IntendedVerbDescription': intendedVerbDescription

    }
#conditional sorting statements
    if instrumentcondition == 'Instrument':
        movie_item['NParticipants'] = 3
        movie_item['Participants'] = [{'ID':agent,'Role':'Agent','isAnimate':1},
        {'ID':patient,'Role':'Patient','isAnimate':0},
        {'ID':instrument,'Role':'Instrument','isAnimate':0}]

    else:
        movie_item['NParticipants'] = 2
        movie_item['Participants'] = [{'ID':agent,'Role':'Agent','isAnimate':1},
        {'ID':patient,'Role':'Patient','isAnimate':0}]


    movie_item.update({'yamlFilename': yamlfilename})
    movie_items.append(movie_item)

#end of function definition


try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)



    #Read out movie files
    for mi in movie_items:
        if(mi['yamlFilename']):
            out_file = open('CBMovies yamls/' + mi['yamlFilename'], "w")
            out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
            out_file.close()



finally:
    in_file.close()
 
