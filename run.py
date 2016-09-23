from app import app
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='debug', action='store_true', help='Debug Mode')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    if args.debug:
        print(' * Debug Mode')
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print(' * Production Mode')
        app.run(host='0.0.0.0', port=5000)