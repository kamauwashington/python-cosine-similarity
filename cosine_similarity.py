from typing import OrderedDict, List, Tuple
import math
import re

# simple pattern to extract words based on word boundary
pattern = re.compile(r'\w+')


# this function seperates words in a body of text, this can be expanded to remove non alpha numerics within words
def gather_words (input : str) -> List[str] :

    # words are lowercased to allow for easier matching between sets of words
    return list(map(lambda w : w.lower(), re.findall(pattern,input)))


# this function counts the occurances of words in two bodys of text obtaining two vectors of equal length.
# these vectors are used to calculate the cosine distance https://en.wikipedia.org/wiki/Cosine_similarity 
def cosine_similarity (inputA : str, inputB : str) -> Tuple[List[int],List[int]] :

    # an ordered dictionary is used to ensure that further calculations or aggregations are evaluated in order
    catalog : OrderedDict[str,Tuple[int,int]] = OrderedDict()

    # using the words in inputA, add 1 the Tuple's first position to indicate an occurance of a word
    for word in gather_words(inputA) :
        # Tuples cannot be updated so, geting and setting is the approach taken
        tupe : Tuple[int,int] = catalog.get(word) or (0,0)
        # increment tuple representing the current word in inputA
        catalog[word] = tupe[0]+1,0
    
    # using the words in inputB, add 1 the Tuple's second position to indicate an occurance of a word
    for word in gather_words(inputB) :
        # Tuples cannot be updated so, geting and setting is the approach taken
        tupe : Tuple[int,int] = catalog.get(word) or (0,0)
        # increment tuple representing the current word in inputB
        catalog[word] = tupe[0],tupe[1]+1

    # ~~~~~~~~~~~~~~~~~~ this is the true "cosine similarity" where vectors are compared vs words ~~~~~~~~~~~~~~~~~~ #

    # https://en.wikipedia.org/wiki/Dot_product
    # dot_prod = (v1[0] * v2[0]) + (v1[1] * v2[1]) * ..... (v1[n] * v2[n])
    dot_product : float = 0

    # https://en.wikipedia.org/wiki/Magnitude_(mathematics)
    # magnitued is a number's distance from 0
    magnitude_of_a : float = 0
    magnitude_of_b : float = 0

    # items() returns an enumerable vs a list. If iterated as a list, each item is [key,Tuple] not Tuple (IMPORTANT)
    for word,vectors in  catalog.items() :
        dot_product += vectors[0] * vectors[1]
        magnitude_of_a += math.pow(vectors[0], 2) 
        magnitude_of_b += math.pow(vectors[1], 2)

    cos_sim : float = dot_product / (math.sqrt(magnitude_of_a) * math.sqrt(magnitude_of_b))
    return round(cos_sim,2)

print(cosine_similarity("my cat has fleas in its fur","my cat has ticks in the fur on its head"))