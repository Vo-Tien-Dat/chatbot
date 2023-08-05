def GetDataFromTrainingCost(majorName, data):
    value = data[majorName]['credit']['value']
    number = data[majorName]['number']
    return [value, number]

def SolTrainingCosts(majorName, data):
    value = data[majorName]['credit']['value']
    number = data[majorName]['number']
    cost = int(value) * int(number)
    return cost

