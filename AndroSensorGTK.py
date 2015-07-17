import bpy
import csv
import math
fp = ""

bl_info = {"name": "AndroSensor GTK", "category": "Animation"}
class Panel(bpy.types.Panel):
    """AndroSensor Panel"""
    bl_label = "AndroSensor GTK"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text="AndroSensor Gyro CSV to keyframes", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Object that keyframes will be applied to: " + obj.name)
        
        row = layout.row()
        row.operator("import.some_data")
        row = layout.row()
        row.label(text=fp)
        row = layout.row()
        if fp != "":    
            row.operator("convert.run")
        

       
       

class OBJECT_OT_KeyButton(bpy.types.Operator):
    """reads user-inputed csv file and generates animation (ikr reeeeeaaal coool)"""
    bl_idname = "convert.run"
    bl_label = "Add Keyframes"
    fn = bpy.props.StringProperty()
    def execute(self, context):
        global fp
        results = []
        obj = context.object
        with open(fp, newline='') as inputfile:
        	for row in csv.reader(inputfile):
        		results.append(row)

        line = 0

        for x in results:
            line += 1
            if line > 2:
                currentFrame = str(x)
                currentFrame = currentFrame.replace("['", "")
                currentFrame = currentFrame.replace("']", "")
        #        print(currentFrame)
                xRot, yRot, zRot,_,_ = currentFrame.split(';')
                print(xRot + " " + yRot + " " + zRot)
                xRot =  (math.radians(float(xRot)))/24
                yRot = (math.radians(float(yRot)))/24
                zRot = (math.radians(float(zRot)))/24
                obj.rotation_euler[0] += float(xRot)
                obj.rotation_euler[1] += float(yRot)
                obj.rotation_euler[2] += float(zRot)
                obj.keyframe_insert(data_path="rotation_euler", frame=line, index=-1)
                  
class ImportSomeData(bpy.types.Operator):
    """Choose the directory where you AndroSensor CSV file is"""
    bl_idname = "import.some_data"
    bl_label = "Import AndroSensor CSV file"
    result = ""
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        global fp
        fp = self.filepath
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}



def register():
    bpy.utils.register_module(__name__)



def unregister():
    bpy.utils.unregister_module(__name__)



if __name__ == "__main__":
    register()
