
import numpy as np
import matplotlib.pyplot as plt

Boxes = np.array([[100, 100, 210, 210, 0.72],
                  [250, 250, 400, 400, 0.8],
                  [220, 220, 320, 370, 0.92],
                  [100, 150, 235, 200, 0.79],
                  [230, 240, 355, 350, 0.81],
                  [220, 230, 315, 340, 0.9],
                  [140, 175, 255, 270, 0.95]])

def nms(boxes, iou_thresh):
    # 每个 box 的坐标和置信度
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    scores = boxes[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    keep_boxes = []
    index = scores.argsort()[::-1]
    while len(index) > 0:
        i = index[0]
        keep_boxes.append(i)
        x1_overlap = np.maximum(x1[i], x1[index[1:]])
        y1_overlap = np.maximum(y1[i], y1[index[1:]])
        x2_overlap = np.minimum(x2[i], x2[index[1:]])
        y2_overlap = np.minimum(y2[i], y2[index[1:]])
        w = np.maximum(0, x2_overlap - x1_overlap + 1)
        h = np.maximum(0, y2_overlap - y1_overlap + 1)
        overlap_area = w * h
        ious = overlap_area / (areas[i] + areas[index[1:]] - overlap_area)
        idx = np.where(ious <= iou_thresh)[0]
        index = index[idx + 1]
    return keep_boxes

def plot_bbox(dets, c='k'):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    plt.plot([x1, x2],[y1, y1], c)
    plt.plot([x1, x1],[y1, y2], c)
    plt.plot([x1, x2],[y2, y2], c)
    plt.plot([x2, x2],[y1, y2], c)
    plt.title("NMS")

if __name__ == '__main__':
    plt.figure(1)
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)

    plt.sca(ax1)
    plot_bbox(Boxes, 'g')

    keep_boxes = nms(Boxes, iou_thresh=0.8)
    plt.sca(ax2)
    plot_bbox(Boxes[keep_boxes], 'r')

    ax1.set_xlim([50, 450])
    ax1.set_ylim([50, 450])
    ax2.set_xlim([50, 450])
    ax2.set_ylim([50, 450])
    plt.show()


