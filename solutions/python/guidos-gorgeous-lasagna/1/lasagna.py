"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of pasta layers added in lasagna.
    :return: int - total preparation time derived by 'number_of_layers'.

    Function that takes the number of layers for the lasagna as
    an argument and returns how many minutes you need to prepare it considering a preparation time (stored in the constant PREPARATION_TIME) of 2 minutes per layer based on the `EXPECTED_BAKE_TIME`.
    """
    return number_of_layers* PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time already spent baking (in minutes).
    :return: int - total time elapsed (in minutes) since starting preparation.

    Function that takes the number of layers for the lasagna and the elapsed       baking time (in minutes) as an argument and returns how many minutes elapsed since starting to prepare the lasagna based on the `number_of_layers` and 'elapsed_bake_time'.
    """
    return (number_of_layers*PREPARATION_TIME) + elapsed_bake_time

