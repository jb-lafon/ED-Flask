# ==========
# File : __init__.py.py
# Author : Jb
# First created on : 21/11/2018
# Description: App init file
# ==========

from flask_assets import Bundle, Environment
from app import appli

# config_slug = getenv('FLASK_CONFIG')
# app = create_app(config_slug)

bundles = {
    'home_css': Bundle(
        'css/home.css',
        output='gen/home.css',
        filters='cssmin'
    ),
    'home_unlogged_css': Bundle(
        'css/home_not_logged.css',
        output='gen/home.css',
        filters='cssmin'
    ),
    's2r_css': Bundle(
        'css/s2r.css',
        output='gen/s2r.css',
        filters='cssmin'
    )
}

assets = Environment(appli)

assets.register(bundles)
