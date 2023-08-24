import cv2
import os
from pathlib import Path
save_dir = "results"
Path(save_dir).mkdir(exist_ok=True, parents=True)
img_fps = [f for f in os.listdir() if f.endswith(".png")]

for img_fp in img_fps:
    print(img_fp)
    X = cv2.imread(img_fp)
    X = X[30:-20, 150:-130].copy()
    cv2.imwrite(os.path.join(save_dir, img_fp), X)

