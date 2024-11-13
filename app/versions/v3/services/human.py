from app.versions.v3.models.human import Human
from app.versions.v3.classes.human import Human as HumanClass


def is_mutant(dna):
    """
    Check if the DNA is from a mutant
    :param dna:
    :return:
    """
    is_mutant_var = HumanClass().is_mutant(dna)
    Human().save_human(dna, is_mutant_var)
    return is_mutant_var

def stats():
    """
    Get the stats of the humans
    :return:
    """
    return Human().get_stats()