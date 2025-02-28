# RAM Robotics CV Workshop

A fork of [opnecv_zoo](https://github.com/opencv/opencv_zoo)

## Start

Start by creating a virtual environment for python and installing the required packages.
```sh 
cd path/to/cv_workshop
python -m venv env
```
- For Mac
```sh
source env/bin/activate
```
- For Windows
```sh
.\env\Scripts\activate
```

Install required packages (may need pip3)
```sh
pip install -r requirements
```

Then run
```sh
python yunet_cam.py
```

## Pose Estimation

run
```sh
python models/pose_estimation_mediapipe
```

## More Resources

### Face Detection with [YuNet](./models/face_detection_yunet/)

![largest selfie](./models/face_detection_yunet/example_outputs/largest_selfie.jpg)

### Face Recognition with [SFace](./models/face_recognition_sface/)

![sface demo](./models/face_recognition_sface/example_outputs/demo.jpg)

### Facial Expression Recognition with [Progressive Teacher](./models/facial_expression_recognition/)

![fer demo](./models/facial_expression_recognition/example_outputs/selfie.jpg)

### Human Segmentation with [PP-HumanSeg](./models/human_segmentation_pphumanseg/)

![messi](./models/human_segmentation_pphumanseg/example_outputs/messi.jpg)

### Image Segmentation with [EfficientSAM](./models/image_segmentation_efficientsam/)

![sam_present](./models/image_segmentation_efficientsam/example_outputs/sam_present.gif)

### License Plate Detection with [LPD_YuNet](./models/license_plate_detection_yunet/)

![license plate detection](./models/license_plate_detection_yunet/example_outputs/lpd_yunet_demo.gif)

### Object Detection with [NanoDet](./models/object_detection_nanodet/) & [YOLOX](./models/object_detection_yolox/)

![nanodet demo](./models/object_detection_nanodet/example_outputs/1_res.jpg)

![yolox demo](./models/object_detection_yolox/example_outputs/3_res.jpg)

### Object Tracking with [VitTrack](./models/object_tracking_vittrack/)

![webcam demo](./models/object_tracking_vittrack/example_outputs/vittrack_demo.gif)

### Palm Detection with [MP-PalmDet](./models/palm_detection_mediapipe/)

![palm det](./models/palm_detection_mediapipe/example_outputs/mppalmdet_demo.gif)

### Hand Pose Estimation with [MP-HandPose](models/handpose_estimation_mediapipe/)

![handpose estimation](models/handpose_estimation_mediapipe/example_outputs/mphandpose_demo.webp)

### Person Detection with [MP-PersonDet](./models/person_detection_mediapipe)

![person det](./models/person_detection_mediapipe/example_outputs/mppersondet_demo.webp)

### Pose Estimation with [MP-Pose](models/pose_estimation_mediapipe)

![pose_estimation](models/pose_estimation_mediapipe/example_outputs/mpposeest_demo.webp)

### QR Code Detection and Parsing with [WeChatQRCode](./models/qrcode_wechatqrcode/)

![qrcode](./models/qrcode_wechatqrcode/example_outputs/wechat_qrcode_demo.gif)

### Chinese Text detection [PPOCR-Det](./models/text_detection_ppocr/)

![mask](./models/text_detection_ppocr/example_outputs/mask.jpg)

### English Text detection [PPOCR-Det](./models/text_detection_ppocr/)

![gsoc](./models/text_detection_ppocr/example_outputs/gsoc.jpg)

### Text Detection with [CRNN](./models/text_recognition_crnn/)

![crnn_demo](./models/text_recognition_crnn/example_outputs/CRNNCTC.gif)

## License

OpenCV Zoo is licensed under the [Apache 2.0 license](./LICENSE). Please refer to licenses of different models.
