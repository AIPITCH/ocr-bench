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
parser.add_argument("-f", "--result-file", type = str, help = "Result file to process", required = True)
parser.add_argument("-i", "--image-file", type = str, nargs = '?', const = 'all', help = "Image file of interest", default = 'select')
parser.add_argument("-m", "--model", type = str, nargs = '?', const = "all", help = "Model name of interest", default = 'select')
parser.add_argument("-o", "--output", type = str, help = "Output directory for bbox drawings", required = True)
args = parser.parse_args()

result_file = Path(args.result_file)
output_dir = args.output

sys.stderr.write("####\n")
sys.stderr.write("Selected results file: {}\n".format(result_file))
sys.stderr.write("Selected image: {}\n".format(args.image_file))
sys.stderr.write("Selected model(s): {}\n".format(args.model))
sys.stderr.write("Selected output directory: {}\n".format(args.output))
sys.stderr.write("####\n\n")

def draw_bboxes(file: Path | str, model_name: str, bboxes: list) -> None:
    img = Image.open(file).convert("RGB")
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
    img.save("{}/{}_{}_{}_bboxes.png".format(output_dir, result_id, file.name, model_name))

with open(result_file, "r") as f:
    data = json.load(f)

result_id = re.search(r"^(\d+)_run_results\.json", result_file.name).group(1)

if args.model == 'select':
    available_models = [model['name'] for model in data['models']]
    selected_models = questionary.checkbox(
        "Select models:",
        choices=available_models,
    ).ask()

if args.image_file == 'select':
    available_files = [file['filename'] for file in data['files']]
    selected_files = questionary.checkbox(
        "Select files:",
        choices=available_files,
    ).ask()
    selected_files = [
        Path("{}/{}".format(file['filepath'], file['filename']))
            for file in data['files']
                for selected_file in selected_files
                    if selected_file == file['filename']]
elif args.image_file == 'all':
    selected_files = [Path("{}/{}".format(file['filepath'], file['filename'])) for file in data["files"]]
else:
    selected_files = [Path(args.image_file)]

for result in data['results']:
    if (result['file'] in [file.name for file in selected_files] or args.image_file == 'all') and ( args.model == result['model'] or args.model == 'all' or result['model'] in selected_models):
        sys.stderr.write("Processing {} output... ".format(result['model']))

        try:
            items = result['model_response']['items']
        except:
            sys.stderr.write("No valid result found for model {} in this result file\n\n".format(result['model']))
            continue
        sys.stderr.write("Processing {} output... ".format(result['model']))

        model_response_bboxes = [ item['bbox'] for item in items ]
        [image_file] = ([
            Path("{}/{}".format(file['filepath'], file['filename'])) for file in data['files']
                if result['file'] in [file.name for file in selected_files]
                and result['file'] == file['filename']
        ])
        draw_bboxes(image_file, result['model'], model_response_bboxes)
        sys.stderr.write("done\n\n")

