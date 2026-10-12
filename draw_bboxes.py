#!/usr/bin/env python3

import re
import sys
import json
import argparse
import questionary
from pprint import pp
from pathlib import Path
from PIL import Image, ImageDraw


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

def draw_bboxes(file: str, model_name: str, bboxes: list) -> None:
    img = Image.open("samples/" + file).convert("RGB")
    width, height = img.size
    draw = ImageDraw.Draw(img)

    for bbox in bboxes:
        left, top, right, bottom = bbox 
        bbox = [
            round(left * width / 999),
            round(top * height / 999),
            round(right * width / 999),
            round(bottom * height / 999),
        ] 
        draw.rectangle(bbox, outline="red", width=1)
    img.save("{}/{}_{}_{}_bboxes.png".format(output_dir, result_id, file, model_name))

with open(result_file, "r") as f:
    data = json.load(f)

result_id = re.search(r"^run_results_(\d+)\.json", result_file.name).group(1)

if args.model == 'select':
    available_models = [model['name'] for model in data['models']]
    selected_models = questionary.checkbox(
        "Select models:",
        choices=available_models,
    ).ask()

for result in data['results']:
    if args.image_file == result['file'] and (args.model == result['model'] or args.model == 'all' or result['model'] in selected_models):
        try:
            items = result['model_response']['items']
        except:
            sys.stderr.write("No result found for model {} on this file\n\n".format(result['model']))
            continue

        sys.stderr.write("Processing {} output... ".format(result['model']))

        model_response_bboxes = [ item['bbox'] for item in items ]
        draw_bboxes(args.image_file, result['model'], model_response_bboxes)
        sys.stderr.write("done\n\n")

