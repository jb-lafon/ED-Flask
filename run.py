from edsm import app
from sys import argv

if str(argv[1]) == '-l':
    # Local deployment
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8888)
elif str(argv[1]) == '-o':
    # Online deployment
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80)
else:
    print("Incorrect optional arguments, please use one of the following :\n"
          "\n"
          "-l\tLocal deployment.\n"
          "-o\tOnline deployment (requires sudo permissions).\n"
          "\n"
          "Example usage:\n"
          "python3 run.py -l\n")
