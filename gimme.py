import yaml

with open('teams.yaml', 'r') as f:
    TEAMS = yaml.load(f)

team_db = {}

for team in TEAMS:
    team_db[team['id']] = team

def gimme(team):
    tm = team_db[team.upper()]
    if 'team' in tm:
        print "{0}: {1}".format(tm['id'], tm['team'])
    else
        print tm['id']
    if 'college' in tm:
        print "{0}".format(tm['college'])
    for note in tm.get('notes', ()):
        print " - {0}".format(note)
    print ""

import sys

for arg in sys.argv[1:]:
    gimme(arg)

