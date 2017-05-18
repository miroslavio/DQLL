def startendTime(start, end):
    passChecks = 0
    if ( start > end ):
        passChecks = 1
    return passChecks

def durationCheck(duration):
    passChecks = 0
    if ( duration >= 1800 ):
        passChecks = 1
    return passChecks

def crateHVstatusAcheck(array):
    passChecks = 1
    for i in array:
        if array[i] == "false":
            passChecks = 0
    return passChecks

def crate16HVstatusB(owlHVon):
    passChecks = 0
    if owlHVon == "true":
        passChecks = 1
    return passChecks

def crateHVdacA(dacCounts):
    passChecks = 1
    for i in dacCounts:
        if dacCounts[i] <= 0:
            passChecks = 0
    return passChecks

def crate16HVdacB(value):
    passChecks = 0
    if value > 0:
        passChecks = 1
    return passChecks
