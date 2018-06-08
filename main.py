import html
import urllib
from flask import Flask, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label>
            I want to add
            <input type="text" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# TODO write get_current_watchlist(), just a stub for now
def get_current_watchlist():
    return [
        'Star Wars: A New Hope',
        'I Heart Huckabees',
        'Apocalypto',
        'Snow Piercer',
        'Love and Basketball',
    ]

# TODO Build a list of <option> tags using the returned value of get_current_watchlist()
option_tags = ''
for movie in get_current_watchlist():
    # <option value="12">Neverending Story</option>
    option_tags += '<option value="{movie}">{movie}</option>'.format(movie=movie)


# a form for crossing off watched movies
# TODO Make this options list based on a python list.
#
crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {option_tags}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(option_tags=option_tags)


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']
    # TODO Check that crossed_off_movie is actually a movie on the list.
    if crossed_off_movie not in get_current_watchlist():
        return redirect('/?error={}'.format(
            urllib.parse.quote("That movie isn't on your watchlist & you're silly for trying!")))
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
    content = page_header + "<p>" + confirmation + "</p>" + page_footer

    return content


@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # TODO check if error was passed
    if request.args.get('error'):
        error_elem = '<p>' + html.escape(request.args.get('error')) + '</p>'
    else:
        error_elem = ''
    # TODO add an error element to content
    # TODO escape error so users can't add <button>stuff</button>
    # or <script>alert('the creator of this page stinks!')</script>
    # build the response string
    content = page_header + error_elem + edit_header + add_form + crossoff_form + page_footer

    return content


app.run()
