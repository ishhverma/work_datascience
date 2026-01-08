from flask import Flask, request
import random
import html  # For safely escaping user input

# Create the Flask app
app = Flask(__name__)

# Fun greetings and colors
GREETINGS = ["Hey", "Hello", "Yo", "Hiya", "Greetings", "Salutations"]
COLORS = ["red", "green", "blue", "purple", "orange", "teal", "magenta"]

@app.route('/')
def home():
    # Get 'name' from query parameters, default to 'Guest'
    name = request.args.get('name', 'Guest').strip()
    
    # Escape HTML to prevent injection
    safe_name = html.escape(name)
    
    # Convert to uppercase
    name_upper = safe_name.upper()
    
    # Reverse the name
    name_reversed = safe_name[::-1]
    
    # Name score (sum of ASCII codes)
    name_score = sum(ord(char) for char in safe_name)
    
    # Pick random greeting and color
    greeting = random.choice(GREETINGS)
    color = random.choice(COLORS)
    
    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Fun Name App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f0f8ff;
            }}
            h1 {{
                font-size: 3em;
            }}
            p {{
                font-size: 1.2em;
            }}
            code {{
                background-color: #eee;
                padding: 2px 5px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <h1 style="color:{color};">{greeting}, {name_upper}!</h1>
        <p>Your name backwards is: <strong>{name_reversed}</strong></p>
        <p>Your name score is: <strong>{name_score}</strong></p>
        <p>Try changing your name in the URL like this: <code>?name=YourName</code></p>
    </body>
    </html>
    """
    
    return html_content

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


