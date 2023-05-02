#!/usr/bin/env python3

def return_evens(num_list):
    evens = [int for int in num_list if int % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    exclamations = [str + "!" for str in sentence_list]
    return exclamations