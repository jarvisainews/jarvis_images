import os

with open("services.txt", "r") as f:
  services = f.read().splitlines()
f.close()

all = {}

for service in services:
  first_char = service[0]
  if first_char.isdigit():
    if all.get("#") == None:
      all["#"] = 1
    else:
      all["#"] += 1
    os.mkdir(f"./#/{service}/") if not os.path.exists(f"./#/{service}/") else None
    os.mknod(f"./#/{service}/placeholder.bin") if not os.path.exists(f"./#/{service}/placeholder.bin") else None
    with open (f"./#/.current.toml", "a") as f:
      f.write(f"[{service}]\n")
      f.write("square = \n")
      f.write("long = \n\n")
    f.close()
  else:
    if all.get(first_char.upper()) == None:
      all[first_char.upper()] = 1
    else:
      all[first_char.upper()] += 1
    os.mkdir(f"./{first_char.upper()}/{service}/") if not os.path.exists(f"./{first_char.upper()}/{service}/") else None
    os.mknod(f"./{first_char.upper()}/{service}/placeholder.bin") if not os.path.exists(f"./{first_char.upper()}/{service}/placeholder.bin") else None
    with open (f"./{first_char.upper()}/.current.toml", "a") as f:
      f.write(f"[{service}]\n")
      f.write("square = \n")
      f.write("long = \n\n")
    f.close()

with open("readme.md", "w") as f:
  for key in all:
    f.write(f"{key}/ ({all[key]}) - not completed\n\n")
