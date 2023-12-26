import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_obelisk():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #вершины
    vertices = [
        [1, 1, -1], #A
        [1, -1, -1], #B
        [-1, -1, -1], #C
        [-1, 1, -1], #D

        [0.6, 0.6, 0.6], #A1
        [0.6, -0.6, 0.6], #B1
        [-0.6, -0.6, 0.6], #C1
        [-0.6, 0.6, 0.6] #D1
    ]
    #грани
    faces = [
        [0, 1, 2, 3], #ABCD
        [4, 5, 6, 7], #A1B1C1D1
        [0, 1, 4, 5], #ABA1B1
        [1, 2, 5, 6], #BCB1C1
        [2, 3, 6, 7], #CDC1D1
        [3, 0, 7, 4]  #DAD1A1
    ]
    for vertex in vertices:
        ax.scatter(vertex[0], vertex[1], vertex[2], color='purple')

    for face in faces:
        x = [vertices[i][0] for i in face]
        # [print(vertices[i][0]) for i in face]
        y = [vertices[i][1] for i in face]
        z = [vertices[i][2] for i in face]
        # print(x, y, z)
        ax.plot_trisurf(x, y, z, color='yellow')

    plt.show()

draw_obelisk()