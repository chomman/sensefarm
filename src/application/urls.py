"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views
from application import page
from application import contact


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=page.home)

# Say hello
app.add_url_rule('/hello/<username>', 'say_hello', view_func=views.say_hello)

# Examples list page
app.add_url_rule('/examples', 'list_examples', view_func=views.list_examples, methods=['GET', 'POST'])

# Examples list page (cached)
app.add_url_rule('/examples/cached', 'cached_examples', view_func=views.cached_examples, methods=['GET'])

# Contrived admin-only view example
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

# Edit an example
app.add_url_rule('/examples/<int:example_id>/edit', 'edit_example', view_func=views.edit_example, methods=['GET', 'POST'])

# Delete an example
app.add_url_rule('/examples/<int:example_id>/delete', view_func=views.delete_example, methods=['POST'])


# URL for Sensefarm static pages
app.add_url_rule('/company/', view_func=page.company)
app.add_url_rule('/company/<pagename>', view_func=page.company)
app.add_url_rule('/service/', view_func=page.service)
app.add_url_rule('/service/<pagename>', view_func=page.service)
app.add_url_rule('/process/', view_func=page.process)
app.add_url_rule('/process/<pagename>', view_func=page.process)

app.add_url_rule('/contact/', view_func=contact.list_contact)



## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

