import bpy


class ImageGenNode(bpy.types.Node):
    """
    Tooltip: Generate a simple image
    """
    bl_idname = "kitfox.image_gen_node"
    bl_label = "Image Gen"
#    bl_icon = "COLOR"
    bl_icon = "SPEAKER"

    # size : bpy.props.FloatProperty(
        # name="Size", description="Size param", default = 10
    # )

    #object : PointerProperty(type=Object)
    color_out : bpy.props.FloatVectorProperty(
        default = [.5, .5, .5, 1.0], size=4, subtype = "COLOR", soft_min = 0.0, soft_max = 1.0
    )
    
    # width : bpy.props.IntProperty(
        # name="Width", description="Width of image", default = 512, min=1, soft_max = 1024
    # )

    # height : bpy.props.IntProperty(
        # name="Height", description="Height of image", default = 512, min=1, soft_max = 1024
    # )


    def init(self, context):
        super().init(context)
        # self.inputs.new("NodeSocketFloat", "Width")
        # self.inputs.new("NodeSocketFloat", "Height")
        
        self.outputs.new("NodeSocketColor", "Color")
        #self.outputs.new("cm_socket.object", "Object")
        
        # self.use_custom_color = True
        # self.color = (0.4, 0.3, 0.4)
        
        print("ImageGenNode init()")

    def execute(self):
        # sockets = self.inputs.keys()
        # input_values = get_socket_values(self, sockets, self.inputs)
        # input = connected_node_output(self, 0)
        # if input is not None:
                # colour = input["colour"]
        print("ImageGenNode execute()")
                
#        return {"objects": self.object}
        return {"color_out": self.color_out}

    def output(self):
        print("ImageGenNode output()")
        return self.execute()
        
        
    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        print("ImageGenNode draw_buttons()")
        # layout.label(text="Image settings")
        # layout.prop(self, "size")
        #layout.prop(self, "object", text="")
        layout.prop(self, "color_out", text="walla")
        
    @classmethod
    def poll(cls, ntree):
#        return ntree.bl_idname == 'CustomTreeType'
        print("ImageGenNode poll()")
        return True
        
    # # Detail buttons in the sidebar.
    # # If this function is not defined, the draw_buttons function is used instead
    # def draw_buttons_ext(self, context, layout):
        # layout.prop(self, "size")

    # # Optional: custom label
    # # Explicit user label overrides this, but here we can define a label dynamically
    # def draw_label(self):
        # return "My Image Generating Node"
        

def register():
    bpy.utils.register_class(ImageGenNode)

    print("Registered ImageGenNode")

    # from bpy.utils import register_class
    # for cls in classes:
        # register_class(cls)

    # nodeitems_utils.register_node_categories('CUSTOM_NODES', node_categories)


def unregister():
    bpy.utils.unregister_class(ImageGenNode)

    # nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

    # from bpy.utils import unregister_class
    # for cls in reversed(classes):
        # unregister_class(cls)


if __name__ == "__main__":
    register()
