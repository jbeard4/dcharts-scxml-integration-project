"""
__DChartsSCXMLGenerator_MM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: jacob
Modified: Sat Oct 23 16:02:28 2010
______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Class3 import *
from graph_Class3 import *
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

def DChartsSCXMLGenerator_MM_MDL(self, rootNode, ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG ClassDiagramsV3 ---
    if( ClassDiagramsV3RootNode ): 
        # name
        ClassDiagramsV3RootNode.name.setValue('DChartsSCXMLGenerator')

        # author
        ClassDiagramsV3RootNode.author.setValue('Annonymous')

        # showCardinalities
        ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # description
        ClassDiagramsV3RootNode.description.setValue('\n\n\nGenerates SCXML from a DCharts model\n')
        ClassDiagramsV3RootNode.description.setHeight(15)

        # showAttributes
        ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj26=Class3(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # QOCA
    self.obj26.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj26.Graphical_Appearance.setValue( ('Class_0', self.obj26))

    # name
    self.obj26.name.setValue('Class_0')

    # attributes
    self.obj26.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj26.attributes.setValue(lcobj2)

    # Abstract
    self.obj26.Abstract.setValue((None, 0))
    self.obj26.Abstract.config = 0

    # cardinality
    self.obj26.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj26.cardinality.setValue(lcobj2)

    # display
    self.obj26.display.setValue('')
    self.obj26.display.setHeight(15)

    # Actions
    self.obj26.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj26.Actions.setValue(lcobj2)

    # Constraints
    self.obj26.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj26.Constraints.setValue(lcobj2)

    self.obj26.graphClass_= graph_Class3
    if self.genGraphics:
       new_obj = graph_Class3(140.0,60.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    # Connections for obj26 (graphObject_: Obj1) named Class_0
    self.drawConnections(
 )

newfunction = DChartsSCXMLGenerator_MM_MDL

loadedMMName = 'ClassDiagramsV3_META'

atom3version = '0.3'
