"""
__DChartsSCXMLJSSimulationEnvironment_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: jacob
Modified: Fri Nov  5 11:39:36 2010
__________________________________________________________________________________________________
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

def DChartsSCXMLJSSimulationEnvironment_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('DChartsSCXMLJSSimulationEnvironment_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('DChartsSCXMLJSSimulationEnvironment_META')
    # --- ASG attributes over ---


    self.obj23=ButtonConfig(self)
    self.obj23.isGraphObjectVisual = True

    if(hasattr(self.obj23, '_setHierarchicalLink')):
      self.obj23._setHierarchicalLink(False)

    # Action
    self.obj23.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import startStopDebugServer\nstartStopDebugServer(self)\n'))

    # Drawing_Mode
    self.obj23.Drawing_Mode.setValue((' ', 0))
    self.obj23.Drawing_Mode.config = 0

    # Contents
    self.obj23.Contents.Text.setValue('Start/Stop Debug Server')
    self.obj23.Contents.Image.setValue('')
    self.obj23.Contents.Image.setNone()
    self.obj23.Contents.lastSelected= "Text"

    self.obj23.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,80.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.obj23.postAction( rootNode.CREATE )

    self.obj24=ButtonConfig(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # Action
    self.obj24.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import startStopClientServer\nstartStopClientServer(self)\n'))

    # Drawing_Mode
    self.obj24.Drawing_Mode.setValue((' ', 0))
    self.obj24.Drawing_Mode.config = 0

    # Contents
    self.obj24.Contents.Text.setValue('Start/Stop Client Server')
    self.obj24.Contents.Image.setValue('')
    self.obj24.Contents.Image.setNone()
    self.obj24.Contents.lastSelected= "Text"

    self.obj24.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,160.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=ButtonConfig(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # Action
    self.obj25.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import regenerateClientServerCode\nregenerateClientServerCode(self)\n'))

    # Drawing_Mode
    self.obj25.Drawing_Mode.setValue((' ', 0))
    self.obj25.Drawing_Mode.config = 0

    # Contents
    self.obj25.Contents.Text.setValue('Regenerate Client Server')
    self.obj25.Contents.Image.setValue('')
    self.obj25.Contents.Image.setNone()
    self.obj25.Contents.lastSelected= "Text"

    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,240.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    self.obj26=ButtonConfig(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # Action
    self.obj26.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import exportSCXML\nexportSCXML(self)\n'))

    # Drawing_Mode
    self.obj26.Drawing_Mode.setValue((' ', 0))
    self.obj26.Drawing_Mode.config = 0

    # Contents
    self.obj26.Contents.Text.setValue('Export SCXML')
    self.obj26.Contents.Image.setValue('')
    self.obj26.Contents.Image.setNone()
    self.obj26.Contents.lastSelected= "Text"

    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,320.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    self.obj27=ButtonConfig(self)
    self.obj27.isGraphObjectVisual = True

    if(hasattr(self.obj27, '_setHierarchicalLink')):
      self.obj27._setHierarchicalLink(False)

    # Action
    self.obj27.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import exportJavaScript\nexportJavaScript(self)\n'))

    # Drawing_Mode
    self.obj27.Drawing_Mode.setValue((' ', 0))
    self.obj27.Drawing_Mode.config = 0

    # Contents
    self.obj27.Contents.Text.setValue('Export JavaScript')
    self.obj27.Contents.Image.setValue('')
    self.obj27.Contents.Image.setNone()
    self.obj27.Contents.lastSelected= "Text"

    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,400.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.obj27.postAction( rootNode.CREATE )

    # Connections for obj23 (graphObject_: Obj2) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj24 (graphObject_: Obj3) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj25 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj27 (graphObject_: Obj6) of type ButtonConfig
    self.drawConnections(
 )

newfunction = DChartsSCXMLJSSimulationEnvironment_META

loadedMMName = 'Buttons'

atom3version = '0.3'
