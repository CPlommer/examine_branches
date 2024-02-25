# examine_branches
PoC to generate an HTML output page given parameters.

PARAM1 = OLD_BRANCH

PARAM2 = NEW_BRANCH

PARAM3 = REPOSITORY


Here's a suggestion on how to approach this:

Web Application Framework:
Choose a web application framework like Flask (Python), Express (Node.js), or Ruby on Rails (Ruby) to build the form-based application.

Form Handling:
Implement a form in your chosen framework where users can input the three parameters: repository_path, github_branch_1, and github_branch_2.

GitHub API Integration:
Utilize the GitHub API to retrieve information about the branches and commits of the specified repository. You can use libraries or make direct HTTP requests to interact with the GitHub API.

Branch Comparison:
Write logic in your application to compare the differences (commits) between the two specified branches. You can fetch commit information for each branch and analyze the changes programmatically.

HTML Page Generation:
Once you have the comparison results, generate HTML content dynamically based on the differences between the branches. You can use templating engines provided by your chosen framework to render HTML pages with the desired content.

Output HTML Page:
Finally, serve the generated HTML page to the user through your web application.

Here's a high-level overview of the workflow:

User fills out the form with the repository path and branch names.
Your application fetches commit information for the specified branches using the GitHub API.
It compares the commits and generates HTML content summarizing the differences.
The application renders the HTML page and serves it to the user.
By following this approach, you can create a custom solution tailored to your specific requirements for comparing GitHub branches and generating HTML output.
