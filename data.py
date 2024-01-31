# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:37:50 2024

@author: Mingyu LIAO

file title: data treatment

description: treat the data and provides the functions to calculate detail information of the match
"""

import numpy as np
import pandas
import csv
from class_file import Match
from class_file import Event
from class_file import Shoot

results = pandas.read_csv("archive/ginf.csv")   #read the database
events = pandas.read_csv("archive/events.csv")   #read the database


def extract_all_events(id_odsp):
    '''
    Parameters
    ----------
    id_odsp : str
        the id of the given game
    -------
    
    Return
    ----------
    events_objects : list
        a list of data type Event containing all the objects of the given match
    -------
    
    This function creates a list of data type Event containing all the objects of the given match.
    
    ps. input of data events is necessary:
    #events = pandas.read_csv("archive/events.csv")
    '''
    events_chosen = events[events['id_odsp'] == id_odsp]

    events_objects = []
    for index,row in events_chosen.iterrows():
        event_object = Event()
        event_object.set_event_data(row)
        events_objects.append(event_object)
    return events_objects
        
        


def extract_all_location(id_odsp):
    '''
    Parameters
    ----------
    id_odsp : str
        the id of the given game
    -------
    This function creates a list of data type Event containing all the objects of the given match.
    
    ps. input of data events is necessary:
    #events = pandas.read_csv("archive/events.csv")
    '''
    location_objects = []
    events_chosen = events[events['id_odsp'] == id_odsp]  
    locations = pandas.DataFrame(columns=events_chosen.columns)
    
    for index, value in enumerate(events_chosen['location']):
        if not pandas.isna(value) and isinstance(value, (float, np.float64)):
            locations = locations.append(events_chosen.iloc[index])
            
    for index,row in locations.iterrows():
        location_object = Event()
        location_object.set_event_data(row)
        location_objects.append(location_object)
    return location_objects


def extract_all_pass(location_objects):
    for item in location_objects:
        if not np.isnan(item.location):
            location_objects.remove(item)
    return location_objects

def extract_all_shoot(id_odsp):
    
    shoot_objects = []
    events_chosen = events[events['id_odsp'] == id_odsp]
    shoots = pandas.DataFrame(columns=events_chosen.columns)
    
    for index, value in enumerate(events_chosen['shot_place']):
        if not pandas.isna(value) and isinstance(value, (float, np.float64)):
            shoots = shoots.append(events_chosen.iloc[index])
            
    for index,row in shoots.iterrows():
        shoot_object = Shoot()
        shoot_object.set_shoot_data(row)
        shoot_objects.append(shoot_object)
    return shoot_objects



def calculate_attack_distribution(location_objects):
    '''
    Parameters
    ----------
    location_objects : list of object Event

    Returns
    -------
    output : a matrix which describes the attack distribution of home team and away team

    '''
    #initialization of matrix
    output = np.array([[0, 0],             #left away team & home team
                   [0, 0],                 #center away team & home team
                   [0, 0]],  dtype=float)  #right away team & home team

    #calculate different location appearance
    #board = np.empty((2, 19), dtype=float)
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #home team
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #away team
    for obj in location_objects:
        if obj.side == 1:
            board[0][int(obj.location)-1] +=1
        if obj.side == 2:
            board[1][int(obj.location)-1] +=1


    output[0][1]= board[0][0]*0.2 + board[0][3] + board[0][8] + board[0][6] + board[0][9]                               #home team left
    output[1][1]= board[0][0]*0.6 + board[0][3] + board[0][12] + board[0][13] + board[0][5]+ board[0][15]+ board[0][14] #home team center
    output[2][1]= board[0][0]*0.2 + board[0][10] + board[0][4] + board[0][7] + board[0][11]                             #home team right
    output[0][0]= board[1][0]*0.2 + board[1][3] + board[1][8] + board[1][6] + board[1][9]                               #home team left
    output[1][0]= board[1][0]*0.6 + board[1][3] + board[1][12] + board[1][13] + board[1][5]+ board[1][15]+ board[1][14] #home team center
    output[2][0]= board[1][0]*0.2 + board[1][10] + board[1][4] + board[1][7] + board[1][11]                             #home team right
    #uniformization home team
    a=output[1][1]+output[0][1]+output[2][1]
    output[0][1]= output[0][1]/a
    output[1][1]= output[1][1]/a
    output[2][1]= output[2][1]/a
    #uniformization away team
    b=output[1][0]+output[0][0]+output[2][0]
    output[0][0]= output[0][0]/b
    output[1][0]= output[1][0]/b
    output[2][0]= output[2][0]/b

    
    return output

def calculate_pass_distribution(location_objects):
    '''
    Parameters
    ----------
    location_objects : list of object Event

    Returns
    -------
    output : a matrix which describes the pass distribution of home team and away team

    '''
    #initialization of matrix
    output = np.array([[0, 0],             #left away team & home team
                   [0, 0],                 #center away team & home team
                   [0, 0]],  dtype=float)  #right away team & home team

    #calculate different location appearance
    #board = np.empty((2, 19), dtype=float)
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #home team
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #away team
    for obj in location_objects:
        if obj.side == 1:
            board[0][int(obj.location)-1] +=1
        if obj.side == 2:
            board[1][int(obj.location)-1] +=1


    output[0][1]= board[0][0]*0.2 + board[0][3] + board[0][8] + board[0][6] + board[0][9]                               #home team left
    output[1][1]= board[0][0]*0.6 + board[0][3] + board[0][12] + board[0][13] + board[0][5]+ board[0][15]+ board[0][14] #home team center
    output[2][1]= board[0][0]*0.2 + board[0][10] + board[0][4] + board[0][7] + board[0][11]                             #home team right
    output[0][0]= board[1][0]*0.2 + board[1][3] + board[1][8] + board[1][6] + board[1][9]                               #home team left
    output[1][0]= board[1][0]*0.6 + board[1][3] + board[1][12] + board[1][13] + board[1][5]+ board[1][15]+ board[1][14] #home team center
    output[2][0]= board[1][0]*0.2 + board[1][10] + board[1][4] + board[1][7] + board[1][11]                             #home team right
    #uniformization home team
    a=output[1][1]+output[0][1]+output[2][1]
    output[0][1]= output[0][1]/a
    output[1][1]= output[1][1]/a
    output[2][1]= output[2][1]/a
    #uniformization away team
    b=output[1][0]+output[0][0]+output[2][0]
    output[0][0]= output[0][0]/b
    output[1][0]= output[1][0]/b
    output[2][0]= output[2][0]/b

    
    return output
    
    
def calculate_heat_map(location_objects):
    '''
    Parameters
    ----------
    location_objects : list of object Event

    Returns
    -------
    output : a matrix which describes the heat map of home team and away team

    '''
    #initialization of heat map
    heatmap = np.array([[0, 0, 0, 0],             #upper side of heat map
                   [0, 0, 0, 0],                  #center side of heat map
                   [0, 0, 0, 0]],  dtype=float)   #lower side of heat map
    
    #calculate different location appearance
    #board = np.empty((2, 19), dtype=float)
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #home team
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #away team
    for obj in location_objects:
        if obj.side == 1:
            board[0][int(obj.location)-1] +=1
        if obj.side == 2:
            board[1][int(obj.location)-1] +=1
    #home team side
    heatmap[0][3]= board[0][0]*0.1 + board[0][8] + board[0][3]*0.5                    #home team left front
    heatmap[1][3]= board[0][0]*0.3 + board[0][2] + board[0][12] + board[0][13]        #home team center front
    heatmap[2][3]= board[0][0]*0.1 + board[0][10] + board[0][4]*0.5                   #home team right front
    heatmap[0][2]= board[0][0]*0.1 + board[0][6] + board[0][3]*0.5 + board[0][9]      #home team left back
    heatmap[1][2]= board[0][0]*0.3 + board[0][5] + board[0][15] + board[0][14]        #home team center back
    heatmap[2][2]= board[0][0]*0.1 + board[0][7] + board[0][4]*0.5 + board[0][11]     #home team right back
    #away team side
    heatmap[2][0]= board[1][0]*0.1 + board[1][8] + board[1][3]*0.5                    #home team left front
    heatmap[1][0]= board[1][0]*0.3 + board[1][2] + board[1][12] + board[1][13]        #home team center front
    heatmap[0][0]= board[1][0]*0.1 + board[1][10] + board[1][4]*0.5                   #home team right front
    heatmap[2][1]= board[1][0]*0.1 + board[1][6] + board[1][3]*0.5 + board[1][9]      #home team left back
    heatmap[1][1]= board[1][0]*0.3 + board[1][5] + board[1][15] + board[1][14]        #home team center back
    heatmap[1][1]= board[1][0]*0.1 + board[1][7] + board[1][4]*0.5 + board[1][11]     #home team right back
    
    return heatmap
'''
def calculate_heat_map_advanced(location_objects):
        
    #initialization of heat map
    heatmap = np.zeros((8, 6))
    
    for obj in location_objects:
        if obj.side == 1:
            if obj.location == 1:
                middle_col = matrix.shape[1] // 2
                heatmap[:, middle_col:] += 0.1
            if obj.location == 2:
                middle_col = matrix.shape[1] // 2
                heatmap[:, :middle_col] += 0.1
            if obj.location == 3:
                heatmap
            if obj.location == 4:
        
    #home team side
    
    
    
    
    return heatmap
'''

def calculate_shoot_map(shoot_objects):
    shoot_map=[0, 0, 0, 0, 4, 0, 0, 0,0, 0]
    is_goal = [0, 0, 0, 0, 0, 0, 0, 0,0, 0]
    '''
    8	Misses to the left
    12	Top left corner
    11	top centre of the goal
    13	Top right corner
    3	Bottom left corner
    5	Centre of the goal
    4	Bottom right corner
    9	Misses to the right
    1	Bit too high
    7	Hits the bar
    '''
    for item in shoot_objects:
        if item.shot_place == 1:
            shoot_map[8] +=1
            if item.is_goal == 1:
                is_goal[8] +=1
        if item.shot_place == 3:
            shoot_map[4] +=1
            if item.is_goal == 1:
                is_goal[4] +=1
        if item.shot_place == 4:
            shoot_map[6] +=1
            if item.is_goal == 1:
                is_goal[6] +=1
        if item.shot_place == 5:
            shoot_map[5] +=1
            if item.is_goal == 1:
                is_goal[5] +=1
        if item.shot_place == 6:
            shoot_map[8] +=1
            if item.is_goal == 1:
                is_goal[8] +=1
        if item.shot_place == 7:
            shoot_map[9] +=1
            if item.is_goal == 1:
                is_goal[9] +=1
        if item.shot_place == 8:
            shoot_map[0] +=1
            if item.is_goal == 1:
                is_goal[0] +=1
        if item.shot_place == 9:
            shoot_map[7] +=1
            if item.is_goal == 1:
                is_goal[7] +=1
        if item.shot_place == 10:
            shoot_map[8] +=1
            if item.is_goal == 1:
                is_goal[8] +=1
        if item.shot_place == 11:
            shoot_map[2] +=1
            if item.is_goal == 1:
                is_goal[2] +=1
        if item.shot_place == 12:
            shoot_map[1] +=1
            if item.is_goal == 1:
                is_goal[1] +=1
        if item.shot_place == 13:
            shoot_map[4] +=3
            if item.is_goal == 1:
                is_goal[4] +=1
    
    
    return shoot_map,is_goal

def extract_one_team(name):
    match_history = []
    matches = results[(results['ht'].astype(str) == name) | (results['at'].astype(str) == name)]
    for index,row in matches.iterrows():
        match = Match()
        match.set_match_data(row)
        match_history.append(match)
    
    return match_history

def extract_two_team(home_team, away_team):
    match_history = []
    matches = results[((results['ht'].astype(str) == home_team) & (results['at'].astype(str) == away_team) 
                       | (results['ht'].astype(str) == away_team) & (results['at'].astype(str) == home_team))]
    for index,row in matches.iterrows():
        match = Match()
        match.set_match_data(row)
        match_history.append(match)
    
    return match_history

def calculate_total_score(team_name):
    score =0
    match_history=extract_one_team(team_name)
    for item in match_history:
        if item.at == team_name:
            score = score + item.atscore
        if item.ht == team_name:
            score = score + item.htscore
            
    return score
    



# Example usage:
if __name__ == "__main__":
    
    id_odsp='UFot0hit/'
    events_chosen = events[events['id_odsp'] == id_odsp]
    location_objects = extract_all_location(id_odsp)
    shoot_objects = extract_all_shoot(id_odsp)
    shoot_map,is_goal = calculate_shoot_map(shoot_objects)
    print('shoot map:')
    print(shoot_map)
    print('is goal:')
    print(is_goal)
    
    
    attack_distribition = calculate_attack_distribution(location_objects)
    print('attack distribution:')
    print(attack_distribition)
    
    pass_objects = extract_all_pass(location_objects)
    pass_distribition = calculate_pass_distribution(pass_objects)
    print('pass distribution:')
    print(pass_distribition)
    
    heat_map = calculate_heat_map(location_objects)
    print('heat map:')
    print(heat_map)
    
    
    name1 = 'Bordeaux'
    name2 = 'Lyon'
    match_history = extract_one_team(name2)
    total_score = calculate_total_score(name2)
    print('total score:')
    print(total_score)















