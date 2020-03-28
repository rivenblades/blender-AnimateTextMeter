_author_="rivenblades"
_version_="0.0.1"
_date_="28/3/2020"
import bpy
UNDEFINED_AREA_X=0
UNDEFINED_AREA_Y=0
UNDEFINED_AREA_Z=100
bUseHideRenderAbility=True
LETTER_WIDTH=0.4
numbers = []
def MoveObjAtLocation(ob,x,y,z):
    bpy.context.view_layer.objects.active = ob
    #bpy.ops.transform.translate(value=(x, y, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.context.object.location[0] = x
    bpy.context.object.location[1] = y
    bpy.context.object.location[2] = z

def hideObj(ob,frame):
    bpy.context.view_layer.objects.active = ob
    if not bUseHideRenderAbility:
        
    ##    bpy.ops.object.hide_view_set(unselected=False)
    #    secs = 0
    #    
    #    while secs < delay:
    #        secs+=0.0000001
    #    ob.hide_set(True)
        MoveObjAtLocation(ob,UNDEFINED_AREA_X,UNDEFINED_AREA_Y,UNDEFINED_AREA_Z)
        ob.keyframe_insert(data_path="location", frame=frame)
    else:
        
        bpy.context.object.hide_render = True
        ob.keyframe_insert(data_path="hide_render", frame=frame)
        
        bpy.context.object.hide_viewport = True
        ob.keyframe_insert(data_path="hide_viewport", frame=frame)
for i in range(0,10):
    
    bpy.ops.object.text_add()
    ob=bpy.context.object
    ob.data.body = str(i)
    numbers.append(ob)

for num in numbers:
    hideObj(num,0)
    num.keyframe_insert(data_path="location", frame=0)
#MoveObjAtLocation(numbers[9],1,1)
#numbers[9].keyframe_insert(data_path="location", frame=30)


previous_letters = []

def FormNumber(num, fromFrame, toFrame, duration=1):
    
#    for pre in previous_letters:

#        hideObj(pre)
#        pre.keyframe_insert(data_path="location", frame=fromFrame)
#        #del pre
    xpos = 0
    for c in num:
        #MoveObjAtLocation(numbers[int(c)],UNDEFINED_AREA_X,UNDEFINED_AREA_Y)
        #numbers[int(c)].keyframe_insert(data_path="location", frame=fromFrame)
    
        MoveObjAtLocation(numbers[int(c)],xpos,0,0)
        xpos+=LETTER_WIDTH
        #num.keyframe_insert(data_path="location", frame=fromFrame)
        
        bpy.context.object.hide_render = False
        bpy.context.object.hide_viewport = False
        numbers[int(c)].keyframe_insert(data_path="hide_viewport", frame=toFrame)
        numbers[int(c)].keyframe_insert(data_path="hide_viewport", frame=toFrame+duration)
        numbers[int(c)].keyframe_insert(data_path="hide_render", frame=toFrame)
        numbers[int(c)].keyframe_insert(data_path="hide_render", frame=toFrame+duration)
        numbers[int(c)].keyframe_insert(data_path="location", frame=toFrame)
        numbers[int(c)].keyframe_insert(data_path="location", frame=toFrame+duration)
        previous_letters.append(numbers[int(c)])

        hideObj(numbers[int(c)], frame=toFrame+duration+1)
        #numbers[int(c)].keyframe_insert(data_path="location", frame=toFrame+duration+1)        
FormNumber("92",0,10, 5)
FormNumber("13",16,16,5)
FormNumber("14",16,22,5)
FormNumber("15",16,28,5)
FormNumber("16",16,34,5)
FormNumber("17",16,40,5)