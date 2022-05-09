lakewood = {
    'rank':3,
    'wd':[110, 80],
    'we':[90, 80]
}

bridgewood = {
    'rank':4,
    'wd':[160, 110],
    'we':[60, 50]
}

ridgewood = {
    'rank':5,
    'wd':[220, 100],
    'we':[150, 40]
}

def check_cheap(af, day):
    
    if day == 0:
        val_l = lakewood['wd']
        val_b = bridgewood['wd']
        val_r = ridgewood['wd']
    else:
        val_l = lakewood['we']
        val_b = bridgewood['we']
        val_r = ridgewood['we']

    if val_l[af] < val_b[af] and val_l[af] < val_r[af]:
        aux = ["Lakewood", lakewood['rank'], val_l[af]]
        
    elif val_b[af] < val_r[af]:
        aux = ["Bridgewood", bridgewood['rank'], val_b[af]]
        
    else:
        aux = ["Ridgewood", ridgewood['rank'], val_r[af]]
    
    return aux

def get_cheapest_hotel(af, day):   #DO NOT change the function's name
    
    aux_cheap = check_cheap(af, day[0])
    
    for i in range(1,3):
        
        cheap = check_cheap(af, day[i])
        
        if cheap[2] < aux_cheap[2]:
            aux_cheap = cheap

        elif cheap[2] == aux_cheap[2]:
            if cheap[1] > aux_cheap[1]:
                aux_cheap = cheap
        
    return cheap[0]
