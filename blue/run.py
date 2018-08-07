
# This file is used to handle the all blueprint files

from flask import Flask
from blue .user .access import user_blueprint
from blue .user  .AdminPermission import admin
from blue .user .permission import check_permission


app = Flask(__name__, instance_relative_config=True)

# Register all Blueprint here

app.register_blueprint(user_blueprint)
# app.register_blueprint(access_blueprint)
app.register_blueprint(admin)


app.run(debug=True)
