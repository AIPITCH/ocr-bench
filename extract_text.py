#!/usr/bin/env python3

import re
import sys
import json
import argparse
import questionary
from pprint import pp
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--result-file", type = str, help = "Input result file")
parser.add_argument("-i", "--image-file", type = str, help = "Image file")
parser.add_argument("-m", "--model", type = str, nargs = '?', const = "all", help = "Model name", default = 'select')
parser.add_argument("-o", "--output", type = str, help = "Output directory")
args = parser.parse_args()

result_file = Path(args.result_file)
output_dir = args.output

sys.stderr.write("####\n")
sys.stderr.write("Selected results file: {}\n".format(result_file))
sys.stderr.write("Selected image: {}\n".format(args.image_file))
sys.stderr.write("Selected model(s): {}\n".format(args.model))
sys.stderr.write("Selected output directory: {}\n".format(args.output))
sys.stderr.write("####\n\n")

with open(result_file, "r") as f:
    data = json.load(f)

result_id = re.search(r"^run_results_(\d+)\.json", result_file.name).group(1)

if args.model == 'select':
    available_models = [model['name'] for model in data['models']] 
    selected_models = questionary.checkbox(
        "Select models:",
        choices=available_models,
    ).ask()

fulltext=""
for result in data['results']:
    if args.image_file == result['file'] and (args.model == result['model'] or args.model == 'all' or result['model'] in selected_models):
        try:
            items = result['model_response']['items']
        except:
            sys.stderr.write("No result found for model {} on this file\n\n".format(result['model']))
            continue

        sys.stderr.write("Processing {} output... ".format(result['model']))
        for item in items:
            fulltext += item['text']+"\n"

        filename = "{}_{}_{}.txt".format(result_id, args.image_file, result['model'])
        with open(output_dir + '/' + filename, "w") as fulltext_file:
            fulltext_file.write(fulltext)

        sys.stderr.write("done ({})\n\n".format(output_dir + '/' + filename))

