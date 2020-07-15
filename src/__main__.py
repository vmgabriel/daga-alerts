# develop vmgabriel

# Libraries
from flask import Flask, jsonify
from flask_mail import Mail

from config.server import configuration as conf

# Routes
from protocols.http.v0.index import mod
from protocols.http.v0.email import get_blueprint

# Email Sender
from utils.middlewares.email_sender import EmailSender

app = Flask(__name__, template_folder=conf['files_path_upload'])

email_sender_data = EmailSender(app)

app.register_blueprint(mod, url_prefix='/api')
app.register_blueprint(get_blueprint(email_sender_data), url_prefix='/api/email')

if __name__ == '__main__':
    app.run (
        host=conf['host'],
        debug=conf['debug'],
        port=conf['port']
    )

