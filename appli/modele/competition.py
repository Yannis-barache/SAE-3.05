"""
Module contenant la classe Competition
"""

import math
import constantes as const
from categorie import Categorie
from arme import Arme
from lieu import Lieu
from escrimeur import Escrimeur
from exceptions import PasAssezDArbitres
from poule import Poule
from phase_final import PhaseFinal
from club import Club
from piste import Piste
from datetime import date, datetime


class Competition:
    """
    Classe Competition
    """

    def __init__(self, id_comp: int, nom: str, date_comp: str,
                 date_fin_inscription: str, saison: str, lieu: Lieu,
                 arme: Arme, categorie: Categorie, coefficient: float):
        """
        Constructeur de la classe Competition

        Args :
            id_comp (int) : L'id de la competition
            nom (str) : Le nom de la competition
            date (str) : La date de la competition
            date_fin_inscription (str) : La date de fin d'inscription de la competition
            saison (str) : La saison de la competition
            lieu (Lieu) : Le lieu de la competition
            arme (Arme) : L'arme de la competition
            categorie (Categorie) : La catégorie de la competition
        """
        self.__id = id_comp
        self.__nom = nom
        self.__date = date_comp
        self.__date_fin_inscription = date_fin_inscription
        self.__saison = saison
        self.__lieu = lieu
        self.__arme = arme
        self.__categorie = categorie
        self.__coefficient = coefficient
        self.__phase_final: PhaseFinal | None  = None

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la competition

        Returns :
            int : id de la competition
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de la competition

        Returns :
            str : nom de la competition
        """
        return self.__nom

    def get_date(self) -> str:
        """
        Fonction qui retourne la date de la competition

        Returns :
            str : date de la competition
        """
        return self.__date

    def get_date_fin_inscription(self) -> str:
        """
        Fonction qui retourne la date de fin d'inscription de la competition
        
        Returns :
            str : date de fin d'inscription de la competition
        """
        return self.__date_fin_inscription

    def get_saison(self) -> str:
        """
        Fonction qui retourne la saison de la competition

        Returns :
            str : La saison de la competition
        """
        return self.__saison

    def get_lieu(self) -> Lieu:
        """
        Fonction qui retourne le lieu de la competition

        Returns :
            Lieu : Le lieu de la competition
        """
        return self.__lieu

    def get_arme(self) -> Arme:
        """
        Fonction qui retourne l'arme de la competition

        Returns :
            Arme : L'arme de la competition
        """
        return self.__arme

    def get_categorie(self) -> Categorie:
        """
        Fonction qui retourne la catégorie de la competition

        Returns :
            Categorie : La catégorie de la competition
        """
        return self.__categorie

    def get_coefficient(self) -> float:
        """
        Fonction qui retourne le coefficient de la competition

        Returns :
            float : Le coefficient de la competition
        """
        return self.__coefficient

    def est_finis(self) -> bool:
        """
        Fonction qui retourne si la competition est finis ou non

        Returns :
            bool : True si la competition est finis, False sinon
        """
        return self.__phase_final is not None and self.__phase_final.est_finis(
        )

    def get_etat(self) -> str:
        """
        Fonction qui retourne l'etat de la competition

        Returns :
            str : L'etat de la competition
        """
        if self.__date_fin_inscription is None:
            return "Pas disponible"
        if isinstance(self.__date, date):
            self.__date = self.__date.strftime("%d-%m-%Y")
        if isinstance(self.__date_fin_inscription, date):
            self.__date_fin_inscription = self.__date_fin_inscription.strftime(
                "%d-%m-%Y")
        if self.est_finis():
            return "Terminée"
        elif datetime.strptime(self.__date, "%d-%m-%Y").date() <= date.today():
            return "En cours"
        elif datetime.strptime(self.__date_fin_inscription,
                               "%d-%m-%Y").date() > date.today():
            return "Inscription ouverte"
        else:
            return "À venir"

    def set_id(self, id_comp: int) -> None:
        """
        Fonction qui modifie l'id de la competition

        Args :
            id_comp (int): id de la competition
        """
        self.__id = id_comp

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de la competition

        Args :
            nom (str) : nom de la competition
        """
        self.__nom = nom

    def set_date(self, date_comp: str) -> None:
        """
        Fonction qui modifie la date de la competition

        Args :
            date (str) : date de la competition
        """
        self.__date = date_comp

    def set_date_fin_inscription(self, date_fin_inscription: str) -> None:
        """
        Fonction qui modifie la date de fin d'inscription de la competition

        Args :
            date_fin_inscription (str) : date de fin d'inscription de la competition
        """
        self.__date_fin_inscription = date_fin_inscription

    def set_saison(self, saison: str) -> None:
        """
        Fonction qui modifie la saison de la competition

        Args :
            saison (str) : saison de la competition
        """
        self.__saison = saison

    def set_lieu(self, lieu: Lieu) -> None:
        """
        Fonction qui modifie le lieu de la competition

        Args :
            lieu (Lieu) : lieu de la competition
        """
        self.__lieu = lieu

    def set_arme(self, arme: Arme) -> None:
        """
        Fonction qui modifie l'arme de la competition

        Args :
            arme (Arme) : arme de la competition
        """
        self.__arme = arme

    def set_categorie(self, categorie: Categorie) -> None:
        """
        Fonction qui modifie la catégorie de la competition

        Args :
            categorie (Categorie) : catégorie de la competition
        """
        self.__categorie = categorie

    def set_coefficient(self, coefficient: float) -> None:
        """
        Fonction qui modifie le coefficient de la competition

        Args :
            coefficient (float) : coefficient de la competition
        """
        self.__coefficient = coefficient

    def set_phase_final(self, phase_final: PhaseFinal) -> None:
        """
        Fonction qui modifie la phase finale de la competition

        Args:
            phase_final (PhaseFinal): phase finale de la competition
        Args :
            phase_final (PhaseFinal) : phase finale de la competition
        """
        self.__phase_final = phase_final

    @staticmethod
    def generation_poule(
        liste_escrimeur: list[Escrimeur], liste_arbitre: list[Escrimeur]
    ) -> dict[Poule, tuple[Escrimeur, list[Escrimeur]]] | None :
        """
        Fonction qui genere les poules de la competition

        Args :
            liste_escrimeur (list) : liste des escrimeurs de la competition
            liste_arbitre (list) : liste des arbitres de la competition
        
        Returns :
            dict[int, tuple[Escrimeur, list[Escrimeur]]] :
                dictionnaire contenant les poules de la competition
            La clé est le numéro de la poule et la valeur est un tuple 
            contenant l'arbitre de la poule et la liste des escrimeurs de la poule
        """
        try:
            liste_escrimeur = Competition.trie_classement_initial(
                liste_escrimeur)
            nombre_poule = Competition.nombre_poule(len(liste_escrimeur),
                                                    len(liste_arbitre))[0]
            poule_int: dict[int, tuple[Escrimeur, list[Escrimeur]]] = {}

            # On initialise les poules avec les arbitres
            for i in range(nombre_poule):
                poule_int[i] = (liste_arbitre[i], [])

            # On ajoute les escrimeurs dans les poules
            for i in range(len(liste_escrimeur)):
                poule_int[i % nombre_poule][1].append(liste_escrimeur[i])

            # On transforme les poules en poules de type Poule
            poule: dict[Poule, tuple[Escrimeur, list[Escrimeur]]] = {}
            for i in range(nombre_poule):
                poule[Poule(-1)] = poule_int[i]
            return poule
        except PasAssezDArbitres:
            print("Pas assez d'arbitres pour couvrir chaque poule.")
            return None

    @staticmethod
    def trie_classement_initial(liste_escrimeur: list[Escrimeur]):
        """
        Fonction qui trie les escrimeurs par classement initial

        Args :
            liste_escrimeur (list[Escrimeur]) : liste des escrimeurs de la competition

        Returns :
            list[Escrimeur] : liste des escrimeurs de la competition triée par classement initial
        """
        return sorted(liste_escrimeur,
                      key=lambda escrimeur:
                      (escrimeur.get_classement() is not None,
                       escrimeur.get_classement()))

    @staticmethod
    def nombre_poule(nombre_escrimeur: int,
                     nombre_arbitre: int) -> tuple[int, int]:
        """
        Fonction qui retourne le nombre de poules et le nombre d'escrimeurs par poule

        Args :
            nombre_escrimeur (int) : nombre d'escrimeurs de la competition
            nombre_arbitre (int) : nombre d'arbitres de la competition

        Returns :
            tuple[int, int] : Le nombre de poules et le nombre d'escrimeurs par poule
        """
        min_arbitres_necessaires = math.ceil(
            nombre_escrimeur / const.NOMBRE_MAXIMAL_ESCRIMEUR_POULE)
        if nombre_arbitre < min_arbitres_necessaires:
            raise PasAssezDArbitres(
                "Pas assez d'arbitres pour couvrir chaque poule.")
        nombre_poule = math.ceil(nombre_escrimeur /
                                 const.NOMBRE_MAXIMAL_ESCRIMEUR_POULE)
        nombre_escrimeur_par_poule = math.ceil(nombre_escrimeur / nombre_poule)
        return nombre_poule, nombre_escrimeur_par_poule

    @staticmethod
    def etablir_classement_provisoire(
            les_poules: list[Poule]) -> list[Escrimeur]:
        """
        Fonction qui établit le classement provisoire de la competition apres les poules

        Args :
            les_poules (list[Poule]) : La liste des poules de la competition

        Returns :
            list[Escrimeur] : Le classement provisoire de la competition
        """
        infos = {}
        for poule in les_poules:
            for escrimeur in poule.get_les_escrimeurs():
                indice_escrimeur = poule.get_nb_victoires(escrimeur) / (
                    poule.get_nb_escrimeurs() - 1)
                infos[escrimeur] = (indice_escrimeur,
                                    poule.get_nb_touche_marquee(escrimeur),
                                    poule.get_nb_touche_prise(escrimeur))
        classement_provisoire = sorted(
            infos.keys(),
            key=lambda escrimeur:
            (infos[escrimeur][0], infos[escrimeur][1], infos[escrimeur][2]),
            reverse=True)
        return classement_provisoire

    @staticmethod
    def get_puissance_sup(nb_escrimeur: int) -> int:
        """
        Fonction qui retourne la puissance de 2 supérieurs au nombre d'escrimeurs passé en paramètre.

        Args :
            nb_escrimeur (int) : Le nombre d'escrimeurs de la competition

        Returns :
            int : La puissance de 2 supérieurs au nombre d'escrimeurs passé en paramètre
        """
        puissance = 0
        while 2**puissance < nb_escrimeur:
            puissance += 1
        return puissance

    @staticmethod
    def generer_phase_finale(
            les_poules: list[Poule], les_arbitres: list[Escrimeur],
            heure_debut: float,
            liste_pistes: list[Piste]) -> tuple[PhaseFinal, list]:
        """
        Fonction qui genere la phase finale de la competition

        Args :
            les_poules (list[Poule]) : La liste des poules de la competition
            les_arbitres (list[Escrimeur]) : La liste des arbitres de la competition
            heure_debut (float) : L'heure de debut de la competition

        Returns :
            PhaseFinal : La phase finale de la competition
            list[Match] : La liste des matchs de la phase finale de la competition
        """
        club_none = Club(1, "None", "None", "None")
        categorie_none = Categorie(1, "None")
        escrimeur_none = Escrimeur(308, "None", "None", "None", "None", "None",
                                   "None", "None", 0, club_none,
                                   categorie_none, False)

        classement_provisoire = Competition.etablir_classement_provisoire(
            les_poules)
        puissance = Competition.get_puissance_sup(len(classement_provisoire))
        liste_escrimeur: list[Escrimeur] = []
        for escrimeur in classement_provisoire:
            liste_escrimeur.append(escrimeur)
        while len(liste_escrimeur) < 2**puissance:
            liste_escrimeur.append(escrimeur_none)
        phase_finale = PhaseFinal(-1)
        phase_finale.set_les_pistes(liste_pistes)
        les_matchs = phase_finale.generer_les_matchs(liste_escrimeur,
                                                     les_arbitres, heure_debut)
        return phase_finale, les_matchs

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la competition

        Returns :
            str : informations de la competition
        """
        return f"Competition : {self.__id}, {self.__nom}, {self.__date}, " \
            f"{self.__date_fin_inscription}, {self.__saison}, {self.__lieu}, " \
            f"{self.__arme}, {self.__categorie} |"
