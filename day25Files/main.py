with open('weather_data.csv', 'r') as weather:
    wd = weather.readlines()
    w_list = [line.strip() for line in wd]
    # w_list = [line for line in wd]
    # for line in wd:
    #     line = line.strip()
    #     w_list.append(line)
    print(w_list)
    print(wd)
