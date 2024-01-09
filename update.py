import os
import json 
import time
with open("current.txt", "r") as f:
    tmp_txt = f.read()
f.close()

current_toml = {}
for lines in tmp_txt.split("\n\n"):
    if lines != "":
        lines = lines.split("\n")
        current_toml[lines[0].strip("[]")] = {
            "square": lines[3].replace("Square:", "") if lines[3].replace("Square:", "") != "" else " ",
            "long": lines[4].replace("Long:", "") if lines[4].replace("Long:", "") != "" else " "
        }

json.dump(current_toml, open("./.support/current.json", "w"), indent=4)

readme = '''
# Current Images for JarvisAI

![Jarvis's](./.support/jarvis_office.jpeg)

## Finished:
-  Total {}%  |  {} / 5098
-  Square {}%  |  {} / 2549
-  Long {}%  |  {} / 2549

## Needed:
-  Total {}%  |  {} / 5098
-  Square {}%  |  {} / 2549
-  Long {}%  |  {} / 2549
'''

needed, finished = [], []

_index = [key for key in current_toml if current_toml[key]['long'] == '  ' and current_toml[key]['square'] == '  ']


long = [key for key in current_toml if current_toml[key]["long"] == "  "]
square = [key for key in current_toml if current_toml[key]["square"] == "  "]
needed.extend(long)
needed.extend(square)

long_ = [key for key in current_toml if current_toml[key]["long"] != "  "]
square_ = [key for key in current_toml if current_toml[key]["square"] != "  "]
finished.extend(long_)
finished.extend(square_)

with open("./README.md", "w") as f:
    f.write(readme.format(
        round((len(finished)/(len(current_toml)*2))*100, 4), len(finished),
        round((len(square_)/len(current_toml)*100),4), len(square_),
        round((len(long_)/len(current_toml)*100),4), len(long_),
        round((len(needed)/(len(current_toml)*2))*100, 4), len(needed),
        round((len(square)/len(current_toml)*100),4), len(square),
        round((len(long)/len(current_toml)*100),4), len(long)
    ))
f.close()

needed, finished = set(needed), set(finished)
with open("./.support/needed.txt", "w") as f:
    f.write("\n".join(needed))
f.close()

with open("./.support/finished.txt", "w") as f:
    f.write("\n".join(finished))
f.close()