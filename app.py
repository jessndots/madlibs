from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret" 
debug=DebugToolbarExtension(app)
from stories import *





@app.route('/')
def form(): 
    """return madlibs form"""
    return render_template('madlibs.html', story=story)


@app.route('/story')
def show_story():
    """show story with submitted prompts"""

    story_text = story.generate(request.args)

    return render_template('story.html', story=story, story_text=story_text)

