from flask import render_template, redirect, url_for, g, flash, request
from flask_login import logout_user, current_user
from . import main
from .. import db
from app import login_manager, app
from ..models import Item, User
from forms import addlinkForm
from ..search.forms import searchForm
from datetime import datetime

timestamp = datetime.today()

@main.before_request
def before_request():
    #current_user.ping()
    g.user = current_user



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = searchForm(request.form)
    search_term = form.searchString.data

    if request.method == 'POST' and form.validate():

        print "hello"
        return redirect(url_for('search.searchresults', search_term=search_term))
    return render_template('index.html', form=form)




@main.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



@main.route('/about', methods=['GET', 'POST'])

def about():
    return render_template('about.html')



@main.route('/addurl', methods=['GET', 'POST'])
def addurl():

    form = addlinkForm(request.form)

    print ("Create Item Page")
    if request.method == 'POST':
        if form.validate():
            if form.validate_recpatcha(form.picture):
                items = Item(
                            link="HTTP://" + form.link.data.upper() + ".ONION/",
                            title = '',
                            description = '',
                            member_since=timestamp,
                            click_count= '',
                            last_updated=timestamp
                            )
                try:
                    db.session.add(items)
                    db.session.commit()
                    print ("Link Created")
                    flash('Website sucessfully added')
                    return redirect(url_for('user'))
                except Exception as e:
                    print str(e)

                    db.session.rollback()
                    db.session.flush()
            else:

                flash("Bad Recaptcha! Please Try Again.  Robots Go Away")
                return redirect(url_for('main.addurl'))
        else:
            print ("wrong going back to first")
            flash("Error Uploading site! Already present in database ..")
            return redirect(url_for('main.addurl'))

    return render_template('add.html', form=form)


@main.route('/linkcreated', methods=['GET', 'POST'])
def viewlink():


    return render_template('search/myonions.html')


@main.route('/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()



    return render_template('auth/viewperson.html', user=user)

