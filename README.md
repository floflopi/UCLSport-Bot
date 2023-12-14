## UCLSport AutoInscription

Ce programme permet d'automatiser l'inscription à une séance particulière sur le site [UCLSport](https://sites.uclouvain.be/uclsport) pour chaque semaine

## Comment le set up ?

Pour configurer le bot, suivez ces étapes :

1. **Télécharger le fichier zip contenant le programme en cliquant sur le bouton vert "<> Code" puis "Download Zip"**

2. **Ouvrez le Planificateur de tâches :**
   - Appuyez sur `Win + S` pour ouvrir la recherche Windows.
   - Tapez "Planificateur de tâches" et appuyez sur Entrée.

3. **Créez une nouvelle tâche :**
   - Dans le volet de gauche, sélectionnez "Bibliothèque du Planificateur de tâches".
   - Dans le volet de droite, cliquez avec le bouton droit de la souris et sélectionnez "Créer une tâche de base..."

4. **Configurez les propriétés de la tâche :**
   - Donnez un nom à la tâche dans l'onglet "Général".
   - Passez à l'onglet "Déclencheurs" et cliquez sur "Nouveau".
   - Choisissez "Quotidien" et configurez les détails selon vos besoins (heure, répétition quotidienne, etc.).

5. **Configurez l'action :**
   - Passez à l'onglet "Actions" et cliquez sur "Nouveau".
   - Choisissez "Démarrer un programme" comme action.
   - Parcourez et sélectionnez le programme automate_UCLsport.exe

6. **Configurez d'autres options si nécessaire :**
   - Passez en revue les autres onglets pour configurer d'autres paramètres, tels que les conditions, les paramètres, etc.

7. **Terminez la configuration :**
   - Cliquez sur "OK" pour créer la tâche.

Le bot essayera désormais chaque jour de s'inscrire à la séance suivante pour le jour configuré si vous n'êtes pas encore inscrit.Dans le cas contraire il ne fera rien.
## Questions/Remarques

### **Comment je sais si ton programme n'est pas un virus?**
Vous pouvez toujours lancer votre antivirus pour vous assurer que le programme ne hack pas votre pc.
Si vous pensez toujours que le programme est un virus,
automate_UCLsport.exe a été généré grâce à pyinstaller pour transformer un fichier .py en .exe. Vous pouvez alors inspecter directement le fichier .py et runnez vous-même la commande pour générer le fichier .exe: 
```bash
pyinstaller --onefile --hidden-import selenium --hidden-import cv2 --hidden-import os --hidden-import re --hidden-import time --hidden-import sys --hidden-import datetime --hidden-import ffpyplayer.player.MediaPlayer --distpath . automate_UCLsport.py
```

### **Comment je fais pour arrêter le bot de m'inscrire à une séance ?**
Si vous voulez changer d'heure/de séance il suffit de changer le fichier info.txt avec une autre heure/séance.
Si vous voulez arrêter le bot complètement, il suffit