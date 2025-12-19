#----1----
commandes = {
    "CMD001" : {
        "client" : "Ali" ,
        "Produits" : [("Clavier",250,1),("Souris",120,2)]
    },
    "CMD002" : {
        "client" : "Sara" , 
        "Produits" : [("Ecran",1800,1),("Calvier",250,1)]
    },
    "CMD003" : {
        "client" : "Ali" , 
        "Produits" : [("Souris",120,1),("Webcam",300,1)]
    },
    "CMD004" : {
        "client" : "Fahd" , 
        "Produits" : [("USB",40,3),("Webcam",300,2)]
    },
}

#afficher lescommandes sous la forme :
#CMD001 :ALi
#Clavier|250DH|1QQTE

for cmd , infos in commandes.items() :
    print(f"{cmd}:{infos["client"]}")
    for nom,prix,quantité in infos["Produits"] :
        print(f"{nom} | {prix} DH | {quantité} QQTE")
    print("\n")

#----2=3----et---4------
chifre_affaires = 0
for cmd , infos in commandes.items() :
    montant_total = 0
    for nom , prix , quantité in infos["Produits"] :
        montant_de_produit = prix * quantité
        montant_total += montant_de_produit
    print(f"Le montant total de la commande du client {infos["client"]} est : {montant_total}")
    print("\n")
    chifre_affaires += montant_total
print(f"Le chifre d'affaire est : {chifre_affaires}")   #---4--

#------5------
