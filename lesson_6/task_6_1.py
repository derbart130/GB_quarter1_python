import time


class TrafficLight:
    __colors = ['Red', 'Yellow', 'Green']

    def running(self):
        c = int(input("Enter number of cycles: "))
        i = 1
        while i <= c:
            for el in TrafficLight.__colors:
                if el == 'Red':
                    print(f"\033[31m{TrafficLight.__colors[0]}")
                    time.sleep(7)
                elif el == 'Yellow':
                    print(f"\033[33m{TrafficLight.__colors[1]}")
                    time.sleep(2)
                else:
                    print(f"\033[32m{TrafficLight.__colors[2]}")
                    time.sleep(10)
            i += 1


traffic = TrafficLight()
traffic.running()