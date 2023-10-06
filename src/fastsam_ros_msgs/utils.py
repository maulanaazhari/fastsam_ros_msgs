import cv2
import numpy as np
# from fastsam_ros_msgs.msg import Detection, 
# from fastsam_trt_ros
def cvContourToPolyXYMsg(contour):
    c = contour.astype(np.int32).reshape((-1,2))
    poly_x = c[:, 0].reshape((1,-1))[0]
    poly_x = poly_x.tolist()

    poly_y = c[:, 1].reshape((1,-1))[0]
    poly_y = poly_y.tolist()

    return poly_x, poly_y

def cvContourFromPolyXYMsg(poly_x, poly_y):
    c = np.array([poly_x, poly_y], dtype=np.int32).transpose()
    c = c.reshape((-1, 1, 2))
    return c

def npMaskToMsg(mask:np.ndarray):
    # if(mask.dtype != bool):
    mask.astype(bool)
    mask = mask.reshape((1,-1))[0]
    # print(mask.shape)
    return mask.tolist()

def npMaskFromMsg(mask:np.ndarray, width:int, height:int):
    mask = np.asarray(mask, dtype=np.bool)
    mask = mask.reshape((height, width))
    return mask