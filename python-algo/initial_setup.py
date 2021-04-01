#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:16:54 2021

@author: alrick
"""

"""
Spawning intial structure.
"""

def spawn_initial_structure():
    """
    Inputs: None (Fixed starting strategy)
    Outputs: Coordinates of structure units at the start of the game.
    
    Description: Return positions of Wall, Turrets and Support at the start of 
    game. Function is called in Algo_strategy.strategy function when turn==0.
    """
    
    #U-shape WALL
    WALL_LOC = [[12,4],[11,5],[10,6],[9,7],[8,8],[7,9],[6,10],[5,11],[4,12],\
                [15,4],[16,5],[17,6],[18,7],[19,8],[20,9],[21,10],[22,11],[23,12],[24,13]]
    
    #TURRETs at end positions
    TURR_LOC = [[4,11],[6,9],[24,12],[22,10]]
    
    #SUPPORTS CURRENTLY NOT DECIDED EXACT LOCATIONS.
    
    return [WALL_LOC, TURR_LOC]