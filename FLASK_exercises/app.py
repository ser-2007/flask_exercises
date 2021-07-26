from flask import Flask, render_template,request,redirect,url_for #html templatelerimizi aliyor ve response olarak dönmemizzi sagliyor

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", number = 10, number2 = 20)
@app.route("/if")
def kosul():
    message = "this is a message"
    return render_template("if.html",message = message)
@app.route("/numbers")
def numbers():
    numbers = [1,2,3,4,5,6,7]
    return render_template("numbers.html",numbers=numbers)
@app.route("/search")
def search():
    return "search" 

@app.route("/requ")
def reqst():
    return render_template("request.html") 

@app.route("/toplam", methods=["GET","POST"])
def toplam():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("num.html", total = int(number1) + int(number2)) 
    else:
        return render_template("num.html")


@app.route("/redirect", methods = ["GET","POST"])
def redrect():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("num.html", total = int(number1) + int(number2)) 
    else:
        return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def delet(id):
    return "Id: " + id
#if __name__ == "__main__":
  #  app.run(debug=True)
   # app.run(host='0.0.0.0', port=80)
if __name__ == "__main__":
    app.run(debug=True)