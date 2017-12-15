# -*-: coding utf-8 -*-
""" Baby Care skill for Snips. """

import requests


class SnipsBabyCare:
    """ Baby Care skill for Snips. """

    def __init__(self, ifttt_key=None):
        """ Initialisation.

        :param ifttt_key: IFTTT Key
        """

    def send_allaitement(self, duration=None):
        """ Log an entry for allaitement for [duration] minutes. """

        requests.post('https://maker.ifttt.com/trigger/allaitement/with/key/ff4VTSbWZaeAp6o72bnYgkqHL4JK0zxF_prKTwZRM6p', 
            data = {"value1":"233m"})


if __name__ == "__main__":
    sbc = SnipsBabyCare()
    # sh.light_on_set("gold", 42, "Bedroom")
    # sh.light_on_set("gold", 42, "Office")
    sbc.send_allaitement(30)
