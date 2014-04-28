import os
import stripe
from config import *
from flask import Flask, redirect, render_template, url_for, request
from flask_flatpages import FlatPages

# Configurations
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
stripe.api_key = stripe_keys['secret_key']


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

@app.route('/reading_list')
def reading_list():
    return render_template('reading_list.html',
                           page={'title': 'reading_list'},
                           key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    amount = 99

    customer = stripe.Customer.create(
        email = 'customer@example.com',
        card = request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer = customer.id,
        amount = amount,
        currency = 'usd',
        description = 'Flask Charge'
    )

    return render_template('charge.html', amount=amount, page={'title': 'paid!'})

if __name__=='__main__':
    app.run()
