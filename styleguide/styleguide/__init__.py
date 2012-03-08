from flask import Flask
app = Flask(__name__)
#app.debug = True
app.secret_key = "'\xd6\x91]\xd8\x0eI<\xa4\x15%\x02O\x0e\xcf/\x0bw\xd2\xa85*G.G'"

#MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017

app.config.from_object(__name__)
import styleguide.views

