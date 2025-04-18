# fichier : gestionnaire_de_comptes.py

class CompteClient:
    def __init__(self, identifiant, nom, solde=0.0):
        self.identifiant = identifiant
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"{montant}€ déposé sur le compte de {self.nom}. Nouveau solde : {self.solde}€")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"{montant}€ retiré du compte de {self.nom}. Nouveau solde : {self.solde}€")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def afficher_details(self):
        print(f"Compte #{self.identifiant} - Nom: {self.nom} - Solde: {self.solde}€")


class GestionnaireDeComptes:
    def __init__(self):
        self.comptes = {}

    def ajouter_compte(self, compte):
        self.comptes[compte.identifiant] = compte
        print(f"Compte de {compte.nom} ajouté.")

    def obtenir_compte(self, identifiant):
        return self.comptes.get(identifiant)

    def afficher_tous_les_comptes(self):
        for compte in self.comptes.values():
            compte.afficher_details()


# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireDeComptes()

    client1 = CompteClient(1, "Alice", 500)
    client2 = CompteClient(2, "Bob", 300)

    gestionnaire.ajouter_compte(client1)
    gestionnaire.ajouter_compte(client2)

    client1.deposer(150)
    client2.retirer(100)

    gestionnaire.afficher_tous_les_comptes()
