def calculate_iou(box1, box2):

    # 提取box1的坐标
    x1_box1, y1_box1, x2_box1, y2_box1 = box1
    # 提取box2的坐标
    x1_box2, y1_box2, x2_box2, y2_box2 = box2
    # 计算交集的坐标
    w = max(0, min(x2_box1, x2_box2) - max(x1_box1, x1_box2))
    h = max(0, min(y2_box1, y2_box2) - max(y1_box1, y1_box2))
    # 计算交集区域的面积
    intersection_area = w * h
    # 计算并集区域的面积
    box1_area = (x2_box1 - x1_box1) * (y2_box1 - y1_box1)
    box2_area = (x2_box2 - x1_box2) * (y2_box2 - y1_box2)
    # 计算Iou
    union_area = box1_area + box2_area - intersection_area
    iou = intersection_area / union_area
    return iou

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    box1 = [100, 100, 210, 210]
    box2 = [100, 150, 235, 200]
    iou = calculate_iou(box1, box2)
    print("iou: ", iou)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
