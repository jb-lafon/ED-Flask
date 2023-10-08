# import os
from app import app
from sys import argv
from flask_socketio import SocketIO


if str(argv[1]) == '-o':
        # config_slug = 'prod'  # os.getenv('FLASK_CONFIG')
        # app = create_app(config_slug)
        if __name__ == '__main__':
                # port = 5000
                # SocketIO.run(app, app=app, host='0.0.0.0', port=port)
                app.run(host='0.0.0.0', port=8080, threaded=True)
else:
        # config_slug = os.getenv('FLASK_CONFIG')
        # app = create_app(config_slug)
        if __name__ == '__main__':
                app.run(host='127.0.0.1', port=8080)

# if str(argv[1]) == '-l':
#
#     config_slug = os.getenv('FLASK_CONFIG')
#     app = create_app(config_slug)
#
#     if __name__ == '__main__':
#         app.run(host='127.0.0.1', port=8888)
# elif str(argv[1]) == '-o':
#     config_slug = 'prod'
#     app = create_app(config_slug)
#     if __name__ == '__main__':
#         app.run(host='0.0.0.0', port=80)
# else:
#     print("Incorrect optional arguments, please use one of the following :\n"
#           "\n"
#           "-l\tLocal deployment.\n"
#           "-o\tOnline deployment (requires sudo permissions).\n"
#           "\n"
#           "Example usage:\n"
#           "flask run -l\n")
