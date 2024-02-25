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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        repository_path = request.form['repository_path']
        github_branch_1 = request.form['github_branch_1']
        github_branch_2 = request.form['github_branch_2']
        # Process the form data here (e.g., compare branches, generate HTML, etc.)
        # For now, let's just print the values to the console
        print(f'Repository Path: {repository_path}')
        print(f'GitHub Branch 1: {github_branch_1}')
        print(f'GitHub Branch 2: {github_branch_2}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
