from cv2 import cv2

from mnist_morpho_encode.morph_encode import read_img_and_threshold


def resize_for_display(image):
    return cv2.resize(image, (200, 200))


if __name__ == '__main__':
    path_prefix = '/home/yashrahmed/Documents/datasets/kaggle-mnist-as-images/trainingSample'
    digit_2_prefix = f'{path_prefix}/trainingSample/2'
    digit_3_prefix = f'{path_prefix}/trainingSample/3'
    digit_5_prefix = f'{path_prefix}/trainingSample/5'

    threshold_type = cv2.THRESH_BINARY
    threshold_value = 20
    img_of_2 = read_img_and_threshold(f'{digit_2_prefix}/img_22.jpg', threshold_value, threshold_type)

    """
    OpenCV indirectly imposes a size restriction.
    See https://github.com/opencv/opencv_contrib/blob/342f8924cca88fe6ce979024b7776f6815c89978/modules/xfeatures2d/src/brief.cpp#L249
    //Remove keypoints very close to the border
    KERNEL_SIZE=48 and PATCH_SIZE=9
    KeyPointsFilter::runByImageBorder(keypoints, image.size(), PATCH_SIZE/2 + KERNEL_SIZE/2);
    Also see https://github.com/opencv/opencv_contrib/blob/master/modules/xfeatures2d/src/generated_32.i
    1. OpenCV does not do pixel comparison. Instead it compares differences of cumulative gray values
       b/w small image patches.
    2. Integral image are used for #1.
    3. OpenCV supports 16, 32 and 64 BYTE BRIEF descriptors. Each value in the descriptor array is an 8-bit signature.
    4. Encoding each value in the descriptor to binary and concatenating will give the complete descriptor. 
    """
    img_of_2 = cv2.resize(img_of_2, (60, 60))
    test_kp = [cv2.KeyPoint(28, 28, 16)]
    brief_extr = cv2.xfeatures2d.BriefDescriptorExtractor_create(16)
    brief_kp, des = brief_extr.compute(img_of_2, test_kp)

    cv2.imshow('image', resize_for_display(img_of_2))
    cv2.waitKey(0)
