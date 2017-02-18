import cv2
import numpy as np
import argparse


def main(path, out_path):
  img = cv2.imread(path, cv2.IMREAD_COLOR)
  h, w = img.shape[:2]
  c = int((w - h) / 2)
  clp = img[0:h, c:w - c]
  resized = cv2.resize(clp, (128, 128))
  cv2.imwrite(out_path, resized)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='clipping and resize')
    parser.add_argument('--input', '-i', default='input.jpg',
                        help='input file')
    parser.add_argument('--output', '-o', default='output.jpg',
                        help='output file')
    args = parser.parse_args()
    main(args.input, args.output)
