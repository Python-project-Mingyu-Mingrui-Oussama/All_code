# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:37:50 2024

@author: Mingyu LIAO

file title: project database with data from ginf.csv and events.csv


"""

import numpy as np
import pandas
import csv

results = pandas.read_csv("archive/ginf.csv")   #read the database
events = pandas.read_csv("archive/events.csv")   #read the database

#print(results)


# <codecell>

#leagues = results['league']           #extract all the league data

results_E0 = results[results['league'] == 'E0']  #extract primer league data

#print(results_E0)

results_D1 = results[results['league'] == 'D1']  #extract bundesliga data
results_F1 = results[results['league'] == 'F1']  #extract ligue 1 data
results_SP1 = results[results['league'] == 'SP1']  #extract la liga data
results_I1 = results[results['league'] == 'I1']  #extract seria A data





# <codecell>

match_test = results_D1[results_D1['id_odsp'] == 'UFot0hit/']
events_test = events[events['id_odsp'] == 'UFot0hit/']
event_test  = events_test[events_test['id_event'] == 'UFot0hit1']
goals_test = events_test[events_test['is_goal']==1]

# <codecell>
club_names = pandas.concat([results['ht'], results['at']]).unique()  #get the name list of all the clubes



def select_team_result(input_team):
    results_team_h = results[results['ht'] == input_team]
    results_team_a = results[results['at'] == input_team]

    results_team = pandas.concat([results_team_h, results_team_a], ignore_index=True)
    results_team = results_team.sort_values(by='date')
    return results_team


def corresponding_event(id_odsp):

    return events[events['id_odsp'] == id_odsp]




