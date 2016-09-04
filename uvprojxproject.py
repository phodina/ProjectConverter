# -*- coding: utf-8 -*-

import os
from lxml import objectify
    
class UVPROJXProject (object):
    
    def __init__(self, path, xmlFile):
        
        self.path = path
        self.project = {}
        self.xmlFile = xmlFile
        xmltree = objectify.parse(xmlFile)
        self.root = xmltree.getroot()
    
    def parseProject (self):
        
        self.project['name'] = self.root.Targets.Target.TargetName
        self.project['chip'] = str(self.root.Targets.Target.TargetOption.TargetCommonOption.Device)
        self.project['incs'] = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.IncludePath.text.split(';')
        self.project['mems'] = self.root.Targets.Target.TargetOption.TargetCommonOption.Cpu
        self.project['defs'] = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.Define.text.split(',')
        
        self.project['srcs'] = []
        for element in self.root.Targets.Target.Groups.getchildren():
            
            print ('GroupName: ' + element.GroupName.text)
            if hasattr(element,'Files'):
                for file in element.Files.getchildren():
                    if not str(file.FilePath.text).endswith('.s'):
                        self.project['srcs'].append(str(file.FilePath.text).replace('..', self.path))
        
        for i in range(0, len(self.project['incs'])):
            self.project['incs'][i] = self.project['incs'][i].replace('..', self.path)
            
        
        self.project['files']=[]
        i=0        
        
        if os.path.exists(self.path + '/Drivers/CMSIS/Device/ST/STM32F0xx/Source/Templates/gcc'):
            for entry in os.listdir(self.path + '/Drivers/CMSIS/Device/ST/STM32F0xx/Source/Templates/gcc'):
                if entry.endswith('.S') or entry.endswith('.s'):          
                    self.project['files'].append(self.path + '/Drivers/CMSIS/Device/ST/STM32F0xx/Source/Templates/gcc/'+ entry)
                            

    def displaySummary(self):
        
        print ('Project Name:' + self.project['name'])
        print ('Project chip:' + self.project['chip'])
        print ('Project includes: ' + ' '.join(self.project['incs']))        
        print ('Project defines: ' + ' '.join(self.project['defs']))                
        print ('Project srcs: ' + ' '.join(self.project['defs']))
        print ('Project: ' + self.project['mems'])
        
    def getProject(self):
        
        return self.project
    
