import udp_forza
import pygame

def main():
    while True:
        un_data = udp_forza.recive_udp(True)

        is_race_on = un_data[0]
        print(f"is_race_on: {is_race_on}")
    pass

if __name__ == "__main__":
    main()