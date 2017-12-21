# -*-: coding utf-8 -*-
""" Baby Care skill for Snips. """

import requests
import json

def load_state():
    with open('state.json') as data_file:    
        state = json.load(data_file)
    return state
        
def write_state(state):
    with open('state.json', 'w') as outfile:
        json.dump(state, outfile)


class SnipsBabyCare:
    """ Baby Care skill for Snips. """

    def __init__(self, ifttt_key=None, locale=None):
        """ Initialisation.

        :param ifttt_key: IFTTT Key
        """
        self.ifttt_key = ifttt_key


    def send_row(self, action, value=None):
        """ Log an entry for allaitement for [duration] minutes. """

        with open('test.json', 'w') as outfile:
            json.dump({ "key": self.ifttt_key, "action": action, "value": value }, outfile)

        requests.post('https://maker.ifttt.com/trigger/breastfeeding/with/key/{0}'.format(self.ifttt_key), 
            data = {"value1": action, "value2": value})


    def log_breast(self, side=None):
        if side is not None:
            state = load_state()
            state["side"] = side
            write_state(state)


    def last_breast(self):
        state = load_state()
        return state.get("side", "")

    def next_breast(self):
        state = load_state()
        side = state.get("side", None)
        if side is "gauche":
            return "droite"
        elif side is "droite":
            return "gauche"
        else:
            return ""
        
if __name__ == "__main__":
    sbc = SnipsBabyCare()
    # sh.light_on_set("gold", 42, "Bedroom")
    # sh.light_on_set("gold", 42, "Office")
    sbc.send_allaitement(30)
