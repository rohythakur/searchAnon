from flask import render_template, redirect, url_for, g, flash, request, current_app
from . import search
#from .. import main


from flask_login import current_app, session
from ..models import Item
from flask_paginate import Pagination
from .forms import searchForm

#from sqlalchemy.sql import func





@search.route('/<search_term>', methods=['GET', 'POST'])
def searchresults(search_term):
    form = searchForm(request.form)
    search = False
    q = request.args.get('q')
    if q:
        search = True

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    PER_PAGE = 10
    inner_window = 4
    outer_window = 3
    offset = page * 1

    # doesnt work
    links = Item.query.filter(Item.description.like('%' + search_term + '%')).paginate(page, 10, True)

    # links = db.query.filter(func.mid(Item.description, 1, 3).all()).paginate(page, 10, True)

    total = Item.query.filter(Item.title.like('%' + search_term + '%')).count()
    pagination = get_pagination(page=page,
                                links=links,
                                per_page=PER_PAGE,
                                offset=offset,

                                search_term=search_term,
                                inner_window=inner_window,
                                outer_window=outer_window,
                                search=search,

                                total=total,  # total number of results
                                format_total=True,  # format total. example 1,024
                                format_number=True,  # turn on format flag
                                record_name='links'

                                )
    return render_template('search/searchPage.html', links = links, pagination = pagination,
                           page = page, per_page = PER_PAGE, form=form, search_term=search_term)

def get_css_framework():
    return 'bootstrap3'

def get_link_size():
    return 'sm'  #option lg

def show_single_page_or_not():
    return True


def get_page_items():
    form = searchForm()
    search_term = form.searchString.data
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = current_app.config.get('PER_PAGE', 10)
    else:
        per_page = int(per_page)

    offset = (page - 1) * per_page

    return page, per_page, offset, search_term

def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'repositories')

    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      show_single_page=show_single_page_or_not(),

                      **kwargs

                      )
