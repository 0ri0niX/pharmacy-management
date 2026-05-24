"""
Module contenant la classe Pharmacien, qui hérite de Personne.
"""

from models.personne import Personne


class Pharmacien(Personne):
    """
    Représente un pharmacien employé de la pharmacie.
    Hérite de Personne et ajoute un matricule et des droits d'accès.
    Démontre : Héritage, Polymorphisme.
    """

    def __init__(self, nom: str, prenom: str, telephone: str, matricule: str) -> None:
        """
        Initialise un pharmacien.

        Args:
            nom: Nom de famille du pharmacien.
            prenom: Prénom du pharmacien.
            telephone: Numéro de téléphone.
            matricule: Identifiant unique du pharmacien.
        """
        super().__init__(nom, prenom, telephone)  # Appel du constructeur parent
        self.__matricule: str = matricule  # Encapsulation : attribut privé
        self.ventes_effectuees: int = 0   # Compteur de ventes

    def get_matricule(self) -> str:
        """Retourne le matricule du pharmacien."""
        return self.__matricule

    def enregistrer_vente(self) -> None:
        """Incrémente le compteur de ventes du pharmacien."""
        self.ventes_effectuees += 1

    def afficher_infos(self) -> None:
        """
        Affiche les infos du pharmacien. (Polymorphisme)
        Surcharge la méthode de la classe Personne.
        """
        print(f"\n👨‍⚕️ PHARMACIEN")
        print(f"  Nom        : {self.prenom} {self.nom}")
        print(f"  Tél        : {self.get_telephone()}")
        print(f"  Matricule  : {self.__matricule}")
        print(f"  Ventes     : {self.ventes_effectuees}")

    def __str__(self) -> str:
        """Représentation textuelle du pharmacien."""
        return f"Pharmacien : {self.prenom} {self.nom} ({self.__matricule})"
