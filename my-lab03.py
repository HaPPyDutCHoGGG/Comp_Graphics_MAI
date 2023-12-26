import math
import matplotlib.pyplot as plt
import numpy as np
#для ползунка
from matplotlib.widgets import Slider
from matplotlib.colors import LightSource

psiLight = 0
phiLight = 0
def onChangeValueG(value: np.float64):
    global g
    g = value
    redraw(phiLight, psiLight)
def onChangeValueV(value: np.float64):
    global v
    v = value
    redraw(psiLight, phiLight)

def lightPhiChange(value: np.float64):
    global phiLight
    global psiLight
    phiLight = value
    redraw(phiLight, psiLight)
def lightPsiChange(value: np.float64):
    global phiLight
    global psiLight
    psiLight = value
    redraw(phiLight, psiLight)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# размеры
v = 1.0
# грани+1
g = 5
faces_t = []

def redraw(phiLight, psiLight):
    #глобальные переменные
    global v
    global g

    Xc, Yc, Zc = data_for_sfier_along_z(v, 1.25*v, g)
    ax.clear()
    ls = LightSource(phiLight, psiLight)
    # пострение поверхности
    ax.plot_surface(Xc, Yc, Zc, color='red', alpha=1, lightsource=ls)

    fig.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(False)
    ax.w_xaxis.pane.fill = False
    ax.w_yaxis.pane.fill = False
    ax.w_zaxis.pane.fill = False
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-1, 5])

axes_slider_G = plt.axes((0.2, 0.1, 0.6, 0.02))
slider_G = Slider(axes_slider_G, label='approximation', valmin=3, valmax=200, valinit=5, valstep=1, orientation='horizontal')
slider_G.on_changed(onChangeValueG)
axes_slider_V = plt.axes((0.2, 0.15, 0.6, 0.02))
slider_V = Slider(axes_slider_V, label='size', valmin=1, valmax=60, valinit=1, valstep=1, orientation='horizontal')
slider_V.on_changed(onChangeValueV)

axes_slider_PhiLight = plt.axes([0.2, 0.05, 0.6, 0.02])
slider_Phi = Slider(axes_slider_PhiLight, label='phiLight', valmin=-180, valmax=180, valinit=0, valstep=1, orientation='horizontal')
slider_Phi.on_changed(lightPhiChange)
axes_slider_PsiLight = plt.axes([0.2, 0, 0.6, 0.02])
slider_Psi = Slider(axes_slider_PsiLight,label='psiLight', valmin=-180, valmax=180, valinit=0, valstep=1, orientation='horizontal')
slider_Psi.on_changed(lightPsiChange)
# cтроить будем в cферической системе координат,
# в которой каждая точка пространства определяется тремя числами
# r - расстояние до начала координат (радиальное расстояние),
# theta  и varphi  — зенитный и азимутальный углы соответственно.
def data_for_sfier_along_z(radius, height_z, den_t):
    # Экземпляр, который возвращает плотную (или детализированную) сетку при индексировании,
    # так что каждый возвращаемый аргумент имеет одинаковую форму
    # сетка от о до 2пи поделённая на 2g частей и от 0 до пи поделённая на g частей

    # theta - цэ зенитный, направление вертикального подъёма над произвольно выбранной точкой (точкой наблюдения)
    # varphi - цэ азимутальный, угол между произвольно выбранным лучом фундаментальной
    # плоскости с началом в точке наблюдения и другим лучом этой плоскости, имеющим общее начало с первым.
    # Аргументы mgrid по каждому измерению: (start : stop : step).
    varphi, theta = np.mgrid[0:2 * np.pi:1j*den_t, 0:np.pi:1j*den_t]

    x_grid = radius*1.2*np.sin(theta) * np.cos(varphi)
    y_grid = radius*1.2*np.sin(theta) * np.sin(varphi)
    z_grid = radius*np.cos(theta) + height_z

    return x_grid, y_grid, z_grid
Xc, Yc, Zc = data_for_sfier_along_z(v, 1.25*v, g)

if __name__ == "__main__":

    ls = LightSource(0, 90)
    ax.plot_surface(Xc, Yc, Zc, color='red', alpha=1, lightsource=ls)

    fig.set_facecolor('white')
    ax.set_facecolor('white')
    ax.grid(False)

    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])


    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-1, 5])

    plt.show()