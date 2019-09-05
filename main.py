'''Submitting all authority to Google Python Style Guide
https://google.github.io/styleguide/pyguide.html'''

import json
import os
import argparse
from copy import deepcopy


# read the file and return the contents
def get_file_contents(filename):
    with open(filename, 'r', encoding='utf8') as fh:
        contents = fh.readlines()
    return ''.join(contents)


# read the json file and return its contents
def get_json_contents(filename):
    with open(filename, 'r', encoding='utf8') as fh:
        data = json.load(fh)
    return data


# save the file
def save_file_contents(filename, contents, output_folder):
    if output_folder[-1] != os.path.sep:
        output_folder += os.path.sep
    filepath = "%s%s" % (output_folder, filename)
    fh = open(filepath, 'w')
    fh.write(contents)
    fh.close()


# run the program
def run_program(template, data, output_folder):
    # gather all the resources
    contents = get_file_contents(template)
    data = get_json_contents(data)
    # loop through the json
    for file_details in data['files']:
        new_contents = deepcopy(contents)
        new_filename = file_details.pop('filename')
        for key, details_var in file_details.items():
            key_subtitute = "${%s}" % (key)
            new_contents = new_contents.replace(key_subtitute, details_var)
        save_file_contents(new_filename, new_contents, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create HTML files from template using json data')
    parser.add_argument('-o', '--outdir', dest='output_folder',
                        default='out', help="directory for the output html files")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-t', '--template', dest='template', required=True,
                               help="template HTML file that will be used to replace data")
    required_args.add_argument('-j', '--json', dest='data', required=True,
                               help="data to use to replace HTML file placeholders")
    args = parser.parse_args()
    run_program(args.template, args.data, args.output_folder)
