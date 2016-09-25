# -*- coding: utf-8 -*-

""" Entry point for project conversion
    @file
"""

import os
import argparse
import cmake
import ewpproject
import uvprojxproject

def find_file(path, fileext):
    """ Find file with extension in path
        @param path Root path of the project
        @param fileext File extension to find
        @return File name
    """
    filename = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileext):
                file = os.path.join(root, filename)
    return filename

if __name__ == '__main__':
    """ Parses params and calls the right conversion"""

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Root directory of project")
    parser.add_argument("--ewp", help="Search for *.EWP file in project structure", action='store_true')
    parser.add_argument("--uvprojx", help="Search for *.UPROJX file in project structure", action='store_true')
    args = parser.parse_args()

    if os.path.isdir(args.path):
        if args.ewp:
            print('Looking for *.ewp file in ' + args.path)
            filename = find_file(args.path, '.ewp')
            if len(filename):
                print('Found project file: ' + filename)
                project = ewpproject.EWPProject(args.path, filename)
                project.parseProject()
                project.displaySummary()
                cmakefile = cmake.CMake(project.getProject(), args.path)
                cmakefile.populateCMake()
            else:
                print('No project *.ewp file found')
        elif args.uvprojx:
            print('Looking for *.uvprojx file in ' + args.path)
            filename = find_file(args.path, '.uvprojx')
            if len(filename):
                print('Found project file: ' + filename)
                project = uvprojxproject.UVPROJXProject(args.path, filename)
                project.parseProject()
                project.displaySummary()

                cmakefile = cmake.CMake(project.getProject(), args.path)
                cmakefile.populateCMake()
            else:
                print('No project *.uvprojx file found')
    else:
        print('Not a valid file path')
