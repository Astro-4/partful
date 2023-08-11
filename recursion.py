import bpy
import math

# Recursive function to draw Sierpinski Triangle
def draw_sierpinski(level, vertices):
    if level == 0:
        mesh = bpy.data.meshes.new("Triangle")
        obj = bpy.data.objects.new("Triangle", mesh)
        bpy.context.collection.objects.link(obj)

        mesh.from_pydata(vertices, [], [(0, 1, 2)])
        mesh.update()
    else:
        v1 = vertices[0]
        v2 = vertices[1]
        v3 = vertices[2]
        mid1 = ((v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2)
        mid2 = ((v2[0] + v3[0]) / 2, (v2[1] + v3[1]) / 2)
        mid3 = ((v1[0] + v3[0]) / 2, (v1[1] + v3[1]) / 2)

        draw_sierpinski(level - 1, [v1, mid1, mid3])
        draw_sierpinski(level - 1, [mid1, v2, mid2])
        draw_sierpinski(level - 1, [mid3, mid2, v3])

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Vertices of the initial triangle
vertices = [(-2, -2), (2, -2), (0, 2)]

# Draw Sierpinski Triangle
draw_sierpinski(3, vertices)

