#BOOT MODULE:SERVER

from flask import request
from flask_api import FlaskAPI

import HISTORY
import PUMP

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/init/', methods=["POST"])
def api_init():
    if request.method == "POST":
	HISTORY.saveEventDeviceInit()
    return {"data":{}}

@app.route('/pouring/', methods=["POST"])
def api_pouring():
    if request.method == "POST":
	seconds = float(request.data.get("seconds"))
	HISTORY.saveEventManualPour(seconds)
	PUMP.setup()
	PUMP.start(seconds)
    return {"data":{}}

@app.route('/history/', methods=["GET"])
def api_history():
    if request.method == "GET":
	events = HISTORY.loadAllEvents()
    return {"data":{"events":events}}

#MAIN

if __name__ == "__main__":
    app.run()
