# -*- coding: utf-8 -*-
from lxml import objectify
    
class UVPROJXProject (object):
    
    def __init__(self, path, xmlFile):
        
        self.project = {}
        self.xmlFile = xmlFile
        xmltree = objectify.parse(xmlFile)
        self.root = xmltree.getroot()
    
    def parseProject (self):
        
        self.project['name'] = self.root.Targets.Target.TargetName
        self.project['chip'] = self.root.Targets.Target.TargetOption.TargetCommonOption.Device
        self.project['svd'] = self.root.Targets.Target.TargetOption.TargetCommonOption.SFDFile
        self.project['incs'] = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.IncludePath.text.split(';')
        self.project['mems'] = self.root.Targets.Target.TargetOption.TargetCommonOption.Cpu
        self.project['defs'] = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.Define.text.split(',')
        
        self.project['srcs'] = []
        for element in self.root.Targets.Target.Groups.getchildren():
            
            print ('GroupName: ' + element.GroupName.text)
            if hasattr(element,'Files'):
                for file in element.Files.getchildren():
                    #print ('FileName: ' + file.FileName.text)
                    print ('FilePath: ' + file.FilePath.text)

    def displaySummary(self):
        
        print ('Project Name:' + self.project['name'])
        print ('Project chip:' + self.project['chip'])
        print ('Project svd:' + self.project['svd'])
        print ('Project includes: ' + ' '.join(self.project['incs']))        
        print ('Project defines: ' + ' '.join(self.project['defs']))
        print ('Project: ' + self.project['mems'])
        
    def getProject(self):
        
        return self.project
    
