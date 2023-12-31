class AllViewMenu:

    @staticmethod
    def main_menu():
        print("\n-----MENU PRINCIPAL-----")
        print("1) Menu Joueurs.")
        print("2) Menu Tournois.")
        print("3) Quitter le programme.")

    @staticmethod
    def player_menu():
        print("\n-----MENU JOUEUR-----")
        print("1) Renseigner un nouveau joueur.")
        print("2) Afficher la liste des joueurs.")
        print("3) Retour au Menu Principal.")

    @staticmethod
    def tournament_menu():
        print("\n-----MENU TOURNOI-----")
        print("1) Créer et initialiser un nouveau tournoi.")
        print("2) Visualiser les tournois en cours.")
        print("3) Finir et renseigner un round.")
        print("4) Retour au Menu Principal.")

    @staticmethod
    def in_tournament_menu():
        print("\n--Informations complémentaires--")
        print("1) Obtenir toutes les informations sur un tournoi.")
        print("2) Liste des participants par ordre alphabétique.")
        print("3) Liste de tous les tours du tournoi et de tous les matchs du tour.")
        print("4) Revenir au Menu Tournoi.")

    @staticmethod
    def input_error():
        print("Erreur de saisie!")

    @staticmethod
    def choise():
        return input("Votre choix: ")
