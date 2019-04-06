from Utils import utils

import pandas as pd
import numpy as np
import cv2


def read_frame_data(f_path, channels=False):
    parameters_path = f_path.replace('samples', 'parameters.txt')
    samples_paths = utils.get_dirs(f_path)

    dataX = []
    dataY = []

    for p in samples_paths:
        dataX.append([cv2.imread(p + '/' + str(i) + '.png', 0) for i in range(20)])
        y_image = np.array(cv2.imread(p + '/20.png', 0))
        dataY.append(y_image.reshape(y_image.size))

    dataX = np.array(dataX, dtype="float") / 255
    dataY = np.array(dataY, dtype="float") / 255

    if channels:
        dataX = np.expand_dims(dataX, axis=-1)

    parameters = pd.read_csv(parameters_path, sep=' ')

    return parameters, dataX, dataY


def get_positions(predictions, real, dim):
    predict_pos = []
    real_pos = []
    maximum = []
    for i, p in enumerate(predictions):
        p = p.reshape(dim)
        predict_pos.append(np.unravel_index(p.argmax(), p.shape))
        r = real[i].reshape(dim)
        real_pos.append(np.unravel_index(r.argmax(), r.shape))
        maximum.append(np.linalg.norm(np.array((0, 0)) - np.array(dim)))

    return np.array(predict_pos), np.array(real_pos), np.array(maximum)


def draw_frame(fig, real_data, pred_data, dim):
    bw_image_real = real_data.reshape(dim)
    bw_image_real = bw_image_real.astype(np.uint8) * 255
    color_image_real = np.dstack([bw_image_real, bw_image_real, bw_image_real])

    pred_data[np.argmax(pred_data)] = 1
    pred_data = np.round(pred_data)
    bw_image_pred = pred_data.reshape(dim)
    bw_image_pred = bw_image_pred.astype(np.uint8) * 255
    color_image_pred = np.dstack([bw_image_pred, np.zeros(dim, np.uint8), np.zeros(dim, np.uint8)])

    color_image = color_image_pred + color_image_real
    fig.imshow(color_image)

    return fig
