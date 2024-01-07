"""DOESNT WORK YET"""

import tomli
import os

lines = []
lines.append("# Current Images for JarvisAI\n\n")
lines.append("![Jarvis's](./.support/jarvis_office.jpeg)\n\n")
lines.append("## Add Links to .current.toml\n")
lines.append("## Add images to folder\n\n")
totals = [43,1065,460,977,499,296,373,405,272,335,116,188,383,572,207,189,714,109,432,1093,576,136,241,313,28,78,85]

folders = os.listdir("./")
rm = [".support", ".gitignore", ".git", "readme.md", "mkdirs.py", "update_md.py"]
for r in rm:
  folders.remove(r)

current_toml = tomli.load(open(".support/totals.toml", "rb"))
current = current_toml["images"]
folders.sort()

for fn, folder in zip(current, folders):
  n_folders = os.listdir("./" + folder)
  for folder_i in n_folders:
    ni_folders = os.listdir("./" + folder + "/" + folder_i) if os.path.isdir("./" + folder + "/" + folder_i) else []
    num_ni_folders = len(ni_folders) - 1
    current_toml['images'][fn] += num_ni_folders

  folder_toml = tomli.load(open("./" + folder + "/.current.toml", "rb"))
  for key in folder_toml:
    current_toml['images'][fn] += 1 if folder_toml[key]['square'] is not None else 0
    current_toml['images'][fn] += 1 if folder_toml[key]['long'] is not None else 0

#save totals.toml
with open(".support/totals.toml", "w") as f:
  tomli.dump(current_toml, f)

template = "{} ({} / {})\n\n"
for fn, total in zip(current, totals):
  lines.append(template.format(str(fn), current[fn], total))

with open("readme.md", "w") as f:
  f.writelines(lines)