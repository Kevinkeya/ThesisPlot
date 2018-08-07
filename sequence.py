import os
import json


def get_sequence_files():
    compress_ = "compress"
    subfolders = [f.path for f in os.scandir(compress_) if f.is_dir()]
    seq_files = dict()
    for subfolder in subfolders:
        files = [f.path for f in os.scandir(subfolder) if not f.is_dir()]
        seq_file = None
        for file in files:
            if file.endswith("template_seq_matirx.json"):
                seq_file = file
                break

        seq_files[subfolder] = seq_file

    # print(json.dumps(seq_files, indent=4))
    return seq_files


def count_seq_file(seq_dict):
    for k, v in seq_dict.items():
        print("host_name:", k)
        if v is not None:
            with open(v, 'r') as input:
                cur_seq_dict = json.load(input)
                print(json.dumps(cur_seq_dict, indent=4))
        break


seq_dict = get_sequence_files()
count_seq_file(seq_dict)
