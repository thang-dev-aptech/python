scores = [8, 5, 9, 4, 7, 10, 6, 5, 8]

def score_dict(score):
    yeu = []
    kha = []
    gioi = []
    for i in score:
        if i >= 8:
            gioi.append(i)
            
        elif i >=6 :
            kha.append(i)
        else:
            yeu.append(i)

    return {
        "avg" : sum(score) / len(score),
        "max" : max(score),
        "min" : min(score),
        "gioi" : gioi,
        "kha" : kha,
        "yeu" : yeu
    } 

print(score_dict(scores))