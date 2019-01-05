def isGdEqual(result,prediction):
    resultSplit = result.split('\n')[0].split('-')
    predictionSplit = prediction.split('\n')[0].split('-')
    return (int(resultSplit[0]) - int(resultSplit[1]) == int(predictionSplit[0]) - int(predictionSplit[1])) and (resultSplit[0] != resultSplit[1])

def isDrawPredicted(result,prediction):
    resultSplit = result.split('\n')[0].split('-')
    predictionSplit = prediction.split('\n')[0].split('-')
    return (resultSplit[0] == predictionSplit[0]) and (resultSplit[1] == predictionSplit[1])

def isWinnerCorrect(match, result, prediction):
    actualWinner = getWinner(match,result)
    predictedWinner = getWinner(match,prediction)
    return actualWinner == predictedWinner

def getWinner(match, result):
    home = match.split('/\n')[0]
    away = match.split('/\n')[1]
    homeScore = int(result.split('\n')[0].split('-')[0])
    awayScore = int(result.split('\n')[0].split('-')[1])
    if len(result.split('\n')) > 1:
        return result.split('\n')[1][1:-1]
    elif homeScore > awayScore:
        return home
    else:
        return away


def calculate(columns):
    score = {}
    score[columns[1][0]] = 240
    i = 1
    result = []
    while i < len(columns[1]):
        if columns[1][i] != '':
            result.append(columns[1][i])
        i += 1

    for column in columns[2:]:
        points = 0
        i = 0
        while i < len(result):
            if result[i] == column[i+1]:
                points+= 20
            elif isGdEqual(result[i],column[i+1]):
                points+=15
            elif isWinnerCorrect(columns[0][i+1],result[i],column[i+1]):
                points+=10
            elif isDrawPredicted(result[i],column[i+1]):
                points+=10
            i += 1
        score[column[0]] = points

    return score