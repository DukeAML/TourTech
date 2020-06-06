from sys import path
path.append('../parser')
from logparser.logparser import Drain

from backend.logFetcher import LogFetcher
import backend.config


class Parser:
    def __init__(self, input_dir, output_dir, log_file, log_format, regex, sim_threshold, depth):
        self.parserObj = Drain.LogParser(log_format, indir=input_dir, output=output_dir, depth=depth, st=sim_threshold)
        self.logFetcher = LogFetcher('local', '')

    def parseLine():
        if self.parserObj is not None:
            self.parserObj.parseLine(line)
        else:
            print('ERROR: PARSER OBJECT NOT INITIATED')


# SAMPLE USE

# input_dir  = 'logs/'  # The input directory of log file
# output_dir = 'syslogResult/'  # The output directory of parsing results
# log_file   = 'syslog.log'  # The input log file name
# log_format = '<Date>T<Time> <Content>'  # our log format
# # Regular expression list for optional preprocessing (default: [])

# #  provide simple regular expressions based on domain knowledge that represent commonly-used variables, such as IP address and block ID

# #   r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b' # IP... potentially without port? Replaced this... 

# regex      = [
#     r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)' # IP with port?
# ]

# st         = 0.4  # Similarity threshold ==> should we lower this? the whole wifi1 thing
# depth      = 4  # Depth of all leaf nodes

# # Creation of initial log parser model, can add more lines through parser.parseLine() function on same object.... would we have to re-instantiate training on base model every time we start up?

# parser = Drain.LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
# parser.parse(log_file)
# parser.parseLine("2019-09-19T15:36:26+00:00 10.50.0.1 php-fpm[15314]: /index.php: Successful login for user 'admin' from: 172.24.1.30 (Local Database)")