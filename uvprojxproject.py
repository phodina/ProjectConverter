# -*- coding: utf-8 -*-
from lxml import objectify
    
class UVPROJXProject (object):
    
    def __init__(self, path, xmlFile):
        
        self.xmlFile = xmlFile
        xmltree = objectify.parse(xmlFile)
        self.root = xmltree.getroot()
    
    def parseProject (self):
        
        self.projectName = self.root.Targets.Target.TargetName
        self.chip = self.root.Targets.Target.TargetOption.TargetCommonOption.Device
        self.svd = self.root.Targets.Target.TargetOption.TargetCommonOption.SFDFile
        self.includes = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.IncludePath.text.split(';')
        self.memories = self.root.Targets.Target.TargetOption.TargetCommonOption.Cpu
        self.defines = self.root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.Define.text.split(',')
        
        self.sources = []
        for element in self.root.Targets.Target.Groups.getchildren():
            
            
            print ('GroupName: ' + element.GroupName.text)
            if hasattr(element,'Files'):
                for file in element.Files.getchildren():
                    #print ('FileName: ' + file.FileName.text)
                    print ('FilePath: ' + file.FilePath.text)

    def displaySummary(self):
        
        print ('Project Name:' + self.projectName)
        print ('Project chip:' + self.chip)
        print ('Project svd:' + self.svd)
        print ('Project includes: ' + ' '.join(self.includes))        
        print ('Project defines: ' + ' '.join(self.defines))
        print ('Project: ' + self.memories)
    
