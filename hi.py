# input for chat
# showing messages
# to not reload webpage
# ip shown as name


from rec import mtain_rec
from src import user
from flask import Flask, render_template, request
from flask_socketio import SocketIO,emit
from flask_tor import run_with_tor

app = Flask(__name__)
#port = run_with_tor()
socketio = SocketIO(app)


@app.route('/')
def back():
    return render_template("back.html")


@app.route('/hi')
def hi():
    return render_template("hi.html")


messages = []
#messages = set()  #for now 

@app.route('/chat', methods=["GET", "POST"])
def chat():
    global messages
    
    if request.method == "POST":
        user_message = request.form.get("message")
        sender_ip = request.remote_addr
        
        if user_message not in messages:
            print(f"user_messaeg: {user_message}")
            messages.append([f"ip:{sender_ip}",f"message:{user_message}"])
        else:
            messages = ''
    return render_template("chat.html", messages = messages)
    
print(messages)

if __name__ == '__main__':
    
    app.run('0.0.0.0',port='5550')
    #app.run(port=port)
