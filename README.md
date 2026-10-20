# -- CONFIGURATION --

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# -- DÉMARRAGE --

git init # Initialise un nouveau dépôt
git clone <url> # Clone un dépôt existant

# -- WORKFLOW CLASSIQUE --

#Il faut faire ad . puis commit

git status # Vérifie l'état des fichiers
git add <file> # Ajoute un fichier spécifique à la zone de préparation
git add . # Ajoute tous les fichiers modifiés
git commit -m "Message" # Enregistre les modifications préparées
git commit -am "Message" # Ajoute et enregistre les fichiers modifiés suivis
git log #permet de voir l'historique des commit
git show #pareil que log mais avec plus d'info

# -- REDIGER UN COMMIT --

titre du commit

Description

#ensuite il faut faire echap puis :wq
#pour sortir de l'éditeur il faut faire echap puis :q!

# -- BRANCHES --

git branch # Liste les branches
git switch <branch> # Change de branche
git switch -c <new-branch> # Crée une branche et bascule dessus
git branch -d <branch> # Supprime une branche locale
git checkout -b <new-branch> # Crée une branche
git merge <branch> #fusionne <branch> avec la branche en cours d'utilisation

# -- SYNCHRONISATION (REMOTE) --

git push -u origin main # Envoie les commits de la branche main et crée le lien de suivi
git push -u origin <nom de branche> # Envoie les commits de la branche et crée le lien de suivi
git push # Envoie les commits (si lien déjà établi)
git pull # Télécharge et fusionne les nouveautés du serveur distant
git branch --unset-upstream # Supprime un lien de suivi distant obsolète

# -- ANNULATION --

git restore --staged <file> # Retire un fichier de la zone de préparation (avant d'avoir commit)
git restore <file> # Annule les modifications non commitées d'un fichier
