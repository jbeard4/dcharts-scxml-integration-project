"""
__DChartsDebugServer_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: jacob
Modified: Wed Oct 27 11:37:18 2010
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ButtonConfig import *
from graph_ButtonConfig import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def DChartsDebugServer_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('DChartsDebugServer_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('DChartsDebugServer_META')
    # --- ASG attributes over ---


    self.obj37=ButtonConfig(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # Action
    self.obj37.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DChartsDebugServer\nport_number = 12345\nif DChartsDebugServer.isServerRunning():\n        DChartsDebugServer.stopServer()\nelse:\n        DChartsDebugServer.startServer(self, self.ASGroot, port_number)\n\n'))

    # Drawing_Mode
    self.obj37.Drawing_Mode.setValue((' ', 0))
    self.obj37.Drawing_Mode.config = 0

    # Contents
    self.obj37.Contents.Text.setValue('Start/Stop Server')
    self.obj37.Contents.Image.setValue('')
    self.obj37.Contents.Image.setNone()
    self.obj37.Contents.lastSelected= "Text"

    self.obj37.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(140.0,120.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )

newfunction = DChartsDebugServer_META

loadedMMName = 'Buttons'

atom3version = '0.3'
