# -*- coding: utf-8 -*-
import xmltree
from lxml import objectify
    
class EWPProject (object):
    
    def __init__(self, xmlFile):
                
        self.xmlFile = xmlFile
        self.xmltree = objectify.parse(xmlFile)
        self.root = xmltree.getroot()

    def parseProject(self):
        
        self.projectName = self.root.configuration.name
        
        self.chip = ''
    
        #TODO: parse into tree structure    
        self.searchGroups(self.root)
        
        self.defines = []
        self.includes = []
        
        for element in self.root.configuration.getchildren():
            
            if element.tag == 'settings':
                for e in element.data.getchildren():
     
                    if e.tag == 'option':                
                        if e.name.text == 'OGChipSelectEditMenu':                                          
                            self.chip = e.state 
                        elif e.name.text == 'CCDefines':
                            for d in e.getchildren():
                                if d.tag == 'state':
                                    self.defines.append(d.text)
                        elif e.name.text == 'CCIncludePath2':
                            for d in e.getchildren():
                                if d.tag == 'state':
                                    self.includes.append(d.text)
          
    def displaySummary(self):
             
             
        print ('Project Name:' + self.projectName)
        print ('Project chip:' + self.chip)
        print ('Project includes: ' + self.includes)
        print ('Project defines: ' + self.defines)
        
    def searchGroups(self, xml):
    
        for element in xml.getchildren():
    
            if element.tag == 'group':
                self.searchGroups(element)
                
            elif element.tag == 'file':  
                print (element.name)
        