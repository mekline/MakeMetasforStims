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
    #print(itemNo)
    primaryVerbDescription = line[2]
    #inside the row, column 13 gives whatever is labeled there
    #assuming this is the base/object change/ unintentional stuff
    primarySentenceDescription = line[12]
    secondarySentenceDescription = line[13]
    verboseDescription = ['TO ADD', 'Multiple items']
    agent = line[5]
    patient = line [7]

    try:
        movielength = float(line[12])
        #is there a movie lenght?? its not on line 12 tho
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined...
    filePrefix = line[3] + line[14] 
    # Audio items are easy (though check KnockOver, it's named wrong...)
    # sentConditions = ["Transitive","Periphrastic","NonCausal","BadPassive","Passive"]
    # for i in range(5):
    #     audio_item = {
    #         'Filename': sentConditions[i] + '_' + filePrefix + '.yml',
    #         'ItemNo': itemNo,
    #         'ItemCondition': sentConditions[i],
    #         'Length': 'not specified',
    #         'Verb': primaryVerbDescription,
    #         'Sentence': line[15 + i],
    #         'NParticipants':2,
    #         'Participants': [{'ID':'addUniqueID','Role':'Agent','isAnimate':1},{'ID':'addUniqueID','Role':'Patient','isAnimate':0}]

    #             }
    #     audio_items.append(audio_item)

    #Movie items are a bit harder because different items have different sets of conditions available
    #What conditions do we have? Get the Stimset and ChangeAvailable vars so we 
    #can populate the list of conditions + filenames 

    Stimset = line[0]
    hasConditions = line[1]

    if Stimset == 'Original': #Only noInstrument versions
        if hasConditions == "MannerResult":
            MovieConditions = ["Base","MannerChange","ResultChange"]
            InstConditions = ["NoInstrument"]

        elif hasConditions == "Unintentional":
            MovieConditions = ["Base","Unintentional"]
            InstConditions = ["NoInstrument"]
        else: #None
            MovieConditions = ["Base"]
            InstConditions = ["NoInstrument"]
    else: #All changes, and both instrument and noinstrument exist!!
            MovieConditions = ["Base","BackgroundChange",
            "BigAgentChange","SmallAgentChange","MannerChange","ResultChange","ObjectChange","InstrumentChange"]
            InstConditions = ["NoInstrument", "Instrument"]

    #Now build each of those condition combos out into movie items!

    for m in xrange(len(MovieConditions)):
        for i in xrange(len(InstConditions)):
            mc = MovieConditions[m]
            inst = InstConditions[i]
            movie_item = {}
            movie_item = {
                'ItemNo': itemNo,
                #'Agent':agent
                #got super sassy with syntax when I added agent and patient
                #adding agent to yaml
                #'Patient':patient
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

            #Gosh the filenaming conventions were inconsistent
            fi = ''
            if hasConditions == 'MannerResult':
                if mc == 'Base':
                    fi = filePrefix + '_' + line[4] +'.yml'                    
                elif mc == 'MannerChange':
                    fi = filePrefix + '_' + line[9]+'.yml'
                elif mc == 'ResultChange':
                    fi = filePrefix + '_' + line[10]+'.yml'
            elif hasConditions == 'Unintentional':
                if mc == 'Base':
                    fi = filePrefix + '_' + line[4]+'.yml'
                elif mc == 'Unintentional':
                    fi = filePrefix + '_' + line[5]+'.yml'
            elif hasConditions == 'None':
                fi = filePrefix + '_' + line[4]+'.yml'
            elif hasConditions == 'All':
                fi = filePrefix + '_' + mc + '_' + inst + '.yml'

            #Funny exception: There is no such thing as NoInstrument + InstrumentChange
            if not((inst == "NoInstrument") & (mc == "InstrumentChange")):
                #print(fi)
                movie_item.update({'Filename': fi})
                movie_items.append(movie_item)

#end of function definition


try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)

mkdir(CBMovies yamls Claire)
    # #Read out audio files
    # for ai in audio_items:
    #     out_file = open('CBAudio yamls/' + ai['Filename'], "w")
    #     out_file.write( yaml.dump(ai, default_flow_style=False, allow_unicode=True) )
    #     out_file.close()

    #Read out movie files
    for mi in movie_items:
        out_file = open('CBMovies yamls Claire/' + mi['Filename'], "w")
        out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
        out_file.close()


    #NOTE: Audio: Manually remove these ones because the audio files aren't available!
    # Passive_TurnOff
    # Passive_Start
    # Passive_SlideChair
    # Passive_KnockOver
    # BadPassive_TurnOff
    # BadPassive_Start
    # BadPassive_SlideChair
    # BadPassive_KnockOver

    #Note: video. Following videos don't seem to actually exist:
    #ChangeChannel, TightenScrew, TurnOnFan  Instrument versions
    #All Original set videos have the 4th Manner x Result combo!
    #Scary missing videos: SlideChair_Base_Noinstrument


finally:
    in_file.close()
 
