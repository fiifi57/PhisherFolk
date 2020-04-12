#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun April 04 12:44am 2020

@authors: arhin@rpi.edu
"""
import sys 

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings("ignore", category=DeprecationWarning)

import numpy as np
import pandas as pd

from nltk.corpus import wordnet as wn

class phf:
    def get_roots(root_word, level):
        '''
        root_word - the main word for which you are trying to find synonyms
        level - how deep down the tree you want the search to go (range is 3)
        '''
        
        if level == 0:
            return root_word
        
        
        if level == 1:
            # get synonyms of root_word
            level_1 = []
            for syn in wn.synsets(root_word): 
                for le in syn.lemmas(): 
                    level_1.append(le.name()) 
            return set(level_1)
                
        if level == 2:
            # get synonyms of root_word
            level_1 = []
            for syn in wn.synsets(root_word): 
                for le in syn.lemmas(): 
                    level_1.append(le.name()) 

            # get all related words of synonyms in level_1
            level_2 = []
            for l1 in set(level_1):
                for syn in wn.synsets(l1): 
                    for le in syn.lemmas(): 
                        level_2.append(le.name())
            return set(level_2)
        
        
        if level == 3:                 
            # get synonyms of root_word
            level_1 = []
            for syn in wn.synsets(root_word): 
                for le in syn.lemmas(): 
                    level_1.append(le.name()) 

            # get all related words of synonyms in level_1
            level_2 = []
            for l1 in set(level_1):
                for syn in wn.synsets(l1): 
                    for le in syn.lemmas(): 
                        level_2.append(le.name())

            # get all related words level_2 (include nouns, verbs, etc)
            level_3a = []
            for l2 in level_2:
                for syn in wn.synsets(l2):
                    level_3a.append(syn)

            level_3b = []
            for i, syn in enumerate(level_3a):
                level_3b.append(syn.lemma_names())
                level_3c = ",".join([item for sublist in level_3b for item in sublist])
                level_3c = level_3c.split(",")

            return set(level_3c)