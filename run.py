from flask import Flask, render_template, request
from flask_mail import Mail, Message
from mydetails import email, password
# enitionalizing
app=Flask(__name__)
mail=Mail(app)

# Configuring vars for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        msg = Message(request.form.get("Subject"), sender='botharoyden01@gmail.com', recipients=[request.form.get("Email")])
        msg.body = "Thank for your email"
        mail.send(msg)
        return render_template("result.html", result="Successfully sent!")
    else:
        return render_template("result.html", result="Sorry, Your message failed to send")

if __name__ =='_main_':
   app.run(debug=True)