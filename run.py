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


#### parameters
ollama_url = "http://localhost:11434"
ollama_timeout = 60
ollama_loader_timeout = 120
ollama_prompt = 'Reproduce all visible text and special characters exactly as written, preserving line breaks and any tabular structure, without summarizing, translating, or interpreting the content. Prefix watermarked text including special characters with [WATERMARK]'
samples_dir = "~/git/ocr-bench/samples/"
image_extensions = ['.png', '.jpg', '.jpeg']


#### function definitions
def get_available_models():
    # get list of models
    response = requests.get(ollama_url + "/api/tags")
    
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
        path
        for path in samples_path.glob('*')
        if path.is_file() and path.suffix.lower() in image_extensions
    ]
    
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


def unload_models(model_to_keep,loader):
    # use empty string in model_to_keep to unload all models
    ps = loader.ps()
    already_found = False
    for i in ps.models:
        if i['name'] != model_to_keep or already_found:
            print('Unloading ' + i['name'])
            loader.generate(model = i['name'], prompt = "", keep_alive = 0)
        else:
            already_found = True


def load_model(model_name,loader):
    loader.generate(model = model_name, prompt = "")
    ps = loader.ps()
    return ps['models'][0].size_vram


def write_results():
    with open("run_results_" + datetime.datetime.now().strftime('%s') + ".json", "w") as results_file:
        results_file.write(json.dumps(results))


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
    
    models=get_available_models()
    print("########")
    print("Available models:")
    for i in range(len(models)):
        print("    [" + str(i) + "] " + models[i]['name'])
    
    files=get_list_of_files()
    print("\n########")
    print("Files to be considered:")
    for i in range(len(files)):
        print("    [" + str(i) + "] " + files[i].name)
    
    if args.dry_run:
        sys.exit(1)
    
    results["files"] = [str(file) for file in files]
    results["models"] = models
    results["results"] = []
    for model in models:
        model_name = model['model']
        unload_models(model_name,loader)
        print("\nLoading " + model_name + " ...")
        vram_usage=load_model(model_name, loader)
        print("done")
        for file in files:
            current_result = {"model": model_name, "vram_usage": vram_usage, "file": file.name}
            print("Processing " + file.name + " with " + model_name)
            
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
                            'images': [file],
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
