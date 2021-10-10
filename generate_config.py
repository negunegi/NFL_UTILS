from mmcv import Config
from pathlib import Path
baseline_cfg_path = "/mnt/ssd1/studentData/linyinglun/lyl练习用/kaggle_vip/kaggle_helmet/mmdetection/configs/cascade_rcnn/cascade_rcnn_x101_32x4d_fpn_1x_coco.py"
cfg = Config.fromfile(baseline_cfg_path)
cfg_path = f'{Path(baseline_cfg_path).name}_helmet_2'
cfg.dump(cfg_path)