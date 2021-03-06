from arm.logicnode.arm_nodes import *

class PlayActionFromNode(ArmLogicTreeNode):
    """Plays action starting from the given frame."""
    bl_idname = 'LNPlayActionFromNode'
    bl_label = 'Play Action From'
    arm_version = 1

    def init(self, context):
        super(PlayActionFromNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('ArmNodeSocketAnimAction', 'Action')
        self.add_input('NodeSocketInt', 'Start Frame')
        self.add_input('NodeSocketFloat', 'Blend', default_value=0.25)

        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketAction', 'Done')
