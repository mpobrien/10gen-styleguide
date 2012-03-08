from styleguide import app
from flask import Flask
from flask import render_template, request, jsonify, g, redirect, url_for, session, abort, flash
import re, os, sys, json
from unidecode import unidecode


NAV = {
            "logos": {"name":"Logos",
                      "sub": ["Logo Variations", "Correct Usage", "Spelling"]},
            "colors":{"name":"Colors",
                      "sub":["Palette","Usage", "On Photography"]},
            "fonts":{"name":"Fonts",
                     "sub":["Typeface", "Headings","Body Copy"]},
            "images":{"name":"Images",
                      "sub":["Thumbnails", "Labels", "Sizes", "Ratios" ]},
            "layouts":{"name":"Layouts",
                       "sub":["Grid", "Layouts", "Responsive Design"]},
            "widgets":{"name":"Widgets",
                       "sub":
                       ["Quote Box", "Footer", "Navigation","Carousel",
                        "Image Gallery", "Localization", "Overlay Panels",
                        "Identity", "Infographics", "Local Search",
                        "Accordions", "Alerts", "Modals", "Drag and Drop",
                        "Sortable Timeline", "Mapping", "Legacy Content", "Vote"]},
            "fundamental-elements":
                {"name":"Fundamental Elements",
                 "sub": ["Tables", "Forms", "Buttons", "Icons",
                         "Tabs", "Pills", "Tooltips", "Pagination"]}
           }

SECTIONS = set([section["name"] for section in NAV.itervalues()])
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

@app.template_filter('slugify')
def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unicode(delim.join(result))

@app.route("/")
def home():
  return render_template("index.html",
                         topnav=NAV,
                         topnav_active=section)

@app.route("/<section>")
def section(section):
    if section not in NAV:
        abort(404)

    subnav = NAV[section]['sub']
    
    return render_template(section + ".html",
                           topnav=NAV,
                           topnav_active=section,
                           subnav=subnav
                           )


