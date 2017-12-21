# -*-: coding utf-8 -*-
""" Baby Care skill for Snips. """

import requests
import json

class SnipsBabyCare:
    """ Baby Care skill for Snips. """

    def __init__(self, ifttt_key=None, locale=None):
        """ Initialisation.

        :param ifttt_key: IFTTT Key
        """
        self.ifttt_key = ifttt_key

    def send_allaitement(self, duration=None):
        """ Log an entry for allaitement for [duration] minutes. """

        with open('test.json', 'w') as outfile:
            json.dump({ "key": self.ifttt_key, "duration": duration }, outfile)

        requests.post('https://maker.ifttt.com/trigger/breastfeeding/with/key/{0}'.format(self.ifttt_key), 
            data = {"value1": "34m"})


if __name__ == "__main__":
    sbc = SnipsBabyCare()
    # sh.light_on_set("gold", 42, "Bedroom")
    # sh.light_on_set("gold", 42, "Office")
    sbc.send_allaitement(30)
