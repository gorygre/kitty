import argparse
import logging

import parser

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.INFO,
		filename = 'parse.log'
	)

	argparser = argparse.ArgumentParser(description='Meow meow')
	argparser.add_argument('script', help='file to run')
	args = argparser.parse_args()
	script = open(args.script, 'r')
	parser.parser.parse(script.read(), debug=logging.getLogger())
	script.close()
