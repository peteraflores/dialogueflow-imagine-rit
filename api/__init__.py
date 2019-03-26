from flask import Flask, request

app = Flask(__name__)
print("Flask running")
# PUT CODE HERE
responseDict = {}

@app.route("/", methods=["POST","GET"])
def root_post():
    if request.method == "POST":
        print(request.json)
        responseDict = request.json
        print(responseDict["queryResult"]["fulfillmentText"])
        return "",200
    else:
        return"""<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>"""