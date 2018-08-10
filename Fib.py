#!/usr/bin/python

import argparse
import sys

def _parseargs():
    '''This helper function parses the command line arguments and ensure
    they are correct.
    '''

    description = 'This script is used to calculate a Fibonacci sequence '\
				  'to the index limit provided'
    prog        = 'Fib'
    usage       = '[-h] sequence_limit'
    epilog      = '''
        Examples:
            Fib.py 5
                  '''
    parser = argparse.ArgumentParser(epilog=epilog,\
                                     usage = usage,\
                                     prog=prog,\
                                     description=description,\
                                     formatter_class=argparse.\
                                     RawTextHelpFormatter)

    parser.add_argument('sequence_limit',
                        help='the iteration limit for calculating the Fibonacci sequence')
    parser.add_argument('--version',
                        action='version',
                        version='Peter Wihl '\
                                '(peter.wihl@gmail.com)\n'\
                                '%(prog)s 0.1 (12/29/2015)')
    return parser.parse_args()

def _f_cal1(seq_limit):
	'''
	This helper function expects a sequence limit 
	'''
	if seq_limit == 0:
		return 0
	elif seq_limit == 1:
		return 1
	else:
		return _f_cal1(seq_limit-1) + _f_cal1(seq_limit-2)

def _f_cal2(seq_limit):
	'''
	This helper function expects a sequence limit 
	'''

	f_seq = [1,1]
	for item in xrange(2,seq_limit,1):
		f_seq.append(f_seq[-1]+f_seq[-2])

	return f_seq

def main():
	options = _parseargs()
	seq_limit = int(options.sequence_limit)

	if seq_limit < 0:
		print('Error: "{:d}" less than 0'.format(seq_limit))
		exit(-1)
	elif seq_limit == 0:
		return 0
	elif seq_limit == 1:
		print('Memoization Version:')
		sys.stdout.write('1\n')
		return 0
	elif seq_limit == 2:
		print('Memoization Version:')
		sys.stdout.write('1,1\n')
		return 0
	else:
		print('Memoization Version:')
		f_seq = _f_cal2(seq_limit)

	if seq_limit < 30:
		sys.stdout.write(str(f_seq[0]))
		for item in f_seq[1:]:
			sys.stdout.write(',')
			sys.stdout.write(str(item))
	else:
		sys.stdout.write(str(f_seq[-1]))
	sys.stdout.write('\n')

	print('Recursive Version:')

	num = _f_cal1(seq_limit)
	print num

	return 0

if __name__ == '__main__':
    main()
    sys.exit(main())
	
