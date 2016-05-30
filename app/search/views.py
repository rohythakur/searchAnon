from flask import render_template, redirect, url_for, g, flash, request, current_app
from . import search
#from .. import main
from .. import db
from app import app

from flask_login import current_user, current_app, session
from ..models import Item, User
from flask.ext.paginate import Pagination
from .forms import searchForm
import click
from sqlalchemy.sql import func


@search.before_request
def before_request():
    g.user = current_user


@search.route('/search', methods=['GET', 'POST'])
def search():
    form = searchForm()
    search_term = form.searchString.data

    print search_term
    search = False
    q = request.args.get('q')
    if q:
        search = True


    page = int(request.args.get('page', 1))
    PER_PAGE = 10
    inner_window = 10
    outer_window = 10
    offset = page * 1


    links = Item.query.filter(Item.title.like('%' +search_term + '%')).paginate(page, 10, True)
    #links = Item.query(func.mid(Item.title, 1, 3).like('%' +search_term + '%')).paginate(page, 10, True)

    total = Item.query.count()
    pagination = get_pagination(page=page,
                                 per_page=PER_PAGE,
                                offset=offset,

                                inner_window=inner_window,
                                outer_window = outer_window,
                                search=search,


                                total = total,        #total number of results
                                format_total=True,   #format total. example 1,024
                                format_number=True,  #turn on format flag
                                record_name='links',

                            )

    return render_template('search/searchPage.html', form=form, links=links, pagination=pagination, page=page, per_page = PER_PAGE)




def get_css_framework():
    return 'bootstrap3'

def get_link_size():
    return 'sm'  #option lg

def show_single_page_or_not():
    return True


def get_page_items():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = current_app.config.get('PER_PAGE', 10)
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
