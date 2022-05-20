# TP_Ransomware
A great simulation of a bad thing...


Le virus dans le dépot est innofensif, et a été créé pour simuler l'utilisation d'un ransomware et d'en voir toutes les étapes.

Le code est commenté pour comprendre son utilisation.

Pour que le virus fonctionne, il faut déposer le "dossier_mega_important" sur le burreau, et executer ce virus depuis les téléchargements.


CE QU'IL RESTE A FAIRE :

But de l'installation du TP :
L'idéal serait que le TP soit divisé par îlots. Sur chaque îlot, il y aurait une machine kali-linux pour pouvoir effectuer l'attaque par dictionnaire via l'outil hydra.
En plus de cette machine, chaque élève en aura une depuis laquelle il pourra envoyer des mails, infectés ou non, et depuis laquelle il pourra recevoir des mails des victimes infectées. De plus, chacune de ces machines devra pouvoir observer les trames SMTP, via Wireshark, des mails envoyés automatiquement vers l'attaquant.
Chacun des équipements sera un machine virtuelle qui devra avoir un serveur ssh pour la connexion à distance.

 - Ne fonctionne que sur Windows (il faudrait adapter le virus pour les OS Linux si possible)
 - Setup de la ferme :
        - Serveur mail à installer sur la ferme de serveurs (pour des raisons de sécurité ne pas utiliser Outlook)
        - Serveurs ssh sur chaque machine pour l'attaque par dictionnaire (avec Cygwin par exemple)
        - Une machine kali pour l'attaque par dictionnaire
 - Créer un dictionnaire de mots de passe en fonction des machine virtuelles que vous aurez créées (avec des mauvais et le bon parmi eux)
 - Etablir une liste des bonnes pratiques pour éviter ce type d'attaque ou l'inclure dans le TP
        
