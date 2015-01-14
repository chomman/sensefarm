"""
contact.py

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ContactForm
from models import ContactModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def list_contact():
    contacts = ContactModel.query()
    form = ContactForm()
    if form.validate_on_submit():
        contact = ContactModel(
            contact_title = form.contact_title.data,
            contact_description = form.contact_description.data,
            contact_company = form.contact_company.data,
            contact_department = form.contact_department.data,
            contact_position = form.contact_position.data,
            contact_name = form.contact_name.data,
            contact_address = form.contact_address.data,
            contact_phone = form.contact_phone.data,
            contact_mobile = form.contact_mobile.data,
            contact_email = form.contact_email.data,
            contact_call_time1 = form.contact_call_time1.data,
            contact_call_time2 = form.contact_call_time2.data
        )
        try:
            contact.put()
            contact_id = contact.key.id()
            flash(u'Contact %s successfully saved.' % contact_id, 'success')
            return redirect(url_for('list_contact'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_contact'))
    return render_template('contact/list_contact.html', contacts=contacts, form=form)