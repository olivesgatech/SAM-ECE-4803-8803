import numpy as np
import matplotlib.pyplot as plt
from config import *

def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30 / 255, 144 / 255, 255 / 255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def show_points(coords, labels, ax, marker_size=50):
    pos_points = coords[labels == 1]
    neg_points = coords[labels == 0]

    ax.scatter(pos_points[:, 0], pos_points[:, 1], color=GREEN_COLOR, marker='*', s=marker_size, edgecolor='white',
            linewidth=LINEWIDTH)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color=RED_COLOR, marker='*', s=marker_size, edgecolor='white',
            linewidth=LINEWIDTH)

def closetn(node, nodes):
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return np.argmin(dist_2)

#%%
def delete_point(green, red, current_color, x, y, ax, greenx, greeny, redx, redy):
    if not green and not red:
        print("no points to delete")
    elif green:
        print(current_color)
        if current_color == 'green':
            indx = closetn((x, y), green)
            print(indx)
            for line in ax[0].lines:
                if len(line.get_xdata()) > 0:
                    if line.get_xdata()[0] == green[indx][0] and line.get_ydata()[0] == green[indx][1]:

                        line.set_data([], [])
                        break
            for line in ax[1].lines:
                if len(line.get_xdata()) > 0:
                    if line.get_xdata()[0] == green[indx][0] and line.get_ydata()[0] == green[indx][1]:
                        line.set_data([], [])
                        break
            del green[indx]
            del greenx[indx]
            del greeny[indx]
            plt.draw()
        elif red:
            print("delete red")
            print(current_color)
            indx = closetn((x, y), red)
            print(indx)

            for line in ax[0].lines:
                if len(line.get_xdata()) > 0:
                    print()
                    if line.get_xdata()[0] == red[indx][0] and line.get_ydata()[0] == red[indx][1]:
                        line.set_data([], [])
                        break
            for line in ax[1].lines:
                if len(line.get_xdata()) > 0:
                    if line.get_xdata()[0] == red[indx][0] and line.get_ydata()[0] == red[indx][1]:
                        line.set_data([], [])
                        break
            del red[indx]
            del redx[indx]
            del redy[indx]
            plt.draw()
    return green, red, greenx, greeny, redx, redy