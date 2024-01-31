# -*- coding: utf-8 -*-
"""

The object-oriented data treating of the database.

A father class "Match" and a son class "Event".

@author: Mingyu LIAO
"""
import numpy as np

import data_events
from data_events import results_E0, results_SP1, results_D1, results_I1, results_F1 # , events_SP1, events_I1, events_F1, events_E0, events_D1


#father class "Match"
class Match:
    def __init__(self, id_odsp =None, date=None, league=None, season=None, country=None, ht=None, at=None, htscore=None, atscore=None, oddh= None, oddd= None ,odda = None):
        self.id_odsp = id_odsp
        self.date = date
        self.league = league
        self.season = season
        self.country = country
        self.ht = ht
        self.at = at
        self.htscore = htscore
        self.atscore = atscore
        self.oddh = oddh
        self.oddd = oddd
        self.odda = odda
        
    def update_score(self, htscore, atscore):
        self.htscore = htscore
        self.atscore = atscore

    def get_winner(self):
        if self.htscore > self.atscore:
            return f"{self.ht} wins!"
        elif self.atscore > self.htscore:
            return f"{self.at} wins!"
        else:
            return "It's a draw!"

    def find_match_index(database, date, home_team, away_team):
        for match in database:
            if match.date == date and match.ht == home_team and match.at == away_team:
                return match.id
            return -1  # Return -1 if the match is not found in the database
    
    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id   
    
    def get_odda(self):
        return self.odda

    def set_odda(self, new_odda):
        self.odda = new_odda
        
    def get_oddd(self):
        return self.oddd

    def set_oddd(self, new_oddd):
        self.oddd = new_oddd
        
    def get_oddh(self):
        return self.oddh

    def set_oddh(self, new_oddh):
        self.oddh = new_oddh

    def get_league(self):
        return self.league

    def set_league(self, new_league):
        self.league = new_league

    def get_season(self):
        return self.season

    def set_season(self, new_season):
        self.season = new_season
        
    def display_match_details(self):
        print(f"Match Details:")
        print(f"Id: {self.id_odsp}")
        print(f"Date: {self.date}")
        print(f"League: {self.league}")
        print(f"Season: {self.season}")
        print(f"Country: {self.country}")
        print(f"Home Team: {self.ht}")
        print(f"Away Team: {self.at}")
        print(f"Home Team Score: {self.htscore}")
        print(f"Away Team Score: {self.atscore}")
        
    def set_match_data(self, data):
        self.id_odsp = data[0]
        self.date = data[3]
        self.league = data[4]
        self.season = data[5]
        self.country = data[6]
        self.ht = data[7]
        self.at = data[8]
        self.htscore = data[9]
        self.atscore = data[10]
        self.oddh = data[11]
        self.oddd = data[12]
        self.odda = data[13]


# class "Event"

class Event():
    def __init__(self, id_odsp=None, id_event=None, minutes=None, sorted_time=None, discription=None,
                 event_type=None, side=None, player1=None, player2=None, event_type2=None):
        self.id_odsp = id_odsp
        self.id_event = id_event
        self.minutes = minutes
        self.sorted_time = sorted_time
        self.discription = discription
        self.event_type = event_type
        self.event_type2 = event_type2
        self.side = side
        self.player1 = player1
        self.player2 = player2

    def set_event_data(self, data):
        self.id_odsp = data[0]
        self.id_event = data[1]
        self.minutes = data[3]
        self.sorted_time = data[2]
        self.discription = data[4]
        self.event_type = data[5]
        self.side = data[7]
        self.player1 = data[10]
        self.player2 = data[11]
        self.event_type2 = data[6]

    def display_event_details(self):
        print(f"Event Details:")
        print(f"Sorted Time Order: {self.sorted_time}")
        print(f"Minutes: {self.minutes}")
        print(f"Event Type: {self.event_type} and {self.event_type2}")
        print(f"Side: {self.side}")
        print(f"Player 1: {self.player1}")
        if self.player2:
            print(f"Player 2: {self.player2}")

    def check_event_match(self, match):
        if self.id_odsp == match.id_odsp:
            print("Is the same match")
        else:
            print("Not the same match")

    def check_if_attempt(self):
        if not isinstance(self.event_type2, float) or not np.isnan(self.event_type2):
            return True
        else:
            return False




'''
# Example usage:
if __name__ == "__main__":
    # Create a Match object


    #match_test = results_D1[results_D1['id_odsp'] == 'UFot0hit/']
    #events_test = events[events['id_odsp'] == 'UFot0hit/']
    #event_test  = events_test[events_test['id_event'] == 'UFot0hit1']
    
    
    #match = Match(match_test.iloc[0,0],match_test.iloc[0,3],match_test.iloc[0,4],match_test.iloc[0,5],match_test.iloc[0,6],match_test.iloc[0,7],match_test.iloc[0,8],match_test.iloc[0,9],match_test.iloc[0,10])
    #match.display_match_details()
    #print(match.get_winner())
    #event = Event.from_match(match, event_test.iloc[0,3], event_test.iloc[0,2],event_test.iloc[0,5],event_test.iloc[0,7],event_test.iloc[0,10],event_test.iloc[0,11])
    
    #match1 = Match()
    #match1.set_match_data(match_test)
    #match1.display_match_details()
    #print(match1.get_winner())
    
    #event1 = Event.from_match(match1)
    #event1.set_event_data(event_test)
    #event1.display_event_details()
    
    
    #把两千场英超全存为match对象
    matches_objects = []
    for index, row in results_E0.iterrows():
        match_object = Match()
        match_object.set_match_data(row)
        matches_objects.append(match_object)
'''
E0_results = []
SP1_results = []
D1_results = []
I1_results = []
F1_results = []
for index, row in results_E0.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    E0_results.append(match_object)
for index, row in results_SP1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    SP1_results.append(match_object)
for index, row in results_D1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    D1_results.append(match_object)
for index, row in results_I1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    I1_results.append(match_object)
for index, row in results_F1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    F1_results.append(match_object)

E0_event = []
SP1_event = []
D1_event = []
I1_event = []
F1_event = []

'''
for index, row in events_E0.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    E0_event.append(match_object)
for index, row in events_SP1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    SP1_event.append(match_object)
for index, row in events_D1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    D1_event.append(match_object)
for index, row in events_I1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    I1_event.append(match_object)
for index, row in events_F1.iterrows():
    match_object = Match()
    match_object.set_match_data(row)
    F1_event.append(match_object)
'''


def choosed_team_result(input_team):
    results_team = data_events.select_team_result(input_team)
    team_result = []
    for index, row in results_team.iterrows():
        match_object = Match()
        match_object.set_match_data(row)
        team_result.append(match_object)

    return team_result

def get_event_from_result(id_odsp):
    events_team = data_events.corresponding_event(id_odsp)
    team_event = []
    for index, row in events_team.iterrows():
        match_object = Event()
        match_object.set_event_data(row)
        team_event.append(match_object)
    return team_event

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    