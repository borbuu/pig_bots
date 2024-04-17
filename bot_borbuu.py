if player == 1:
    flab = pow(1-1/6, (100-scores[0])/4)
    crate = pow(1-1/6, (100-(scores[1]+score))/4)
    if scores[0]-scores[1] >= 10:
        if score >= 20:
            hold = 0
        if score <= 20:
            hold = 1
    elif scores[0]-scores[1] >= 30:
        if score >= 25:
            hold = 0
        if score <= 25:
            hold = 1
    else:
        if score >= 16:
            hold = 0
        if score <= 16:
            hold = 1
    advice = random.choice(d6)
    if advice <= 5:
        if ((score >= 15*(1+flab-crate) and crate < 0.5) or scores[1]+score >= 100):
            return False
        else:
            return True
        if advice == 6:
            if hold == 0:
                return False
            if hold == 1:
                return True
