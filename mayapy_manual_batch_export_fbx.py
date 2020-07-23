import maya.standalone
maya.standalone.initialize(name = 'pyhton')
import maya.cmds as cmds
import pymel.core as pm

cmds.loadPlugin("fbxmaya", quiet=True) # LOAD PLUGIN

# IMPORT FROM
path = "C:/Users/valiant/Desktop/" # Path From
filename = "hotpot_all" # From Filename
ext = ".fbx"
pm.mel.FBXImport(f=path + filename + ext ,t="TAKE")

# SAVE FILE TO
path = "D:/Submission/" #Change Path
mayaname = "hotpot_all" # Change Name
ext = ".ma"
typefile = "mayaAscii"

cmds.file(rename=path + mayaname + ext )
cmds.file(save=True, type=typefile)

