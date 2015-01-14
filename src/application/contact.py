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


def new_contacts():
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
            return redirect(url_for('list_contacts'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_contacts'))
    return render_template('contact/new_contact.html', contacts=contacts, form=form)


def list_contacts():
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


def edit_contact(contact_id):
    contact = ContactModel.get_by_id(contact_id)
    form = ContactForm(obj=contact)
    if request.method == "POST":
        if form.validate_on_submit():
            
            contact.contact_title = form.data.get('contact_title')
            contact.contact_description = form.data.get('contact_description')
            contact.contact_company = form.data.get('contact_company')
            contact.contact_department = form.data.get('contact_department')
            contact.contact_position = form.data.get('contact_position')
            contact.contact_name = form.data.get('contact_name')
            contact.contact_address = form.data.get('contact_address')
            contact.contact_phone = form.data.get('contact_phone')
            contact.contact_mobile = form.data.get('contact_mobile')
            contact.contact_email = form.data.get('contact_email')
            contact.contact_call_time1 = form.data.get('contact_call_time1')
            contact.contact_call_time2 = form.data.get('contact_call_time2')
            
            contact.put()
            
            flash(u'Contact %s successfully saved.' % contact_id, 'success')
            return redirect(url_for('list_contacts'))
    return render_template('edit_contact.html', contact=contact, form=form)