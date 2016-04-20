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

    page, per_page, offset = get_page_items()

    links = Item.query.paginate()
    total = Item.query.count()
    pagination = get_pagination(page=page,
                            per_page=per_page,
                            offset = offset,    #results per page
                            total = total,        #total number of results
                            format_total=True,   #format total. example 1,024
                            format_number=True,  #turn on format flag
                            record_name='links', #provide context
                            )
    #links  = Item.query.filter(Item.title.like == x or Item.link.like == y)

    return render_template('search/searchPage.html', total=total, links=links, pagination=pagination, per_page=per_page, page=page, offset=offset)




def get_css_framework():
    return 'bootstrap3'

def get_link_size():
    return 'sm'  #option lg

def show_single_page_or_not():
    return False

def get_page_items():
    page = int(request.args.get('page', 1))
    per_page = 20
    if not per_page:
        per_page = 10
    else:
        per_page = int(per_page)
    offset = (page - 1) * per_page
    return page, per_page, offset


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'repositories')
    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      show_single_page=show_single_page_or_not(),
                      **kwargs
                      )