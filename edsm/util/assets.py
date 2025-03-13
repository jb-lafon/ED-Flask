from flask_assets import Bundle, Environment
from edsm import app

bundles = {
    'home_css': Bundle(
        # 'css/common.css',
        'css/home.css',
        output='gen/home.css',
        filters='cssmin'
    ),
    's2r_css': Bundle(
        # 'css/common.css',
        'css/s2r.css',
        output='gen/s2r.css',
        filters='cssmin'
    )
}

assets = Environment(app)

assets.register(bundles)
