
## reférence : https://www.irif.fr/~francoisl//DIVERS/m1algo-progdynamique.pdf

##Essayer de retourner une solution 

def plssc(T):
    maxsofar, imax = 0, 0
    L, Pred = [0]*len(T), [0]*len(T) 
    for j in range(len(T)):
        aux = 0
        iaux = None
        for i in range(j):
           
            if (T[i] < T[j] and L[i] > aux):
                aux = L[i]
                iaux = i
        L[j] = 1 + aux 
        Pred[j] = iaux
        if (L[j] > maxsofar):
            maxsofar = L[j] 
            jmax = j
    return maxsofar


T=[5,2,8,6,3,6,9,7] 

m=plssc(T)

print(m)


def d(u,v):
    D = [[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
    choix = [["" for i in range(len(v)+1)] for j in range(len(u)+1)]
    for i in range(len(v)+1):
        for j in range(len(u)+1):
            if i==0:
                D[i][j] = j
            elif j==0:
                D[i][j] = i
            elif u[i-1] == v[j-1]:
                D[i][j] == D[i-1][j-1]
                choix[i][j] = "="
            else:
                M = D[i-1][j-1] +1
                I = D[i][j-1] +1
                S = D[i-1][j] +1
                if M<=I and M<=S:
                    D[i][j] = M
                    choix[i][j] = "M"
                elif I<=S:
                    D[i][j] = I
                    choix[i][j] = "I"
                else:
                    D[i][j] = S
                    choix[i][j] = "S"
                