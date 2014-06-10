import argparse, os

def format4fileCorpus(inputName, outputName):
    inputFile = open(inputName, 'r')
    outputFile = open(outputName, 'w')
    for line in inputFile:
        line = line.rstrip()
        # remove all label, doc id, null string
        if len(line.split(' ')) <= 1:
            continue
        else:
            outputFile.write(line.strip()+' ')
    outputFile.close()
    inputFile.close()

def format4pathCorpus(dirPath, output):
    fileList = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath,f))]
    fout = open(output, 'w')
    for fileName in fileList:
        fin = open(os.path.join(dirPath,fileName), 'r')
        for line in fin:
            fout.write(line.strip()+' ')
        fin.close()
    fout.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputCorpus', help='the input corpus which is word-splitted')
    inputG = parser.add_mutually_exclusive_group(required=True)
    inputG.add_argument('-p','--pathCorpus', help='the input is the directory path including lots of corpus files', action='store_true')
    inputG.add_argument('-f','--fileCorpus', help='the input is a file of corpus', action='store_true')
    parser.add_argument('word2vecCorpus', help='the output corpus which is formatted for the word2vec program')
    args = parser.parse_args()

    if args.pathCorpus is True:
        format4pathCorpus(args.inputCorpus, args.word2vecCorpus)
    elif args.fileCorpus is True:
        format4fileCorpus(args.inputCorpus, args.word2vecCorpus)
    else:
        print('Please enter a correct input format, -h looks more info')

