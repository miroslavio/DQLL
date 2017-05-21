def startendTime(start, end):
    passChecks = 0
    if ( start > end ):
        passChecks = 1
    return passChecks

def durationCheck(duration):
    if ( duration >= 1800 ):
        return 1
    else:
        return 0

def crateHVstatusAcheck(array):
    passChecks = 1
    for i in array:
        if array[i] == "false":
            passChecks = 0
    return passChecks

def crate16HVstatusBcheck(owlHVon):
    return owlHVon

def crateHVdacAcheck(dacCounts):
    passChecks = 1
    for i in dacCounts:
        if i <= 0:
            passChecks = 0
    return passChecks

def crate16HVdacBcheck(value):
    if value > 0:
        return 1
    else:
        return 0
