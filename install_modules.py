import pip
import json

modules = json.load(open("modules.json", "rt", encoding="utf-8"))

for module in modules:
    pip.main(["install", module])