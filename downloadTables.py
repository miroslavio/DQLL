from rat import ratdb
from subprocess import call

def downloadDQLL(firstRun, lastRun):
    runs = range(firstRun, lastRun+1)
    db = ratdb.RATDBConnector(server="postgres://snoplus:dontestopmenow@pgsql.snopl.us:5400/ratdb")
    db.dump_table(obj_type="DQLL", runs=runs)
            
    ### UNZIP THE TABLES ###
    filename = 'DQLL_'+str(firstRun)+'-'+str(lastRun)+'.ratdb.bz2'
    call('bunzip2 ' + filename, shell=True)
