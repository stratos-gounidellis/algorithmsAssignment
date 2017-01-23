import csv
import sys
import argparse
import itertools

#parse the arguments
parser = argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numeric", help="items are numeric",
                    action="store_true", default=False)
parser.add_argument("support", help="support threshold")
parser.add_argument("-p", "--percentage",
                    action="store_true", default=False,
                    help="treat support threshold as percentage value")
parser.add_argument("filename", help="input filename")
parser.add_argument("-o", "--output", type=str, help="output file")
args = parser.parse_args()
support = int(args.support)

#check if the current set's impressions are greater
#than the given support.
def checkSupport(counts, flag):
    freq = {}
    for item, count in counts.items():
        if args.percentage is True:
            if count >= ((support/100) * flag):
                freq[item] = count
        else:
            if count >= support:
                freq[item] = count
    return freq


def aPrioriFirstPass(filename):
    flag = 0
    counts = {}
    freq = {}
    input_file = open(filename, 'r')
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        # check if the user wants to read integers
        if args.numeric is False:
            unique_row_items = set([field.lower().strip() for field in row])
        else:
            unique_row_items = set([int(field) for field in row])
        flag = flag + 1
        for item in unique_row_items:
            firstTuple = (item,)
            if firstTuple in counts.keys():
                counts[firstTuple] = counts[firstTuple] + 1
            else:
                counts[firstTuple] = 1
    freq = checkSupport(counts, flag)
    input_file.close()
    return freq


def aPrioriPass(filename, freq, k):
    flag = 0
    freq_new = {}
    counts = {}
    input_file = open(filename, 'r')
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        # process row
        if args.numeric is False:
            unique_row_items = set([field.lower().strip() for field in row])
        else:
            unique_row_items = set([int(field) for field in row])
        #create all the possible combinations
        itemset_pairs = itertools.combinations(list(freq.keys()), 2)
        flag = flag + 1
        candidates = []
        for pair in itemset_pairs:
            fp = set(pair[0])
            sp = set(pair[1])
            #combine the two sets
            candidate = (fp | sp)
            if candidate not in candidates:
                candidates.append(candidate)
                candidateTuple = tuple(sorted(candidate))
                #check the length of the set and if the set is a
                #subset of the current row.
                if len(candidateTuple) == k + 1 and candidate.issubset(unique_row_items):
                    if candidateTuple in counts.keys():
                        counts[candidateTuple] = counts[candidateTuple] + 1
                    else:
                        counts[candidateTuple] = 1
    freq_new = checkSupport(counts,  flag)
    input_file.close()
    return freq_new


def aPriori(filename):
    k = 1
    freqPass = aPrioriFirstPass(args.filename)
    #check if the result should be
    #saved into a new csv file.
    if args.output is not None:
        output_file = open(args.output, 'w',  newline='')
    while len(freqPass) > 0:
        row = []
        for key in sorted(freqPass.keys()):
            row.append("{0}:{1}".format(key, freqPass[key]))
        if args.output is not None:
            csv_writer = csv.writer(output_file, delimiter=';')
            csv_writer.writerow(row)
        else:
            csv_writer = csv.writer(sys.stdout, delimiter=';')
            csv_writer.writerow(row)
        freq = aPrioriPass(args.filename, freqPass, k)
        freqPass = freq
        k = k + 1
    if args.output is not None:
        output_file.close()
        
#check the main method of the algorithm.
aPriori(args.filename)
