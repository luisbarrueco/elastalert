from elastalert.enhancements import BaseEnhancement

class PctgEnhancement(BaseEnhancement):

    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        if 'system' in match:
            if 'filesystem' in match['system']:
                match['system']['filesystem']['used']['pct_enhanced'] = match['system']['filesystem']['used']['pct'] * 100
            if 'memory' in match['system']:
                match['system']['memory']['actual']['used']['pct_enhanced'] = match['system']['memory']['actual']['used']['pct'] * 100
            if 'cpu' in match['system']:
                for cpu_type in match['system']['cpu'].keys():
                    match['system']['cpu'][cpu_type]['pct_enhanced'] = match['system']['cpu'][cpu_type]['pct'] * 100
