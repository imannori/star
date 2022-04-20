import sys


# pour python si on multiplie un char ou string par un nombre entier, on aura une chaine avec plusieur copie du string original.
#exemple : "1"*5 = "11111"
#          "ab"*3 = "ababab"

def case_1(): # si le parametre = 1, alors on imprime l'etoile dirrectement, la parametrisation des espaces dans le triangle si on commence par 1 est problematic
    print("   *")
    print("*** ***")
    print(" *   *")
    print("*** ***")
    print("   *")
    
def case():
    listp=[] # Déclaration d'un tableau/ liste ou stocker des variables listp.append(a) ajoute le contenu de a dans la liste
    
    listp.append(" "*(5+(para-2)*3)+"*") # pointe haute de l'étoile

    for i in list(range(para-1)):
        listp.append((4+3*(para-2)-i)*" "+"*"+(1+2*i)*" "+"*") # ajoute le triangle sans pointe, chaque itération ajoute l'espace avant la première *, l'espace entre les 2 *, et le deuxième *, à la fin on aura un triangle
    listp.append("*"*(para*2+1)+" "*((para-2)*2+1)+"*"*(para*2+1)) # ajoute la ligne avec les * 

    for i in list(range(para-1)):
        listp.append(" "*(i+1)+"*"+(1+(para-1)*6-(i)*2)*" "+"*") # ajoute le deuxième triangle avec l'espace décroissant
    listp.append(" "*para+"*"+" "*((para-1)*4+1)+"*")


    for p in list(range(len(listp))):
        print(listp[p]) # affichage de la premère partie de l'étoile


    for p in list(range(len(listp)-2,-1,-1)):
        print(listp[p])    # affichage de la deuxième partie qui est juste la première partie dans l'ordre inverse (effect de symetries) 
    
    
para=int(sys.argv[1])

# si le parametre = 1, alors on imprime l'etoile dirrectement, la parametrisation des espaces dans le triangle si on commence par 1 est problematic
if para==0:
    pass
elif para== 1:
    case_1()              
else:
    case()

