import math


def circum_area(radius=1):
    '''calculate the area and circumference of a circle from its radius'''
    circum = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circum, area


def main():
    print(f"calc_circle_circum_area.py __name__ = {__name__}")


if __name__ == "__main__":
    main()
