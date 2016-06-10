import csv
import yaml

#Rewrite that crazy csv I made to be in a reasonable format. 1 line per movie, separately 1 line per audio file. 

in_file  = open('CBMovies.csv', "rU")
movie_items = []

movie_header = ["fileNo", "ItemNo",  "ChangeCondition", "InstrumentCondition", "filename"] #header
movie_items.append(movie_header)

def convert_to_csvlines(line, counter):
    itemNo = (line[2])
    primaryVerbDescription = line[13]
    primarySentenceDescription = line[16]
    try:
        movielength = float(line[12])
    except ValueError:
        movielength = 'not specified'
    size = [0,0] #The sizes for the movies are undefined...
    filePrefix = line[3] + line[14] 

    #Movie items are a bit harder because different items have different sets of conditions available
    #What conditions do we have? Get the Stimset and ChangeAvailable vars so we 
    #can populate the list of conditions + filenames 

    Stimset = line[0]
    hasConditions = line[1]

    if Stimset == 'Original': #Only noInstrument versions
        if hasConditions == "MannerResult":
            MovieConditions = ["Base","MannerChange","ResultChange", "CounterbalanceMR"]
            InstConditions = ["NoInstrument"]

        elif hasConditions == "Unintentional":
            MovieConditions = ["Base","Unintentional"]
            InstConditions = ["NoInstrument"]
        else: #None
            MovieConditions = ["Base"]
            InstConditions = ["NoInstrument"]
    else: #All changes, and both instrument and noinstrument exist!!
        if hasConditions == "NoInstOnly": #(except this weirdo)
            MovieConditions = ["Base","BackgroundChange",
            "BigAgentChange","SmallAgentChange","MannerChange","ResultChange","ObjectChange","InstrumentChange"]
            InstConditions = ["NoInstrument"]
        else:
            MovieConditions = ["Base","BackgroundChange",
            "BigAgentChange","SmallAgentChange","MannerChange","ResultChange","ObjectChange","InstrumentChange"]
            InstConditions = ["NoInstrument", "Instrument"]

    #Now build each of those condition combos out into movie items!

    for m in xrange(len(MovieConditions)):
        for i in xrange(len(InstConditions)):

            mc = MovieConditions[m]
            inst = InstConditions[i]

            
            fi = ''
            if hasConditions == 'MannerResult':
                if mc == 'Base':
                    fi = filePrefix + '_' + line[4] +'.mp4'                    
                elif mc == 'MannerChange':
                    fi = filePrefix + '_' + line[9]+'.mp4'
                elif mc == 'ResultChange':
                    fi = filePrefix + '_' + line[10]+'.mp4'
                elif mc == 'CounterbalanceMR':
                    fi = filePrefix + '_' + line[20]+'.mp4'
                    print('get here!')
            elif hasConditions == 'Unintentional':
                 if mc == 'Base':
                    fi = filePrefix + '_' + line[4]+'.mp4'
                 elif mc == 'Unintentional':
                    fi = filePrefix + '_' + line[5]+'.mp4'
            elif hasConditions == 'None':
                fi = filePrefix + '_' + line[4]+'.mp4'
            elif hasConditions == 'All':
                fi = filePrefix + '_' + mc + '_' + inst + '.mp4'
            elif hasConditions == 'NoInstOnly':
                fi = filePrefix + '_' + mc + '_' + inst + '.mp4'
            elif hasConditions == 'Cup': #special cases
                fi = 'Cup.mp4'
            elif hasConditions == "Give":
                fi = "GiveBalloon.mp4"
            elif hasConditions == "Jingle":
                fi = "Jingle.mp4"


            #Funny exception: There is no such thing as NoInstrument + InstrumentChange
            if not((inst == "NoInstrument") & (mc == "InstrumentChange")):
                fileNo = len(movie_items) #Start at 1 (counts the header line) and move forwar
                movie_item = [str(fileNo), itemNo,  mc, inst, fi]
                movie_items.append(movie_item)

#Now read all those lines!

reader = csv.reader(in_file)
next(reader) # skip headers
for counter, line in enumerate(reader):
     convert_to_csvlines(line, counter)


#And save that all to a csv

out_lines = []

for i in xrange(len(movie_items)):
    next_i = ','.join(movie_items[i])
    out_lines.append(next_i)

out_file = '\n'.join(out_lines)
ouf = open('CB_longform.csv', "w")
ouf.write(out_file)
ouf.close

    # #Read out movie files
    # for mi in movie_items:
    #     out_file = open('CBMovie yamls/' + mi['Filename'], "w")
    #     out_file.write( yaml.dump(mi, default_flow_style=False, allow_unicode=True) )
    #     out_file.close()


 
