import maya.standalone
maya.standalone.initialize(name = 'python')
import os
import maya.cmds as cmds
import maya.mel as MEL
path="D:/Submission/FBX_NEW/"
matches = []

cmds.loadPlugin("fbxmaya", quiet=True)

for root, dirnames, filenames in os.walk(path):
    files = [ f for f in filenames if os.path.splitext(f)[1] in ('.fbx', '.FBX') ]
    for filename  in filenames:
        matches.append(os.path.join(root, filename))

for i in matches:
    count=matches.index(i)
    print 'Doing %s: %s of %s' % (i,count+1,len(matches))
    
    fnamea = str(i).split('\\')[-1:][0]
    MEL.eval('string $fnamea = `python "fnamea"`;')
    result = os.path.splitext(fnamea)[0]
    MEL.eval('FBXImport -f $fnamea')
    cmds.file(rename=result+".ma")
    cmds.file(save=True, type="mayaAscii")
    cmds.file(new=1, f=1)
    print ('succes created file in  ' + path )


checking = []
for root, dirnames, filenames in os.walk(path):
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
    PATH = (path + filename)
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print("File exists and is readable")
    else:
        fnamea = str(a).split('\\')[-1:][0]
        MEL.eval('string $fnamea = `python "fnamea"`;')
        result = os.path.splitext(fnamea)[0]
        MEL.eval('FBXImport -f $fnamea')
        cmds.file(rename=result+".ma")
        cmds.file(save=True, type="mayaAscii")
        cmds.file(new=1, f=1)
        print ("File " + tanpaextensi +  " doesnt exist, created new file in " + path)


