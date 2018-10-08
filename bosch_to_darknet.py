#!/usr/bin/env python
"""
This script Converts Yaml annotations to Darknet .txt Files
of the Bosch Small Traffic Lights Dataset.
Example usage:
    python bosch_to_darknet.py input_yaml out_folder
"""

import os
import sys
import yaml
import os.path


def write_xml(savedir, image, imgWidth, imgHeight,
              depth=3, pose="Unspecified"):

    boxes = image['boxes']
    impath = image['path']
    imagename = impath.split('/')[-1]
    imagename = imagename.split('.')[0]
    
    save_path = os.path.join(savedir, imagename + ".txt")
    with open(save_path, 'a') as temp_xml:
        line = ''
        for box in boxes:
            line = '0 '
            line += str(box['x_min']/imgWidth)+' '
            line += str(box['y_min']/imgHeight)+ ' '
            line += str((box['x_max']-box['x_min'])/imgWidth)+ ' '
            line += str((box['y_max']-box['y_min'])/imgHeight)+ '\n'
            temp_xml.write(line)
            line = ''

    
       


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(-1)
    yaml_path = sys.argv[1]
    out_dir = sys.argv[2]
    images = yaml.load(open(yaml_path, 'rb').read())

    for image in images:
        write_xml(out_dir, image, 1280, 720, depth=3, pose="Unspecified")
