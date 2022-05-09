"""
Kapitel 21
Author: Ali Abas Arsalahn
Datum: 02.05.2022
"""

import math



class ListCheckAndSQRT:
    """
    Klasse: ListCheckAndSQRT
    Eigenschaften: -/-
    Methoden:
    """

    @staticmethod
    def is_empty_list(liste: list[any]) -> bool:
        """Nimmt eine Liste als Argument. überprüft ob die Liste leer ist."""
        if not list.__instancecheck__(liste):
            raise TypeError
        return True if len(liste) == 0 else False

    @staticmethod
    def squareroot(zahl: int) -> float:
        """Nimmt eine Zahl als Argument. Gibt die Wurzel der Zahl wieder."""
        if zahl < 0:
            raise ValueError
        return math.sqrt(zahl)
