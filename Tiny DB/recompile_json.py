import csv
import yaml
import sys
import getopt
import csvmapper


def main(argv):
    inputfile = ''
    if len(argv) == 0:
        bailout()
    try:
        opts, args = getopt.getopt(argv, "l:", ["list="])
    except getopt.GetoptError:
        bailout()
    for opt, arg in opts:
        if opt in ("-l", "--list"):
            inputfile = arg
            if inputfile == '':
                bailout()
            elif inputfile not in ['stimuli', 'creators',
                    'people', 'stimsets', 'stimrefs', 'all']:
                     bailout()

    for case in switch(inputfile):
        if case('stimuli'):
            print 1
            break
        if case('creators'):
            print 2
            break
        if case('people'):
            print 10
            break
        if case('stimsets'):
            print 11
            break
        if case('stimrefs'):
            print 11
            break
        if case('all'):
            print "something else!"
        # No need to break here, it'll stop anyway

    fields = ('FirstName', 'LastName', 'IDNumber', 'Messages')
    parser = CSVParser('sample.csv', csvmapper.FieldMapper(fields))
    converter = csvmapper.JSONConverter(parser)
    print converter.doConvert(pretty=True)


# def convert_to_yaml(line, counter):
#     settypes = line[1].strip('{}').replace(' ','').split(',')
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

# try:
#     reader = csv.reader(in_file)
#     next(reader) # skip headers
#     for counter, line in enumerate(reader):
#         convert_to_yaml(line, counter)
#     out_file.write( yaml.dump(items, default_flow_style=False, allow_unicode=True) )

# finally:
#     in_file.close()
#     out_file.close()

def bailout():
    print 'Usage: recompile_json.py -l <list> \nlist is the type of record to update. Options: \nstimuli \ncreators \npeople \nstimsets \nstimrefs \nall'
    sys.exit(2)

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


if __name__ == "__main__":
    main(sys.argv[1:])
