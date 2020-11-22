import argparse

def printLengthStats(inPath, outPath):
    with open(inPath, 'r') as inFile:
        with open(outPath,'a') as outFile:
            outFile.write("\n  1. Length Statisitcs:\n\n")
            lines = inFile.read().strip().split('\n')
            totLen = int(lines[6].split('\t')[1])
            outFile.write("{:5}a. Total length: {} ~ {:.4f} Gb\n".format("", totLen, totLen/1e9))
            outFile.write("{:5}b. Number of Contigs: {}\n".format("", lines[7].split('\t')[1]))
            N50 = int(lines[13].split('\t')[2])
            outFile.write("{:5}c. N50: {} ~ {:.2f} Mb\n".format("", N50, N50/1e6))
            auN = int(lines[19].split('\t')[1])
            outFile.write("{:5}d. auN: {} ~ {:.2f} Mb\n".format("", auN, auN/1e6))
            outFile.write("{:5}e. Nx:\n\n".format(""))
            outFile.write("{:7}--------------------\n".format(""))
            outFile.write("{:7}{:5}{:12}{}\n\n".format("", "x", "Nx", "Lx"))
            for line in lines[8:19]:
                numbers = line.split('\t')
                outFile.write("{:7}{:5}{:12}{}\n".format("", numbers[1],  numbers[2], numbers[3]))
            outFile.write("{:7}--------------------\n".format(""))

def printGeneStats(inPath, outPath):
    with open(inPath, 'r') as inFile:
        with open(outPath,'a') as outFile:
            lines = inFile.read().strip().split('\n')
            outFile.write("\n  2. Gene Completeness:\n\n")
            outFile.write("{:6}---------------------------------\n".format(""))
            numbers = lines[0].split()
            outFile.write("{:6}{:14}{:14}{}\n\n".format("", numbers[1], numbers[2], numbers[3]))
            for line in lines[1:]:
                numbers = line.split()
                outFile.write("{:6}{:14}{:14}{}\n".format("", numbers[1], numbers[2], numbers[3]))
            outFile.write("{:6}---------------------------------\n".format(""))

def printErrorStats(inPath, outPath):
    with open(inPath, 'r') as inFile:
        with open(outPath,'a') as outFile:
            outFile.write("\n  3. Errors:\n\n")
            lines = inFile.read().strip().split('\n')
            switch_error = lines[-2].split()[-1]
            hamm_error = lines[-1].split()[-1]
            outFile.write("{:5}a. Switch error: {:.4f} %\n".format("", float(switch_error) * 100))
            outFile.write("{:5}b. Hamming error: {:.4f} %\n".format("", float(hamm_error) * 100))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--childID')
    parser.add_argument('--patLenStats')
    parser.add_argument('--patGeneStats')
    parser.add_argument('--patErrorStats')
    parser.add_argument('--matLenStats')
    parser.add_argument('--matGeneStats')
    parser.add_argument('--matErrorStats')
    parser.add_argument('--output')
    args = parser.parse_args()
    with open(args.output, 'w') as outFile:
        outFile.write("************* {} *************\n\n".format(args.childID))
        outFile.write("-Paternal\n")
    printLengthStats(args.patLenStats, args.output)
    printGeneStats(args.patGeneStats, args.output)
    printErrorStats(args.patErrorStats, args.output)
    with open(args.output, 'a') as outFile:
        outFile.write("\n-Maternal\n")
    printLengthStats(args.matLenStats, args.output)
    printGeneStats(args.matGeneStats, args.output)
    printErrorStats(args.matErrorStats, args.output)


if __name__ == "__main__":
    main()

