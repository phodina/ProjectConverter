# -*- coding: utf-8 -*-

import os
import platform
import datetime
from jinja2 import Environment, FileSystemLoader

class CMake (object):
    
    def __init__(self, project):
        
        self.project = project
        self.context = {}
        
    def populateCMake (self):
        """ Generate CMakeList.txt file for building the project
        """

        # For debug run cmake -DCMAKE_BUILD_TYPE=Debug or Release
        cmake = {}
        fpu = '-mfpu=fpv5-sp-d16 -mfloat-abi=softfp'
        fpu = ''
        
        core = ''
        
        if 'STM32F0' in self.project['chip']:
            core = '-mcpu=cortex-m0'
        elif 'STM32F1' in self.project['chip']:
            core = '-mcpu=cortex-m3'
        elif 'STM32F2' in self.project['chip']:
            core = '-mcpu=cortex-m3'
        elif 'STM32F3' in self.project['chip']:
            core = '-mcpu=cortex-m4'
        elif 'STM32F4' in self.project['chip']:
            core = '-mcpu=cortex-m4'
        elif 'STM32F7' in self.project['chip']:
            core = '-mcpu=cortex-m7'
        elif 'STM32L0' in self.project['chip']:
            core = '-mcpu=cortex-m0'
        elif 'STM32L1' in self.project['chip']:
            core = '-mcpu=cortex-m3'
        elif 'STM32L4' in self.project['chip']:
            core = '-mcpu=cortex-m4'
            
        cmake['version'] = '3.1'
        cmake['project'] = self.project['name']
        cmake['incs'] = []
        for inc in self.project['incs']:    
            cmake['incs'].append(inc)    
        cmake['srcs'] = []
        cmake['srcs'].append({'path':'src','var':'DIR_SRC'})  

        cmake['cxx'] = 'false'
        
        cmake['c_flags'] = '-g -Wextra -Wshadow -Wimplicit-function-declaration -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes -fno-common -ffunction-sections -fdata-sections -MD -Wall -Wundef -mthumb ' + core + ' ' + fpu

        cmake['cxx_flags'] = '-Wextra -Wshadow -Wredundant-decls  -Weffc++ -fno-common -ffunction-sections -fdata-sections -MD -Wall -Wundef -mthumb ' + core + ' ' + fpu
 
        cmake['asm_flags'] = '-g -mthumb ' + core + ' ' + fpu + ' -x assembler-with-cpp'
        cmake['linker_flags'] = '-g -Wl,--gc-sections -Wl,-Map=' + cmake['project'] + '.map --static -nostartfiles -Wl,--start-group -specs=nosys.specs -lc -lgcc -lnosys -Wl,--end-group -mthumb ' + core + ' ' + fpu
        cmake['linker_script'] = 'stm32.ld'
        cmake['linker_path'] = 'libopencm3/lib'        
        cmake['defines'] = []
        for define in self.project['defs']:
            cmake['defines'].append(define)
            
        cmake['libs'] = []
        #cmake['libs'].append({'name':'opencm3_' + self.root.MCU.attrib['Family'].lower(),'path':'libopencm3/lib'})
        
        self.context['cmake'] = cmake
                
        self.generateFile('CMakeLists.txt')

        print ('Created file CMakeLists.txt')
        
    def generateFile (self, pathSrc, pathDst='', author='Pegasus', version='v1.0.0', licence='licence.txt', template_dir='../PegasusTemplates'):
        
        if (pathDst == ''):
            pathDst = pathSrc
            
        print (os.getcwd())
        self.context['file'] = os.path.basename(str(pathSrc))
        self.context['author'] = author
        self.context['date'] = datetime.date.today().strftime('%d, %b %Y')
        self.context['version'] = version
        self.context['licence'] = licence
        
        env = Environment(loader=FileSystemLoader(template_dir),trim_blocks=True,lstrip_blocks=True)
        template = env.get_template(str(pathSrc))
        
        generated_code = template.render(self.context)
            
        if platform.system() == 'Window':    

            with open(pathDst, 'wb') as f:
                f.write(generated_code)
        
        elif platform.system() == 'Linux':

            with open(pathDst, 'wb') as f:
                f.write(str.encode(generated_code))        
        else:
            # Different OS than Windows or Linux            
            pass