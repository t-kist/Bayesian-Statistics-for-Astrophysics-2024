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
<<<<<<< HEAD
    elif name == 'Myrdhin'
        n = 73
=======
    elif name == 'Niels':
        n = 21
    elif name == 'Benthe': 
        n = 29
>>>>>>> 427076e47668d6597ca8a3f07b69250897888f9f
    else:
        raise ValueError("Person {:s} not recognized.".format(name))

    return n
