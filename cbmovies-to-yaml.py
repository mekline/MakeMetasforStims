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
    primarySentenceDescription = line[13]
    secondarySentenceDescription = line[14]
    thirdSentenceDescription = line[15]
    fourthSentenceDescription = line[16]
    fifthSentenceDescription = line[17]
    verboseDescription = [line[13], line[14], line[15], line[16], line[17]]
    
    agent = line[6]
    patient = line[8]
    instrument = line[7]
    yamlfilename = line[5].split('.')[0] + '.yaml'
    #make consistant
    filename = line[5]
    #add regular filename
    changecondition = line[2]
    instrumentcondition = line[3]
    

    print(filename)

    try:
        movielength = float(line[12])
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined right now...
   

    movie_item = {}
    movie_item = {
        'ItemNo':itemNo,
        'ItemCondition': [changecondition, instrumentcondition],
        'Length':movielength,
        #'Size': 'TO ADD',
        'Color':'full color',
        'PrimaryVerbDescription':primaryVerbDescription,
        'PrimarySentenceDescription':primarySentenceDescription,
        'SecondarySentenceDescription':secondarySentenceDescription,
        'ThirdSentenceDescription':thirdSentenceDescription,
        'FourthSentenceDescription':fourthSentenceDescription,
        'FifthSentenceDescription':fifthSentenceDescription,
        'VerboseDescription': verboseDescription
    }

    if instrumentcondition == 'Instrument':
        movie_item['NParticipants'] = 3
        movie_item['Participants'] = [{'ID':agent,'Role':'Agent','isAnimate':1},
        {'ID':patient,'Role':'Patient','isAnimate':0},
        {'ID':instrument,'Role':'Instrument','isAnimate':0}]

    else:
        movie_item['NParticipants'] = 2
        movie_item['Participants'] = [{'ID':agent,'Role':'Agent','isAnimate':1},
        {'ID':patient,'Role':'Patient','isAnimate':0}]


    movie_item.update({'Filename': yamlfilename})
    #changed to yamlfilename
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
 
