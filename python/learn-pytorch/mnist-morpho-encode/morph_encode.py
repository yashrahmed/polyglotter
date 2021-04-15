from cv2 import cv2
import numpy as np


def inter_over_union(input_img1, input_img2):
    # assumes thersholded image in 0-255 grayscale range
    im1_as_bool = input_img1 > 0
    im2_as_bool = input_img2 > 0
    im_inter = np.sum(im2_as_bool & im1_as_bool)
    im_union = np.sum(im2_as_bool | im1_as_bool)
    return im_inter / im_union


def inter_over_union_features(query_feature, match_tgt_feature):
    # performs IoU operation between 2 arrays of features.
    # where features are output of the multi_dilate_and_shrink_operation
    # The assumption is that len(query_feature) = len(match_tgt_feature) and that they are arranged in the same manner.
    # e.g. both are similarly arranged by output of kernel dims e.g. [30, 20, 10] for both or vice versa.
    result_vector = []
    for i in range(0 , len(query_feature)):
        result_vector.append(inter_over_union(query_feature[i], match_tgt_feature[i]))
    return result_vector


def multi_dilate_and_shrink(input_img):
    tgt_dim = (50, 50)
    kernel_dims = [30, 20, 10]
    kernels = [np.ones(kernel_dims[0]), np.ones(kernel_dims[1]), np.ones(kernel_dims[2])]
    dilation_results = []
    for kernel in kernels:
        dilation_results.append(cv2.resize(cv2.dilate(input_img, kernel), tgt_dim, interpolation=cv2.INTER_LINEAR))
    return dilation_results


def read_img_and_threshold(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th_img = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY_INV)
    return th_img.astype(np.uint8)


if __name__ == '__main__':
    descriptor_of_3 = multi_dilate_and_shrink(read_img_and_threshold('/home/yashrahmed/Desktop/img_3.png'))
    descriptor_of_5 = multi_dilate_and_shrink(read_img_and_threshold('/home/yashrahmed/Desktop/img_5.png'))

    result_vector_1 = inter_over_union_features(descriptor_of_5, descriptor_of_3)
    result_vector_2 = inter_over_union_features(descriptor_of_5, descriptor_of_5)

    print(result_vector_1)
    print(result_vector_2)

    # cv2.imshow('input', th_img)
    # cv2.imshow('dial-30x30', results[0])
    # cv2.imshow('dial-20x20', results[1])
    # cv2.imshow('dial-10x10', results[2])
    # cv2.waitKey(0)