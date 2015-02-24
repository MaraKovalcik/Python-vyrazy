import os
# We require 're' module for validating email address with regular expression
import re

# Using Flask since Python doesn't have built-in session management
# 'request' provides access to the incoming request data
# 'render_template' renders the template with the given parameters

from flask import Flask, request, render_template

# Create a flask app object using a unique name. In this case we are
# using the name of the current file
app = Flask(__name__)

# Generate a secret random key for the session
app.secret_key = os.urandom(24)


# This view method responds to the URL / for the methods GET and POST
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the errors variable to empty string. We will have the error messages
    # in that variable, if any.
    # if request.method == "PUT":

    data = {'cislo1': '',
            'cislo2': '',
            'errors':'',
            'vysledek': ''
    }

    if request.method == "GET":  # If the request is GET, render the form template.
        return render_template("index.html", data=data)
    else:
        # The request is POST with some data, get POST data and validate it.
        # The form data is available in request.form dictionary. Stripping it to remove
        # leading and trailing whitespaces
        cislo1 = request.form['cislo1'].strip()
        cislo2 = request.form['cislo2'].strip()
        # Since gender field is a radio button, it will not be available in the POST
        # data if no choice is selected. If we try to access it in such a scenario, we
        # will get an exception, so we are using the get() method on the 'form' dictionary
        # specify a default value if the key doesn't exist in the dictionary.
        vysledek = request.form.get('vysledek', '')
    
        data = {'cislo1': name,
                'cislo2': email,
                'errors':'',
                'vysledek': vysledek

        }
        # Check if all the fields are non-empty and raise an error otherwise
        if not is_name_valid(name):
            data['errors'] += "Please enter correct name length! :)"
        if not is_den_valid(den):
            data['errors'] += "Please enter valid day!"
        if not is_mes_valid(mes):
            data['errors'] += "Please enter valid month!"
        if not is_rok_valid(rok):
            data['errors'] += "Please enter valid year"
        if not is_cis_valid(cis):
            data['errors'] += "Please enter valid value"

        if not name or not email or not gender or not username or not password or not den or not mes or not rok:
            data['errors'] = "Please enter all the fields."
        if not data['errors']:
            # Validate the email address and raise an error if it is invalid
            if not is_email_address_valid(email):
                data['errors'] += "Please enter a valid email address"
        if not data['errors']:
            # If there are no errors, create a dictionary containing all the entered
            # data and pass it to the template to be displayed
            # Since the form data is valid, render the success template
            return render_template("success.html", data=data)
        # Render the form template with the error messages
        return render_template("index.html", data=data)

# This is the code that gets executed when the current python file is
# executed. 
if __name__ == '__main__':
    # Run the app on all available interfaces on port 80 which is the
    # standard port for HTTP
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )