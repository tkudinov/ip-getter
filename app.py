from flask import Flask, request

app = Flask(__name__)

@app.route("/")

def show_ip():
    user_ip = request.remote_addr

    with open("ips.txt", "w") as file:
        file.write(f"{user_ip} \n")

    return f"Нет, вот это Вы : {user_ip} 😈 \n"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)