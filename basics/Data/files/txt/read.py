
def search(locations):
  print("Searching...")
  with open("locations.txt") as file:
    for line in file.readlines():
      print(f"Looked in {line.strip()}")
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()

