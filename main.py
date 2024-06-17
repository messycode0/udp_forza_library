import udp_forza
import pygame
    
def map_value(value, from_low, from_high, to_low, to_high):
    # Calculate the percentage of the value in the original range
    percentage = (value - from_low) / (from_high - from_low)

    # Map the percentage to the new range
    mapped_value = to_low + percentage * (to_high - to_low)

    return mapped_value

def format_time(seconds):
    # Separate the seconds and milliseconds
    total_seconds = int(seconds)
    milliseconds = int((seconds - total_seconds) * 1000)

    # Calculate minutes and remaining seconds
    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    # Format the time string
    time_string = f"{minutes}:{remaining_seconds:02d}.{milliseconds:03d}"
    return time_string

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Forza UDP Infoscreen [BETA]")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ALT_RED = (220,20,60)

    font_s = pygame.font.Font(None, 34)
    font_m = pygame.font.Font(None, 74)
    font_l = pygame.font.Font(None, 84)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

             
        un_data = udp_forza.recive_udp(True)

        # Start putting Data into Varibles
        is_race_on = un_data[0]
        gear = un_data[81]
        speed = un_data[61]
        speed = speed * 2.23694

        fuel = un_data[69]

        tt_fl = un_data[64]
        tt_fr = un_data[65]
        tt_rl = un_data[66]
        tt_rr = un_data[67]

        best_lap = un_data[71]
        best_lapf = format_time(best_lap)
        cur_lap = un_data[73]
        cur_lapf = format_time(cur_lap)
        last_lapf = format_time(un_data[72])

        cur_race_timef = format_time(un_data[74])

        cur_lap = un_data[75] + 1
        race_pos = un_data[76]

        normalized_driving_line = un_data[83]


        # I Dont know how tirewear relates to the outputed number I get from the packet
        # tw_fl = un_data[85]
        # tw_fr = un_data[86]
        # tw_rl = un_data[87]
        # tw_rr = un_data[88]

        accel = un_data[77]
        brake_ped = un_data[78]
        hand_brake = un_data[80]
        steer = un_data[82]
        steer = round(map_value(steer, -55, 55, -100, 100), 1)

        screen.fill("black")
        # Screen Rendering here

        if is_race_on == 1:
            screen.blit(font_s.render(f'The Sim is Running', True, GREEN), (20, 20))
        else:
            screen.blit(font_s.render(f'The Sim is NOT Running', True, RED), (20, 20))

        if gear == 0:
            screen.blit(font_m.render(f'Gear: {gear} (R)', True, ALT_RED), (20, 70))
        elif gear == 11: screen.blit(font_m.render(f'Gear: (S)', True, YELLOW), (20, 70))
        else: screen.blit(font_m.render(f'Gear: {gear}', True, WHITE), (20, 70))

        screen.blit(font_m.render(f'Accel: {round(map_value(accel, 0, 255, 0, 100), 2)}', True, WHITE), (300, 70))
        screen.blit(font_m.render(f'Break: {round(map_value(brake_ped, 0, 255, 0, 100), 2)}', True, WHITE), (600, 70))
        if hand_brake != 0:
            screen.blit(font_s.render('HB is active', True, RED), (600, 120))     
        else: screen.blit(font_s.render('HB is unactive', True, GREEN), (600, 120)) 
        
        screen.blit(font_m.render(f'Steer: {steer}', True, WHITE), (900, 70))

        # LAP TIMES
        screen.blit(font_m.render(f"CRT: {cur_race_timef}", True, WHITE), (1459, 790))
        screen.blit(font_m.render(f"LL: {last_lapf}", True, WHITE), (1500, 860))
        screen.blit(font_m.render(f"CL: {cur_lapf}", True, WHITE), (1500, 930))
        screen.blit(font_m.render(f"BL: {best_lapf}", True, WHITE), (1500, 1000))


        screen.blit(font_m.render(f"L{cur_lap}", True, WHITE), (1500, 720))
        screen.blit(font_m.render(f"P{race_pos}", True, WHITE), (1650, 720))


        screen.blit(font_m.render(f"Norm Drive line: {normalized_driving_line}", True, WHITE), (1350, 620))

        




        screen.blit(font_s.render(f'Speed (Exact): {speed}', True, WHITE), (20, 130))
        screen.blit(font_m.render(f'Speed (MPH): {round(speed)}', True, WHITE), (20, 170))

        screen.blit(font_m.render(f'Fuel (%): {round(fuel * 100, 3)}', True, WHITE), (20, 220))

        # Tire Info
        screen.blit(font_s.render(f'TIRES', True, WHITE), (20, 280))
        screen.blit(font_s.render(f'TEMP', True, WHITE), (100, 280))
        
        screen.blit(font_l.render(f'{round(tt_fl)}', True, YELLOW), (20, 300))
        screen.blit(font_l.render(f'{round(tt_fr)}', True, YELLOW), (140, 300))
        screen.blit(font_l.render(f'{round(tt_rl)}', True, YELLOW), (20, 370))
        screen.blit(font_l.render(f'{round(tt_rr)}', True, YELLOW), (140, 370))

        



        pygame.display.flip()
        clock.tick(60)


    pass

if __name__ == "__main__":
    main()