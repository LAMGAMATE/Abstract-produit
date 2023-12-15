
from abc import ABC, abstractmethod

class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def code(self):
        return self.__code
    
    @abstractmethod
    def getPrixHT(self):
        pass

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def produit(self):
        return self.__produit
    
    @produit.setter
    def produit(self, value):
        self.__produit = value
    
    @property
    def quantite(self):
        return self.__quantite
    
    @quantite.setter
    def quantite(self, value):
        self.__quantite = value

class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat
    
    def __str__(self):
        return f"Produit Élémentaire: {self.nom}, Code: {self.code}, Prix d'Achat: {self.__prixAchat}"
    
    def getPrixHT(self):
        return self.__prixAchat

class ProduitCompose(Produit):
    tauxTVA = 0.18
    
    def __init__(self, nom, code, fraisFabrication, listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants
    
    @property
    def fraisFabrication(self):
        return self.__fraisFabrication
    
    @property
    def listeConstituants(self):
        return self.__listeConstituants
    
    def __str__(self):
        return f"Produit Composé: {self.nom}, Code: {self.code}, Frais de Fabrication: {self.__fraisFabrication}"
    
    def getPrixHT(self):
        prix_total_constituants = sum(composant.produit.getPrixHT() * composant.quantite for composant in self.__listeConstituants)
        return prix_total_constituants + self.__fraisFabrication
