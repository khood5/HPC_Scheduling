# Kendirc Hood
# Cloud Computing HW 2 
# pt:2 Min-Min / Min-Max scheduler
import argparse
from tasks_parser import parser
from bag import bag, min_min, min_max, sufferage

args = argparse.ArgumentParser(description='Do Min-Min and Min-Max scheduling on a bag of tasks.')

args.add_argument('-i', help='Path to CSV file, header is a list of machines each row is a task and associated cost on machines')
args.add_argument('-o', help='Path to folder or file to output schedule')

inputFile = vars(args.parse_args())['i']
outputFile = vars(args.parse_args())['o']

bag = parser(inputFile)
# min_min(bag,outputFile)
#min_max(bag,outputFile)
sufferage(bag,outputFile)