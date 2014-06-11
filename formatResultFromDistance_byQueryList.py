import argparse, re


def format2sortedCosSimilarity(cosDis, outputName):
    fin = open(cosDis, 'r')
    fout = open(outputName, 'w')
    outputStr = ''
    for idx,line in enumerate(fin):
        lineList = re.split('\s+|\t+', line.strip())
        if lineList[0] == 'Enter':
            if idx == 0:
                continue
            fout.write(outputStr.rstrip(' ')+'\n')
            outputStr = ''
        elif lineList[0] == 'Word:':
            outputStr += lineList[1]+' '
        elif (lineList[0] == 'Word' or lineList[0] == ''):
            continue
        elif lineList[0] == 'Out':
            outputStr += '| |'
        elif not re.match(r'\-+',lineList[0]) is None:
            outputStr += '| '
        else:
            outputStr += (lineList[0]+'('+lineList[1]+') ')
    fin.close()
    fout.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cosDistanceFile', help='the cosine Distance file fron the distance_byQueryList program')
    parser.add_argument('sortedCosDistanceName', help='the same sorted foramt of cosine similarity file')
    args = parser.parse_args()

    format2sortedCosSimilarity(args.cosDistanceFile, args.sortedCosDistanceName)
