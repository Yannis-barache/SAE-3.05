"""
Module contenant la classe Match
"""

from escrimeur import Escrimeur
from piste import Piste

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red, black, green


class Match:
    """
    Classe Match
    """

    def __init__(self, id_match: int, id_phase: int, escrimeur1: Escrimeur,
                 escrimeur2: Escrimeur, arbitre: Escrimeur, heure: float,
                 finis: bool, piste: Piste):
        self.__id = id_match
        self.__id_phase = id_phase
        self.__escrimeur1 = escrimeur1
        self.__escrimeur2 = escrimeur2
        self.__arbitre = arbitre
        self.__heure = heure
        self.__finis = finis
        self.__piste = piste
        self.__les_touches: list = []
        self.__type_phase: str | None = None

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id du match

        Returns:
            int: id du match
        """
        return self.__id

    def get_id_phase(self) -> int:
        """
        Fonction qui retourne l'id de la phase

        Returns:
            int: id de la phase
        """
        return self.__id_phase

    def get_escrimeur1(self) -> Escrimeur:
        """
        Fonction qui retourne le premier escrimeur

        Returns:
            Escrimeur: premier escrimeur
        """
        return self.__escrimeur1

    def get_escrimeur2(self) -> Escrimeur:
        """
        Fonction qui retourne le deuxième escrimeur

        Returns:
            Escrimeur: deuxième escrimeur
        """
        return self.__escrimeur2

    def get_arbitre(self) -> Escrimeur:
        """
        Fonction qui retourne l'arbitre

        Returns:
            Escrimeur: arbitre
        """
        return self.__arbitre

    def get_heure(self) -> float:
        """
        Fonction qui retourne l'heure du match

        Returns:
            float: heure du match
        """
        return self.__heure

    def get_type_phase(self) -> str | None:
        """
        Fonction qui retourne le type de la phase

        Returns:
            str: type de la phase
        """
        return self.__type_phase

    def est_finis(self) -> bool:
        """
        Fonction qui retourne si le match est finis

        Returns:
            bool: si le match est finis
        """
        return self.__finis

    def est_commencer(self) -> bool:
        """
        Fonction qui retourne si le match est commencer

        Returns:
            bool: si le match est commencer
        """
        return len(self.__les_touches) > 0

    def get_les_touches(self) -> list:
        """
        Fonction qui retourne les touches du match

        Returns:
            list[Touche]: touches du match
        """
        return self.__les_touches

    def get_nb_touche(self, escrimeur: Escrimeur) -> int:
        """
        Fonction qui retourne le nombre de touche du match

        Args:
            escrimeur (Escrimeur): escrimeur

        Returns:
            int: nombre de touche du match
        """
        cpt = 0
        for touche in self.__les_touches:
            if int(touche.get_escrimeur().get_id()) == int(escrimeur.get_id()):
                cpt += 1
        return cpt

    def get_gagnant(self):
        """
        Fonction qui retourne le gagnant du match

        Returns :
            Escrimeur | None : gagnant du match
        """
        if self.est_finis():
            if self.__escrimeur1.get_nom() == 'None':
                return self.__escrimeur2
            elif self.__escrimeur2.get_nom() == 'None':
                return self.__escrimeur1
            escrimeur1 = 0
            escrimeur2 = 0
            for touche in self.__les_touches:
                if touche.get_escrimeur().get_id() == self.__escrimeur1.get_id(
                ):
                    escrimeur1 += 1
                else:
                    escrimeur2 += 1
            if escrimeur1 > escrimeur2:
                return self.__escrimeur1
            elif escrimeur1 < escrimeur2:
                return self.__escrimeur2
            return None
        else:
            return None

    def get_piste(self) -> Piste:
        """
        Fonction qui retourne la piste du match

        Returns:
            Piste: piste du match
        """
        return self.__piste

    def get_affiche1(self) -> str:
        """
        Fonction qui retourne l'affiche pour l'escrimeur 1

        Returns:
            str: affiche pour l'escrimeur 1
        """
        if self.est_finis() or self.est_commencer():
            if self.get_gagnant(
            ) == self.__escrimeur1 or self.__escrimeur2.get_nom() == 'None':
                return 'V'
            else:
                return str(self.get_nb_touche(self.__escrimeur1))
        else:
            return '0'

    def get_affiche2(self) -> str:
        """
        Fonction qui retourne l'affiche pour l'escrimeur 2

        Returns:
            str: affiche pour l'escrimeur 2
        """
        if self.est_finis() or self.est_commencer():
            if self.get_gagnant(
            ) == self.__escrimeur2 or self.__escrimeur1.get_nom() == 'None':
                return 'V'
            else:
                return str(self.get_nb_touche(self.__escrimeur2))
        else:
            return '0'

    def ajouter_touche(self, touche) -> None:
        """
        Fonction qui ajoute une touche au match

        Args:
            touche (Touche): touche à ajouter
        """
        self.__les_touches.append(touche)

    def set_id(self, id_match: int) -> None:
        """
        Fonction qui modifie l'id du match

        Args:
            id_match (int): id du match
        """
        self.__id = id_match

    def set_id_phase(self, id_phase: int) -> None:
        """
        Fonction qui modifie l'id de la phase

        Args:
            id_phase (int): id de la phase
        """
        self.__id_phase = id_phase

    def set_escrimeur1(self, escrimeur1: Escrimeur) -> None:
        """
        Fonction qui modifie le premier escrimeur

        Args:
            escrimeur1 (Escrimeur): premier escrimeur
        """
        self.__escrimeur1 = escrimeur1

    def set_escrimeur2(self, escrimeur2: Escrimeur) -> None:
        """
        Fonction qui modifie le deuxième escrimeur

        Args:
            escrimeur2 (Escrimeur): deuxième escrimeur
        """
        self.__escrimeur2 = escrimeur2

    def set_arbitre(self, arbitre: Escrimeur) -> None:
        """
        Fonction qui modifie l'arbitre

        Args:
            arbitre (Escrimeur): arbitre
        """
        self.__arbitre = arbitre

    def set_heure(self, heure: float) -> None:
        """
        Fonction qui modifie l'heure du match

        Args:
            heure (float): heure du match
        """
        self.__heure = heure

    def set_finis(self, finis: bool) -> None:
        """
        Fonction qui modifie si le match est finis

        Args:
            finis (bool): si le match est finis
        """
        self.__finis = finis

    def set_touche(self, touches: list) -> None:
        """
        Fonction qui modifie les touches du match

        Args:
            touches (list[Touche]): touches du match
        """
        self.__les_touches = touches

    def set_type_phase(self, type_phase: str | None) -> None:
        """
        Fonction qui modifie le type de la phase

        Args:
            type_phase (str): type de la phase
        """
        self.__type_phase = type_phase

    def set_piste(self, piste: Piste) -> None:
        """
        Fonction qui modifie la piste du match

        Args:
            piste (Piste): piste du match
        """
        self.__piste = piste

    def generer_pdf(self) -> None:
        """
        Fonction qui génère le pdf du match
        """
        canva = canvas.Canvas(f'match_{self.__id}.pdf', pagesize=letter)
        canva.setFont('Helvetica', 18)
        heures = int(str(self.__heure).split(':', maxsplit=1)[0])
        minutes = int(str(self.__heure).split(':')[1])
        format_horloge = f"{heures}h{minutes:02d}"
        canva.drawCentredString(
            letter[0] / 2, 740,
            'Match numéro ' + str(self.__id) + " - " + str(format_horloge))
        canva.setFont('Helvetica', 14)
        canva.drawCentredString(
            letter[0] / 2, 720, 'Arbitre : ' + str(self.__arbitre.get_nom()) +
            ' ' + str(self.__arbitre.get_prenom()))
        canva.setFont('Helvetica', 18)
        self.dessiner_escrimeur1(canva)
        self.dessiner_escrimeur2(canva)
        self.dessiner_score(canva)
        self.dessinner_touche(canva)
        canva.showPage()
        canva.save()

    def dessiner_escrimeur1(self, canva) -> None:
        """
        Fonction qui dessine l'escrimeur 1

        Args:
            canva (canvas): canvas
        """
        canva.setFont('Helvetica', 15)
        classement = self.__escrimeur1.get_classement()
        if classement is None:
            classement2 = 'NC'
        else:
            classement2 = "n°" + str(classement)
        canva.drawString(75, 680, "Escrimeur rouge")

        rayon_rond = 5
        x_centre_rond = 65
        y_centre_rond = 680 + 4
        canva.setFillColor(red)
        canva.circle(x_centre_rond,
                     y_centre_rond,
                     rayon_rond,
                     stroke=0,
                     fill=1)
        canva.setFillColor(black)

        canva.drawString(
            60, 660,
            str(self.__escrimeur1.get_nom()) + ' ' +
            str(self.__escrimeur1.get_prenom() + ' - ' + str(classement2)))
        canva.drawString(60, 640, str(self.__escrimeur1.get_club().get_nom()))
        canva.drawString(60, 620,
                         str(self.__escrimeur1.get_categorie().get_nom()))

    def dessiner_escrimeur2(self, canva) -> None:
        """
        Fonction qui dessine l'escrimeur 2

        Args:
            canva (canvas): canvas
        """
        classement = self.__escrimeur2.get_classement()
        if classement is None:
            classement2 = 'NC'
        else:
            classement2 = "n°" + str(classement)
        width = canva.stringWidth("Escrimeur vert", 'Helvetica', 15)
        canva.drawString(610 - width - 70 - 15, 680, "Escrimeur vert")
        rayon_rond = 5
        x_centre_rond = 610 - 70 - 5
        y_centre_rond = 680 + 4
        canva.setFillColor(green)
        canva.circle(x_centre_rond,
                     y_centre_rond,
                     rayon_rond,
                     stroke=0,
                     fill=1)
        canva.setFillColor(black)
        width = canva.stringWidth(
            str(self.__escrimeur2.get_nom()) + ' ' +
            str(self.__escrimeur2.get_prenom() + ' - ' + str(classement2)),
            'Helvetica', 15)
        canva.drawString(
            610 - width - 70, 660,
            str(self.__escrimeur2.get_nom()) + ' ' +
            str(self.__escrimeur2.get_prenom() + ' - ' + str(classement2)))
        width = canva.stringWidth(str(self.__escrimeur2.get_club().get_nom()),
                                  'Helvetica', 15)
        canva.drawString(610 - width - 70, 640,
                         str(self.__escrimeur2.get_club().get_nom()))
        width = canva.stringWidth(
            str(self.__escrimeur2.get_categorie().get_nom()), 'Helvetica', 15)
        canva.drawString(610 - width - 70, 620,
                         str(self.__escrimeur2.get_categorie().get_nom()))

    def dessiner_score(self, canva) -> None:
        """
        Fonction qui dessine le score

        Args:
            canva (canvas): canvas
        """
        canva.setFont('Helvetica', 15)
        canva.rect(240, 560, 40, 40, stroke=1, fill=0)
        canva.setFont('Helvetica', 28)
        width = canva.stringWidth(str(self.get_nb_touche(self.__escrimeur1)),
                                  'Helvetica', 28)
        canva.drawString(260 - width / 2, 580 - 20 / 2,
                         str(self.get_nb_touche(self.__escrimeur1)))
        canva.drawString(303, 580 - 20 / 2, '-')
        canva.rect(333, 560, 40, 40, stroke=1, fill=0)
        width = canva.stringWidth(str(self.get_nb_touche(self.__escrimeur2)),
                                  'Helvetica', 28)
        canva.drawString(353 - width / 2, 580 - 20 / 2,
                         str(self.get_nb_touche(self.__escrimeur2)))

    def get_escrimeur_touche(self, num_toucher: int) :
        """
        Fonction qui retourne l'escrimeur qui a touché

        Args :
            num_toucher (int) : numéro de la touche

        Returns :
            Escrimeur | None : escrimeur qui a touché
        """
        for touche in self.__les_touches:
            if touche.get_numero() == num_toucher:
                return touche.get_escrimeur()
        return None

    def dessinner_touche(self, canva) -> None:
        """
        Fonction qui dessine les touches

        Args:
            canva (canvas): canvas
        """
        cpt = 0
        if self.__type_phase == 'Poule':
            debut = 230
            cpt = 9
        else:
            debut = 40
            cpt = 29
        for i in range(cpt):
            if self.get_escrimeur_touche(i + 1) and self.get_escrimeur_touche(i + 1).get_id() == self.__escrimeur1.get_id():
                canva.setFillColor(red)
                canva.circle(debut + 14 * i + i * 5, 500, 7, stroke=1, fill=1)
                canva.setFillColor(black)
            elif self.get_escrimeur_touche(i + 1) and self.get_escrimeur_touche(i + 1).get_id() == self.__escrimeur2.get_id():
                canva.setFillColor(green)
                canva.circle(debut + 14 * i + i * 5, 500, 7, stroke=1, fill=1)
                canva.setFillColor(black)
            else:
                if self.est_finis():
                    canva.circle(debut + 14 * i + i * 5,
                                 500,
                                 7,
                                 stroke=1,
                                 fill=0)
                    canva.line(debut + 14 * i + i * 5 - 7 + 2, 500 - 7 + 2,
                               debut + 14 * i + i * 5 + 7 - 2, 500 + 7 - 2)
                else:
                    canva.circle(debut + 14 * i + i * 5,
                                 500,
                                 7,
                                 stroke=1,
                                 fill=0)

    def __str__(self):
        return (
            f'Match : {self.__id} - {self.__id_phase} - {self.__escrimeur1} - '
            f'{self.__escrimeur2} - {self.__arbitre} - {self.__heure} - '
            f'{self.__finis}|')
