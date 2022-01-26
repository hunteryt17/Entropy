import numpy as np

def entropy(probs):
    """ Asssumes that input is a numpy array and 
        that it is a valid probability vector."""
    entropy_value = -(probs * np.log(probs))
    return entropy_value

if __name__ == "__main__":
    pass
