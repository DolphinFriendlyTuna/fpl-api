import json
from unittest import TestCase

from fpl import Player, convert_float_strings


class TestPlayer(TestCase):

    def test_constructor(self):
        input = '{"id":1,"photo":"48844.jpg","web_name":"Ospina","team_code":3,"status":"i","code":48844,"first_name":"David","second_name":"Ospina","squad_number":13,"news":"Back injury - Expected back 30 Apr","now_cost":47,"chance_of_playing_this_round":0,"chance_of_playing_next_round":0,"value_form":"0.1","value_season":"0.4","cost_change_start":-3,"cost_change_event":0,"cost_change_start_fall":3,"cost_change_event_fall":0,"in_dreamteam":false,"dreamteam_count":0,"selected_by_percent":"0.2","form":"0.4","transfers_out":7683,"transfers_in":3373,"transfers_out_event":26,"transfers_in_event":3,"loans_in":0,"loans_out":0,"loaned_in":0,"loaned_out":0,"total_points":2,"event_points":0,"points_per_game":"1.0","ep_this":"0.0","ep_next":"0.0","special":false,"minutes":143,"goals_scored":0,"assists":0,"clean_sheets":0,"goals_conceded":4,"own_goals":0,"penalties_saved":0,"penalties_missed":0,"yellow_cards":0,"red_cards":0,"saves":4,"bonus":0,"bps":18,"influence":"28.8","creativity":"0.0","threat":"0.0","ict_index":"2.9","ea_index":56,"element_type":1,"team":1}'
        data = json.loads(input)
        convert_float_strings(data)
        p = Player(data)

        self.assertEqual(1, p.id)  # test int
        self.assertEqual('David Ospina', p.name)  # test property
        self.assertEqual(0.0, p.threat)  # test float
