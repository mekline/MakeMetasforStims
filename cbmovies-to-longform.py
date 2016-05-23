import csv
import yaml

#Rewrite that crazy csv I made to be in a reasonable format. 1 line per movie, separately 1 line per audio file. 

in_file  = open('CBMovies.csv', "rU")
movie_lines = []
audio_lines = []

movie_header = ["StimSet",  "StimNo",  "ChangeCondition", "InstrumentCondition", "MovieLength", "Verb", "Object"] 
audio_header = StimSet  StimNo  Verb    Object  Sentence_Transitive Sentence_Periphrastic   Sentence_Noncausal  Sentence_Badpassive Sentence_Passive

def convert_to_csvlines(line, counter):
    itemNo = int(line[2])
    primaryVerbDescription = line[13]
    primarySentenceDescription = line[16]
    verboseDescription = ['TO ADD', 'Multiple items']

    try:
        movielength = float(line[12])
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined...
    filePrefix = line[3] + line[14] 

    #Audio items are easy (though check KnockOver, it's named wrong...)
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
                print(fi)
                movie_item.update({'Filename': fi})
                movie_items.append(movie_item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)

    # #Read out audio files
    # for ai in audio_items:
    #     out_file = open('CBAudio yamls/' + ai['Filename'], "w")
    #     out_file.write( yaml.dump(ai, default_flow_style=False, allow_unicode=True) )
    #     out_file.close()

    #Read out movie files
    for mi in movie_items:
        out_file = open('CBMovie yamls/' + mi['Filename'], "w")
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
 
