# Kendirc Hood
# Cloud Computing HW 2 
# pt:2 Min-Min / Min-Max scheduler
import argparse
from tasks_parser import parser

args = argparse.ArgumentParser(description='Do Min-Min and Min-Max scheduling on a bag of tasks.')

args.add_argument('file_path', help='Path to CSV file, header is a list of machines each row is a task and associated cost on machines')

path = vars(args.parse_args())['file_path']

bag = parser(path)