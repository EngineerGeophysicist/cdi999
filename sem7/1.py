from time import sleep
from datetime import datetime as dt


class TrafficLight:
    __color = {'красный': 7, 'желтый': 2, 'зеленый': 7}
    _c = ''

    def running(self):
        for color, sw_time in self.__color.items():
            self._c = color
            start_state_time = dt.now()

            print(f"Светофор включился на '{self._c}' "
                  f"на {sw_time} секунд")

            sleep(sw_time)


tl = TrafficLight()
tl.running()

