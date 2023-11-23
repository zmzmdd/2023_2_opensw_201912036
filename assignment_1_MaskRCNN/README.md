환경 구축 및 설정

1. Anaconda에서 새로운 가상환경 생성
   1. conda create -n [가상환경 이름] python==3.7
   2. conda activate [가상환경 이름]
2. mask rcnn 다운
    1. git clone https://github.com/matterport/Mask_RCNN
3. pip install keras==2.1.2
4. pip install tensorflow-gpu==1.15.5
5. pip install protobuf==3.20.*
6. git clone한 폴더로 가서 Mask-RCNN - model - balloon - datasets - logs와 같이 폴더를 생성
7. Mask_RCNN 폴더에 다음 파일을 다운 받아서 복사
   1. https://github.com/matterport/Mask_RCNN/releases/download/v2.1/mask_rcnn_balloon.h5
   2. https://github.com/matterport/Mask_RCNN/releases/download/v1.0/mask_rcnn_coco.h5
8. https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip
   1. Mask_RCNN/model/balloon/datasets 폴더에 해제
   2. datasets 폴더에 train과 val 폴더가 압축 해제 되어야 함
9. pip install -U scikit-image==0.16.2
10. python balloon.py --dataset ../../model/balloon/datasets --weights ../../mask_rcnn_balloon.h5 --logs ../../model/balloon/logs --image ../../model/balloon/datasets/val/3800636873_ace2c2795f_b.jpg splash
    1. val 폴더에 있는 원하는 사진을 입력하면 된다.