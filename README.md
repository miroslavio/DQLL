To run this script you need to create a file called .pgpass and place it in your home directory. The file must contain one line regarding the info for ratdb:

   pgsql.snopl.us:5400:ratdb:username:password

where username and password are the collaboration standard.

Then to run the main script, simply do:

> python dqllPassFailList.py FIRSTRUN-LASTRUN

The script should output a text file called runlistFIRSTRUN_LASTRUN.txt. Its content should look like the example below. 

 Run no | Time | Duration | Crate HV status A | Crate 16 HV status B | Crate HV DAC A | Crate 16 HV DAC B |
--------|------|----------|-------------------|----------------------|----------------|-------------------|
 100450 |   1  |     1    |          1        |           1          |         1      |          1        |
 100451 |   1  |     1    |          1        |           1          |         1      |          1        |
 100452 |   1  |     1    |          1        |           1          |         1      |          1        |
 100453 |   1  |     1    |          1        |           1          |         1      |          1        |
 100454 |   1  |     1    |          1        |           1          |         1      |          1        |
 100455 |   1  |     1    |          1        |           1          |         1      |          1        |
 100456 |   1  |     0    |          1        |           1          |         1      |          1        |
 100458 |   1  |     1    |          1        |           1          |         1      |          1        |
 100459 |   1  |     1    |          1        |           1          |         1      |          1        |
 100460 |   1  |     0    |          1        |           1          |         1      |          1        |    
                 
Each run number shows which DQLL checks (specifically those checks outline in the run selection checklist) passed (1) or failed (0).

The time check is simply making sure that the end_time > start_time. Duration >= 1800s. And the rest are outlined in the run selection checklist.
