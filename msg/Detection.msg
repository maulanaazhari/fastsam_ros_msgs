string class_name
int32 class_id
float32 score
float32 mask_iou #iou for ori_box with mask/polygon
float32 box_iou #iou between ori_box and rot_box
Box ori_box
Box rot_box
int32[] polygon_x
int32[] polygon_y
bool[] mask # Mask encoded as bitset