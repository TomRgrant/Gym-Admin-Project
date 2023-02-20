from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.gym_class_controller import gym_classes_blueprint
import repositories.gym_class_repository as gym_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(gym_classes_blueprint)


@app.route('/')
def home():
    gym_classes = gym_repository.select_all()
    return render_template('index.html', gym_classes = gym_classes)


if __name__ == '__main__':
    app.run(debug=True)
