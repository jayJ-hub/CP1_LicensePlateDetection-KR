# CP1_LicensePlateDetection-KR

A deep learning project with a purpose to detect and recognize ehicle license plates in Korea, especially focused on reaching high accuracy despite the diversity of enviromental condition. May have faults or miscomprehensions within, pointing out errors or sharing insight on the topic is always greatly appreciated.

한국 차량 번호표지판을 인식하는 목적을 가지고 진행한 딥러닝 프로젝트입니다. 특히, 다양한 환경에서도 높은 정확도를 가진 모델을 구축하는데 중점을 두고 진행하고자 합니다. 아직 배우는 단계라 오류나 잘못 이해한 부분이 있을 때 짚어주시거나 이 주제에 관해 의견을 자유롭게 나눠주시는 건 언제든 환영입니다.
(README 파일은 영어 위주로 작성되어 있으며, 결과보고서는 한국어로 작성되어 있으니 참고 부탁드립니다.)


## Directory
├──requirements.txt
├──data_img : test imgs folder
│  ├── img_textOnly  : text imgs
│  ├── *img_licensePlate : manually-cropped licensePlates imgs (50)
│  └── *img_carWithLicense : cars with license imgs
└──
(* : excluded from the repositiory to avoid legal issues)

## Planning
Nov 4    : Planning & Gathering Data
Nov 5, 6 : Data Labeling, EDA/pre-processing
Nov 7, 8 : Baseline model
Nov 9, 10: Improving model performance
Nov 11   : Automate update process
Nov 12,13: (if possible) connect to web application
Nov 14   : ------------[Deadline]------------------

## PROCESS
0. Dataset
1. Data Preprocessing
    (Data Augmentation for more data)
2. Object Detection (Plate) : OpenCV
3. Character Segmentation
4. Character Recognition : Pytesseract
5. Tweaking 
    (light exposure, resolution/quality, noise, constrast, orientation)
    - AutoEncoder, Super Resolution, improving constrast, denoise
6. + experiment with extreme circumstances
7. Hyperparameter tuning -> improve results
8. Automating updating process
    (updating improvement and optimal parameters)
9. Apply to Web application : flaskapp
10. research report

## REFERENCES