from lxml import objectify


def searchGroups(xml):
    
    for element in xml.getchildren():

        if element.tag == 'group':
            searchGroups(element)
            
        elif element.tag == 'file':  
            print (element.name)
    
def parseEWP():
    
    xmlFile = "Test.ewp"
    xmltree = objectify.parse(xmlFile)
    root = xmltree.getroot()
    
    projectName = root.configuration.name
    print ('Project Name:' + projectName)
    
    chip = ''

    #TODO: parse into tree structure    
    searchGroups(root)
    
    defines = []
    includes = []
    
    for element in root.configuration.getchildren():
        
        if element.tag == 'settings':
            for e in element.data.getchildren():
 
                if e.tag == 'option':                
                    if e.name.text == 'OGChipSelectEditMenu':                                          
                        chip = e.state 
                    elif e.name.text == 'CCDefines':
                        for d in e.getchildren():
                            if d.tag == 'state':
                                defines.append(d.text)
                    elif e.name.text == 'CCIncludePath2':
                        for d in e.getchildren():
                            if d.tag == 'state':
                                includes.append(d.text)
                        
    print (includes)
    print (defines)    
    print (chip)
    
def parseUVPROJX():
    
    xmlFile = 'Test.uvprojx'
    xmltree = objectify.parse(xmlFile)
    root = xmltree.getroot()
    
    projectName = root.Targets.Target.TargetName
    
    chip = root.Targets.Target.TargetOption.TargetCommonOption.Device
    svd = root.Targets.Target.TargetOption.TargetCommonOption.SFDFile
    includes = root.Targets.Target.TargetOption.TargetArmAds.Cads.VariousControls.IncludePath.text
    memories = root.Targets.Target.TargetOption.TargetCommonOption.Cpu
    print ('Project Name:' + projectName)
    print ('Project chip:' + chip)
    print ('Project svd:' + svd)
    print ('Project includes: ' + includes)
    print ('Project: ' + memories)
    
    for element in root.Targets.Target.Groups.getchildren():
        
        print ('GroupName: ' + element.GroupName.text)
        for file in element.Files.getchildren():
            print ('FileName: ' + file.FileName.text)
            print ('FilePath: ' + file.FilePath.text)
    
if __name__ == '__main__':
    
    pass