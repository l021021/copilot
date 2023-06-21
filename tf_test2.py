import cv2
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# 加载frozen SSDMobileNetV2模型
model_path = 'path_to_frozen_model/frozen_inference_graph.pb'

# 加载物体类别标签
label_map_path = 'path_to_label_map.pbtxt'

# 加载frozen模型
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(model_path, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# 加载标签映射
category_index = label_map_util.create_category_index_from_labelmap(label_map_path, use_display_name=True)

# 打开视频流
cap = cv2.VideoCapture('rtsp://admin:Bjxy+2023ZYH@192.168.100.48:554/Streaming/Channels/501')

with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        while True:
            # 读取视频帧
            ret, frame = cap.read()

            # 执行物体检测
            image_np_expanded = np.expand_dims(frame, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded}
            )

            # 可视化检测结果
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8
            )

            # 显示帧
            cv2.imshow('Video', frame)

            # 按下q键退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# 释放视频流和关闭窗口
cap.release()
cv2.destroyAllWindows()
