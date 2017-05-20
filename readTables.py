import json
from subprocess import call

def readTables(firstRun,lastRun):
    filename = 'DQLL_'+str(firstRun)+'-'+str(lastRun)+'.ratdb'
    file = open(filename, 'r')
    tables = []
    for entry in file:
        tables.append(json.loads(entry))
    for table in tables:
        print "Start time: ", table["start_time"]
        print "End time: ", table["end_time"]
        print "Duration: ", table["duration_seconds"]
        print "Crate_hv_status_a: ", table["crate_hv_status_a"]
        print "Crate_hv_status_b: ", table["crate_16_hv_status_b"]
        print "Crate_hv_dac_a: ", table["crate_hv_dac_a"]
        print "Crate_16_hv_dac_b: ", table["crate_16_hv_dac_b"]
    call(['rm', filename]) #delete table, no longer needed
