import csv
import yaml

# This is gonna be a routine that turns rows of the complicatedly formatted
# CBMovies.csv into a set of metadata files (one per movie that actually
# exists, with the same name)

in_file  = open('CBMovies_longform.csv', "rU")
movie_items = []
audio_items = []

def convert_to_yaml(line, counter):
    itemNo = int(line[1])
    primaryVerbDescription = line[2]
    #inside the row, column 13 gives whatever is labeled there
    #assuming this is the base/object change/ unintentional stuff
    primarySentenceDescription = line[12]
    secondarySentenceDescription = line[13]
    verboseDescription = ['TO ADD', 'Multiple items']
    agent = line[5]
    patient = line[7]
    filename = line[4].split('.')[0] + '.yaml'
    mc ='placeholder'
    inst = 'placeholder'

    print(filename)

    try:
        movielength = float(line[12])
        #is there a movie lenght?? its not on line 12 tho
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined right now...
   

    movie_item = {}
    movie_item = {
        'ItemNo':itemNo,
        'Agent':agent,
        #got super sassy with syntax when I added agent and patient
        #adding agent to yaml
        'Patient':patient,
        #adding patient to yaml
        #woah why is patient invalid? line 83
        'ItemCondition': [mc, inst],
        'Length':movielength,
        'Size': 'TO ADD',
        'Color':'full color',
        'PrimaryVerbDescription':primaryVerbDescription,
        'PrimarySentenceDescription':primarySentenceDescription,
        'VerboseDescription': verboseDescription
    }

    if inst == 'Instrument':
        movie_item['NParticipants'] = 3
        movie_item['Participants'] = [{'ID':'addUniqueID','Role':'Agent','isAnimate':1},
        {'ID':'addUniqueID','Role':'Patient','isAnimate':0},
        {'ID':'addUniqueID','Role':'Instrument','isAnimate':0}]

    else:
        movie_item['NParticipants'] = 2
        movie_item['Participants'] = [{'ID':'addUniqueID','Role':'Agent','isAnimate':1},
        {'ID':'addUniqueID','Role':'Patient','isAnimate':0}]


    movie_item.update({'Filename': filename})
    movie_items.append(movie_item)

#end of function definition


try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)

#mkdir(CBMovies yamls Claire)
#this doesn't work because it is not a python code


    #Read out movie files
    for mi in movie_items:
        if(mi['Filename']):
            out_file = open('CBMovies yamls Claire/' + mi['Filename'], "w")
            out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
            out_file.close()



finally:
    in_file.close()
 
