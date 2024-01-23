# yolov7-kelp-training

## Setup 

Clone this repository by

``git clone --recurse-submodules https://github.com/dave-quesadilla/yolov7-kelp-training.git``

to include the original yolov7 repository as a submodule. 

## Training 
To train the base model,

1. Get *original* weights e.g. 

``wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt ``

2. Extract training data into folder 'sporophytes'

3. Train model 
``python yolov7/train.py --device 0 --cfg yolov7-sporophyte.yaml --weights yolov7_training.pt --data sporophyte-dataset.yaml --hyp yolov7/data/hyp.scratch.custom.yaml --name yolov7-sporophyte --epochs 1200``

For other models use train_aux.py. To train the larger models, use fix from https://github.com/WongKinYiu/yolov7/pull/1858. For example you can change to the yolov7 directory and 

``gh pr checkout 1858``

 Other steps are similar. 

## Testing


``python yolov7/test.py --data sporophyte-dataset.yaml --img 640 --batch 32 --conf 0.001 --iou 0.5 --device 0 --weights yolov7-sporophyte.pt --name yolov7-sporophyte-640-val &> yolov7-sporophyte-test.txt``

## Inference
For example, to show detection results on test data,
``python yolov7/detect.py --weights yolov7-sporophyte.pt --conf 0.25 --img-size 640 --source sporophytes/test/images``
