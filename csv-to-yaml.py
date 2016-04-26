import csv
import yaml


in_file  = open('stimsets.csv', "rU")
out_file = open('yaml_file.yaml', "w")
items = []

def convert_to_yaml(line, counter):
    settypes = line[1].strip('{}').replace(' ','').split(',')
    itemfactors = line[6].strip('{}').replace(' ','').split('},{')
    itemversions = {}
    for f in itemfactors:
        toadd = f.split(':')
        if len(toadd)>1:
            [mykey, mylist] = [toadd[0],toadd[1]]
            itemversions[mykey] = mylist.split(',')
    participants = line[10].strip('{}').replace(' ','').split(',')
    roles = line[11].strip('{}').replace(' ','').split(',')

    item = {
        'Name': line[0],
        'SetTypes': settypes,
        'Filetype':line[2],
        'Creator':line[3],
        'Citation':line[4],
        'Email': line[5],
        'ItemConditions': itemversions,
        'Language': line[7],
        'Kind': line[8],
        'Modality': line[9],
        'Participants':participants,
        'Roles':roles

            }
    items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
    out_file.write( yaml.dump(items, default_flow_style=False, allow_unicode=True) )

finally:
    in_file.close()
    out_file.close()
 
