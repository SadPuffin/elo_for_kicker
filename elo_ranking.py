#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:48:38 2021

@author: freshharakl
"""

default_rank = 1400


def expected(Ra, Rb):
    '''

    Parameters
    ----------
    Ra : int
        рейтинг игрока A;.
    Rb : int
       рейтинг игрока B.

    Returns
    -------
    E : float
        Oжидаемое количество очков, 
        которое наберёт игрок A в партии с B.

    '''
    E = 1 / (1 + 10**((Rb-Ra)/400))
    return E

def elo(Ra, Score, E):
    '''
    Parameters
    ----------
    Ra : TYPE
        рейтинг игрока A.
    Score : float
        Фактически набранное игроком A количество очков 
        (1 очко за победу, 0,5 — за ничью и 0 — за поражение
    E : float
        Oжидаемое количество очков, 
        которое наберёт игрок A в партии с B..

    Returns
    -------
    rank : int
        DESCRIPTION.

    '''
    if Ra >= 2400:
        k = 10
    elif (Ra < 2400)&(Ra > default_rank):
        k = 20
    else:        
        k = 40
    
    rank = Ra + k * (Score - E)
    return rank

def team_play(a1, a2, b1, b2, Score):
    mean_a = (a1 + a2) / 2
    mean_b = (b1 + b2) / 2
    Ea = expected(mean_a, mean_b)
    Eb = expected(mean_b, mean_a)
    rank_a = elo(mean_a, Score, Ea)
    rank_b = elo(mean_b, abs(1 - Score), Eb)
    a1 += rank_a - mean_a
    a2 += rank_a - mean_a
    b1 += rank_b - mean_b
    b2 += rank_b - mean_b
    return a1, a2, b1, b2, rank_a, rank_b
    
