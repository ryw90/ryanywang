import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    entries = (p for p in pages if 'published' in p.meta)
    return render_template('blog.html', entries=entries)
    
@app.route('/<path:path>/')
def page(path):
    page = pages.get(path, default={'title':path,
                                    'html':'<h2>Under Construction</h2>'})                         
    return render_template('base.html', page=page)                

if __name__=='__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()    