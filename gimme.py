import yaml

with open('teams.yaml', 'r') as f:
    TEAMS = yaml.load(f)

team_db = {}

for team in TEAMS:
    team_db[team['id']] = team

def gimme(team):
    tm = team_db[team.upper()]
    if 'team' in tm:
        print "{0}: {1}".format(tm['id'], tm['team'].encode('utf-8'))
    else:
        print tm['id']
    if 'college' in tm:
        print "{0}".format(tm['college'].encode('utf-8'))
    for note in tm.get('notes', ()):
        items = note.split('-')
        for item in items:
            print " - {0}".format(item.strip().encode('utf-8'))
    print ""

import sys

for arg in sys.argv[1:]:
    gimme(arg)

