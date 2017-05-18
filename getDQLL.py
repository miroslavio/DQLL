import argparse
import json
import subprocess
import glob

### PASS RUN NUMBER AS ARGUMENT TO GET THE DESIRED TABLE ###
parser = argparse.ArgumentParser()
parser.add_argument('run_number', type=str, help='run number for the dqll table')
args = parser.parse_args()

### DOWNLOAD THE TABLE ###
command = 'ratdb -s \"postgres://snoplus:dontestopmenow@pgsql.snopl.us:5400/ratdb\" dump_table \
DQLL ' + args.run_number
output, error = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

print output

### UNZIP THE TABLE ###
for filename in glob.glob('*'+args.run_number+'.ratdb.bz2'):
    subprocess.call('bunzip2 ' + filename, shell=True)
    
### READ THE TABLE AND DELETE IT(optional) ###
for filename in glob.glob('*'+args.run_number+'.ratdb'):
    data_file = open(filename, "r")
    data = json.load(data_file)
    print "Start time: ", data["start_time"]
    print "End time: ", data["end_time"]
    print "Duration: ", data["duration_seconds"]
    print "Crate_hv_status_a: ", data["crate_hv_status_a"]
    print "Crate_hv_status_b: ", data["crate_16_hv_status_b"]
    print "Crate_hv_dac_a: ", data["crate_hv_dac_a"]
    print "Crate_16_hv_dac_b: ", data["crate_16_hv_dac_b"]
    subprocess.call(['rm', filename]) #delete table
