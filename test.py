import random
import json
import pandas as pd
import os
import obd
import time

connection = obd.OBD()


while True:

    speed = connection.query(obd.commands.SPEED).value
    rpm = connection.query(obd.commands.RPM).value
    oil_temp = connection.query(obd.commands.OIL_TEMP).value
    coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value

    data = {
        "speed": speed,
        "rpm": rpm,
        "oil_temp": oil_temp,
        "coolant_temp": coolant_temp
    }

    print(data)


    if os.path.exists("data/data.json"):
        os.remove("data/data.json")

    with open("data/data.json", "a") as f:
        f.write(json.dumps(data))

    time.sleep(5)
