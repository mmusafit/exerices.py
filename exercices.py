
#def split(nombre):
    #mots = nombre.split(",")
    #somme=len(nombre)
    #print(somme)
    #print(mots)
    #return nombre
    
#def split(phrase):
    #mots=phrase.split()
    #somme=len(phrase)
    #print(somme)
    #print(mots)
    #return phrase
    
#def split(prenom):
    #mots=prenom.split()
    #print(mots)
    #return mots
def join(nombres):
    séparateur = '-'
    chaine_concaténée = séparateur.join(nombres)
    print(chaine_concaténée) 
    return chaine_concaténée
   
#test de la fonction split
#liste=input("saisir une liste de nombres séparés par de virgule")
#nombre="ciao virginia come stai"
#print(split(nombre))
#liste=input("saisir une liste de phrase  séparés par des espace")
#phrase="Le Python est un langage de programmation"
#print(split(phrase))
#liste=input("saisir une liste de prenom  séparés un par  un")
#prenom="Alice,Bob,Charlie,David"
#print(split(prenom))
#test de la fonction
liste=input("ecrivez le nombres que vous vouliez separe")
nombres = ['1', '2', '3', '4', '5']
print(join(nombres))



