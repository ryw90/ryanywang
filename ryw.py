from flask import Flask, redirect, render_template, url_for
from flask_flatpages import FlatPages

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
	return redirect(url_for('page', path='about'))

@app.route('/blog/')
def blog():
    entries = (p for p in pages if 'published' in p.meta)
    entries = sorted(entries, reverse=True, key=lambda p: p.meta['published'])
    return render_template('blog.html', entries=entries, page={'title':'blog'})

@app.route('/<path:path>/')
def page(path):
    page = pages.get(path, default={'title':path,
                                    'html':'Under Construction...'})
    return render_template('base.html', page=page)

if __name__=='__main__':
    app.run()
