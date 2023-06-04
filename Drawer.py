from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Driver.Driver import Driver


class Drawer:
    def __init__(self, driver: Driver):
        self.__driver = driver
        self.__car = driver.get_car

    """Method of displaying information about the driver and the car"""
    def draw_order(self):
        space = '\n    '
        driver_info = 'CAR: ' + self.__car.get_license_plate + space \
                      + self.__car.get_color + ' ' + self.__car.get_brand + space \
                      + self.__car.get_category
        driver_info += '\nDRIVER: '
        driver_info += (self.__driver.get_full_name + space + self.__driver.get_location)

        # Adding main titles
        fig, ax = plt.subplots()
        fig.set_size_inches((4, 4))
        fig.suptitle('Your order', fontsize=14, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.text(0.5, 0.65, driver_info, style='oblique', horizontalalignment='center',
                bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 5}, fontsize=11)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Adding the image of car
        car_image = mpimg.imread(self.__car.get_image)
        imagebox = OffsetImage(car_image, zoom=0.1)
        ab = AnnotationBbox(imagebox, (0.5, 0.30))
        ax.add_artist(ab)
        plt.draw()
        for pos in ['right', 'top', 'bottom', 'left']:
            plt.gca().spines[pos].set_visible(False)
        plt.show()
