"""
company.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ExampleForm
from models import ExampleModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    return redirect(url_for('company'))
    #return render_template('index.html', category='company', action='company/ceo', title="Sensefarm")


def company(pagename = 'ceo'):
    return render_template('company/'+pagename+'.html', category='company', action='company/'+pagename)

def service(pagename = 'naming'):
    return render_template('service/'+pagename+'.html', category='service', action='service/'+pagename)

def process(pagename = 'step'):
    return render_template('process/'+pagename+'.html', category='process', action='process/'+pagename)
