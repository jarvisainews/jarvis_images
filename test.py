import tomli
import os
import json 

current_toml = tomli.load(open("./current.toml", "rb"))
json.dump(current_toml, open("./current.json", "w"), indent=4)

