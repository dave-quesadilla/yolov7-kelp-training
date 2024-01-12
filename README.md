# yolov7-kelp-training

0. Fix bug training larger models (see https://github.com/WongKinYiu/yolov7/pull/1858) for details. You can checkout the branch using the github command line tool, or manually modify the files in question. 

``cd yolov7/``
``gh pr checkout 1858``

1. Get weights e.g. 

``wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt ``
``wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6_training.pt``

2. Train model (from scratch)
For the base model, use 
``python yolov7/train.py --device 0 --cfg yolov7-sporophyte.yaml --weights yolov7_training.pt --data sporophyte-dataset.yaml --hyp yolov7/data/hyp.scratch.custom.yaml --name yolov7-sporophyte --epochs 600``
For other models use train_aux.py:
``python yolov7/train_aux.py --device 0 --cfg yolov7-w6-sporophyte.yaml --weights yolov7-w6_training.pt --data sporophyte-dataset.yaml --hyp yolov7/data/hyp.scratch.custom.yaml --name yolov7-w6--sporophyte --epochs 600``

3. Testing
Depeding on which run you want to use,

``python yolov7/test.py --data sporophyte-dataset.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights <weights_path>.pt --name yolov7<-model_prefix>_sporophyte_640_val &> yolov7-<-model_prefix>sporophyte-test.txt``