import yaml

with open('teams.yaml', 'r') as f:
    TEAMS = yaml.load(f)

team_db = {}

for team in TEAMS:
    team_db[team['id']] = team

def gimme(team):
    tm = team_db[team.upper()]
    print "{0}: {1}".format(tm['id'], tm['team'])
    print "{0}".format(tm['college'])
    for note in tm['notes']:
        print " - {0}".format(note)
    print ""

import sys

for arg in sys.argv[1:]:
    gimme(arg)

