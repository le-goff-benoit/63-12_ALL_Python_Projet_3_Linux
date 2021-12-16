# 63-12_ALL_Projet 3: Récolte et nettoyage de données automatisées (LINUX)

## Utilisation

```bash
python3 script/main.py
```

## Consigne

### Description

Le script doit s’activer automatiquement lorsque l’un des fichier de test (valide ou non-valide) se trouve sur le FTP.

Dans un premier temps, le script doit vérifier que le fichier reçu contient toutes les colonnes du fichier de test valide. Si ce n’est pas le cas, le script Python annule le processus, place le fichier dans un dossier spécifique du FTP et avertit l’utilisateur par email.

Dans un second temps si le fichier est valide, le script vérifie que les données (les lignes) contenues dans le fichier test (valide) sont corrects. Certaines lignes du fichier de test (valide) vont avoir des erreurs (un string à la place d’un double, des données manquantes, etc…).

Additionner les colonnes identiques nommé : « Daysum » sur chaque ligne pour n’en faire plus qu’une par ligne avec la somme de tous les « Daysum » qui s’appellera « DaysumTot »

* Le script doit, une fois le fichier récupéré, réaliser un nettoyage automatisé des lignes erronées (suppression de la ligne en question).

* Une fois le nettoyage réalisé, le script doit envoyer sur un second FTP le nouveau fichier nettoyé.

Un email de confirmation contenant le nombre de lignes effacées doit être envoyé à l’utilisateur en cas de succès de la procédure.

### Prérequis

Les groupes reçoivent, en début de projet, les éléments suivants :

* Les accès aux FTP (une semaine après la formation des groupes)
* Un fichier de test valide et non-valide contenant des données anonymisées (une semaine après la formation des groupes)

## Rendu

La documentation doit inclure les points importants du développement suivants :

* Explication de la mise en place de l’environnement
* Description des principales fonctions du code
* Visuel + explications du cheminement des fichiers csv (automatisation du processus visio ou autre)

Le script Python, remis comme code de preuve de la réalisation du projet doit :

* Avoir des commentaires expliquant les fonctions
* Etre au format standard de présentation/découpage/fonction du monde professionnel
* Pouvoir être exécuté par les correcteurs
  
## Participants

* Benoît Le Goff
* De Carvalho Tony
* Loureiro Christophe
* Hebert Patrick
* Grujicic Damjan

## Informations techniques

### FTP Input

* Hote : d73kw.ftp.infomaniak.com
* Username : d73kw_projet3_groupe1_i
* Password : 6zNr8c9TrHV4
* Repertoire cible : /Cours/Projet3/Groupe1/Input

### FTP Output

* Hote : d73kw.ftp.infomaniak.com
* Username : d73kw_projet3_groupe1_o
* Password : 84JN59cHQbvg
* Repertoire cible : /Cours/Projet3/Groupe1/Output
  
## Fichiers de tests

### Valide

./test/Projet3_Groupe1_FichierValide.csv

### Invalide

./test/Projet3_Groupe1_FichierNonValide.csv
