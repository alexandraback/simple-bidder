import orjson
import os
from datetime import datetime
import json
from simple_bidder.helper import load_campaigns


def test_function():
    dummy_dict = {"a": 1, "b": datetime.now()}
    x = orjson.dumps(dummy_dict)
    print(x)


def test_my_life():
    print(load_campaigns())
