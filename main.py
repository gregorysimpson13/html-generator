'''Submitting all authority to Google Python Style Guide
https://google.github.io/styleguide/pyguide.html'''

import json
import os

# GLOBALS
IN_TEMPLATE = 'test.in.html'
IN_JSON = 'details.json'
OUTPUT_FOLDER = 'out/'


# read the file and return the contents
def get_file_contents(filename):
    with open(filename, 'r') as fh:
        contents = fh.readlines()
    return ''.join(contents)


# read the json file and return its contents
def get_json_contents(filename):
    with open(filename) as fh:
        data = json.load(fh)
    return data


# save the file
def save_file_contents(filename, contents, output_folder=OUTPUT_FOLDER):
    if output_folder[-1] != os.path.sep:
        output_folder += os.path.sep
    filepath = "%s%s" % (output_folder, filename)
    fh = open(filepath, 'w')
    fh.write(contents)
    fh.close()


# run the program
def run_program():
    # gather all the resources
    contents = get_file_contents('test.in.html')
    data = get_json_contents(IN_JSON)
    # loop through the json
    for file_details in data['files']:
        new_filename = file_details.pop('filename')
        for key, details_var in file_details.items():
            key_subtitute = "${%s}" % (key)
            new_contents = contents.replace(key_subtitute, details_var)
        save_file_contents(new_filename, new_contents)


if __name__ == "__main__":
    run_program()
