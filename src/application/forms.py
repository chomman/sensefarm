"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ExampleModel, ContactModel


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

# App Engine ndb model form example
ExampleForm = model_form(ExampleModel, wtf.Form, field_args={
    'example_name': dict(validators=[validators.Required()]),
    'example_description': dict(validators=[validators.Required()]),
})


ContactForm = model_form(ContactModel, wtf.Form, field_args={
    'contact_title': dict(validators=[validators.Required()]),
    'contact_description': dict(validators=[validators.Required()]),
    'contact_company': dict(validators=[]),
    'contact_department': dict(validators=[]),
    'contact_position': dict(validators=[validators.Required()]),
    'contact_name': dict(validators=[validators.Required()]),
    'contact_address': dict(validators=[validators.Required()]),
    'contact_phone': dict(validators=[validators.Required()]),
    'contact_mobile': dict(validators=[validators.Required()]),
    'contact_email': dict(validators=[validators.Required()]),
    'contact_call_time1': dict(validators=[validators.Required()]),
    'contact_call_time2': dict(validators=[validators.Required()]),
})
