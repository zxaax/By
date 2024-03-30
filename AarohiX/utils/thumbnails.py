title1 = truncate(title)
    draw.text((text_x_position, 180), title1[0], fill=(255, 255, 255), font=title_font)
    draw.text((text_x_position, 230), title1[1], fill=(255, 255, 255), font=title_font)
    draw.text((text_x_position, 320), f"{channel}  |  {views[:23]}", (255, 255, 255), font=arial)

    
    line_length = 580  

    
    red_length = int(line_length * 0.6)
    white_length = line_length - red_length

    
    start_point_red = (text_x_position, 380)
    end_point_red = (text_x_position + red_length, 380)
    draw.line([start_point_red, end_point_red], fill="red", width=9)

    
    start_point_white = (text_x_position + red_length, 380)
    end_point_white = (text_x_position + line_length, 380)
    draw.line([start_point_white, end_point_white], fill="white", width=8)

    
    circle_radius = 10 
    circle_position = (end_point_red[0], end_point_red[1])
    draw.ellipse([circle_position[0] - circle_radius, circle_position[1] - circle_radius,
                  circle_position[0] + circle_radius, circle_position[1] + circle_radius], fill="red")
    draw.text((text_x_position, 400), "00:00", (255, 255, 255), font=arial)
    draw.text((1080, 400), duration, (255, 255, 255), font=arial)

    play_icons = Image.open("AarohiX/assets/play_icons.png")
    play_icons = play_icons.resize((580, 62))
    background.paste(play_icons, (text_x_position, 450), play_icons)

    try:
        os.remove(f"cache/thumb{videoid}.png")
    except:
        pass
    background.save(f"cache/{videoid}_v4.png")
    return f"cache/{videoid}_v4.png"
