import maya.standalone
maya.standalone.initialize(name = 'python')
import os
import maya.cmds as cmds
import maya.mel as MEL
path="D:/Submission/FBX_NEW/"
path_maya = "D:/Submission/MAYA_FILE/"
matches = []

cmds.loadPlugin("fbxmaya", quiet=True)

for root, dirnames, filenames in os.walk(path):
    files = [ f for f in filenames if os.path.splitext(f)[1] in ('.fbx', '.FBX') ]
    for filename  in filenames:
        matches.append(os.path.join(root, filename))

for i in matches:
    fnamea = str(i).split('\\')[-1:][0]
    fname = str(i).rsplit("\\",1)
    final = (os.path.basename(fname[0]))
    tanpaextensi = (os.path.splitext(final)[0])
    PATH = (path_maya + filename)
    # Import Functions
    try:
        if not os.path.isfile(PATH):
            MEL.eval('string $fnamea = `python "fnamea"`;')
            MEL.eval('FBXImport -f $fnamea')
            cmds.file(rename=path_maya + tanpaextensi +".ma")
            cmds.file(save=True, type="mayaAscii")
            cmds.file(new=1, f=1)
        else:
            pass
    except:
        pass

checking = []
for root, dirnames, filenames in os.walk(path_maya):
    files = [ f for f in filenames if os.path.splitext(f)[1] in ('.ma', '.MA') ]
    for filename  in filenames:
        checking.append(os.path.join(root, filename))

for a in checking:
    count=checking.index(a)
    print 'Doing %s: %s of %s' % (a,count+1,len(checking))
    fname = str(a).rsplit("\\",1)
    final = (os.path.basename(fname[0]))
    tanpaextensi = (os.path.splitext(final)[0])
    filename = tanpaextensi + '.ma'
    PATH = (path_maya + filename)
    try:
        if not os.path.isfile(PATH):
            fnamea = str(a).split('\\')[-1:][0]
            MEL.eval('string $fnamea = `python "fnamea"`;')
            result = os.path.splitext(fnamea)[0]
            MEL.eval('FBXImport -f $fnamea')
            cmds.file(rename=result+".ma")
            cmds.file(save=True, type="mayaAscii")
            cmds.file(new=1, f=1)
            print ("File " + tanpaextensi +  " doesnt exist, created new file in " + path)
        else:
            pass
    except:
        pass
    # Auto Directory
    if len(path_maya) > 0:
        try:
            os.startfile(path_maya)
        except:
            subprocess.Popen(['xdg-open', act.export_dir])
    else:
        pass

