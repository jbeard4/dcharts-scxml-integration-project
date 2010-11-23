"""
__DChartsSCXMLJSSimulationEnvironment_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: jacob
Modified: Fri Nov  5 18:06:12 2010
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


    self.obj196=ButtonConfig(self)
    self.obj196.isGraphObjectVisual = True

    if(hasattr(self.obj196, '_setHierarchicalLink')):
      self.obj196._setHierarchicalLink(False)

    # Action
    self.obj196.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import startStopDebugServer\nstartStopDebugServer(self)\n'))

    # Drawing_Mode
    self.obj196.Drawing_Mode.setValue((' ', 0))
    self.obj196.Drawing_Mode.config = 0

    # Contents
    self.obj196.Contents.Text.setValue('Start/Stop Debug Server')
    self.obj196.Contents.Image.setValue('')
    self.obj196.Contents.Image.setNone()
    self.obj196.Contents.lastSelected= "Text"

    self.obj196.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,80.0,self.obj196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj196)
    self.globalAndLocalPostcondition(self.obj196, rootNode)
    self.obj196.postAction( rootNode.CREATE )

    self.obj197=ButtonConfig(self)
    self.obj197.isGraphObjectVisual = True

    if(hasattr(self.obj197, '_setHierarchicalLink')):
      self.obj197._setHierarchicalLink(False)

    # Action
    self.obj197.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import startStopClientServer\nstartStopClientServer(self)\n'))

    # Drawing_Mode
    self.obj197.Drawing_Mode.setValue((' ', 0))
    self.obj197.Drawing_Mode.config = 0

    # Contents
    self.obj197.Contents.Text.setValue('Start/Stop Client Server')
    self.obj197.Contents.Image.setValue('')
    self.obj197.Contents.Image.setNone()
    self.obj197.Contents.lastSelected= "Text"

    self.obj197.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,160.0,self.obj197)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj197.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj197)
    self.globalAndLocalPostcondition(self.obj197, rootNode)
    self.obj197.postAction( rootNode.CREATE )

    self.obj198=ButtonConfig(self)
    self.obj198.isGraphObjectVisual = True

    if(hasattr(self.obj198, '_setHierarchicalLink')):
      self.obj198._setHierarchicalLink(False)

    # Action
    self.obj198.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from ButtonBehaviours import regenerateClientServerCode\nregenerateClientServerCode(self)\n'))

    # Drawing_Mode
    self.obj198.Drawing_Mode.setValue((' ', 0))
    self.obj198.Drawing_Mode.config = 0

    # Contents
    self.obj198.Contents.Text.setValue('Regenerate Client Server')
    self.obj198.Contents.Image.setValue('')
    self.obj198.Contents.Image.setNone()
    self.obj198.Contents.lastSelected= "Text"

    self.obj198.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,240.0,self.obj198)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj198.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj198)
    self.globalAndLocalPostcondition(self.obj198, rootNode)
    self.obj198.postAction( rootNode.CREATE )

    self.obj199=ButtonConfig(self)
    self.obj199.isGraphObjectVisual = True

    if(hasattr(self.obj199, '_setHierarchicalLink')):
      self.obj199._setHierarchicalLink(False)

    # Action
    self.obj199.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import ButtonBehaviours\nreload(ButtonBehaviours)\nfrom ButtonBehaviours import exportSCXML\nexportSCXML(self)\n'))

    # Drawing_Mode
    self.obj199.Drawing_Mode.setValue((' ', 0))
    self.obj199.Drawing_Mode.config = 0

    # Contents
    self.obj199.Contents.Text.setValue('Export SCXML')
    self.obj199.Contents.Image.setValue('')
    self.obj199.Contents.Image.setNone()
    self.obj199.Contents.lastSelected= "Text"

    self.obj199.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,320.0,self.obj199)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj199.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj199)
    self.globalAndLocalPostcondition(self.obj199, rootNode)
    self.obj199.postAction( rootNode.CREATE )

    self.obj200=ButtonConfig(self)
    self.obj200.isGraphObjectVisual = True

    if(hasattr(self.obj200, '_setHierarchicalLink')):
      self.obj200._setHierarchicalLink(False)

    # Action
    self.obj200.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import ButtonBehaviours\nreload(ButtonBehaviours)\nfrom ButtonBehaviours import exportJavaScript\nexportJavaScript(self)\n'))

    # Drawing_Mode
    self.obj200.Drawing_Mode.setValue((' ', 0))
    self.obj200.Drawing_Mode.config = 0

    # Contents
    self.obj200.Contents.Text.setValue('Export JavaScript')
    self.obj200.Contents.Image.setValue('')
    self.obj200.Contents.Image.setNone()
    self.obj200.Contents.lastSelected= "Text"

    self.obj200.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(100.0,400.0,self.obj200)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj200.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj200)
    self.globalAndLocalPostcondition(self.obj200, rootNode)
    self.obj200.postAction( rootNode.CREATE )

    # Connections for obj196 (graphObject_: Obj211) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj197 (graphObject_: Obj212) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj198 (graphObject_: Obj213) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj199 (graphObject_: Obj214) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj200 (graphObject_: Obj215) of type ButtonConfig
    self.drawConnections(
 )

newfunction = DChartsSCXMLJSSimulationEnvironment_META

loadedMMName = 'Buttons'

atom3version = '0.3'
