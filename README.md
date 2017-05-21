To run this script you need to create a file called .pgpass and place it in your home directory. The file must contain one line regarding the info for ratdb:

   pgsql.snopl.us:5400:ratdb:username:password

where username and password are the collaboration standard.

Then to run the main script, simply do:

> python dqllPassFailList.py FIRSTRUN-LASTRUN

The script should output a list, that currently only shows whether or not the DQLL passed or failed using the same checks as in the run selection checklist. An example of the list is below, where 1 indicated DQLL passed for the run and 0 means DQLL failed.

 Run no | Pass |
--------|------|
 100450 |  1   |
 100451 |  1   |
 100452 |  1   |
 100453 |  1   |
 100454 |  1   |
 100455 |  1   |
 100456 |  0   |
 100458 |  1   |
 100459 |  1   |
 100460 |  0   |
                 

