import json
import sys
import os.path


# this method returns a dictionary with
# the names and the preferences of the men/women
def parse_json(choice, filename):
    dictionary = {}
    f = open(filename, 'r')
    j = json.load(f)
    f.close()
    j_string = json.dumps(j, sort_keys=True, indent=4)
    data = json.loads(j_string)
    selection = data[choice]
    for key, value in selection.items():
        dictionary[key] = value
    return dictionary


class Person:
    # this method initializes the objetc Person
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.mate = None
        self.preferenceNumber = 0
        self.preferencesRanking = {}
        for preferenceOrder in range(len(preferences)):
            self.preferencesRanking[preferences[preferenceOrder]] = preferenceOrder

    # this method check if a Mate is preferable than the
    # the Person already has.
    def evaluateProposal(self, possible_Mate):
        # if the current mate is not preferable than the possible
        # future mate return true.
        choice = self.preferencesRanking[possible_Mate] < self.preferencesRanking[self.mate]
        return choice

    # this method finds the next Person
    # to propose.
    def nextProposal(self):
        possible_mate = self.preferences[self.preferenceNumber]
        self.preferenceNumber = self.preferenceNumber + 1
        return possible_mate


# method to create the male and female lists.
def createLists(filename, gender):
    unmatchedPeople = []
    males = parse_json('men_rankings', filename)
    malesDict = {}
    for key in males:
        malesDict[key] = Person(key, males.get(key, 0))

    females = parse_json('women_rankings', filename)
    femalesDict = {}
    for key in females:
        femalesDict[key] = Person(key, females.get(key, 0))
    return (unmatchedPeople, malesDict, femalesDict)


def createMatches(unmatchedList, malesDict, femalesDict):
    check = True
    if gender == "-w":
        check = False
        unmatchedList = list(femalesDict.keys())
    else:
        unmatchedList = list(malesDict.keys())
    # check if there are unmatched People and if yes
    # continue the loop
    while len(unmatchedList) > 0:
        if check is False:
            x = femalesDict[unmatchedList[0]]
            y = malesDict[x.nextProposal()]
        else:
            x = malesDict[unmatchedList[0]]
            y = femalesDict[x.nextProposal()]
        # if this Person does not have a mate
        # then add as its mate the Person who is
        # now proposing.
        if y.mate is None:
            unmatchedList.remove(x.name)
            y.mate = x.name
            x.mate = y.name
        # else if this Person has a mate check
        # if it prefers its current mate or
        # proposing person.
        elif y.evaluateProposal(x.name):
            if check is False:
                previousMate = femalesDict[y.mate]
            else:
                previousMate = malesDict[y.mate]
            previousMate.mate = None
            unmatchedList.append(previousMate.name)
            unmatchedList.remove(x.name)
            y.mate = x.name
            x.mate = y.name
    if check is False:
        return femalesDict
    else:
        return malesDict


# method to print the result
# or to create a JSON file.
def printMatches(result, outputfile=None):
    keys = sorted(result.keys())
    marriages = {}
    for person in keys:
        marriages[result[person].name] = result[person].mate
    result = json.dumps(marriages, sort_keys=True, indent=4)
    if outputfile is None:
        print(result)
    else:
        with open(outputfile, 'w') as fp:
            json.dump(marriages, fp, sort_keys=True, indent=4)
        print(result)


if len(sys.argv) < 3:
    print("Error! You should give your choice " +
          "of gender and the file to be read.")
    sys.exit(2)

gender = str(sys.argv[1])
if not (gender == "-m" or gender == "-w"):
    print("Error! You should type either -m for men or -w for women.")
    sys.exit(2)

filename = str(sys.argv[2])
if not(os.path.exists(filename)):
    print("Error! File does not exist.")
    sys.exit(2)

if len(sys.argv) > 3:
    output = str(sys.argv[3])
    outputFile = None
    if output == "-o":
        outputFile = str(sys.argv[4])
        marriageTuple = createLists(filename, gender)
        printMatches(createMatches(marriageTuple[0],
                                   marriageTuple[1],
                                   marriageTuple[2]), outputFile)
else:
    marriageTuple = createLists(filename, gender)
    printMatches(createMatches(marriageTuple[0],
                               marriageTuple[1], marriageTuple[2]))
