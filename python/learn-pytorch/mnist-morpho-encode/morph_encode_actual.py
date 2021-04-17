from cv2 import cv2

from morph_encode import read_img_and_threshold, multi_dilate_and_shrink, inter_over_union_features


def resize_for_display(image):
    return cv2.resize(image, (200, 200))


def show_img_and_descriptors(image, descriptors, name='N/A'):
    cv2.imshow(f'orig-{name}', resize_for_display(image))
    cv2.imshow(f'dial-3x3-{name}', resize_for_display(descriptors[0]))
    cv2.imshow(f'dial-2x2-{name}', resize_for_display(descriptors[1]))
    cv2.imshow(f'dial-1x1-{name}', resize_for_display(descriptors[2]))


if __name__ == '__main__':
    path_prefix = '/home/yashrahmed/Documents/datasets/kaggle-mnist-as-images/trainingSample'
    digit_2_prefix = f'{path_prefix}/trainingSample/2'
    digit_3_prefix = f'{path_prefix}/trainingSample/3'
    digit_5_prefix = f'{path_prefix}/trainingSample/5'

    threshold_type = cv2.THRESH_BINARY
    threshold_value = 20
    kernel_sizes = [4, 3, 2]
    tgt_dim = (8, 8)

    img_of_2 = read_img_and_threshold(f'{digit_2_prefix}/img_22.jpg', threshold_value, threshold_type)
    img_of_3 = read_img_and_threshold(f'{digit_3_prefix}/img_7.jpg', threshold_value, threshold_type)
    img_of_5 = read_img_and_threshold(f'{digit_5_prefix}/img_107.jpg', threshold_value, threshold_type)
    query_img_of_3 = read_img_and_threshold(f'{path_prefix}/img_46.jpg', threshold_value, threshold_type)
    image_records = {
        '2': img_of_2,
        '3': img_of_3,
        '5': img_of_5,
    }

    img_of_2_desc = multi_dilate_and_shrink(kernel_sizes, tgt_dim, img_of_2)
    img_of_3_desc = multi_dilate_and_shrink(kernel_sizes, tgt_dim, img_of_3)
    img_of_5_desc = multi_dilate_and_shrink(kernel_sizes, tgt_dim, img_of_5)
    descriptor_records = {
        '2': img_of_2_desc,
        '3': img_of_3_desc,
        '5': img_of_5_desc
    }
    query_img_of_3_desc = multi_dilate_and_shrink(kernel_sizes, tgt_dim, query_img_of_3)

    show_img_and_descriptors(query_img_of_3, query_img_of_3_desc, name='query')
    for digit in ['2', '3', '5']:
        result = inter_over_union_features(query_img_of_3_desc, descriptor_records[digit])
        print(f'{digit} - {result}')
        show_img_and_descriptors(image_records[digit], descriptor_records[digit], name=digit)

    cv2.waitKey(0)
