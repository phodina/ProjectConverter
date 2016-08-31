# -*- coding: utf-8 -*-
import os
import argparse
import ewpproject
import uvprojxproject

def findFile (path,fileext):
    
    file = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileext):
                file = os.path.join(root, file)
    
    return file 
             
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Root directory of project")    
    parser.add_argument("--ewp",help="Search for *.EWP file in project structure",action='store_true')    
    parser.add_argument("--uvprojx",help="Search for *.UPROJX file in project structure",action='store_true')
    
    args = parser.parse_args()
        
    if (os.path.isdir (args.path)):
        
        if args.ewp:
            print ('Looking for *.ewp file in ' + args.path)
            file = findFile(args.path,'.ewp')
            if (len(file)):
                print ('Found project file: ' + file)
                project = ewpproject.EWPProject(file)
                project.parseProject()
                project.displaySummary()
            else:
                print ('No project *.ewp file found')
                
        elif args.uvprojx:
            print ('Looking for *.uvprojx file in ' + args.path)
            file = findFile(args.path,'.uvprojx')
            if (len(file)):
                print ('Found project file: ' + file)
                project = uvprojxproject.UVPROJXProject(file)
                project.parseProject()
                project.displaySummary()
            else:
                print ('No project *.uvprojx file found')
    else:

        print ('Not a valid file path')               

