"""
Module contenant la classe PhaseFinal
"""

from equipe import Equipe
from match import Match
from escrimeur import Escrimeur
from piste import Piste
from club import Club
from categorie import Categorie
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape


class PhaseFinal:
    """
    La classe PhaseFinal
    """

    def __init__(self, id_phase_f: int):
        self.__id_phase_f = id_phase_f
        self.__les_matchs: list[Match] = []
        self.__les_pistes: list[Piste] = []
        self.__index_piste = 0
        self.__heure: float = 0.0

    def get_id_phase_f(self) -> int:
        """
        Fonction qui retourne l'id de la phase finale

        Returns:
            int: id de la phase finale
        """
        return self.__id_phase_f

    def get_les_matchs(self) -> list[Match]:
        """
        Fonction qui retourne la liste des matchs

        Returns:
            list: liste des matchs
        """
        return self.__les_matchs

    def get_les_pistes(self) -> list[Piste]:
        """
        Fonction qui retourne la liste des pistes

        Returns:
            list: liste des pistes
        """
        return self.__les_pistes

    def set_id_phase_f(self, id_phase_f: int) -> None:
        """
        Fonction qui modifie l'id de la phase finale

        Args:
            id_phase_f (int): id de la phase finale
        """
        self.__id_phase_f = id_phase_f

    def set_match(self, match: Match) -> None:
        """
        Fonction qui ajoute un match à la liste des matchs

        Args:
            match (Match): match
        """
        self.__les_matchs.append(match)

    def set_les_matchs(self, liste_matchs: list[Match]) -> None:
        """
        Fonction qui ajoute une liste de matchs à la liste des matchs

        Args:
            liste_matchs (list): liste des matchs
        """
        self.__les_matchs = liste_matchs

    def set_les_pistes(self, liste_pistes: list[Piste]) -> None:
        """
        Fonction qui ajoute une piste à la liste des pistes

        Args:
            piste (Piste): piste
        """
        self.__les_pistes = liste_pistes

    def generer_les_matchs(self, liste_escrimeurs: list[Escrimeur],
                           liste_arbitres: list[Escrimeur],
                           heure_debut: float) -> list[Match]:
        """
        Fonction qui génère les matchs de la phase finale

        Args:
            liste_escrimeurs (list): liste des escrimeurs
            liste_arbitres (list): liste des arbitres
            heure_debut (float): heure de début

        Returns:
            list: liste des matchs
        """
        self.__heure = heure_debut
        cpt = 0
        liste_matchs = []
        while cpt < len(liste_escrimeurs) / 2:
            escrimeur1 = liste_escrimeurs[cpt]
            escrimeur2 = liste_escrimeurs[-(cpt + 1)]
            arbitre = random.choice(liste_arbitres)
            if escrimeur1.get_nom() == 'None' or escrimeur2.get_nom(
            ) == 'None':
                liste_matchs.append(
                    Match(-1, self.__id_phase_f, escrimeur1, escrimeur2,
                          arbitre, heure_debut, True,
                          self.__les_pistes[self.__index_piste]))
            else:
                liste_matchs.append(
                    Match(-1, self.__id_phase_f, escrimeur1, escrimeur2,
                          arbitre, heure_debut, False,
                          self.__les_pistes[self.__index_piste]))
            self.__index_piste += 1
            if self.__index_piste == len(self.__les_pistes):
                self.__index_piste = 0
                self.__heure += 0.25
                if self.__heure % 1 >= 0.6:
                    self.__heure += 0.4
            cpt += 1
        self.__les_matchs = liste_matchs
        return liste_matchs

    def generer_les_matchs_equipe(self, liste_equipes: list[Equipe],
                                  liste_arbitres: list[Escrimeur],
                                  heure_debut: float) -> list[Match]:
        """
        Fonction qui génère les matchs de la phase finale pour les équipes

        Args:
            liste_equipes (list): liste des équipes
            liste_arbitres (list): liste des arbitres
            heure_debut (float): heure de début

        Returns:
            list: liste des matchs
        """
        self.__heure = heure_debut
        cpt = 0
        liste_matchs = []
        while cpt < len(liste_equipes) / 2:
            equipe1 = liste_equipes[cpt]
            equipe2 = liste_equipes[-(cpt + 1)]
            arbitre = random.choice(liste_arbitres)
            liste_matchs.append(
                Match(-1, self.__id_phase_f, equipe1, equipe2, arbitre,
                      heure_debut, False,
                      self.__les_pistes[self.__index_piste]))
            self.__index_piste += 1
            if self.__index_piste == len(self.__les_pistes):
                self.__index_piste = 0
                self.__heure += 0.25
                if self.__heure % 1 >= 0.6:
                    self.__heure += 0.4
            cpt += 1
        self.__les_matchs = liste_matchs
        return liste_matchs

    def est_finis(self) -> bool:
        """
        Fonction qui vérifie si la phase finale est finis

        Returns:
            bool: True si la phase finale est finis, False sinon
        """
        if len(self.__les_matchs) == 0:
            return False
        for match in self.__les_matchs:
            if not match.est_finis():
                return False
        return True

    def clear_matchs(self) -> None:
        """
        Fonction qui vide la liste des matchs
        """
        self.__les_matchs = []

    def tour_finnis(self) -> bool:
        """
        Fonction qui vérifie si le tour est finis

        Returns:
            bool: True si le tour est finis, False sinon
        """
        if len(self.__les_matchs) == 0:
            return False
        for match in self.__les_matchs:
            if not match.est_finis():
                return False
        return True

    def phase_finis(self) -> bool:
        """
        Fonction qui vérifie si la phase finale est finis

        Returns:
            bool: True si la phase finale est finis, False sinon
        """
        if len(self.__les_matchs) == 0:
            return False
        if len(self.__les_matchs) % 2 == 1:
            return True
        return False

    def generer_tour_suivant(self, liste_arbitres: list[Escrimeur],
                             heure_debut: float):
        """
        Méthode qui permet de généré les matchs suivants
        """
        for match in self.__les_matchs:
            if not match.est_finis():
                return None
        liste_gagnants = []
        for match in self.__les_matchs:
            liste_gagnants.append(match.get_gagnant())
        dico: dict[Escrimeur, int] = {}
        for gagnant in liste_gagnants:
            if gagnant.get_id() in dico:
                dico[gagnant.get_id()] += 1
            else:
                dico[gagnant.get_id()] = 1
        max_valeurs = max(dico.values())
        liste_gagnants_2 = []
        for key, value in dico.items():
            if value == max_valeurs:
                liste_gagnants_2.append(key)
        # On garde le bon ordre
        deja = []
        liste_gagnants_final = []
        for gagnant in liste_gagnants:
            if gagnant.get_id() in liste_gagnants_2 and gagnant.get_id(
            ) not in deja:
                liste_gagnants_final.append(gagnant)
                deja.append(gagnant.get_id())
        les_matchs = []
        self.__index_piste = 0
        for i in range(0, len(liste_gagnants_final), 2):
            escrimeur1 = liste_gagnants_final[i]
            escrimeur2 = liste_gagnants_final[i + 1]
            arbitre = random.choice(liste_arbitres)
            les_matchs.append(
                Match(-1, self.__id_phase_f, escrimeur1, escrimeur2, arbitre,
                      heure_debut, False,
                      self.__les_pistes[self.__index_piste]))
            self.__index_piste += 1
            if self.__index_piste == len(self.__les_pistes):
                self.__index_piste = 0
                heure_debut += 0.25
                if heure_debut % 1 >= 0.6:
                    heure_debut += 0.4
        return les_matchs

    def generer_pdf(self) -> None:
        """
        Fonction qui génère le pdf de la phase finale
        """
        canva = canvas.Canvas("Phase_finale_" + str(self.__id_phase_f) +
                              ".pdf",
                              pagesize=landscape(letter))
        canva.setFont('Helvetica', 18)
        canva.drawCentredString(letter[1] / 2, 570,
                                "Phase finale : " + str(self.__id_phase_f))
        canva.setFont('Helvetica', 12)

        # self.dessine_match(canva, self.__les_matchs[0], 10, 510)

        self.dessine_tour(canva, self.__les_matchs, 10, 510, 0)

        canva.save()

    def dessine_tour(self, canvas, liste_matchs: list[Match], x: int | float,
                     y: int | float, tour: int) -> None:
        """
        Fonction qui dessine un tour

        Args:
            canvas
            liste_matchs (list): liste des matchs
            x (int): coordonnée x
            y (int): coordonnée y
            tour (int): numéro du tour
        """
        ensemble = []
        liste_matchs_2 = []
        cpt = 0
        for match in liste_matchs:
            if match.get_escrimeur1().get_nom() == "" or match.get_escrimeur1(
            ).get_nom() == "" or match.get_escrimeur1().get_nom(
            ) == "None" or match.get_escrimeur2().get_nom(
            ) == "None" or match.get_escrimeur1().get_id(
            ) not in ensemble and match.get_escrimeur2().get_id(
            ) not in ensemble:
                ensemble.append(match.get_escrimeur1().get_id())
                ensemble.append(match.get_escrimeur2().get_id())
                if len(liste_matchs) == 1:
                    typee = 0
                else:
                    typee = cpt % 2 + 1
                if len(liste_matchs) == 2:
                    type2 = 0
                else:
                    type2 = cpt % 4 + 1
                self.dessine_match(canvas, match, x, y - cpt * 45, typee,
                                   type2)
                cpt += 1
            else:
                liste_matchs_2.append(match)
        while len(liste_matchs_2) < len(ensemble) / 4:
            club = Club(-1, "", "", "")
            cate = Categorie(-1, "")
            liste_matchs_2.append(
                Match(
                    -1, -1,
                    Escrimeur(-1, "", "None", "None", "None", "None", "None",
                              "None", 0, club, cate, False),
                    Escrimeur(-1, "", "None", "None", "None", "None", "None",
                              "None", 0, club, cate, False),
                    Escrimeur(-1, "", "None", "None", "None", "None", "None",
                              "None", 0, club, cate, True), -1, False,
                    Piste(-1, -1, "None")))
        if len(liste_matchs) > 1:
            self.dessine_tour(canvas, liste_matchs_2, x + 280,
                              y - 45 / (tour + 1), tour + 1)

    def dessine_match(self, canvas, match: Match, x: float | int,
                      y: float | int, typee: int, type2: int) -> None:
        """
        Fonction qui dessine un match

        Args:
            canvas ([type]): [description]
            match (Match): match
            x (int): coordonnée x
            y (int): coordonnée y
            type (int): type de match
            0 : pas de suite
            1 : suite en haut
            2 : suite en bas
        """
        canvas.setFont('Helvetica', 12)
        canvas.rect(x, y, 120, 20)
        # Nom escrimeur 1
        if match.get_escrimeur1().get_nom() != 'None':
            canvas.drawString(x + 5, y + 5, match.get_escrimeur1().get_nom())
        else:
            canvas.drawString(x + 5, y + 5, "Exempt")
        canvas.rect(x, y - 20, 120, 20)
        # Nom escrimeur 2
        if match.get_escrimeur2().get_nom() != 'None':
            canvas.drawString(x + 5, y - 15, match.get_escrimeur2().get_nom())
        else:
            canvas.drawString(x + 5, y - 15, "Exempt")
        canvas.rect(x + 100, y, 20, 20)
        canvas.rect(x + 100, y - 20, 20, 20)
        if match.get_escrimeur2().get_nom() == 'None':
            # Dessiner un V dans la case du jeoueur 1 et 0 dans l'autre
            canvas.drawString(x + 106.5, y + 5, "V")
            canvas.drawString(x + 106.5, y - 15, "0")
        elif match.get_escrimeur1().get_nom() == 'None':
            # Dessiner un V dans la case du jeoueur 2 et 0 dans l'autre
            canvas.drawString(x + 106.5, y + 5, "0")
            canvas.drawString(x + 106.5, y - 15, "V")
        else:
            if match.est_commencer():
                if match.est_finis():
                    if match.get_gagnant().get_id() == match.get_escrimeur1(
                    ).get_id():
                        canvas.drawString(x + 106.5, y + 5, "V")
                        canvas.drawString(
                            x + 106.5, y - 15,
                            str(match.get_nb_touche(match.get_escrimeur2())))
                    else:
                        canvas.drawString(
                            x + 106.5, y + 5,
                            str(match.get_nb_touche(match.get_escrimeur1())))
                        canvas.drawString(x + 106.5, y - 15, "V")
                else:
                    canvas.drawString(
                        x + 106.5, y + 5,
                        str(match.get_nb_touche(match.get_escrimeur1())))
                    canvas.drawString(
                        x + 106.5, y - 15,
                        str(match.get_nb_touche(match.get_escrimeur2())))
            elif match.get_escrimeur1().get_nom(
            ) != '' and match.get_escrimeur2().get_nom() != '':
                canvas.drawString(x + 106.5, y + 5, "0")
                canvas.drawString(x + 106.5, y - 15, "0")
        if typee == 1:
            canvas.line(x + 120, y, x + 200, y)
            canvas.line(x + 200, y, x + 200, y - 45)
        elif typee == 2:
            canvas.line(x + 120, y, x + 200, y)
            canvas.line(x + 200, y, x + 200, y + 45)
        if type2 == 0 and typee == 1:
            canvas.line(x + 200, y - 22.5, x + 280, y - 22.5)
        elif type2 == 1 and typee == 1:
            canvas.line(x + 200, y - 37, x + 280, y - 37)
        elif type2 == 4 and typee == 2:
            canvas.line(x + 200, y + 37, x + 280, y + 37)

    def __str__(self):
        return f'Phase finale : {self.__id_phase_f} |'
