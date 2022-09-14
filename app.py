from flask import Flask
import pygit as git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./TBDS_ML_Clf_WaterQuality_flask')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route("/", methods=['GET'])
def home():
    return 'Hola es el home'

if __name__ == "__main__":
    app.run()