import sys
sys.path.append('../source')
from HoughTransform import Huogh_line_highlight
from matplotlib import pyplot as plt
import pytest

def test_1_lines():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/lines.png"))
    plt.savefig("result_image/lines.png")

def test_2_iroad():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/iroad.jpeg"))
    plt.savefig("result_image/iroad.png")

def test_3_building():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/building.jpg"))
    plt.savefig("result_image/building.png")

def test_4_parking():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/parking.png"))
    plt.savefig("result_image/parking.png")

def test_5_square():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/square.png"))
    plt.savefig("result_image/square.png")

def test_6_road():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/road.jpeg"))
    plt.savefig("result_image/road.png")

def test_7_straight_lines_samples():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/straight_lines_samples.JPG"))
    plt.savefig("result_image/straight_lines_samples.png")

def test_8_grayscale():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/sunset.png"))
    plt.savefig("result_image/sunset.png")

def test_9_10x10():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/10x10.jpeg"))
    plt.savefig("result_image/10x10.png")

def test_10_1000x1000():
    plt.figure()
    plt.imshow(Huogh_line_highlight("./test_image/1000x1000.jpeg"))
    plt.savefig("result_image/1000x1000.png")