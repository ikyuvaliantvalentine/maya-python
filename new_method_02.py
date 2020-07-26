import maya.standalone
maya.standalone.initialize(name = 'python')
import os
import maya.cmds as cmds
import maya.mel as MEL
import pymel.core as pm
path="D:\Submission\FBX_NEW".replace('\\', '/') + '/' # Change this Directory
matches = []

cmds.loadPlugin("fbxmaya", quiet=True)

# Detect Extensions
for filenames in os.listdir(path):
    files = [ f for f in filenames if os.path.splitext(f)[1] in ('.fbx', '.FBX', '.ma', '.MA') ]
    if os.path.isfile(os.path.join(path, filenames)):
        matches.append(os.path.join(path, filenames))
# for root, dirnames, filenames in os.walk(path):
#     files = [ f for f in filenames if os.path.splitext(f)[1] in ('.fbx', '.FBX', '.ma', '.MA') ]
#     for filename  in filenames:
#         matches.append(os.path.join(root, filename))
#     break #stop loop

for i in matches:
    count=matches.index(i)
    fnamea = str(i).split('\\')[-1:][0] 
    fname = str(i).rsplit("\\",1)
    final = (os.path.basename(fname[0])) 
    tanpaextensi = (os.path.splitext(final)[0])
    filename = tanpaextensi + '.ma'
    PATH = (path + filename)
    # Import Functions
    try:
        if not os.path.isfile(PATH):
            # MEL.eval('string $fnamea = `python "fnamea"`;')
            result = os.path.splitext(fnamea)[0]
            # pm.mel.FBXImport(f=fnamea ,t="TAKE")
            pm.mel.FBXImport(f=path + final ,t="TAKE")
            # MEL.eval('FBXImport -f $fnamea')
            cmds.file(rename=result+".ma")
            cmds.file(save=True, type="mayaAscii")
            cmds.file(new=1, f=1)
            print ("File " + tanpaextensi +  " doesnt exist, created new file in " + path)
            print 'Doing %s: %s of %s' % (i,count+1,len(matches))
            print ('succes created file in  ' + path )
        else:
            print ("File " + final + " exist in " + path)
    except:
        pass
    # Auto Open Directory
    if len(path) > 0:
        try:
            os.startfile(path)
        except:
            subprocess.Popen(['xdg-open', act.export_dir])
    else:
        pass

