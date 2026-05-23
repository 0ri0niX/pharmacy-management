"""
Module contenant la classe Medicament.
"""

from datetime import datetime


class Medicament:
    """
    Représente un médicament dans le stock de la pharmacie.
    Encapsule les données et fournit des méthodes de gestion du stock.
    """

    # Tuple utile : catégories autorisées (données fixes)
    CATEGORIES: tuple = ("Antibiotique", "Antidouleur", "Antipaludéen", "Vitamine", "Autre")

    def __init__(self, nom: str, prix: float, quantite: int,
                 date_expiration: str, categorie: str = "Autre") -> None:
        """
        Initialise un médicament.

        Args:
            nom: Nom du médicament.
            prix: Prix unitaire en FCFA.
            quantite: Quantité en stock.
            date_expiration: Date d'expiration au format JJ/MM/AAAA.
            categorie: Catégorie du médicament.
        """
        self.nom: str = nom
        self.__prix: float = prix              # Encapsulation
        self.__quantite: int = quantite        # Encapsulation
        self.date_expiration: str = date_expiration
        self.categorie: str = categorie if categorie in self.CATEGORIES else "Autre"

    def get_prix(self) -> float:
        """Retourne le prix du médicament."""
        return self.__prix

    def get_quantite(self) -> int:
        """Retourne la quantité en stock."""
        return self.__quantite

    def reduire_stock(self, quantite: int) -> bool:
        """
        Réduit le stock après une vente.

        Args:
            quantite: Quantité vendue.

        Returns:
            True si la réduction est possible, False sinon.
        """
        if quantite <= self.__quantite:
            self.__quantite -= quantite
            return True
        return False

    def augmenter_stock(self, quantite: int) -> None:
        """
        Augmente le stock lors d'un réapprovisionnement.

        Args:
            quantite: Quantité ajoutée.
        """
        self.__quantite += quantite

    def est_expire(self) -> bool:
        """
        Vérifie si le médicament est expiré.

        Returns:
            True si expiré, False sinon.
        """
        try:
            date_exp = datetime.strptime(self.date_expiration, "%d/%m/%Y")
            return datetime.now() > date_exp
        except ValueError:
            return False

    def stock_bas(self) -> bool:
        """Retourne True si le stock est inférieur à 5 unités."""
        return self.__quantite < 5

    def afficher(self) -> None:
        """Affiche les informations complètes du médicament."""
        statut_exp = "⚠️ EXPIRÉ" if self.est_expire() else "✅ Valide"
        statut_stock = "🔴 Stock bas" if self.stock_bas() else "🟢 En stock"

        print(f"\n  💊 {self.nom}")
        print(f"     Catégorie   : {self.categorie}")
        print(f"     Prix        : {self.__prix} FCFA")
        print(f"     Quantité    : {self.__quantite} unité(s) — {statut_stock}")
        print(f"     Expiration  : {self.date_expiration} — {statut_exp}")

    def vers_csv(self) -> str:
        """
        Convertit le médicament en ligne CSV pour sauvegarde.

        Returns:
            Chaîne formatée pour le fichier CSV.
        """
        return f"{self.nom},{self.__prix},{self.__quantite},{self.date_expiration},{self.categorie}"

    def __str__(self) -> str:
        """Représentation textuelle du médicament."""
        return f"{self.nom} ({self.__quantite} unités - {self.__prix} FCFA)"
