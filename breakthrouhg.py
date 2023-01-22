import random

def kommandering(talen_0, talen_X, vinst_0, vinst_X, mojliga_tal):
    schackbrade(talen_0, talen_X)
    while True:
        valen = []
        step = []
        
        for i in range(0, len(talen_0)):
            if talen_0[i] - 9 in talen_X:
                valen = valen + [eliminering_vanster_0]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om 0 vinner med att eliminera en X vänster om 0, så utförs denna if sats
                if talen_0[i] - 9 in vinst_0:
                    eliminering_vanster_0(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "0 vann!"
                    return
                
            if talen_0[i] + 11 in talen_X:
                valen = valen + [eliminering_hoger_0]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om 0 vinner med att eliminera en X höger om 0, så utförs denna if sats
                if talen_0[i] + 11 in vinst_0:
                    eliminering_hoger_0(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "0 vann!"
                    return
                
            if talen_0[i] + 1 not in talen_X and talen_0[i] + 1 not in talen_0:
                valen = valen + [framat_0]
                step = step +[i]
                #Vettighetskontroll/Vinst kollare
                #Om 0 vinner med att gå ett steg framåt, så utförs denna if sats
                if talen_0[i] + 1 in vinst_0:
                    framat_0(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "0 vann!"
                    return

            if talen_0[i] + 11 not in talen_0 and talen_0[i] + 11 not in talen_X and talen_0[i] + 11 in mojliga_tal:
                valen = valen + [diagonalt_hoger_0]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om 0 vinner med att gå diagonalt (höger), så utförs denna if sats
                if talen_0[i] + 11 in vinst_0:
                    diagonalt_hoger_0(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "0 vann!"
                    return

            if talen_0[i] - 9 not in talen_0 and talen_0[i] - 9 not in talen_X and talen_0[i] - 9 in mojliga_tal:
                valen = valen + [diagonalt_vanstar_0]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om 0 vinner med att gå diagonalt (vänster), så utförs denna if sats
                if talen_0[i] - 9 in vinst_0:
                    diagonalt_vanstar_0(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "0 vann!"
                    return
                
        if len(valen) == 0:
            oavgjort(talen_0, talen_X)

        random_val(talen_0, talen_X, i, valen, step)    
        
        #Reset av listorna valen och step
        valen = []
        step = []
        
        for i in range(0, len(talen_X)):
            if talen_X[i] + 9 in talen_0:
                valen = valen + [eliminering_vanster_X]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om X vinner med att eliminera en 0 bonde vänster om X, så utförs denna if sats
                if talen_X[i] + 9 in vinst_X:
                    eliminering_vanster_X(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "X vann!"
                    return
                
            if talen_X[i] - 11 in talen_0:
                valen = valen + [eliminering_hoger_X]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om X vinner med att eliminera en 0 bonde höger om X, så utförs denna if sats
                if talen_X[i] - 11 in vinst_X:
                    eliminering_hoger_X(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "X vann!"
                    return
                
            if talen_X[i] - 1 not in talen_0 and talen_X[i] - 1 not in talen_X:
                valen = valen + [framat_X]
                step = step +[i]
                #Vettighetskontroll/Vinst kollare
                #Om X vinner med att gå ett steg framåt, så utförs denna if sats
                if talen_X[i] - 1 in vinst_X:
                    framat_X(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "X vann!"
                    return

            if talen_X[i] - 11 not in talen_0 and talen_X[i] - 11 not in talen_X and talen_X[i] - 11 in mojliga_tal:
                valen = valen + [diagonalt_hoger_X]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om X vinner med att gå diagonalt (höger), så utförs denna if sats
                if talen_X[i] - 11 in vinst_X:
                    diagonalt_hoger_X(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "X vann!"
                    return

            if talen_X[i] + 9 not in talen_0 and talen_X[i] + 9 not in talen_X and talen_X[i] + 9 in mojliga_tal:
                valen = valen + [diagonalt_vanstar_X]
                step = step + [i]
                #Vettighetskontroll/Vinst kollare
                #Om X vinner med att gå diagonalt (vänster), så utförs denna if sats
                if talen_X[i] + 9 in vinst_X:
                    diagonalt_vanstar_X(talen_0, talen_X, i)
                    schackbrade(talen_0, talen_X)
                    print "X vann!"
                    return
            
        if len(valen) == 0:
            oavgjort(talen_0, talen_X)
            
        random_val(talen_0, talen_X, i, valen, step)

#Alla drag
def framat_0(talen_0, talen_X, i):
    talen_0[i] = talen_0[i] + 1

def diagonalt_hoger_0(talen_0, talen_X, i):
    talen_0[i] = talen_0[i] + 11

def diagonalt_vanstar_0(talen_0, talen_X, i):
    talen_0[i] = talen_0[i] - 9

def eliminering_hoger_0(talen_0, talen_X, i):
    talen_X.remove(talen_0[i] + 11)                   
    talen_0[i] = talen_0[i] + 11
    
def eliminering_vanster_0(talen_0, talen_X, i):
    talen_X.remove(talen_0[i] -9)                   
    talen_0[i] = talen_0[i] - 9

def framat_X(talen_0, talen_X, i):
    talen_X[i] = talen_X[i] - 1

def diagonalt_hoger_X(talen_0, talen_X, i):
    talen_X[i] = talen_X[i] - 11

def diagonalt_vanstar_X(talen_0, talen_X, i):
    talen_X[i] = talen_X[i] + 9

def eliminering_hoger_X(talen_0, talen_X, i):
    talen_0.remove(talen_X[i] - 11)                   
    talen_X[i] = talen_X[i] - 11

def eliminering_vanster_X(talen_0, talen_X, i):
    talen_0.remove(talen_X[i] + 9)                   
    talen_X[i] = talen_X[i] + 9

#En funktion som visuellt represnterar positionerna av X och 0
def schackbrade(talen_0, talen_X):
    schackbrade = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87, 16, 26, 36, 46, 56, 66, 76, 86, 15, 25, 35, 45, 55, 65, 75, 85, 14, 24, 34, 44, 54, 64, 74, 84, 13, 23, 33, 43, 53, 63, 73, 83, 12, 22, 32, 42, 52, 62, 72, 82, 11, 21, 31, 41, 51, 61, 71, 81]
    for i  in range(0,len(schackbrade)):
        if schackbrade[i] in talen_0:
            schackbrade[i] = "0"
        elif schackbrade[i] in talen_X:
            schackbrade[i] = "X"
        else:
            schackbrade[i] = "_"
                
    print schackbrade[0: 8]
    print schackbrade[8: 16]
    print schackbrade[16: 24]
    print schackbrade[24: 32]
    print schackbrade[32: 40]
    print schackbrade[40: 48]
    print schackbrade[48: 56]
    print schackbrade[56: 64]
    print "--------------------------------------"

#En funktion som kollar vem som vinner om bönderna inte kan göra mera drag
def oavgjort(talen_0, talen_X):
    if len(talen_0) == len(talen_X):
        print "Oavgjort"
        return
    else:
        if len(talen_0) > len(talen_X):
            print "0 vann!"
            return
        if len(talen_0) < len(talen_X):
            print "X vann!"
            return

#En funktion som väljer en av de möjliga dragen
def random_val(talen_0, talen_X, i, valen, step):
    random_talet = random.randrange(0, len(valen))
    #i spara positionen av piäsen som kunde spelas
    i = step[random_talet]
    valen[random_talet](talen_0, talen_X, i)
    schackbrade(talen_0, talen_X)
    

def main():
    talen_0 = [11, 21, 31, 41, 51, 61, 71, 81, 12, 22, 32, 42, 52, 62, 72, 82]
    talen_X = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87]
    vinst_0 = [18, 28, 38, 48, 58, 68, 78, 88]
    vinst_X = [11, 21, 31, 41, 51, 61, 71, 81]
    mojliga_tal = [18, 28, 38, 48, 58, 68, 78, 88, 17, 27, 37, 47, 57, 67, 77, 87, 16, 26, 36, 46, 56, 66, 76, 86, 15, 25, 35, 45, 55, 65, 75, 85, 14, 24, 34, 44, 54, 64, 74, 84, 13, 23, 33, 43, 53, 63, 73, 83, 12, 22, 32, 42, 52, 62, 72, 82, 11, 21, 31, 41, 51, 61, 71, 81]
    kommandering(talen_0, talen_X, vinst_0, vinst_X, mojliga_tal)

main()


    

