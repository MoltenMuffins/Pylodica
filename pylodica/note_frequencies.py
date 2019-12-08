import numpy as np

SAMPLING_FREQUENCY = 8000

def tone_frequency(n):
    '''
    Formula for calculating the frequency of the nth key
    '''
    return 440 * (((2)**(1/12))**(n-49))

# TODO: Figure out how many notes we wanna start out with?
NOTE_DICT = {k+1:tone_frequency(k+49) for k in range(12)}

if __name__ == "__main__":
    print(NOTE_DICT)