from pathlib import Path

a = input("Entrer le nom du dossier : ")

try:
    Path(a).mkdir(parents=True, exist_ok=False)
    print(f"Le dossier '{a}' a été créé avec succès.")
except FileExistsError:
    print(f"Erreur : le dossier '{a}' existe déjà.")
