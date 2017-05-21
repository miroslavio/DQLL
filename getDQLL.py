import sys
from downloadTables import downloadDQLL
import argparse
from dqllChecks import *

def initRunlistFile(firstRun, lastRun):
    #Open runlist file:
    runlistFileName = "runlist_%s-%s.txt" % (firstRun, lastRun)
    runlistFile = open(runlistFileName, "w")

    # Print list header
    runlistFile.write("\n")
    runlistFile.write(" Run no | Pass |\n" + \
                      "--------|------|\n")
    return runlistFile

def processRun(table, runlistFile):
    #Unpack DQLL table data
    runNumber = table[0]["data"]["run_range"][0]
    start_time = table[0]["data"]["start_time"]
    end_time = table[0]["data"]["end_time"]
    duration = table[0]["data"]["duration_seconds"]
    crateHVstatusA = table[0]["data"]["crate_hv_status_a"]
    crate16HVstatusB = table[0]["data"]["crate_16_hv_status_b"]
    crateHVdacA = table[0]["data"]["crate_hv_dac_a"]
    crate16HVdacB = table[0]["data"]["crate_16_hv_dac_b"]
    
    if durationCheck(duration) and crateHVstatusAcheck(crateHVstatusA) and crate16HVstatusBcheck(crate16HVstatusB) and crateHVdacAcheck(crateHVdacA) and crate16HVdacBcheck(crate16HVdacB):
        runlistFile.write(" %s" %str(runNumber) + " |  1   |\n")
    else:
        runlistFile.write(" %s" %str(runNumber) + " |  0   |\n")
        
def dqllPassFailList(firstRun, lastRun):

    # Open and initiate run-list file:
    runlistFile = initRunlistFile(firstRun, lastRun)

    # Download all the DQLL tables from firstRun to lastRun
    tables = downloadDQLL(firstRun, lastRun)
    for table in tables:
        print table, "\n"
        processRun(table, runlistFile)
        
    
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

    print "Running dqllPassFailList for run range %i-%i" % (firstRun, lastRun)
    dqllPassFailList(firstRun, lastRun)
    sys.exit(0)
