import csv
import yaml

#This is gonna be a routine that turns rows of the complicatedly formatted CBMovies.csv into
#a set of metadata files (one per movie that actually exists, with the same name)

in_file  = open('CBMovies.csv', "rU")
movie_items = []
audio_items = []

def convert_to_yaml(line, counter):
    itemNo = int(line[2])
    primaryVerbDescription = line[13]
    primarySentenceDescription = line[16]
    verboseDescription = 'TO ADD'
    print(line[12])
    try:
        movielength = float(line[12])
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined...
    filePrefix = line[3] + line[14] 

    #Audio items are easy (though check KnockOver, it's named wrong...)
    sentConditions = ["Transitive","Periphrastic","NonCausal","BadPassive","Passive"]
    for i in range(5):
        audio_item = {
            'Filename': sentConditions[i] + '_' + filePrefix + '.yml',
            'ItemNo': itemNo,
            'ItemCondition': sentConditions[i],
            'Length': 'not specified',
            'Verb': primaryVerbDescription,
            'Sentence': line[15 + i],
            'NParticipants':2,
            'Participants': [{'ID':'addUniqueID','Role':'Agent','isAnimate':1},{'ID':'addUniqueID','Role':'Patient','isAnimate':0}]

                }
        audio_items.append(audio_item)


#     #What conditions do we have? Get the Stimset and ChangeAvailable vars so we 
#     #can populate the list of conditions + filenames 

#     Stimset = line[0]
#     hasConditions = line[1]

#     if Stimset == 'Original': #Only noInstrument versions
#         if hasConditions == "MannerResult":
#             MovieConditions = ["Base","MannerChange","ResultChange"]
#             InstConditions = ["NoInstrument"]

#         elif hasConditions == "Unintentional":
#             MovieConditions = ["Base","Unintentional"]
#             InstConditions = ["NoInstrument"]
#         else: #None
#             MovieConditions = ["Base"]
#             InstConditions = ["NoInstrument"]
#     else: #All changes, and both instrument and noinstrument exist!!
#             MovieConditions = ["Base","Unintentional","BackgroundChange",
#             "BigAgentChange","SmallAgentChange","MannerChange","ResultChange","ObjectChange"]
#             InstConditions = ["NoInstrument", "Instrument"]

#     #Now build each of those condition combos out into movie items!

# thisdict = {} #Filename, ItemCondition, NParticipants,{ParticipantIDs}, {ParticipantRoles}, {ParticipantisAnimate}
    
#     {Instrument:Instrument,NoInstrument},{EventVersion:Base,Unintentional,BackgroundChange,BigAgentChange,SmallAgentChange,MannerChange,ResultChange,ObjectChange}


#     itemfactors = line[6].strip('{}').replace(' ','').split('},{')
#     itemversions = {}
#     for f in itemfactors:
#         toadd = f.split(':')
#         if len(toadd)>1:
#             [mykey, mylist] = [toadd[0],toadd[1]]
#             itemversions[mykey] = mylist.split(',')
#     participants = line[10].strip('{}').replace(' ','').split(',')
#     roles = line[11].strip('{}').replace(' ','').split(',')

#     item = {
#         'Name': line[0],
#         'SetTypes': settypes,
#         'Filetype':line[2],
#         'Creator':line[3],
#         'Citation':line[4],
#         'Email': line[5],
#         'ItemConditions': itemversions,
#         'Language': line[7],
#         'Kind': line[8],
#         'Modality': line[9],
#         'Participants':participants,
#         'Roles':roles

#             }
#     items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)

    #Read out audio files
    for ai in audio_items:
        out_file = open('CBAudio yamls/' + ai['Filename'], "w")
        out_file.write( yaml.dump(ai, default_flow_style=False, allow_unicode=True) )
        out_file.close()

    #NOTE: Manually remove these ones because the audio files aren't available!
    # Passive_TurnOff
    # Passive_Start
    # Passive_SlideChair
    # Passive_KnockOver
    # BadPassive_TurnOff
    # BadPassive_Start
    # BadPassive_SlideChair
    # BadPassive_KnockOver


finally:
    in_file.close()
 
