from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret12345"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_story():
    """Show list-of-stories form."""

    return render_template("home.html",stories=stories.values())


@app.route("/form")
def ask_questions():
    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("form.html",story_id=story_id, title=story.title, prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)
