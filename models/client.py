"""
Module contenant la classe Client, qui hérite de Personne.
"""

from models.personne import Personne


class Client(Personne):
    """
    Représente un client de la pharmacie.
    Hérite de Personne et ajoute un historique d'achats.
    Démontre : Héritage, Polymorphisme.
    """

    def __init__(self, nom: str, prenom: str, telephone: str, email: str) -> None:
        """
        Initialise un client.

        Args:
            nom: Nom de famille du client.
            prenom: Prénom du client.
            telephone: Numéro de téléphone.
            email: Adresse email du client.
        """
        super().__init__(nom, prenom, telephone)  # Appel du constructeur parent
        self.email: str = email
        self.historique: list = []  # Liste utile : historique des achats

    def ajouter_achat(self, achat: dict) -> None:
        """
        Ajoute un achat à l'historique du client.

        Args:
            achat: Dictionnaire contenant les infos de l'achat.
        """
        self.historique.append(achat)

    def afficher_historique(self) -> None:
        """Affiche l'historique complet des achats du client."""
        if not self.historique:
            print("Aucun achat enregistré.")
            return

        print(f"\n📋 Historique de {self.prenom} {self.nom} :")
        for i, achat in enumerate(self.historique, 1):
            print(f"  {i}. {achat['medicament']} - {achat['quantite']} unité(s) - {achat['date']}")

    def afficher_infos(self) -> None:
        """
        Affiche les infos du client. (Polymorphisme)
        Surcharge la méthode de la classe Personne.
        """
        print(f"\n👤 CLIENT")
        print(f"  Nom     : {self.prenom} {self.nom}")
        print(f"  Tél     : {self.get_telephone()}")
        print(f"  Email   : {self.email}")
        print(f"  Achats  : {len(self.historique)} commande(s)")

    def __str__(self) -> str:
        """Représentation textuelle du client."""
        return f"Client : {self.prenom} {self.nom}"
