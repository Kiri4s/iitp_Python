import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import argparse


# EDGE_PIXEL_THRESHOLD = 255
# LOWER_CANNY_THRESHOLD = 300
# UPPER_CANNY_THRESHOLD = 400
# LINE_SELECT_THRESHOLD = 180


def Hough_line_detect(canny_image, edge_pixel_threshold):
    theta = np.arange(0, 180, 1)  # Theta [-90, 90] degrees ( or (0 - 180))

    rho_max = round(
        math.sqrt(canny_image.shape[0] ** 2 + canny_image.shape[1] ** 2))  # rho_max = sqrt(x^2 + y^2) = diagonal
    accumulator = np.zeros((2 * rho_max, len(theta)))  # Accumulator matrix to store the values

    edge_pixels = np.where(
        canny_image == int(edge_pixel_threshold))  # Threshold to get edges pixel location (x,y)
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    cos = np.cos(np.deg2rad(theta))  # Calculate 'cos' and 'sin'
    sin = np.sin(np.deg2rad(theta))  # value ahead to improve running time

    # Calculate rho value for each edge location (x,y) with all the theta range
    for i in range(len(coordinates)):
        for j in range(len(theta)):
            rho = int(round(coordinates[i][1] * cos[j] + coordinates[i][0] * sin[j]))
            # accumulator[rho, j] += 1
            accumulator[rho, j] += 2  # better performance
            # accumulator[rho, j] += 3

    return accumulator

def Huogh_line_highlight(path_to_image, edge_pixel_threshold=255, lower_canny_threshold=300, upper_canny_threshold=400, line_select_threshold=180):
    image = cv2.imread(path_to_image)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(grayscale, int(lower_canny_threshold), int(upper_canny_threshold))
    accumulator = Hough_line_detect(canny_image, edge_pixel_threshold)

    edge_pixels = np.where(
        accumulator > int(line_select_threshold))  # Threshold some high values then draw the line
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    for i in range(len(coordinates)):  # Draw detected line on an original image (from OpenCV tutorial for HoughLine)
        a = np.cos(np.deg2rad(coordinates[i][1]))
        b = np.sin(np.deg2rad(coordinates[i][1]))
        x0 = a * coordinates[i][0]
        y0 = b * coordinates[i][0]
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)

    return image


if __name__ == '__main__':

    argparse = argparse.ArgumentParser()
    argparse.add_argument('-image', required=True, help="Path to source image.")
    argparse.add_argument('--edge_pixel_threshold', required=False, default=255,
                          help='Threshold for defined edges pixels and them locations.')
    argparse.add_argument('--lower_canny_threshold', required=False, default=300,
                          help='Lower threshold for Canny() function from OpenCV.')
    argparse.add_argument('--upper_canny_threshold', required=False, default=400,
                          help='Upper threshold for Canny() function from OpenCV.')
    argparse.add_argument('--line_select_threshold', required=False, default=180,
                          help='threshold for selecting some emergency values and then drawing lines.')
    args = vars(argparse.parse_args())

    image = cv2.imread(args["image"])

    plt.subplot(221)
    plt.imshow(image)
    plt.title('Input image')

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # lower_canny_threshold = int(args["lower_canny_threshold"])
    # upper_canny_threshold = int(args["upper_canny_threshold"])
    canny_image = cv2.Canny(grayscale, int(args["lower_canny_threshold"]), int(args["upper_canny_threshold"]))

    accumulator = Hough_line_detect(canny_image, int(args["edge_pixel_threshold"]))

    edge_pixels = np.where(
        accumulator > int(args["line_select_threshold"]))  # Threshold some high values then draw the line
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    for i in range(len(coordinates)):  # Draw detected line on an original image (from OpenCV tutorial for HoughLine)
        a = np.cos(np.deg2rad(coordinates[i][1]))
        b = np.sin(np.deg2rad(coordinates[i][1]))
        x0 = a * coordinates[i][0]
        y0 = b * coordinates[i][0]
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)

    plt.subplot(222)
    plt.imshow(canny_image)
    plt.title('Canny image')
    plt.subplot(223)
    plt.imshow(image)
    plt.title('Output image')
    plt.subplot(224)
    plt.imshow(accumulator)
    plt.title('Hough space coord.')
    plt.show()
