import json

try:
    config = json.load(open("config/config.json", "r"))
except FileNotFoundError:
    raise FileNotFoundError("Please create and fill in /config/config.json")

"""
config.json needs to be filled in:
{
  "TOKEN": "<token>",
  "PREFIX_RAW": "<prefix>",
  "PREFIX_ARRAY": ["<prefix>", "<prefix_alias_1>", "<prefix_alias_2>", ...]
}
"""

try:
    TOKEN = config["TOKEN"]
    PREFIX_RAW = config["PREFIX_RAW"]
    PREFIX_LEN = len(PREFIX_RAW)
    PREFIX = config["PREFIX_ARRAY"]
except KeyError:
    raise KeyError("Your config.json file is filled in incorrectly." +
                   "Please fill it in as shown in utils/botconstants.py")

MEE6_ID = 159985870458322944
EMOJI = json.load(open("config/emoji.json", "r"))