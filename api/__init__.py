from flask import Flask, request

app = Flask(__name__)
print("Flask running")
# PUT CODE HERE


@app.route("/", methods=["POST","GET"])
def root_post():
	if request.method == "POST":
		print(request.json)
		return "",200
	return """<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>"""