import numpy as np
from cv2 import cv2
from scipy.ndimage import center_of_mass


def cg_scipy(image):
    """
    SCIPY example
    """
    points = []
    for i in range(0, 280):
        t = []
        points.append(t)
        for j in range(0, 280):
            sub_img = image[i:i + 40, j:j + 40]
            if np.sum(sub_img) == 0:
                t.append([100, 100])
            else:
                cm = center_of_mass(sub_img)
                print(i, j, cm)
                t.append([cm[0], cm[1]])
    cms = np.array(points).reshape([280, 280, 2])
    cm_cg = np.sqrt(np.sum(np.power(cms - 19.5, 2), axis=2))
    cm_cg_img = np.array(cm_cg < 5, dtype=np.uint8) * 255
    cv2.imshow('win1', image * 255)
    cv2.imshow('win4', cm_cg_img)
    cv2.waitKey(0)


def cg_numpy(image, x, y):
    anchor_pos = (0, 0)
    mask_vals = np.array([np.arange(0, 40)])
    mask_col = np.repeat(mask_vals, 40, axis=0)
    mask_row = np.array(mask_col).T
    mask_ones = np.ones([40, 40])

    tmp_img = np.array(image[x:x + 40, y:y + 40], dtype=np.uint64)

    row_conv = cv2.filter2D(tmp_img, -1, mask_row, anchor=anchor_pos)
    col_conv = cv2.filter2D(tmp_img, -1, mask_col, anchor=anchor_pos)
    ones_conv = cv2.filter2D(tmp_img, -1, mask_ones, anchor=anchor_pos)
    ones_conv_mask = ones_conv > 0
    ones_conv_zero_avoid = np.where(ones_conv > 0, ones_conv, 1)

    result_img_row = np.multiply(np.divide(row_conv, ones_conv_zero_avoid), ones_conv_mask)
    result_img_col = np.multiply(np.divide(col_conv, ones_conv_zero_avoid), ones_conv_mask)
    result_cg = np.stack([result_img_row, result_img_col], axis=2)
    print(result_cg[0, 0, :])


def encode_as_struct_elems(image):
    """
     Encode input image as an array of simple fixes sized square shaped structural elements.
    """
    # encoding params
    anchor_pos = (-1, -1)
    min_pool_overlap = 5
    min_pool_window_size = [20, 20]

    # structural element params
    elem_size = 40  # only a single value required to describe a square shaped structural element
    elem_cg_dist_threshold = 4  # max dist of the CG of the structural element from its center
    elem_mass_threshold = 0.1  # min required active fraction of the mass within the structural element

    mask_vals = np.array([np.arange(0, elem_size)])
    mask_col = np.repeat(mask_vals, elem_size, axis=0)
    mask_row = np.array(mask_col).T
    mask_ones = np.ones([elem_size, elem_size])

    tmp_img = np.array(image, dtype=np.uint64)

    row_conv = cv2.filter2D(tmp_img, -1, mask_row, anchor=anchor_pos)
    col_conv = cv2.filter2D(tmp_img, -1, mask_col, anchor=anchor_pos)
    ones_conv = cv2.filter2D(tmp_img, -1, mask_ones, anchor=anchor_pos)
    ones_conv_mask = ones_conv >= (elem_mass_threshold * elem_size * elem_size)

    ones_conv_zero_avoid = np.where(ones_conv > 0, ones_conv, 1)

    result_img_row = np.multiply(np.divide(row_conv, ones_conv_zero_avoid), ones_conv_mask)
    result_img_col = np.multiply(np.divide(col_conv, ones_conv_zero_avoid), ones_conv_mask)
    result_cg = np.stack([result_img_row, result_img_col], axis=2)

    # @todo - return result_cg_dist ?
    result_cg_dist = np.sqrt(np.sum(np.power(result_cg - (elem_size / 2), 2), axis=2))
    result_cg_dist = strided_min_pool_sim(result_cg_dist, min_pool_window_size, min_pool_overlap)
    # construct output image
    result_cg_thresh_dist_mask = result_cg_dist <= elem_cg_dist_threshold
    min_cg_dist = np.min(result_cg_dist)
    max_cg_dist = np.max(result_cg_dist)
    result_cg_dist_img = 1 - (result_cg_dist * (1 / (max_cg_dist - min_cg_dist)))
    result_cg_dist_img = np.multiply(result_cg_dist_img, result_cg_thresh_dist_mask)

    return np.array(result_cg_dist_img * 255, dtype=np.uint8)


def strided_min_pool_sim(image, window_size, overlap):
    h_img, w_img = image.shape
    hw, ww = window_size
    h_stride = hw - overlap
    w_stride = ww - overlap
    min_pool_result = []
    for i in range(0, h_img, h_stride):
        row_result = []
        min_pool_result.append(row_result)
        for j in range(0, w_img, w_stride):
            tmp_img = image[i:min(i + hw, h_img), j:min(j + ww, w_img)]
            row_result.append(np.min(tmp_img))
    return np.array(min_pool_result)


if __name__ == '__main__':
    img = cv2.imread('/home/yashrahmed/Desktop/img_5.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, th_img = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY_INV)
    th_img = th_img / 255
    th_img = th_img.astype(np.uint8)
    # print(th_img.shape)  # 280 x 280
    # cg_scipy(th_img)
    # cg_numpy(th_img, 60, 116)
    result_img = encode_as_struct_elems(th_img)
    cv2.imshow('win1', th_img * 255)

    cv2.imshow('win4-cg-np-full', cv2.resize(result_img, (200, 200)))
    cv2.waitKey(0)

    """
    Sample CG points -- 
    57 66 (22.92233009708738, 29.168284789644012)
    57 151 (15.585714285714285, 14.6)
    60 116 (18.716283716283716, 17.318681318681318)
    86 88 (11.041769041769042, 30.722358722358724)
    87 116 (15.721603563474387, 9.643652561247215)
    147 111 (0.0, 39.0)
    147 176 (26.264227642276424, 8.213414634146341)
    147 179 (27.089058524173026, 7.035623409669212)
    """
