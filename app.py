from flask import Flask, render_template, request, flash
import piController

sundown_api="https://api.sunrise-sunset.org/json?lat=30.003580&lng=-90.155418&date=today"
address = 'lhr'
# url = sundown_api + urllib.parse.urlencode({'address': address})
app = Flask(__name__, template_folder='template')
app.secret_key = "password"

# route
@app.route('/')
def index():
  return render_template("index.html")

@app.route("/turnOn/", methods=['POST'])
def turnOnLights():
    forward_message = "Turning On Relay 1"
    print(forward_message)
    piController.turnOn()
    return render_template('index.html', forward_message=forward_message);

@app.route("/turnOff/", methods=['POST'])
def turnOffLights():
    forward_message = "Turning Off Relay 1"
    print(forward_message)
    piController.turnOff()
    return render_template('index.html', forward_message=forward_message);

# listen
if __name__ == "__main__":
  app.run(port="3090")
