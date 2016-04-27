from flask import render_template, redirect, url_for, g, flash, request, current_app
from . import search
from .. import main
from .. import db
from app import app
from flask_login import current_user, current_app
from ..models import Item, User
from flask.ext.paginate import Pagination

import click


@search.before_request
def before_request():
    g.user = current_user


@search.route('/search')
def search():
    ##TODO Search returning 69 results instead of 10
    search = False
    q = request.args.get('q')
    if q:
        search = True


    page = int(request.args.get('page', 1))
    per_page = 10
    inner_window = 10
    outer_window = 10
    offset = page * 10
    links = Item.query.all()
    total = Item.query.count()
    pagination = get_pagination(page=page,
                                 per_page=per_page,
                                offset=offset,

                                inner_window=inner_window,
                                outer_window = outer_window,
                                search=search,


                            total = total,        #total number of results
                            format_total=True,   #format total. example 1,024
                            format_number=True,  #turn on format flag
                            record_name='links',
                           #provide context
                            )
    #links  = Item.query.filter(Item.title.like == x or Item.link.like == y)

    return render_template('search/searchPage.html', links=links, pagination=pagination, per_page=per_page, page=page)




def get_css_framework():
    return 'bootstrap3'

def get_link_size():
    return 'sm'  #option lg

def show_single_page_or_not():
    return True




def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'repositories')

    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      show_single_page=show_single_page_or_not(),

                      **kwargs

                      )