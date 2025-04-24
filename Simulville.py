import random
import os

class SimulVille:
    def __init__(self):
        self.population = 1000
        self.budget = 10000
        self.niveau_satisfaction = 50
        self.taux_emploi = 50
        self.revenus_mensuels = 0
        self.competences_habitants = 0

    def afficher_statistiques(self):
        print()
        print(f"Population : {self.population} habitants")
        print(f"Budget : {self.budget} euros")
        print(f"Niveau de satisfaction : {self.niveau_satisfaction}%")
        print(f"Taux d'emploi : {self.taux_emploi}%")
        print(f"Revenus mensuels : {self.revenus_mensuels} euros")
        print(f"Compétences des habitants : {self.competences_habitants}%")

    def investir_education(self):
        cout = 2000
        if self.budget >= cout:
            self.budget -= cout
            self.competences_habitants += 10
            self.niveau_satisfaction += 5
            print("Investissement dans l'éducation réussi !")
        else:
            print("Pas assez d'argent pour investir dans l'éducation.")

    def investir_habitat(self):
        cout = 3000
        if self.budget >= cout:
            self.budget -= cout
            self.population += 500
            self.niveau_satisfaction += 10
            print("Investissement dans les habitats réussi !")
        else:
            print("Pas assez d'argent pour investir dans les infrastructures.")

    def organiser_evenement(self):
        cout = 1000
        if self.budget >= cout:
            self.budget -= cout
            self.niveau_satisfaction += 10
            self.revenus_mensuels += 500
            print("Événement organisé avec succès !")
        else:
            print("Pas assez d'argent pour organiser un événement.")

    def augmenter_impots(self):
        gain = 1500
        self.budget += gain
        self.niveau_satisfaction -= 5
        print("Impôts augmentés avec succès !")
    
    def diminuer_impots(self):
        cout = 2000
        if cout >= self.budget:
            self.budget - cout
            self.niveau_satisfaction += 3
            print("Impôts diminués avec succès !")

    def choix_action(self):
        liste = ["ie", "ih", "oe", "ai", "di"]
        c1 = random.choice(liste)
        c2 = random.choice(liste)
        if c2 == c1:
            c2 = random.choice(liste)
        
        c3 = random.choice(liste)
        if c3 == c1 or c3 == c2:
            c3 = random.choice(liste)
        
        c4 = random.choice(liste)
        if c4 == c1 or c4 == c2 or c4 == c3:
            c4 = random.choice(liste)
        
        c5 = random.choice(liste)
        if c5 == c1 or c5 == c2 or c5 == c3 or c5 == c4:
            c5 = random.choice(liste)
        return c1, c2, c3, c4, c5
    def sauvegarder(self):
        loop = True
        print("! Avertissement ! le fichier de sauvergarde doit être dans le même dossier racine que celui de SimulVille.py")
        q = input("Voulez-vous enregistrer la partie Ou lancer une suavegarde(Oui enregistrer, Non lancer une sauvegarde) ?\n>>>")
        if q == "oui" or q == "Oui":
            while loop:
                q = input("Veuillez dire dans quelle répertoire mettre le fichier, il doit être dans le même dossier racine que celui de SimulVille.\nExemple: C:\X_utilisateur\X_nom_utilisateur\Desktop\SimulVille\n>>>")
                r = input("Voulez vous donner un nom spécial au fichier (par def: Sauvegarde_SimulVille) ?\n>>>")
                if r == "oui" or r == "Oui":
                    q = input("Nom du fichier : >>>")
                else:
                    q += "\Sauvegarde_SimulVille.txt"
                
                if not os.path.exists(q):
                    pass
                        
                else:
                    print("! Avertissement ! Un fichier de sauvegarde est présent dans ce dossiers")
                #Variable
                popu = self.population * 32 -self.population
                
                budget = self.budget*46-self.budget
                
                s_n = self.niveau_satisfaction*278-self.niveau_satisfaction
                
                t_e = self.taux_emploi*82-self.taux_emploi
                
                r_m = self.revenus_mensuels*17-self.revenus_mensuels
                
                c_h = self.competences_habitants*68-self.competences_habitants
                
                fichier = open("Sauvegarde_SimulVille.txt", "w+")
                fichier.write(f"{popu}")
                fichier.write("   ")
                fichier.write(f"{budget}")
                fichier.write("   ")
                fichier.write(f"{s_n}")
                fichier.write("   ")
                fichier.write(f"{t_e}")
                fichier.write("   ")
                fichier.write(f"{r_m}")
                fichier.write("   ")
                fichier.write(f"{c_h}")

                fichier.close()
                return "Sauvegarde effectuer"
        elif q == "non" or q == "Non":
            q = input("Veuillez dire dans quelle répertoire est le fichier, n'oubliez pas de mettre le nom du fichier a la fin du nom du repertoire\nExemple: C:\X_utilisateur\X_nom_utilisateur\Desktop\SimulVille\Sauvegarde_SimulVille.txt\n>>>")
            if not os.path.exists(q):
                print("Il n'y a pas de fichier de sauvegarde")
            else:
                
                with open('Sauvegarde_SimulVille.txt', 'r') as file:
                    liste_ligne = []
                    for ligne in file:
                        liste_ligne.append(ligne)
                        
                ligne = liste_ligne[0]
                ligne = ligne.split("   ")
                ligne1 = int(ligne[0])
                ligne2 = int(ligne[1])
                ligne3 = int(ligne[2])
                ligne4 = int(ligne[3])
                ligne5 = int(ligne[4])
                ligne6 = int(ligne[5])

                self.populations = ligne1 / 31
                self.budget = ligne2 / 46
                self.niveau_satisfaction = ligne3 / 278
                self.taux_emploi = ligne4 / 82
                self.revenus_mensuels = ligne5 / 17
                self.competences_habitants = ligne6 / 68
                    
                    

        else:
            return "Echec de la sauvegarde"

        
    def jouer(self):
        print("________________________________________________________________")
        print("Bienvenue dans : Simul Ville (V1)")
        print("\nTu es le maire et tu dois avoir au moins toute la satisfaction de tes habitants pour gagner")
        print("________________________________________________________________")
        self.afficher_statistiques()
        while True:
            print("____________________________________________________________")
            
            if self.budget < -1000:
                print("PERDU")
                break
            if self.niveau_satisfaction == 100 and self.budget > 0:
                print("Gagner !!!")
                break
            if self.budget < 0:
                print("ATTENTION tu dois augemter ton argent rapidement\nTu perderas si tu as moins de -1000€")

            print("\nMenu :")
            print("1. Organiser un événement (1000)")
            print("2. Investir dans l'éducation (2000)")
            print("3. Investir dans les logements (3000)")
            print("4. Diminuer les impôts (2000/m)")
            print("5. Augmenter les impôts (+1500)")
            print("6. Sauvegarder/lancer une sauvegarde")
            print("7. Quitter")

            choix = input("Entrez votre choix : ")


            if choix == "1":
                self.organiser_evenement()
                self.afficher_statistiques()
                revenus = self.competences_habitants/2
                self.budget * revenus/2.5
                
                
            elif choix == "2":
                self.investir_education()
                self.afficher_statistiques()
                revenus = self.competences_habitants/2
                self.budget * revenus/2.5
                
            elif choix == "3":
                self.investir_habitat()
                self.afficher_statistiques()
                revenus = self.competences_habitants/2
                self.budget * revenus/2.5
                
            elif choix == "4":
                self.organiser_evenement()
                self.afficher_statistiques()
                revenus = self.competences_habitants/2
                self.budget * revenus/2.5
                
                
            elif choix == "5":
                self.diminuer_impots()
                self.afficher_statistiques()
                revenus = self.competences_habitants/2
                self.budget * revenus/2.5
                
            elif choix == "6":
                print(self.sauvegarder())
                
            elif choix == "7":
                break
            else:
                print("Choix invalide. Veuillez essayer à nouveau.")
        
if __name__ == "__main__":
    jeu = SimulVille()

    jeu.jouer()
