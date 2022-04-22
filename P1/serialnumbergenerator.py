# Projekt: Seriennummergenerator \ Modul: serialnumbergenerator
# Author: Ali Abas Arsalahn
# Datum: 12.03.2022
"""Serialnumbergenerator module"""

from io import UnsupportedOperation
from random import randrange
from string import ascii_letters, digits
import json


class SerialnumberGenerator():
    """Methods: generate_serialnumber, save_serialnumber, validate_serialnumber."""

    def __init__(self) -> None:
        self.sn_map = {"keys": {}}

    def generate_serialnumber(self, sn_type: str, count: int, key_rows: int, row_length: int) -> None:
        """Generates a Serialnumber based on type.
        Takes quantity, rows and row_length as Argmuments"""

        def generate_letter() -> str:
            """returns a random letter."""
            rnd_nmb = randrange(len(ascii_letters) - 1)
            return ascii_letters[rnd_nmb]

        def generate_digit() -> str:
            """returns a random digit."""
            rnd_nmb = randrange((len(digits)) - 1)
            return digits[rnd_nmb]

        def generate_string(sn_type: str, count: int, rows: int, row_length: int, tmp_list: list) -> list:
            """
            Generates Serialnumbers based on type.
            Returns created serialnumbers as item in a list.
            """
            key = ''
            for i in range(rows * row_length):
                key += generate_letter() if sn_type == 'letter' else generate_digit()

            tmp_list.append(key)
            if count <= 1:
                return tmp_list
            else:
                return generate_string(sn_type, (count - 1), rows, row_length, tmp_list)

        tmp_list = []
        end_list = generate_string(
            sn_type, count, key_rows, row_length, tmp_list)
        for key in end_list:
            self.sn_map["keys"][key] = True

    def validate_serialnumber(self, validate_serialnumber: str, directory: str, load_filename: str) -> None:
        """Takes a string as an argument and checks if it is valid a valid serialnumber."""
        with open(directory + f"/{load_filename}", 'r', encoding="utf_8") as file:
            data = json.load(file)
            try:
                if data["keys"][validate_serialnumber]:
                    print("key is valid!")
                else:
                    print("key is not valid")
            except KeyError:
                print("key not found!")

    def save_serialnumber(self, save_directory: str, save_filename: str) -> None:
        """writes existing keys to a json file."""
        try:
            with open(save_directory + f"/{save_filename}", "r", encoding="utf-8") as file:
                data = json.load(file)
            for serialnumber in self.sn_map["keys"]:
                data["keys"][serialnumber] = True
            with open((save_directory + f"/{save_filename}"), "r+", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except (UnsupportedOperation, FileNotFoundError, json.decoder.JSONDecodeError):
            with open((save_directory + f"/{save_filename}"), "w", encoding="utf-8") as file:
                json.dump(self.sn_map, file, indent=4)
