import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

epsilon = 10
# epsilon служит для определения доп области попадания
def checker(p, event) -> bool:
    if (event.xdata <= p[0] + epsilon) and (event.xdata >= p[0] - epsilon):
        if (event.ydata >= p[1] - epsilon) and (event.ydata <= p[1] + epsilon):
            return True
    return False
# точки по которым строится кривая start
def bezier_curve(points, t):
    # Для трёх точек(2-я степень):
    # x = (1−t)2x1 + 2(1−t)tx2 + t2x3
    # y = (1−t)2y1 + 2(1−t)ty2 + t2y3
    p0, p1, p2 = points
    u = 1 - t
    u1 = u * u
    t1 = t * t

    x = (u1 * p0[0] +
         2 * u * t * p1[0] +
         t1 * p2[0])
    y = (u1 * p0[1] +
         2 * u * t * p1[1] +
         t1 * p2[1])
    return x, y

# массив управляющих точек, их кординаты
ctr = np.array( [(50, 200), (150, 50), (250, 350)])

t_values = np.linspace(0, 1, 50)
curve_points = [bezier_curve(ctr, t) for t in t_values]

# функция для перерисовки графика
def update(points):
    # вот тута и задаются точки по которым строится кривая start
    t_values = np.linspace(0, 1, 50)
    curve_points = [bezier_curve(ctr[:3], t) for t in t_values]

    ax.clear()

    ax.scatter(*zip(*ctr), color='purple')
    ax.plot(*zip(*curve_points), color='orange')
    ax.legend(['Points', 'Interpolated B-spline', 'True'], loc='best')
    plt.title('B-Spline interpolation')

# функция для проверки изменения точек и их собственно передвижения
def motion_notify_callback(event):
    'on mouse movement'
    global yvals
    if event.inaxes is None:
        return
    if event.button != 1:
        return
    for i in ctr:
        if checker(i, event) is True:
            i[0] = event.xdata
            i[1] = event.ydata
            fig.canvas.draw_idle()
            update(1)

ax.scatter(*zip(*ctr), color='purple')
ax.plot(*zip(*curve_points), color='orange')
ax.legend(['Points', 'Interpolated Bezier curve(2nd degree)', 'True'], loc='best')
plt.title('Bezier curve(2nd degree) interpolation')

fig.canvas.mpl_connect('motion_notify_event', motion_notify_callback)

plt.show()