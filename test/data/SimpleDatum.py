import sys, os, logging

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "esam"))

import Constants as c
from Datum import Datum

class SimpleDatum(Datum):
    def __init__(self, name=c.INVALID_NAME):
        logging.info(f"init SimpleDatum")
        super().__init__()