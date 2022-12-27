from app_env import config, env
from os import path
import json


def update_plate():
    plate_template = env.get_template('pico8_plate.j2')
    base_url = config["Web"]["base_url"]
    plate_result = plate_template.render(base_url=base_url)
    
    with open("pico8_plate.html", "w") as output:
        output.write(plate_result)
