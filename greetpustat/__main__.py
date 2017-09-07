import argparse
from .greet import greet
FLAGS = None
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--greeter', type = str, default = 'Min',help = 'the name of the greeter')
    parser.add_argument('--name', type = str,help = 'the name of the person you want to greet')
    FLAGS, unparsed = parser.parse_known_args()
    #print(FLAGS.name)
    greet(FLAGS.name,FLAGS.greeter)

if __name__ == '__main__':
    main()
