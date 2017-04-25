# /events
# /elements
# /element-types
# /fixtures
# /teams
# /region
# /transfers (requires auth)
# /entry/{entryId}
# /entries (doesn't work in pre-season?)
# /my-team/{teamId} (requires auth)
# /leagues-entered/{teamId} (requires auth)
# /leagues-classic/{leagueId} (must be a member)
# /leagues-classic-standings/{leagueId}
# /leagues-h2h/{leagueId} (must be a member)
# /leagues-h2h-standings/{leagueId}
import abc
import json

import requests

ROOT = 'https://fantasy.premierleague.com/drf/'


class FplObject(object):
    __metaclass__ = abc.ABCMeta

    _SUFFIX = None

    def __init__(self, info):
        self.__dict__.update(info)

    @classmethod
    def generate(cls):
        response = requests.get('{}{}'.format(ROOT, cls._SUFFIX))

        if response.status_code != 200:
            raise Exception('RequestFailed: {}'.format(response.reason))  # FIXME, should return a custom exception

        data = json.loads(response.content)
        for d in data:
            convert_float_strings(d)
            yield cls(d)

    @classmethod
    def collection(cls):
        return list(cls.generate())

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, {'id': self.id, 'name': self.name})

    def __str__(self):
        return self.__repr__()


class Player(FplObject):
    _SUFFIX = 'elements'

    @property
    def name(self):
        return '{} {}'.format(self.first_name.encode('utf-8'), self.second_name.encode('utf-8'))


class Team(FplObject):
    _SUFFIX = 'teams'


class Fixture(FplObject):
    _SUFFIX = 'fixtures'

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, {'id': self.id})


# convenience methods
get_players = Player.collection
get_teams = Team.collection
get_fixtures = Fixture.collection


def convert_float_strings(d):
    def try_float(s):
        try:
            return float(s)
        except:
            return s

    for k, v in d.iteritems():
        if isinstance(v, dict):
            convert_float_strings(v)
        elif isinstance(v, list):
            new_v = []
            for e in v:
                new_v.append(try_float(e))
        elif isinstance(v, basestring):
            d[k] = try_float(v)
