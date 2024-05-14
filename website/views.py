from flask import Blueprint, render_template

view = Blueprint('views', __name__)

html_homepage = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      crossorigin="anonymous"
    />
    <title>{% block title %}Home{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to my page!</h1>
    </header>
    
    <main>
        <section>
            <h2>Content</h2>
            <p>This is the main content of your page.</p>
            <button id="targetButton">Click Me</button>
        </section>
    </main>
    
    <footer>
        <section>
            <h2>Contact</h2>
            <p>You can contact us at phat.huynh@t-systems.com</p>
        </section>
    </footer>

    <script>
        // Define the URL as a JavaScript variable
        var targetUrl = "https://www.google.com";

        // Get the button element by its ID
        var button = document.getElementById("targetButton");

        // Add a click event listener to the button
        button.addEventListener("click", function() {
            // Redirect to the target URL when the button is clicked
            window.location.href = targetUrl;
        });
    </script>
</body>
</html>
'''

@view.route("/")
def homepage():
    return render_template("home.html")


