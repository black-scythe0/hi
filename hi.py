# input for chat
# showing messages
# to not reload webpage
# ip shown as name

from flask import Flask, render_template, request
from flask_socketio import SocketIO,emit
from flask_tor import run_with_tor

app = Flask(__name__)
port = run_with_tor()
socketio = SocketIO(app)

messages = []

@app.route('/', methods=["GET", "POST"])
def back():
    global messages
    
    if request.method == "POST":
        user_message = request.form.get("message")
        sender_ip = request.remote_addr
        
        if user_message:
            messages.append([f"ip:{sender_ip}",f"message:{user_message}"])
            
    return render_template("hi.html", messages = messages)
    
print(messages)

if __name__ == '__main__':
    
    
    app.run(port=port)
