
from authomatic import Authomatic
import flask
import oauthlib
from bs4 import BeautifulSoup


#response = requests.get("https://app.schoology.com/login")
app = flask.Flask(__name__)

#response.raise_for_status()

#soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
@app.route('/')
def home():
    return "Welcome to my home. We appear to be lacking in <i> furniture <i>."


if __name__ == '__main__':
    app.run(port=3000)
