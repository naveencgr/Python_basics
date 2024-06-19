from pathlib import Path

path = Path("commerce")
print(path.exists())

path = Path("testing")
path.mkdir()
#path.rmdir()

path = Path("")

for file in path.glob("*"):
    print(file)
