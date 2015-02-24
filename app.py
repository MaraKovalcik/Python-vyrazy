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



def is_cislo1_valid(cislo1):
    if cislo1 > 100 and cislo1<1000:
        return True
    else:
        return False


def is_cislo2_valid(cislo2):
    if cislo2 > 0 and cislo2<10:
        return True
    else:
        return False


# This view method responds to the URL / for the methods GET and POST
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the errors variable to empty string. We will have the error messages
    # in that variable, if any.
    # if request.method == "PUT":

    data = {'cislo1': 0,
            'cislo2': 0,
            'errors': '',
            'vysledek1':0,
            'vysledek2':0
    }

    if request.method == "GET":  # If the request is GET, render the form template.
        return render_template("index.html", data=data)
    else:
        # The request is POST with some data, get POST data and validate it.
        # The form data is available in request.form dictionary. Stripping it to remove
        # leading and trailing whitespaces
            #name = request.form['cislo1'].strip()
             #email = request.form['cislo2'].strip()
        # Since gender field is a radio button, it will not be available in the POST
        # data if no choice is selected. If we try to access it in such a scenario, we
        # will get an exception, so we are using the get() method on the 'form' dictionary
        # specify a default value if the key doesn't exist in the dictionary.
        cislo1 =int(request.form['cislo1'].strip())
        cislo2 = int(request.form['cislo2'].strip())
        nasobek = (cislo1*cislo2)
        zbytek = nasobek%3

        data = {'cislo1': cislo1,
                'cislo2': cislo2,
                'errors': '',
                'vysledek1':nasobek,
                'vysledek2':zbytek
        }
        # Check if all the fields are non-empty and raise an error otherwise
        if not is_cislo1_valid(cislo1):
            data['errors'] += "Cislo 1 neni v intervalu 100-1000. "

        if not is_cislo2_valid(cislo2):
            data['errors'] += "Cislo 2 neni v intervalu 0-10."

        if not cislo1 or not cislo2:
            data['errors'] = "Musis vyplnit vsechna pole!"

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