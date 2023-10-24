"""
Module contenant la classe PhaseFinal
"""


class PhaseFinal:
    """
    Une classe permettant de représenter une phase finale

    Attributes:
    ___________
        id_phase_f (int): id de la phase finale

    Methods:
    ________
        get_id_phase_f(self): retourne l'id de la phase finale
        set_id_phase_f(self, id_phase_f: int): modifie l'id de la phase finale
    """

    def __init__(self, id_phase_f: int):
        """Fonction d'instanciation de la classe PhaseFinal

        Args:
            id_phase_f (int): id de la phase finale
        """
        self.id_phase_f = id_phase_f

    def get_id_phase_f(self) -> int:
        """
        Fonction qui retourne l'id de la phase finale

        Returns:
            int: id de la phase finale
        """
        return self.id_phase_f

    def set_id_phase_f(self, id_phase_f: int) -> None:
        """
        Fonction qui modifie l'id de la phase finale

        Args:
            id_phase_f (int): id de la phase finale
        """
        self.id_phase_f = id_phase_f

    def __str__(self):
        return f'{self.id_phase_f}'
