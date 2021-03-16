from torch import cuda

from cv2 import cv2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(cuda.device_count())
    print(cv2.cuda.getCudaEnabledDeviceCount())
