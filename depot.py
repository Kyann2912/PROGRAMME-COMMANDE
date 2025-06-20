import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Échec de la commande : {command}")
        exit(1)

def main():
    print("Déploiement Git Automatisé")

    branch = input("Nom de la branche à créer/pousser (ex: back) : ").strip()
    remote_url = input(" Lien du dépôt GitHub (ex: https://github.com/...) : ").strip()

    print("\nInitialisation du dépôt Git...")
    run_command("git init")

    print("Ajout des fichiers...")
    run_command("git add .")

    print("Commit des fichiers...")
    run_command(f'git commit -m "Initial commit on {branch} branch"')

    print(f"Création/bascule sur la branche '{branch}'...")
    run_command(f"git checkout -b {branch}")

    print("Ajout du dépôt distant...")
    run_command(f"git remote add origin {remote_url}")

    print(f"Poussée de la branche '{branch}' vers GitHub...")
    run_command(f"git push -u origin {branch}")

    print("Déploiement terminé avec succès !")

if __name__ == "__main__":
    main()
