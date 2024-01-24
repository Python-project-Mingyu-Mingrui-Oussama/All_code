# -*- coding: utf-8 -*-
"""

The object-oriented data treating of the database.

A father class "Match" containing all the information of a football match.
A father class "Event" containing the information of a event in a specific match, like goal, penalty, foul.
A son class "Substitution" inherited from the "Event", which contains information of a substitution.
A son class "Attempt" inherited from the "Event", which contains information of an attempt.

@author: Mingyu LIAO
"""

import numpy as np

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
        
        
        
#class "Event"

class Event():
    def __init__(self, id_odsp=None, id_event=None, minutes=None, sorted_time=None, discription=None, 
                 event_type=None, side=None, player1=None, player2=None, event_type2=None, location=None):
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
        self.location = location

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
        self.location = data[17]
        
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
        
    def check_if_location(self):
        if not isinstance(self.location, float) or not np.isnan(self.location):
            return True
        else:
            return False
            
class Attempt(Event):
    def __init__(self, shot_place=None, shot_outcome=None, is_goal=None, location=None, bodypart=None, assist_method=None, situation=None, **kwargs):
        super().__init__(**kwargs)
        self.shot_place = shot_place
        self.shot_outcome = shot_outcome
        self.is_goal = is_goal
        self.location = location
        self.bodypart = bodypart
        self.assist_method = assist_method
        self.situation = situation
        
    @classmethod
    def from_event(cls, event, shot_place=None, shot_outcome=None, is_goal=None, location=None, bodypart=None, assist_method=None, situation=None):
        return cls(shot_place=shot_place, shot_outcome=shot_outcome, is_goal=is_goal, location=location,
                   bodypart=bodypart, assist_method=assist_method, situation=situation, **vars(event))
        
    def set_attempt_data(self, data):
        self.shot_place = data[14]
        self.shot_outcome = data[15]
        self.is_goal = data[16]
        self.location = data[17]
        self.bodypart = data[18]
        self.assist_method = data[19]
        self.situation = data[20]
        
    def display_attempt_details(self):
        print(f"Attempt Details:")
        print(f"shot_place: {self.shot_place}")
        print(f"is_goal: {self.is_goal}")
        print(f"location: {self.location}")
        print(f"bodypart: {self.bodypart}")
        print(f"assist_method: {self.assist_method}")
        print(f"situation: {self.situation}")
        
        
class Substitution(Event):
    def __init__(self, player_in=None, player_out=None, **kwargs):
        super().__init__(**kwargs)
        self.player_in = player_in
        self.player_out = player_out
        
    @classmethod
    def from_event(cls, event, player_in=None, player_out=None):
        return cls(player_in=player_in, player_out=player_out, **vars(event))
        
        
        
    def set_attempt_data(self, data):
        self.player_in = data.iloc[0,14]
        self.player_out = data.iloc[0,15]
        
        
    def display_attempt_details(self):
        print(f"Substitution:")
        print(f"player in: {self.player_in}")
        print(f"player out: {self.player_out}")
        

'''

# Example usage:
if __name__ == "__main__":
'''
