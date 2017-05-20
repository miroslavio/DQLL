import sys
from readTables import readTables
from downloadTables import downloadDQLL
import argparse

### Get run range from user (from Lisa)###
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('run_range', type=str, help='FIRSTRUN-LASTRUN')
    args = parser.parse_args()
    runs = (args.run_range.split("-")) #first and last run

    # Check user input is correct
    parseOK = False
    if (len(runs) >= 1):
        if runs[0].isdigit():
            firstRun = int(runs[0])
            if len(runs) == 2:
                if runs[1].isdigit():
                    lastRun = int(runs[1])
                    parseOK = True
            elif len(runs) == 1:
                lastRun = firstRun
                parseOK = True
    if not parseOK:
        print parser.print_help()
        sys.exit(1)

    # Check that first run <= last run
    if lastRun < firstRun:
        print "Invalid run range: first run must precede, or be equal to, last run"
        sys.exit(1)

    print "Reading DQLL tables for runs %i-%i" % (firstRun, lastRun)
    downloadDQLL(firstRun, lastRun)
    readTable(firstRun, lastRun)
    
