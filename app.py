from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return {"message": "Jobs Scrapper!"}


@socketio.on("message")
def message(message):
    print("Received message: " + str(message))
    emit("response", message)


@socketio.on("scrapeInternhsala")
def scrapeInternhsala(msg):
    try:
        emit("response", {"GOT IT MAN! GOT IT!: ", msg})
    except KeyError as e:
        print(f"KeyError: {e} - The session may be disconnected.")
    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     socketio.run(app, allow_unsafe_werkzeug=True)
