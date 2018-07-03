from flask import Flask, session, request, redirect, flash, get_flashed_messages

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['num_times'] = str(int(session.get('num_times', 0)) + 1)
        flash('You are registered!')
        return redirect('/')
        # return "You've been added to our email list! ({} times so far)".format(session['num_times'])
    else: # GET
        messages = get_flashed_messages()
        return '''
            <h2>Want to sign up for our email list?</h2>

            {}

            <form method="POST">
                <input type="email" name="email" />
                <input type="submit" />
            </form>
        '''.format(messages)

app.secret_key = 'moosefeathers'
app.debug = True

if __name__ == '__main__':
    app.run()
