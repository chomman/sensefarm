"""
models.py

App Engine datastore models

"""
from google.appengine.ext import ndb

class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class ContactModel(ndb.Model):
    """Contact Model"""
    contact_title = ndb.StringProperty(required=True)
    contact_description = ndb.TextProperty(required=True)
    contact_company = ndb.StringProperty
    contact_department = ndb.StringProperty
    contact_position = ndb.StringProperty(required=True)
    contact_name = ndb.StringProperty(required=True)
    contact_address = ndb.StringProperty(required=True)
    contact_phone = ndb.StringProperty(required=True)
    contact_mobile = ndb.StringProperty(required=True)
    contact_email = ndb.StringProperty(required=True)
    contact_call_time1 = ndb.DateTimeProperty
    contact_call_time2 = ndb.DateTimeProperty
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

