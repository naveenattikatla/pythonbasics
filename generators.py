def div(a , b ):
    return  a / b 

def advdiv(fun):
    def inner(a , b ):
        if(a < b ):
            a , b = b,a 
        return fun( a ,b)
    return inner

div =  advdiv(div)
print(div(2,4))

# Geneators allows us to modifing behaviour of code without  changing actual implementation