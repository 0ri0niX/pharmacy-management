"""
PharmaCie Manager - Système de gestion de pharmacie.
Point d'entrée principal du programme.
Cours : Programming I with Python | BIT | Mai 2026
"""

# ─── Imports ────────────────────────────────────────────────
import os
from datetime import datetime

from models.medicament import Medicament
from models.client import Client
from models.pharmacien import Pharmacien
from services.stock import (
    charger_stock, sauvegarder_stock,
    afficher_stock, afficher_alertes, rechercher_medicament
)
from services.vente import enregistrer_vente, afficher_historique

# ─── Constantes ─────────────────────────────────────────────
NOM_PHARMACIE: str = "PharmaCie BIT"
VERSION: str = "1.0"

# ─── Données initiales (objets créés au démarrage) ──────────
pharmacien_actif = Pharmacien("Ouedraogo", "Hamidou", "70000001", "PH-2026-001")
client_par_defaut = Client("Inconnu", "Client", "00000000", "inconnu@email.com")


# ─── Fonctions ──────────────────────────────────────────────

def afficher_menu() -> None:
    """Affiche le menu principal de l'application."""
    print("\n" + "=" * 45)
    print(f"     💊 {NOM_PHARMACIE} — v{VERSION}")
    print("=" * 45)
    print("  1. Afficher le stock")
    print("  2. Ajouter un médicament")
    print("  3. Effectuer une vente")
    print("  4. Voir l'historique des ventes")
    print("  5. Afficher les alertes")
    print("  6. Infos du pharmacien")
    print("  7. Quitter")
    print("=" * 45)


def ajouter_medicament(stock: list) -> None:
    """
    Demande les informations à l'utilisateur et ajoute un médicament au stock.

    Args:
        stock: La liste actuelle des médicaments.
    """
    print("\n➕ AJOUTER UN MÉDICAMENT")
    print("-" * 30)

    nom = input("  Nom du médicament     : ").strip()

    # Vérifier si le médicament existe déjà
    if rechercher_medicament(stock, nom):
        print(f"❌ '{nom}' existe déjà dans le stock.")
        return

    try:
        prix = float(input("  Prix unitaire (FCFA)  : "))
        quantite = int(input("  Quantité en stock     : "))
        date_exp = input("  Date expiration (JJ/MM/AAAA) : ").strip()

        # Afficher les catégories disponibles
        print(f"  Catégories disponibles : {Medicament.CATEGORIES}")
        categorie = input("  Catégorie             : ").strip()

        # Créer l'objet et l'ajouter à la liste
        nouveau_med = Medicament(nom, prix, quantite, date_exp, categorie)
        stock.append(nouveau_med)
        sauvegarder_stock(stock)

        print(f"\n✅ '{nom}' ajouté au stock avec succès !")

    except ValueError:
        print("❌ Erreur : veuillez entrer des valeurs valides.")


def effectuer_vente(stock: list) -> None:
    """
    Gère le processus complet d'une vente.

    Args:
        stock: La liste des médicaments disponibles.
    """
    print("\n💰 EFFECTUER UNE VENTE")
    print("-" * 30)

    # Récupérer les infos du client
    prenom_client = input("  Prénom du client  : ").strip()
    nom_client = input("  Nom du client     : ").strip()
    tel_client = input("  Téléphone         : ").strip()
    email_client = input("  Email             : ").strip()

    # Créer un objet Client
    client = Client(nom_client, prenom_client, tel_client, email_client)

    # Chercher le médicament
    nom_med = input("  Médicament voulu  : ").strip()
    medicament = rechercher_medicament(stock, nom_med)

    if not medicament:
        print(f"❌ Médicament '{nom_med}' introuvable dans le stock.")
        return

    if medicament.est_expire():
        print(f"❌ Ce médicament est expiré. Vente impossible.")
        return

    try:
        quantite = int(input(f"  Quantité (disponible : {medicament.get_quantite()}) : "))
    except ValueError:
        print("❌ Quantité invalide.")
        return

    # Enregistrer la vente
    succes = enregistrer_vente(medicament, client, pharmacien_actif, quantite)

    if succes:
        sauvegarder_stock(stock)  # Mettre à jour le fichier CSV


def main() -> None:
    """
    Fonction principale : charge les données et lance la boucle du menu.
    """
    # Créer les dossiers si nécessaire
    os.makedirs("data", exist_ok=True)

    # Charger le stock depuis le fichier CSV
    stock: list = charger_stock()

    print(f"\n🟢 Bienvenue dans {NOM_PHARMACIE}")
    print(f"   Pharmacien connecté : {pharmacien_actif}")
    print(f"   Date : {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    # ─── Boucle principale (while loop) ─────────────────────
    continuer: bool = True

    while continuer:
        afficher_menu()
        choix: str = input("  Votre choix : ").strip()

        if choix == "1":
            afficher_stock(stock)

        elif choix == "2":
            ajouter_medicament(stock)

        elif choix == "3":
            effectuer_vente(stock)

        elif choix == "4":
            afficher_historique()

        elif choix == "5":
            afficher_alertes(stock)

        elif choix == "6":
            pharmacien_actif.afficher_infos()

        elif choix == "7":
            print("\n👋 Au revoir ! Bonne journée.")
            continuer = False

        else:
            print("❌ Choix invalide. Entrez un chiffre entre 1 et 7.")


# ─── Lancement ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
