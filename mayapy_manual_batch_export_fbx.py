import maya.standalone
maya.standalone.initialize(name = 'pyhton')
import os
import maya.cmds as cmds
import pymel.core as pm

cmds.loadPlugin("fbxmaya", quiet=True) # LOAD PLUGIN

# IMPORT FROM
path="D:\Project\SALMON\New folder\FBX\SSS".replace('\\', '/') + '/' # Change Path
filename = "drinking_fountain_hi" # From Filename
ext = ".fbx"
pm.mel.FBXImport(f=path + filename + ext ,t="TAKE")

# SAVE FILE TO
path_maya = "D:\Project\SALMON\New folder\FBX\SSS\MAYA_FILES".replace('\\', '/') + '/' #Change Path
mayaname = "drinking_fountain_hi_pop" # Change Name
ext = ".ma"
typefile = "mayaAscii"

cmds.file(rename=path_maya + mayaname + ext )
cmds.file(save=True, type=typefile)

# Auto Open Directory
if len(path_maya) > 0:
    try:
        os.startfile(path_maya)
    except:
        subprocess.Popen(['xdg-open', act.export_dir])
else:
    pass
  
  
