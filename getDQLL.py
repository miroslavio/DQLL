import argparse
from rat import ratdb
from subprocess import call
import json

def readDQLLTable(firstRun, lastRun):
    
    ### DOWNLOAD THE TABLES ###
    runs = range(firstRun, lastRun+1)
    db = ratdb.RATDBConnector(server="postgres://snoplus:dontestopmenow@pgsql.snopl.us:5400/ratdb")
    db.dump_table(obj_type="DQLL", runs=runs)
        
    ### UNZIP THE TABLES ###
    filename = 'DQLL_'+str(firstRun)+'-'+str(lastRun)+'.ratdb.bz2'
    call('bunzip2 ' + filename, shell=True)
    
    ### READ THE TABLES AND DELETE(optional) ###
    filename = filename[:-4]
    data_file = open(filename, "r")
    data = json.load(data_file)
    #print "Start time: ", data["start_time"]
    #print "End time: ", data["end_time"]
    #print "Duration: ", data["duration_seconds"]
    #print "Crate_hv_status_a: ", data["crate_hv_status_a"]
    #print "Crate_hv_status_b: ", data["crate_16_hv_status_b"]
    #print "Crate_hv_dac_a: ", data["crate_hv_dac_a"]
    #print "Crate_16_hv_dac_b: ", data["crate_16_hv_dac_b"]
    #call(['rm', filename]) #delete table
    
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
    readDQLLTable( firstRun, lastRun )
