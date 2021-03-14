#  This file is part of the Kitfox Blender Cellular Automa distribution (https://github.com/blackears/blenderCellularAutoma).
#  Copyright (c) 2021 Mark McKay
#  
#  This program is free software: you can redistribute it and/or modify  
#  it under the terms of the GNU General Public License as published by  
#  the Free Software Foundation, version 3.
# 
#  This program is distributed in the hope that it will be useful, but 
#  WITHOUT ANY WARRANTY; without even the implied warranty of 
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#  General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License 
#  along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
import nodeitems_utils 

class SortedNodeCategory(nodeitems_utils .NodeCategory):
    def __init__(self, identifier, name, description="", items=None):
        # for builtin nodes the convention is to sort by name
        if isinstance(items, list):
            items = sorted(items, key=lambda item: item.label.lower())

        super().__init__(identifier, name, description, items)

class ShaderNewNodeCategory(SortedNodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == 'ShaderNodeTree' and
                context.scene.render.use_shading_nodes)


class ImageGenNode(bpy.types.Node):
    """
    Tooltip: Generate a simple image
    """
    bl_idname = "kitfox.image_gen_node"
    bl_label = "Image Gen"
    bl_icon = "SPEAKER"

    color_out : bpy.props.FloatVectorProperty(
        default = [.5, .5, .5, 1.0], size=4, subtype = "COLOR", soft_min = 0.0, soft_max = 1.0
    )


    def init(self, context):
        super().init(context)
        
        self.outputs.new("NodeSocketColor", "Color")
        
        print("ImageGenNode init()")

    def execute(self):
        print("ImageGenNode execute()")
                
        return {"color_out": self.color_out}

    def output(self):
        print("ImageGenNode output()")
        return self.execute()
        
        
    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        print("ImageGenNode draw_buttons()")
        layout.prop(self, "color_out", text="walla")
        
    @classmethod
    def poll(cls, ntree):
        print("ImageGenNode poll()")
        return True
        
        
        
# all categories in a list
shader_node_categories = [
    # identifier, label, items list
    ShaderNewNodeCategory('SH_NEW_TEXTURE', "Texture", items=[
        # our basic node
        nodeitems_utils.NodeItem("ImageGenNode"),
    ])
]

def register():
    bpy.utils.register_class(ImageGenNode)
    
    nodeitems_utils.register_node_categories('SHADER', shader_node_categories)

    print("Registered ImageGenNode")


def unregister():
    bpy.utils.unregister_class(ImageGenNode)


if __name__ == "__main__":
    register()
