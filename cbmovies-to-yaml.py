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
    primaryVerbDescription = line[4]
    primarySentenceDescription = line[12]
    secondarySentenceDescription = line[13]
    thirdSentenceDescription = line[14]
    fourthSentenceDescription = line[15]
    fifthSentenceDescription = line[16]
    verboseDescription = ['TO ADD', 'Multiple items']
    agent = line[5]
    patient = line[7]
    filename = line[4].split('.')[0] + '.yaml'
    mc = line[2]
    inst = line[7]

    print(filename)

    try:
        movielength = float(line[12])
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined right now...
   

    movie_item = {}
    movie_item = {
        'ItemNo':itemNo,
        'Agent':agent,
        'Patient':patient,
        'ItemCondition': [mc, inst],
        'Length':movielength,
        'Size': 'TO ADD',
        'Color':'full color',
        'PrimaryVerbDescription':primaryVerbDescription,
        'PrimarySentenceDescription':primarySentenceDescription,
        'SecondarySentenceDescription':secondarySentenceDescription,
        'ThirdSentenceDescription':thirdSentenceDescription,
        'FourthSentenceDescription':fourthSentenceDescription,
        'FifthSentenceDescription':fifthSentenceDescription,
        'VerboseDescription': verboseDescription
    }

    if inst == 'Instrument':
        movie_item['NParticipants'] = 3
        movie_item['Participants'] = [{'ID':'addUniqueID','Role':'Agent','Agent':agent,'isAnimate':1},
        {'ID':'addUniqueID','Role':'Patient','Patient':patient,'isAnimate':0},
        {'ID':'addUniqueID','Role':'Instrument','isAnimate':0,'Instrument':inst}]

    else:
        movie_item['NParticipants'] = 2
        movie_item['Participants'] = [{'ID':'addUniqueID','Role':'Agent','isAnimate':1,'Agent':agent},
        {'ID':'addUniqueID','Role':'Patient','isAnimate':0,'Patient':patient}]


    movie_item.update({'Filename': filename})
    movie_items.append(movie_item)

#end of function definition


try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)



    #Read out movie files
    for mi in movie_items:
        if(mi['Filename']):
            out_file = open('CBMovies yamls Claire/' + mi['Filename'], "w")
            out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
            out_file.close()



finally:
    in_file.close()
 
