import tomli
import os
import json 

current_toml = tomli.load(open("./current.toml", "rb"))

with open("./current.txt", "w") as f:
    for key in current_toml:
        service_link = current_toml[key]["service_link"]
        image_search = current_toml[key]["image_search"]
        square = current_toml[key]["square"]
        long = current_toml[key]["long"]
        f.write(f"[{key}]\n{service_link}\n{image_search}\nSquare: {square}\nLong: {long}\n\n")


