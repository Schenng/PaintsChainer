import cv2
import numpy as np
import argparse

# http://www.mathgram.xyz/entry/cv/contour
def main(path, output_path):
    neiborhood24 = np.array([[1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1]],
                             np.uint8)
    # グレースケールで画像を読み込む.
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #cv2.imwrite("gray.jpg", gray)

    # 白い部分を膨張させる.
    dilated = cv2.dilate(gray, neiborhood24, iterations=1)
    #cv2.imwrite("dilated.jpg", dilated)

    # 差をとる.
    diff = cv2.absdiff(dilated, gray)
    #cv2.imwrite("diff.jpg", diff)

    # 白黒反転
    contour = 255 - diff
    cv2.imwrite(output_path, contour)
    return contour

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='line drawing')
    parser.add_argument('--input', '-i', default='input.jpg',
                        help='input file')
    parser.add_argument('--output', '-o', default='output.jpg',
                        help='output file')
    args = parser.parse_args()
    main(args.input, args.output)
