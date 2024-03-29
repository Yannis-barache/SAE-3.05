"""
Module de test de la classe Competition
"""

import datetime
import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from competition import Competition
from categorie import Categorie
from arme import Arme
from lieu import Lieu
from escrimeur import Escrimeur
from exceptions import PasAssezDArbitres
from club import Club
from touche import Touche
from phase_final import PhaseFinal
from match import Match
from datetime import date
from piste import Piste


class TestCompetition(unittest.TestCase):
    """
    Classe de test de la classe Competition

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5,False)
        self.assertIsInstance(competition, Competition)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5,False)
        self.assertEqual(competition.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_nom(), 'Escrime comp')

    def test_get_date(self):
        """
        Test de la fonction get_date de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False )
        self.assertEqual(competition.get_date(), '14-05-2004')

    def test_get_date_fin_inscription(self):
        """
        Test de la fonction get_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_date_fin_inscription(), '14-05-2004')

    def test_get_saison(self):
        """
        Test de la fonction get_saison de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_saison(), 'été')

    def test_get_lieu(self):
        """
        Test de la fonction get_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_lieu(), lieu)

    def test_get_arme(self):
        """
        Test de la fonction get_arme de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_arme(), arme)

    def test_get_categorie(self):
        """
        Test de la fonction get_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_get_coefficient(self):
        """
        Test de la fonction get_coefficient de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2005',
                                  '14-05-2005', 'hiver', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.get_coefficient(), 0.5)

    def test_est_finis(self):
        """
        Test de la fonction est_finis de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp2', '14-05-2005',
                                  '14-05-2005', 'hiver', lieu, arme, categorie,
                                  0.5, False)
        self.assertEqual(competition.est_finis(), False)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_id(2)
        self.assertEqual(competition.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_nom('Escrime comp2')
        self.assertEqual(competition.get_nom(), 'Escrime comp2')

    def test_set_date(self):
        """
        Test de la fonction set_date de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_date('15-05-2004')
        self.assertEqual(competition.get_date(), '15-05-2004')

    def test_set_date_fin_inscription(self):
        """
        Test de la fonction set_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_date_fin_inscription('15-05-2004')
        self.assertEqual(competition.get_date_fin_inscription(), '15-05-2004')

    def test_set_saison(self):
        """
        Test de la fonction set_saison de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_saison('hiver')
        self.assertEqual(competition.get_saison(), 'hiver')

    def test_set_lieu(self):
        """
        Test de la fonction set_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        lieu2 = Lieu(2, 'Une grande ville', 'Lyon France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_lieu(lieu2)
        self.assertEqual(competition.get_lieu(), lieu2)

    def test_set_arme(self):
        """
        Test de la fonction set_arme de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        arme2 = Arme(2, 'Epée Femme', 'F')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_arme(arme2)
        self.assertEqual(competition.get_arme(), arme2)

    def test_set_categorie(self):
        """
        Test de la fonction set_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        competition.set_categorie(categorie)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_set_coefficient(self):
        """
        Test de la fonction set_coefficient de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2005',
                                  '14-05-2005', 'hiver', lieu, arme, categorie,
                                  0.5, False)
        competition.set_coefficient(0.6)
        self.assertEqual(competition.get_coefficient(), 0.6)

    def test_generation_poule(self):
        """
        Test de la fonction generation_poule de la classe Competition
        """
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, None, None, False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, None, None, False)
        escrimeur3 = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05',
                               'yannou', 'mdp', 'AB01', 3, None, None, False)
        escrimeur4 = Escrimeur(4, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB02', 4, None, None, False)
        escrimeur5 = Escrimeur(5, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB03', 5, None, None, False)
        escrimeur6 = Escrimeur(6, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB04', 6, None, None, False)
        escrimeur7 = Escrimeur(7, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB05', 7, None, None, False)
        escrimeur8 = Escrimeur(8, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB06', 8, None, None, False)
        escrimeur9 = Escrimeur(9, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB07', 9, None, None, False)
        escrimeur10 = Escrimeur(10, 'Dupont', 'Jean', 'M', '2004-14-05',
                                'jeanjean', 'mdp', 'AB08', 10, None, None,
                                False)

        arbitre1 = Escrimeur(11, 'Dupont', 'Jean', 'M', '2004-14-05',
                             'jeanjean', 'mdp', 'AB09', 11, None, None, True)
        arbitre2 = Escrimeur(12, 'Dupont', 'Jean', 'M', '2004-14-05',
                             'jeanjean', 'mdp', 'AB10', 12, None, None, False)

        liste_escrimeur = [
            escrimeur1, escrimeur2, escrimeur3, escrimeur4, escrimeur5,
            escrimeur6, escrimeur7, escrimeur8, escrimeur9, escrimeur10
        ]
        liste_arbitre = [arbitre1, arbitre2]

        dico = Competition.generation_poule(liste_escrimeur, liste_arbitre)
        self.assertEqual(len(dico), 2)
        dico2 = Competition.generation_poule(liste_escrimeur, [])
        self.assertEqual(dico2, None)

    def test_trie_classement_initial(self):
        """
        Test de la fonction trie_classement_initial de la classe Competition
        """
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, None, None, False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, None, None, False)
        escrimeur3 = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05',
                               'yannou', 'mdp', 'AB01', 3, None, None, False)
        escrimeur4 = Escrimeur(4, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB02', 4, None, None, False)
        liste_trie = [escrimeur1, escrimeur2, escrimeur3, escrimeur4]
        liste_non_trie = [escrimeur4, escrimeur3, escrimeur2, escrimeur1]
        self.assertEqual(
            Competition.trie_classement_initial(liste_non_trie.copy()),
            liste_trie)

    def test_nombre_poule(self):
        """
        Test de la fonction nombre_poule de la classe Competition
        """
        assert Competition.nombre_poule(10, 2) == (2, 5)
        assert Competition.nombre_poule(11, 2) == (2, 6)
        with self.assertRaises(PasAssezDArbitres):
            Competition.nombre_poule(10, 1)

    def test_etablir_classement_provisoire(self):
        """
        Test de la fonction etablir_classement_provisoire de la classe
        """
        club = Club(1, 'nom', 'adresse', 'pays')
        club2 = Club(2, 'nom2', 'adresse2', 'pays2')
        escrimeur1 = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'pseudo', 'mdp', 'licence', 1, club, None,
                               False)
        escrimeur2 = Escrimeur(2, 'nom2', 'prenom2', 'sexe2',
                               'date_naissance2', 'pseudo2', 'mdp2',
                               'licence2', 2, club, None, False)
        escrimeur3 = Escrimeur(3, 'nom3', 'prenom3', 'sexe3',
                               'date_naissance3', 'pseudo3', 'mdp3',
                               'licence3', 3, club, None, False)
        escrimeur4 = Escrimeur(4, 'nom4', 'prenom4', 'sexe4',
                               'date_naissance4', 'pseudo4', 'mdp4',
                               'licence4', 4, club, None, False)
        escrimeur5 = Escrimeur(5, 'nom5', 'prenom5', 'sexe5',
                               'date_naissance5', 'pseudo5', 'mdp5',
                               'licence5', 5, club, None, False)
        escrimeur6 = Escrimeur(6, 'nom6', 'prenom6', 'sexe6',
                               'date_naissance6', 'pseudo6', 'mdp6',
                               'licence6', 6, club2, None, False)
        escrimeur7 = Escrimeur(7, 'nom7', 'prenom7', 'sexe7',
                               'date_naissance7', 'pseudo7', 'mdp7',
                               'licence7', 7, club2, None, False)
        escrimeur8 = Escrimeur(8, 'nom8', 'prenom8', 'sexe8',
                               'date_naissance8', 'pseudo8', 'mdp8',
                               'licence8', 8, club2, None, False)
        escrimeur9 = Escrimeur(9, 'nom9', 'prenom9', 'sexe9',
                               'date_naissance9', 'pseudo9', 'mdp9',
                               'licence9', 9, club2, None, False)
        escrimeur10 = Escrimeur(10, 'nom10', 'prenom10', 'sexe10',
                                'date_naissance10', 'pseudo10', 'mdp10',
                                'licence10', 10, club, None, False)

        arbitre1 = Escrimeur(11, 'nom11', 'prenom11', 'sexe11',
                             'date_naissance11', 'pseudo10', 'mdp11',
                             'licence11', 11, club, None, True)
        arbitre2 = Escrimeur(12, 'nom12', 'prenom12', 'sexe12',
                             'date_naissance12', 'pseudo10', 'mdp12',
                             'licence12', 12, club2, None, True)

        les_escrimeurs = [
            escrimeur1, escrimeur2, escrimeur3, escrimeur4, escrimeur5,
            escrimeur6, escrimeur7, escrimeur8, escrimeur9, escrimeur10
        ]
        les_arbitres = [arbitre1, arbitre2]

        poules = Competition.generation_poule(les_escrimeurs, les_arbitres)
        piste1 = Piste(1, 1, "piste1")
        piste2 = Piste(2, 2, "piste2")
        piste3 = Piste(3, 3, "piste3")
        piste4 = Piste(4, 4, "piste4")
        lsite_pistes = [piste1, piste2, piste3, piste4]
        for poule in poules:
            poule.set_les_pistes(lsite_pistes)
            matchs = poule.generer_matchs(poules.get(poule), 10.5)
            liste = []
            for match in matchs:
                escrimeur11 = match.get_escrimeur1()
                escrimeur22 = match.get_escrimeur2()
                touche = Touche(match, escrimeur11, 1)
                touche2 = Touche(match, escrimeur22, 2)
                touche3 = Touche(match, escrimeur11, 3)
                match.ajouter_touche(touche)
                match.ajouter_touche(touche2)
                match.ajouter_touche(touche3)
                match.set_finis(True)
                liste.append(match)

        classement = Competition.etablir_classement_provisoire(poules)
        self.assertEqual(len(classement), 10)

    def test_get_puissance_sup(self):
        """
        Test de la fonction get_puissance_sup de la classe Competition
        """
        self.assertEqual(Competition.get_puissance_sup(10), 4)

    def test_generer_phase_finale(self):
        """
        Test de la fonction generer_phase_finale de la classe Competition
        """
        club = Club(1, 'nom', 'adresse', 'pays')
        club2 = Club(2, 'nom2', 'adresse2', 'pays2')
        escrimeur1 = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'pseudo', 'mdp', 'licence', 1, club, None,
                               False)
        escrimeur2 = Escrimeur(2, 'nom2', 'prenom2', 'sexe2',
                               'date_naissance2', 'pseudo2', 'mdp2',
                               'licence2', 2, club, None, False)
        escrimeur3 = Escrimeur(3, 'nom3', 'prenom3', 'sexe3',
                               'date_naissance3', 'pseudo3', 'mdp3',
                               'licence3', 3, club, None, False)
        escrimeur4 = Escrimeur(4, 'nom4', 'prenom4', 'sexe4',
                               'date_naissance4', 'pseudo4', 'mdp4',
                               'licence4', 4, club, None, False)
        escrimeur5 = Escrimeur(5, 'nom5', 'prenom5', 'sexe5',
                               'date_naissance5', 'pseudo5', 'mdp5',
                               'licence5', 5, club, None, False)
        escrimeur6 = Escrimeur(6, 'nom6', 'prenom6', 'sexe6',
                               'date_naissance6', 'pseudo6', 'mdp6',
                               'licence6', 6, club2, None, False)
        escrimeur7 = Escrimeur(7, 'nom7', 'prenom7', 'sexe7',
                               'date_naissance7', 'pseudo7', 'mdp7',
                               'licence7', 7, club2, None, False)
        escrimeur8 = Escrimeur(8, 'nom8', 'prenom8', 'sexe8',
                               'date_naissance8', 'pseudo8', 'mdp8',
                               'licence8', 8, club2, None, False)
        escrimeur9 = Escrimeur(9, 'nom9', 'prenom9', 'sexe9',
                               'date_naissance9', 'pseudo9', 'mdp9',
                               'licence9', 9, club2, None, False)
        escrimeur10 = Escrimeur(10, 'nom10', 'prenom10', 'sexe10',
                                'date_naissance10', 'pseudo10', 'mdp10',
                                'licence10', 10, club, None, False)

        arbitre1 = Escrimeur(11, 'nom11', 'prenom11', 'sexe11',
                             'date_naissance11', 'pseudo10', 'mdp11',
                             'licence11', 11, club, None, True)
        arbitre2 = Escrimeur(12, 'nom12', 'prenom12', 'sexe12',
                             'date_naissance12', 'pseudo10', 'mdp12',
                             'licence12', 12, club2, None, True)

        les_escrimeurs = [
            escrimeur1, escrimeur2, escrimeur3, escrimeur4, escrimeur5,
            escrimeur6, escrimeur7, escrimeur8, escrimeur9, escrimeur10
        ]
        les_arbitres = [arbitre1, arbitre2]
        piste1 = Piste(1, 1, "piste1")
        piste2 = Piste(2, 2, "piste2")
        piste3 = Piste(3, 3, "piste3")
        piste4 = Piste(4, 4, "piste4")
        lsite_pistes = [piste1, piste2, piste3, piste4]
        poules = Competition.generation_poule(les_escrimeurs, les_arbitres)
        for poule in poules:
            poule.set_les_pistes(lsite_pistes)
            matchs = poule.generer_matchs(poules.get(poule), 10.5)
            liste = []
            for match in matchs:
                escrimeur11 = match.get_escrimeur1()
                escrimeur22 = match.get_escrimeur2()
                touche = Touche(match, escrimeur11, 1)
                touche2 = Touche(match, escrimeur22, 2)
                touche3 = Touche(match, escrimeur11, 3)
                match.ajouter_touche(touche)
                match.ajouter_touche(touche2)
                match.ajouter_touche(touche3)
                match.set_finis(True)
                liste.append(match)
        phase, matchs_finaux = Competition.generer_phase_finale(
            poules, les_arbitres, 10.3, [Piste(1, 1, "piste1")])
        self.assertEqual(len(matchs_finaux), 8)
        self.assertIsInstance(phase, PhaseFinal)

    def test_get_etat(self):
        date_ojd_plus_1 = (date.today() +
                           datetime.timedelta(days=1)).strftime('%d-%m-%Y')
        date_ojd_moins_1 = (date.today() -
                            datetime.timedelta(days=1)).strftime('%d-%m-%Y')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', None, None, None, 0.5, False)
        phase = PhaseFinal(1)
        competition.set_phase_final(phase)
        match = Match(1, 1, None, None, None, 10.0, False, None)
        phase.set_match(match)
        self.assertEqual(competition.get_etat(), 'En cours')
        match.set_finis(True)
        self.assertEqual(competition.get_etat(), 'Terminée')
        competition.set_date(date_ojd_plus_1)
        competition.set_date_fin_inscription(date_ojd_moins_1)
        phase.clear_matchs()
        self.assertEqual(competition.get_etat(), 'À venir')
        competition.set_date_fin_inscription(date_ojd_plus_1)
        self.assertEqual(competition.get_etat(), 'Inscription ouverte')
        competition.set_date_fin_inscription(date.today())
        competition.set_date(date.today())
        self.assertEqual(competition.get_etat(), 'En cours')
        competition.set_date_fin_inscription(None)
        self.assertEqual(competition.get_etat(), 'Pas disponible')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5, False)
        sortie = (
            'Competition : 1, Escrime comp, 14-05-2004, 14-05-2004, été, '
            'Lieu : Une grande ville Paris France 1 |, Arme : 1 - '
            'Epée Homme - M |, Catégorie : 2 - U20 | |')
        self.assertEqual(str(competition), sortie)
