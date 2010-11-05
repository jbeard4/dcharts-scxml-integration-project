"""
__simple_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: jacob
Modified: Sun Oct 24 15:37:19 2010
____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from contains import *
from Hyperedge import *
from graph_Basic import *
from graph_contains import *
from graph_Hyperedge import *
from graph_Composite import *
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

def simple_MDL(self, rootNode, DChartsRootNode=None):

    # --- Generating attributes code for ASG DCharts ---
    if( DChartsRootNode ): 
        # variables
        DChartsRootNode.variables.setValue('\n')
        DChartsRootNode.variables.setHeight(15)

        # misc
        DChartsRootNode.misc.setValue('\n')
        DChartsRootNode.misc.setHeight(15)

        # event_clauses
        DChartsRootNode.event_clauses.setValue('\n')
        DChartsRootNode.event_clauses.setHeight(15)
    # --- ASG attributes over ---


    self.obj28=Composite(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # auto_adjust
    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0

    # name
    self.obj28.name.setValue('Composite0')

    # is_default
    self.obj28.is_default.setValue((None, 0))
    self.obj28.is_default.config = 0

    # visible
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0

    # exit_action
    self.obj28.exit_action.setValue('alert("exited")\n')
    self.obj28.exit_action.setHeight(15)

    # enter_action
    self.obj28.enter_action.setValue('alert("entered")\n')
    self.obj28.enter_action.setHeight(15)

    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(220.0,120.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,311.0,237.0,375.0,297.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,311.0,230.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Composite0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=Basic(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # is_default
    self.obj29.is_default.setValue((None, 0))
    self.obj29.is_default.config = 0

    # name
    self.obj29.name.setValue('Basic0')

    # exit_action
    self.obj29.exit_action.setValue('\n')
    self.obj29.exit_action.setHeight(15)

    # enter_action
    self.obj29.enter_action.setValue('\n')
    self.obj29.enter_action.setHeight(15)

    self.obj29.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(320.0,240.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,332.0,243.0,350.0,261.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,343.125,270.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Basic0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font185360332')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=Basic(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # is_default
    self.obj30.is_default.setValue((None, 0))
    self.obj30.is_default.config = 0

    # name
    self.obj30.name.setValue('Basic1')

    # exit_action
    self.obj30.exit_action.setValue('\n')
    self.obj30.exit_action.setHeight(15)

    # enter_action
    self.obj30.enter_action.setValue('\n')
    self.obj30.enter_action.setHeight(15)

    self.obj30.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(520.0,240.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,532.0,243.0,550.0,261.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,543.125,270.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Basic1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font185400332')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=contains(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    self.obj31.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(301.671600007,217.809895833,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=Hyperedge(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # name
    self.obj32.name.setValue('')
    self.obj32.name.setNone()

    # broadcast
    self.obj32.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj32.broadcast.setHeight(15)

    # guard
    self.obj32.guard.setValue('1')

    # trigger
    self.obj32.trigger.setValue('e')

    # action
    self.obj32.action.setValue('alert("transitioning")\n')
    self.obj32.action.setHeight(15)

    # broadcast_to
    self.obj32.broadcast_to.setValue('')
    self.obj32.broadcast_to.setNone()

    # display
    self.obj32.display.setValue('e')

    self.obj32.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(418.489668321,261.71762454,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named Composite0
    self.drawConnections(
(self.obj28,self.obj31,[313.0, 267.0, 301.67160000715683, 217.80989583333334],"true", 2),
(self.obj28,self.obj32,[374.0, 267.0, 418.48966832051326, 261.71762453995791],"true", 2) )
    # Connections for obj29 (graphObject_: Obj1) named Basic0
    self.drawConnections(
 )
    # Connections for obj30 (graphObject_: Obj2) named Basic1
    self.drawConnections(
 )
    # Connections for obj31 (graphObject_: Obj3) of type contains
    self.drawConnections(
(self.obj31,self.obj29,[301.67160000715683, 217.80989583333334, 333.34320001431371, 247.61979166666669],"true", 2) )
    # Connections for obj32 (graphObject_: Obj4) named 
    self.drawConnections(
(self.obj32,self.obj30,[418.48966832051326, 261.71762453995791, 532.01149796808693, 252.07819072029443],"true", 2) )

newfunction = simple_MDL

loadedMMName = 'DCharts'

atom3version = '0.3'
