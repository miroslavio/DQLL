def startendTimecheck(start, end):
    if ( start < end ):
        return 1
    else:
        return 0

def durationCheck(duration):
    if ( duration >= 1800 ):
        return 1
    else:
        return 0

def crateHVstatusAcheck(array):
    for i in array:
        if array[i] == "false":
            return 0
    return 1

def crate16HVstatusBcheck(owlHVon):
    if owlHVon:
        return 1
    else:
        return 0

def crateHVdacAcheck(dacCounts):
    for i in dacCounts:
        if i <= 0:
            return 0
    return 1

def crate16HVdacBcheck(value):
    if value > 0:
        return 1
    else:
        return 0
