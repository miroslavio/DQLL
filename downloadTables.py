from rat import ratdb

def downloadDQLL(firstRun, lastRun):
    db = ratdb.RATDBConnector(server="postgres://snoplus@pgsql.snopl.us:5400/ratdb")
    tables = []
    for i in range(firstRun, lastRun+1):
        tables.append(db.fetch(obj_type="DQLL", run = i))
    return tables

if __name__=="__main__":
     downloadDQLL(100440,100450) 
    

    
