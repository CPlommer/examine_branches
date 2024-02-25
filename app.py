# Compare Git branches using the Flask web framework
# Flask is a lightweight and flexible framework that makes it easy to create web applications in Python

# To install Flask for python
# pip install Flask

# To install Flask for python3
# pip3 install Flask

# Import necessary modules from Flask.
# Create an instance of the Flask class.
# Define a route for the root URL ('/'). This route handles both GET and POST requests.
# In the index() function, check if the request method is POST. If it is, retrieve the form data submitted by the user.
# Then render an HTML template called index.html.

# To run:  
# python3 app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve parameters from the form
    repository_path = request.form['repository_path']
    github_branch_1 = request.form['github_branch_1']
    github_branch_2 = request.form['github_branch_2']

    # Process the parameters here
    # For demonstration purposes, we'll simply pass them to another template

    # Render another template and pass the parameters to it
    return render_template('result.html', repository_path=repository_path, github_branch_1=github_branch_1, github_branch_2=github_branch_2)


if __name__ == '__main__':
    app.run(debug=True)
