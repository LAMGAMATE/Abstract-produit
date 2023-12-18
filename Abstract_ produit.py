from abc import ABC, abstractmethod

class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code
    
    @property
    def nom(self):
        return self.__nom
    
    def setnom(self,newName):
        self.__nom = newName
    @property
    def getcode(self):
        return self.__code
    
    def setcode(self,newCode):
        self.__code = newCode
    
    @abstractmethod
    def getPrixHT(self):
        pass
    @abstractmethod
    def __eq__(self,produit):
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

    def __str__(self):
        return f'Produit Name :{self.__produit}\nQuantité : {self.__quantite}'

class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        Produit().__init__(nom, code)
        self.__prixAchat = prixAchat
    
    @property
    def getPrixAchat(self):
        return self.__prixAchat
    
    
    def setPrixAchat(self,newPrixAchat):
        self.__prixAchat = newPrixAchat
    

    def __str__(self):
      return f"Produit Élémentaire: {self.nom}\n Code: {self.code}\n Prix d'Achat: {self.__prixAchat}"
    
    @property

    def getPrixHT(self):
        return self.__prixAchat
    

    def __eq__(self,elementaire):
        if self.__prixAchat == elementaire.__prixAchat and self.__nom == elementaire.__nom :
            return True
        else : 
            return False
    
class ProduitCompose(Produit):
    TVA = 0.18
    def __init__(self, nom, code, fraisFabrication,listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants
    


    @property
    def getfraisFabrication(self):
        return self.__fraisFabrication
    


    def setFraisFabrication(self,newFabrication):
        self.__fraisFabrication = newFabrication
    


    @property
    def getlisteConstituants(self):
        return self.__listeConstituants
    


    def setListeConstituants(self,newListeConstituant):
        self.__listeConstituants = newListeConstituant



    
    def __str__(self):
        return f"Produit Composé: {self.nom}, Code: {self.getcode}, Frais de Fabrication: {self.getfraisFabrication}"



    def getPrixHT(self):
        prix_total_constituants = sum(composant.produit.getPrixHT() * composant.quantite for composant in self.__listeConstituants)
        return prix_total_constituants + self.__fraisFabrication
    


    def __eq__(self,other):
        if self.__nom == other.__nom and self.__produit == other.__produit :
            return True
