from flask import render_template, redirect, url_for, g, flash, request
from flask.ext.login import logout_user, current_user
from . import main
from .. import db
from app import login_manager, app
from ..models import Item, User
from forms import addlinkForm


@app.before_request
def before_request():
    g.user = current_user



@main.route('/auth/index', methods=['GET', 'POST'])

def logout():
    # remove the username from the session if it's there
    logout_user()
    g.user.authenticated = False


    print ("sucessfully logged out")

    return redirect(url_for('auth.login'))


@main.route('/contact', methods=['GET', 'POST'])

def contact():
    return render_template('contact.html')



@main.route('/about', methods=['GET', 'POST'])

def about():
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




@main.route('/addurl', methods=['GET', 'POST'])
def addurl():
    form = addlinkForm()
    items = Item.query.all()


    print ("Create Item Page")
    if request.method == 'POST':
        print "ovber here"
        items = Item(title=form.title.data,
                    link=form.link.data,
                    description=form.description.data
                    )

        db.session.add(items)
        db.session.commit()
        print ("Link Created")

        return redirect(url_for('main.viewlink'))
    return render_template('add.html', form=form)


@main.route('/linkcreated', methods=['GET', 'POST'])
def viewlink():

    return render_template('search/viewlink.html')


@main.route('/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.query.filter_by(username=username).first()



    return render_template('auth/viewperson.html', user=user)

