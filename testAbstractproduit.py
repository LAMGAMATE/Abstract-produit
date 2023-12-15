from Abstract_produit import ProduitElementaire, ProduitCompose, Composition

p1 = ProduitElementaire("Produit 1", "P1", 10)
p2 = ProduitElementaire("Produit 2", "P2", 15)


print(p1)
print(p2)


print("Prix HT Produit 1:", p1.getPrixHT())
print("Prix HT Produit 2:", p2.getPrixHT())

