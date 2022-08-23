from flask import Flask, render_template 
app = Flask(__name__)



@app.route("/")  #localhost:5000/
def index(): #make sure all function names are different.
    return "hello"

@app.route("/play") #localhost:5000/play
def play_route():  #does not need parameter.  Will use defaluts in the next line.
    return render_template("index.html", num = 3, back_color = "blue")

@app.route("/play/<int:xnum>") #localhost:5000/play/xnum
def account(xnum):
    return render_template("index.html", num = xnum, back_color = "blue")

# When converting a string in the route, you need to use string and not str.
@app.route("/play/<int:xnum>/<string:xcolor>") #localhost:5000/play/xnum/xcolor
def num_box_color(xnum, xcolor):
    return render_template("index.html", num = xnum, back_color = xcolor)



if __name__ == "__main__":
    app.run(debug=True) 