from flask import render_template

def home()->str:
    """
        Home view: returns an html template string
        :return template {str} html5 string to be rendered to the client
    """
    return render_template('index.html')
