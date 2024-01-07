import os

with open("services.txt", "r") as f:
  services = f.read().splitlines()
f.close()

for service in services:
  first_char = service[0]
  if first_char.isdigit():
    os.mkdir(f"./#/{service}/") if not os.path.exists(f"./#/{service}/") else None
    with open (f"./#/.current.toml", "a") as f:
      f.write(f"[{service}]\n")
      f.write("square = \n")
      f.write("long = \n\n")
    f.close()
  else:
    os.mkdir(f"./{first_char.upper()}/{service}/") if not os.path.exists(f"./{first_char.upper()}/{service}/") else None
    os.remove(f"./{first_char.upper()}/current.toml") if os.path.exists(f"./{first_char.upper()}/current.toml") else None
    with open (f"./{first_char.upper()}/.current.toml", "a") as f:
      f.write(f"[{service}]\n")
      f.write("square = \n")
      f.write("long = \n\n")
    f.close()
