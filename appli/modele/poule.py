"""
Module contenant la classe Poule
"""

from escrimeur import Escrimeur
from match import Match
import constantes as const

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Poule:
    """
    Classe Poule
    """

    def __init__(self, id_poule):
        self.__id = id_poule
        self.__les_matchs = []
        self.__les_escrimeurs = []
        self.__dico: dict[Escrimeur, list[int, int, int]] = {}

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la poule

        Returns:
            int: id de la poule
        """
        return self.__id

    def get_les_matchs(self) -> list[Match]:
        """
        Fonction qui retourne les matchs de la poule

        Returns:
            list[Match]: les matchs de la poule
        """
        return self.__les_matchs

    def get_les_escrimeurs(self) -> list[Escrimeur]:
        """
        Fonction qui retourne les escrimeurs de la poule

        Returns:
            list[Escrimeur]: les escrimeurs de la poule
        """
        return self.__les_escrimeurs

    def set_id(self, id_poule) -> None:
        """
        Fonction qui modifie l'id de la poule

        Args:
            id_poule (int): id de la poule
        """
        self.__id = id_poule

    def set_les_matchs(self, les_matchs: list[Match]) -> None:
        """
        Fonction qui modifie les matchs de la poule

        Args:
            les_matchs (list[Match]): les matchs de la poule
        """
        self.__les_matchs = les_matchs
        self.set_les_escrimeurs()

    def generer_matchs(self, infos: tuple[Escrimeur, list[Escrimeur]],
                       heure_debut: float) -> list[Match]:
        """
        Fonction qui genere les matchs de la poule

        Args:
            infos (tuple[Escrimeur, list[Escrimeur]]): Les infos de la poule

        Returns:
            list[Match]: liste des matchs de la poule
        """
        les_matchs = []
        arbitre, les_escrimeurs = infos
        for escrimeur1 in les_escrimeurs:
            for escrimeur2 in les_escrimeurs:
                if escrimeur1 != escrimeur2 and escrimeur1.get_id(
                ) < escrimeur2.get_id():
                    les_matchs.append(
                        Match(-1, self.__id, escrimeur1, escrimeur2, arbitre,
                              heure_debut, False))
                    heure_debut += 0.05
                    if heure_debut % 1 >= 0.6:
                        heure_debut += 0.4
        self.__les_matchs = les_matchs
        self.set_les_escrimeurs()
        return les_matchs

    def get_match_by_escrimeurs(self, escrimeur1: Escrimeur,
                                escrimeur2: Escrimeur) -> Match:
        """
        Fonction qui retourne le match entre deux escrimeurs

        Args:
            escrimeur1 (Escrimeur): le premier escrimeur
            escrimeur2 (Escrimeur): le deuxième escrimeur

        Returns:
            Match: le match entre les deux escrimeurs
        """
        for match in self.__les_matchs:
            if match.get_escrimeur1() == escrimeur1 and match.get_escrimeur2(
            ) == escrimeur2 or match.get_escrimeur1(
            ) == escrimeur2 and match.get_escrimeur2() == escrimeur1:
                return match
        return None

    def generer_pdf(self) -> None:
        """
        Fonction qui génère le PDF de la poule
        """
        canva = canvas.Canvas('test.pdf', pagesize=letter)
        canva.setFont('Helvetica', 18)
        canva.drawCentredString(letter[0] / 2, 750,
                                'Poule numéro ' + str(self.__id))
        canva.setFont('Helvetica', 12)
        width_nom = self.dessiner_noms(canva)
        width_clubs = self.dessiner_clubs(canva, width_nom)
        width = self.dessinner_colonne3(canva, width_clubs + width_nom)
        height = self.dessinner_resultats(canva, width)
        self.dessiner_arbitre(canva, height)
        canva.showPage()
        canva.save()

    def get_width_noms(self, canva: canvas) -> int:
        """
        Fonction qui retourne la largeur du rectangle des noms

        Args:
            canva (canvas): le canvas

        Returns:
            int: la largeur du rectangle des noms
        """
        width = 0
        for match in self.__les_matchs:
            texte = match.get_escrimeur1().get_nom()
            if canva.stringWidth(texte, 'Helvetica', 12) + 15 > width:
                width = canva.stringWidth(texte, 'Helvetica', 12) + 15
            texte = match.get_escrimeur2().get_nom()
            if canva.stringWidth(texte, 'Helvetica', 12) + 15 > width:
                width = canva.stringWidth(texte, 'Helvetica', 12) + 15
        return width

    def set_les_escrimeurs(self) -> None:
        """
        Fonction qui modifie les escrimeurs de la poule selon les matchs
        """
        escrimeurs = []
        for match in self.__les_matchs:
            if match.get_escrimeur1() not in escrimeurs:
                escrimeurs.append(match.get_escrimeur1())
            if match.get_escrimeur2() not in escrimeurs:
                escrimeurs.append(match.get_escrimeur2())
        self.__les_escrimeurs = escrimeurs

    def dessiner_noms(self, canva: canvas) -> int:
        """
        Fonction qui dessine les noms des escrimeurs de la poule

        Args:
            canva (canvas): le canvas

        Returns:
            int: la largeur du rectangle des noms
        """
        noms = ['NOMS']
        for escrimeur in self.__les_escrimeurs:
            noms.append(escrimeur.get_nom())
        width_noms = self.get_width_noms(canva)
        width_noms = max(width_noms, const.LARGEUR_NOM_BASE)
        hauteur = const.POSITIONNEMENT_HAUTEUR_RECTANGLE_NOM
        for nom in noms:
            canva.rect(const.DECALAGE_GAUCHE,
                       hauteur,
                       width_noms,
                       const.HAUTEUR_RECTANGLE_NOM,
                       stroke=1,
                       fill=0)
            largeur_noms = canva.stringWidth(nom, 'Helvetica', 12)
            canva.drawString(
                const.DECALAGE_GAUCHE + (width_noms - largeur_noms) / 2,
                hauteur + 10, nom)
            hauteur -= const.HAUTEUR_RECTANGLE_NOM
        return width_noms

    def get_width_clubs(self, canva: canvas) -> int:
        """
        Fonction qui retourne la largeur du rectangle des clubs

        Args:
            canva (canvas): le canvas

        Returns:
            int: la largeur du rectangle des clubs
        """
        width = 0
        for match in self.__les_matchs:
            texte = match.get_escrimeur1().get_club().get_nom()
            if canva.stringWidth(texte, 'Helvetica', 12) + 15 > width:
                width = canva.stringWidth(texte, 'Helvetica', 12) + 15
            texte = match.get_escrimeur2().get_club().get_nom()
            if canva.stringWidth(texte, 'Helvetica', 12) + 15 > width:
                width = canva.stringWidth(texte, 'Helvetica', 12) + 15
        return width

    def dessiner_clubs(self, canva: canvas, width_nom: int) -> int:
        """
        Fonction qui dessine les noms des escrimeurs de la poule

        Args:
            canva (canvas): le canvas
            width_nom (int): la largeur du rectangle des noms

        Returns:
            int: la largeur du rectangle des clubs
        """
        clubs = ['CLUBS']
        for escrimeur in self.__les_escrimeurs:
            clubs.append(escrimeur.get_club().get_nom())
        width_clubs = self.get_width_clubs(canva)
        width_clubs = max(width_clubs, const.LARGEUR_CLUB_BASE)
        hauteur = const.POSITIONNEMENT_HAUTEUR_RECTANGLE_CLUB
        for club in clubs:
            canva.rect(const.DECALAGE_GAUCHE + width_nom,
                       hauteur,
                       width_clubs,
                       const.HAUTEUR_RECTANGLE_NOM,
                       stroke=1,
                       fill=0)
            largeur_club = canva.stringWidth(club, 'Helvetica', 12)
            canva.drawString(
                const.DECALAGE_GAUCHE + width_nom +
                (width_clubs - largeur_club) / 2, hauteur + 10, club)
            hauteur -= const.HAUTEUR_RECTANGLE_CLUB
        return width_clubs

    def dessinner_colonne3(self, canva: canvas, width_clubs: int) -> int:
        """
        Fonction qui dessine la colonne 3

        Args:
            canva (canvas): le canvas
            width_clubs (int): la largeur du rectangle des clubs

        Returns:
            int: la largeur de la colonne 3
        """
        largeur = width_clubs
        for i in range(len(self.__les_escrimeurs) + 1):
            hauteur = const.POSITIONNEMENT_HAUTEUR_RECTANGLE_CLUB
            for j in range(len(self.__les_escrimeurs) + 1):
                if i == 0 and j == 0:
                    canva.line(const.DECALAGE_GAUCHE + width_clubs + 30,
                               hauteur, const.DECALAGE_GAUCHE + width_clubs,
                               hauteur + 30)
                    canva.rect(const.DECALAGE_GAUCHE + width_clubs,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=0)
                elif i == 0 and j != 0:
                    canva.rect(const.DECALAGE_GAUCHE + width_clubs,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=1)
                    canva.setFillColorRGB(1, 1, 1)
                    canva.drawString(
                        const.DECALAGE_GAUCHE + width_clubs + 11.664,
                        hauteur + 10, str(j))
                    canva.setFillColorRGB(0, 0, 0)
                elif i != 0 and j == 0:
                    canva.rect(const.DECALAGE_GAUCHE + largeur,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=1)
                    canva.setFillColorRGB(1, 1, 1)
                    canva.drawString(const.DECALAGE_GAUCHE + largeur + 11.664,
                                     hauteur + 10, str(i))
                    canva.setFillColorRGB(0, 0, 0)
                elif i == j:
                    canva.setFillColorRGB(0.8, 0.8, 0.8)
                    canva.rect(const.DECALAGE_GAUCHE + largeur,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=1)
                    canva.setFillColorRGB(0, 0, 0)
                else:
                    canva.rect(const.DECALAGE_GAUCHE + largeur,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=0)
                    le_match = self.get_match_by_escrimeurs(
                        self.__les_escrimeurs[i - 1],
                        self.__les_escrimeurs[j - 1])
                    self.gestion_match(le_match, canva, i, j, hauteur, largeur)
                hauteur -= const.HAUTEUR_RECTANGLE_CLUB
            largeur += 30
        canva.rect(const.DECALAGE_GAUCHE + largeur,
                   hauteur + 30,
                   6,
                   largeur - width_clubs,
                   stroke=1,
                   fill=0)
        return largeur + 6

    def gestion_match(self, le_match: Match, canva: canvas, i: int, j: int,
                      hauteur: int, largeur: int) -> None:
        """
        Fonction qui gere le match

        Args:
            match (Match): le match
            canva (canvas): le canvas
        """
        # Si le match est commencé:
        if le_match is not None and le_match.est_commencer():

            # Si le match est fini et que le gagnant est le premier escrimeur
            if le_match.get_gagnant() == self.__les_escrimeurs[j - 1]:
                # Dessine un V dans la case
                canva.drawString(const.DECALAGE_GAUCHE + largeur + 11.664,
                                 hauteur + 10, 'V')
                # Si l'escrimeur n'est pas dans le dictionnaire
                if self.__dico.get(self.__les_escrimeurs[j - 1]) is None:
                    self.__dico[self.__les_escrimeurs[j - 1]] = [
                        1,
                        le_match.get_nb_touche(self.__les_escrimeurs[j - 1]),
                        le_match.get_nb_touche(self.__les_escrimeurs[i - 1])
                    ]
                # Sinon
                else:
                    self.__dico[self.__les_escrimeurs[j - 1]][0] += 1
                    self.__dico[self.__les_escrimeurs[
                        j - 1]][1] += le_match.get_nb_touche(
                            self.__les_escrimeurs[j - 1])
                    self.__dico[self.__les_escrimeurs[
                        j - 1]][2] += le_match.get_nb_touche(
                            self.__les_escrimeurs[i - 1])
                if self.__dico.get(self.__les_escrimeurs[i - 1]) is None:
                    self.__dico[self.__les_escrimeurs[i - 1]] = [
                        0,
                        le_match.get_nb_touche(self.__les_escrimeurs[i - 1]),
                        le_match.get_nb_touche(self.__les_escrimeurs[j - 1])
                    ]
                else:
                    self.__dico[self.__les_escrimeurs[i - 1]][0] += 0
                    self.__dico[self.__les_escrimeurs[
                        i - 1]][1] += le_match.get_nb_touche(
                            self.__les_escrimeurs[i - 1])
                    self.__dico[self.__les_escrimeurs[
                        i - 1]][2] += le_match.get_nb_touche(
                            self.__les_escrimeurs[j - 1])
            else:
                canva.drawString(
                    const.DECALAGE_GAUCHE + largeur + 11.664, hauteur + 10,
                    str(le_match.get_nb_touche(self.__les_escrimeurs[j - 1])))

    def dessinner_resultats(self, canva: canvas, width: int) -> int:
        """
        Fonction qui dessine la colonne des resultats

        Args:
            canva (canvas): le canvas
            width (int): la largeur de la colonne 3

        Returns:
            int: la hauteur
        """
        titres = ['Total', 'Indice', 'Place']
        titres2 = ['Victoires']
        largeur = width
        for i in range(len(titres)):
            hauteur = const.POSITIONNEMENT_HAUTEUR_RECTANGLE_CLUB
            for j in range(len(self.__les_escrimeurs) + 1):
                if j == 0:
                    if i < 1:
                        canva.rect(const.DECALAGE_GAUCHE + largeur,
                                   hauteur,
                                   30,
                                   30,
                                   stroke=1,
                                   fill=0)
                        canva.setFont('Helvetica', 7)
                        canva.drawString(
                            const.DECALAGE_GAUCHE + largeur +
                            (30 - canva.stringWidth(titres[i], 'Helvetica', 7))
                            / 2, hauteur + 13, titres[i])
                        canva.drawString(
                            const.DECALAGE_GAUCHE +
                            largeur + (30 - canva.stringWidth(
                                titres2[i], 'Helvetica', 7)) / 2, hauteur + 7,
                            titres2[i])
                        canva.setFont('Helvetica', 12)
                    else:
                        canva.rect(const.DECALAGE_GAUCHE + largeur,
                                   hauteur,
                                   30,
                                   30,
                                   stroke=1,
                                   fill=0)
                        canva.setFont('Helvetica', 7)
                        canva.drawString(
                            const.DECALAGE_GAUCHE + largeur + 6.2465,
                            hauteur + 10, titres[i])
                        canva.setFont('Helvetica', 12)
                else:
                    canva.rect(const.DECALAGE_GAUCHE + largeur,
                               hauteur,
                               30,
                               30,
                               stroke=1,
                               fill=0)
                    if i == 0:
                        if self.__dico.get(
                                self.__les_escrimeurs[j - 1]) is not None:
                            canva.drawString(
                                const.DECALAGE_GAUCHE + largeur + 11.664,
                                hauteur + 10,
                                str(self.__dico[self.__les_escrimeurs[j -
                                                                      1]][0]))
                    elif i == 1:
                        if self.__dico.get(
                                self.__les_escrimeurs[j - 1]) is not None:
                            indice = self.__dico[self.__les_escrimeurs[
                                j - 1]][1] - self.__dico[self.__les_escrimeurs[
                                    j - 1]][2]
                            if indice > 0:
                                indice = '+' + str(indice)
                            else:
                                indice = str(indice)
                            canva.drawString(
                                const.DECALAGE_GAUCHE + largeur +
                                (30 - canva.stringWidth(
                                    str(indice), 'Helvetica', 12)) / 2,
                                hauteur + 10, indice)
                    elif i == 2:
                        if self.__dico.get(
                                self.__les_escrimeurs[j - 1]) is not None:
                            canva.drawString(
                                const.DECALAGE_GAUCHE + largeur + 11.664,
                                hauteur + 10,
                                str(self.classement_poule().get(
                                    self.__les_escrimeurs[j - 1])))
                hauteur -= const.HAUTEUR_RECTANGLE_CLUB
            largeur += 30
        return hauteur

    def dessiner_arbitre(self, canva: canvas, height) -> None:
        """
        Fonction qui dessine l'arbitre

        Args:
            canva (canvas): le canvas
            height (int): la hauteur
        """
        canva.drawString(
            const.DECALAGE_GAUCHE, height, 'Arbitre de la poule : ' +
            self.__les_matchs[0].get_arbitre().get_nom())

    def classement_poule(self) -> dict[Escrimeur, int]:
        """
        Fonction qui retourne le classement de la poule

        Returns:
            dict[Escrimeur, int]: le classement de la poule
        """
        classement = sorted(self.__dico.keys(), key=self.comparer_escrimeurs)
        return {
            escrimeur: position
            for position, escrimeur in enumerate(classement, 1)
        }

    def comparer_escrimeurs(self, escrimeur: Escrimeur):
        victoires, touche_marquee, touche_prise = self.__dico[escrimeur]
        indice = touche_marquee - touche_prise
        return (-victoires, -indice)  # Tri décroissant

    def __str__(self):
        return f'{self.__id}'
