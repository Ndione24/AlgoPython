########################################################################

#************************** Soul is witness ****************************

########################################################################


## Fibonacci Simple Approach ("Top Down")
def fiboSimple(n):
    if n==0: return 0
    if n==1: return 1
    return fiboSimple(n-1)+fiboSimple(n-2)

## Fibonacci dynamic approach ("Top Down")

def fiboDynamic(n):
    if(n==0): return 0
    if(n==1):return 1

    ## create array for memorise values
    T=[None]*(n+1)
    T[0]=0
    T[1]=1

    T[n]= fiboAux(T,n-1)+fiboAux(T,n-2)
    return T[n]



def fiboAux(T,t):
    ## if the position n in T does not have a value
    if(T[t]==None):
        T[t]=fiboAux(T,t-1)+fiboAux(T,t-2)
    return T[t]
    


## Fibonacci dynamic approach ("Bottom-Up")

def fiboBottomUp(n):
    T=[0]*(n+1) ## fil array with value 0
    T[1]=1

    for i in range(2, n+1):
        T[i]=T[i-1]+T[i-2]

    return T[n]


## Test Fibonacci Dynamic
a=fiboDynamic(87)
print(a)

##Test Fibo Simple

##b=fiboSimple(172)
##print(b)


##Test Fibonacci Dynamic approach ("Bottom-Up")

print(fiboBottomUp(87))


