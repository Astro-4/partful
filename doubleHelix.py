import bpy
import string
import random

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0,
0), scale=(1, 1, 1))

#Random name generator
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(5)) + ':' + str(random.randint(100, 999))