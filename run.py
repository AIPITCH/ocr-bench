#!/usr/bin/env python

from ollama import Client
from pathlib import Path
from pprint import pprint as pp
import sys
import argparse
import json
import datetime
import requests
from httpx import TimeoutException
from hashlib import sha256


#### parameters
ollama_url = "http://localhost:11434"
ollama_timeout = 240
ollama_loader_timeout = 120
ollama_prompt = """
You're as OCR/STR engine.
Return ONLY valid JSON. No Markdown and no explanation.

Coordinate system:
- bbox format: [x_min, y_min, x_max, y_max]
- coordinates are integers normalized from 0 to 1000
- origin [0, 0] is the image top-left
- [1000, 1000] is the image bottom-right
- each bbox must tightly cover the visible text
- enforce: 0 <= x_min < x_max <= 1000
- enforce: 0 <= y_min < y_max <= 1000

Return one object per text line in an array in a wrapping top-level object:
{
  "items": [
    {
      "id": "line_001",
      "text": "Reproduce all visible text and special characters exactly as written, preserving line breaks and any tabular structure, without summarizing, translating, or interpreting the content. Prefix watermarked text including special characters with [WATERMARK]",
      "bbox": [x_min, y_min, x_max, y_max],
      "confidence": 0.0
    }
  ]
}
DO NOT PREFIX the answer with the text "json"!
"""
samples_dir = "~/git/ocr-bench/samples/"
image_extensions = ['.png', '.jpg', '.jpeg']


#### function definitions
def get_available_models():
    # get list of models
    try:
        response = requests.get(ollama_url + "/api/tags")
    except requests.ConnectionError as e:
        print("Can't connect to Ollama instance!")
        sys.exit(1)
    
    if response.status_code != 200:
        print("\nCannot get list of models from Ollama, exiting...")
        sys.exit(1)
    
    models = response.json()['models']
    
    if len(models) < 1:
        print("\nNo models available, exiting...")
        sys.exit(1)

    return models


def get_list_of_files():
    samples_path = Path(samples_dir)
    samples_path = samples_path.expanduser()
    
    # get list of jpeg and png files
    files = [
        { 'path': path, 'hash': sha256(path.read_bytes()).hexdigest() }
        for path in samples_path.glob('*')
        if path.is_file() and path.suffix.lower() in image_extensions
    ]

    files = sorted(files, key=lambda file: file['path'].name)

    if len(files) < 1:
        print("\nNo files to process, exiting...")
        sys.exit(1)
    return files


def get_ollama_clients():
    return [
            Client(
                host = 'http://localhost:11434',
                timeout = ollama_timeout
            ),
            Client(
                host = 'http://localhost:11434',
                timeout = ollama_loader_timeout
            )
    ]


def unload_models(model_to_keep, loader):
    # use empty string in model_to_keep to unload all models
    ps = loader.ps()
    already_found = False
    for i in ps.models:
        if i['name'] != model_to_keep or already_found:
            print('Unloading ' + i['name'])
            loader.generate(model = i['name'], prompt = "", keep_alive = 0)
        else:
            already_found = True


def load_model(model_name, loader):
    loader.generate(model = model_name, prompt = "")
    ps = loader.ps()
    return ps['models'][0].size_vram


def write_results():
    ts = datetime.datetime.now().strftime('%s')
    filename = "run_results_" + ts + ".json"
    with open(filename, "w") as results_file:
        results_file.write(json.dumps(results))
    print("\nRun results written to " + filename)


args = sys.argv[1:]
options = "d"
long_options = ["dry-run"]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dry-run", help = "Dry run, only list files & models", action = "store_true")
args = parser.parse_args()

chat_client, loader = get_ollama_clients()

results = {}
def main():
    
    if args.dry_run:
        print("Dry run mode...")
    
    models = get_available_models()
    print("########")
    print("Available model(s):")
    for i in range(len(models)):
        print("    [" + str(i) + "] " + models[i]['name'])
    
    files = get_list_of_files()
    print("\n########")
    print("File(s) to be considered:")
    for i in range(len(files)):
        print("    [" + str(i) + "] " + files[i]['path'].name + " (SHA256: " + files[i]['hash'] + ")")
    
    if args.dry_run:
        sys.exit(1)
    
    results["files"] = [
        { 'filename': file['path'].name, 'filepath': str(file['path'].parents[0]), 'filehash': file['hash'] }
        for file in files
    ]

    results["models"] = models
    results["results"] = []
    for model in models:
        model_name = model['model']
        unload_models(model_name,loader)
        sys.stdout.write("\nLoading " + model_name + " ...")
        vram_usage = load_model(model_name, loader)
        print("done")
        for file in files:
            current_result = {'model': model_name, 'vram_usage': vram_usage, 'file': file['path'].name}
            print("Processing " + file['path'].name + " with " + model_name)
            
            current_result['status'] = 'ok'
            begin = datetime.datetime.now()
            current_result['start_time'] = begin.strftime('%Y/%m/%d %H:%M:%S.%f')
            try:
                response = chat_client.chat(
                    model = model_name,
                    messages = [
                        {
                            'role': 'user',
                            'content': ollama_prompt,
                            'images': [file['path']],
                        }
                    ],
                )
            except TimeoutException:
                print("Timeout!")
                current_result['status'] = 'timeout'
            except Exception as e:
                print("Error!")
                current_result['status'] = 'error'
                current_result['error_message'] = repr(e)
    
            time_spent = datetime.datetime.now() - begin
            print("Time spent: ", time_spent)
            current_result['time_spent'] = time_spent.total_seconds()
            if current_result['status'] == 'ok':
                current_result['model_response'] = response.message.content
            results['results'].append(current_result)
    
    # unload all running models
    unload_models("", loader)
    
    write_results()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        write_results()
        unload_models("", loader)
        print('Interrupted!')
        sys.exit(1)
