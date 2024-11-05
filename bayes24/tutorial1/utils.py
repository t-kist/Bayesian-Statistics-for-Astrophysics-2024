import numpy as np

from IPython import embed

def get_favorite_number(name):
    """
    Print the favorite number of a person.

    Args:
        name (str):
            The name of the person.

    Returns:
        n (float):
            The favorite number of the person.
    """

    if name == 'Alice':
        n = np.pi
    elif name == 'Bob':
        n = np.random.randint(1, 100)
    elif name == 'Timo':
        n = 42
    elif name == 'Niels':
        n = 21
    elif name == 'Benthe':
        n = 29
    elif name == 'Mara':
        n = 100
    else:
        raise ValueError("Person {:s} not recognized.".format(name))

    return n