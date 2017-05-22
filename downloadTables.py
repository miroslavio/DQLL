from rat import ratdb

def downloadDQLL(firstRun, lastRun):
    db = ratdb.RATDBConnector(server="postgres://snoplus@pgsql.snopl.us:5400/ratdb")
    
    tables = []
    for i in range(firstRun, lastRun+1):
        table = db.fetch(obj_type="DQLL", run = i)
        if table: #check the downloaded table is not empty
            print "Fetching DQLL table for run ",i, "\n"
            tables.append(table)
        else:
            print "DQLL Table for run ",i," NOT found\n"

    return tables

if __name__=="__main__":
     downloadDQLL(100440,100450) 
    

    
