def douin_csv_open(command):
    """フォームから入力した動員 1のような言葉を引数として受け取った時にdouin, numberという変数に分割して受け取る"""
    douin, number  = command.split()
    with open('観客動員整理.csv', encoding='utf-8') as open_file:
        read_douin = open_file.read()
        douin_split = read_douin.splitlines()


    douin_dict = {}

    for douin in douin_split:
        team_number, mobilization = douin.split(':')
        douin_dict[team_number] = mobilization

    mobilization_dict = {}
    for team_number in douin_dict:
        audience_mobilizations = douin_dict[team_number].split(',')
        key = audience_mobilizations[0]
        name = audience_mobilizations[1]
        year = audience_mobilizations[2]
        section = audience_mobilizations[3]
        '''audience_mobilization = audience_mobilization[4]はエラーになるのでsを付けた'''
        audience_mobilization = audience_mobilizations[4]
        the_day_of_the_week = audience_mobilizations[5]
        sunny = audience_mobilizations[6]
        sunny_mobilization = audience_mobilizations[7]
        if sunny_mobilization != "観客動員数予測1":
            sunny_mobilization = int(sunny_mobilization)
        cloudy = audience_mobilizations[8]
        cloudy_mobilization = audience_mobilizations[9]
        rain = audience_mobilizations[10]
        rain_mobilyzation = audience_mobilizations[11]
        heavy_rain = audience_mobilizations[12]
        heavy_rain_mobilyzation = audience_mobilizations[13]
        star = audience_mobilizations[14]
        opening_match = audience_mobilizations[15]
        sannno_univ_special_day = audience_mobilizations[16]
        mobilization_dict[team_number] = (name, year, section, audience_mobilization, the_day_of_the_week, sunny, sunny_mobilization, cloudy, cloudy_mobilization, rain, rain_mobilyzation, heavy_rain, heavy_rain_mobilyzation, star, opening_match, sannno_univ_special_day)
        mobilization_dict[team_number] = '{}戦の観客動員数は\n{}の場合{}人\n{}の場合{}人\n{}の場合{}人\n{}の場合{}人よ。'.format(name, sunny, sunny_mobilization, cloudy, cloudy_mobilization, rain, rain_mobilyzation, heavy_rain, heavy_rain_mobilyzation)
        basic_message = '{}戦の観客動員数は\n{}の場合{}人\n{}の場合{}人\n{}の場合{}人\n{}の場合{}人よ。'.format(name, sunny, sunny_mobilization, cloudy, cloudy_mobilization, rain, rain_mobilyzation, heavy_rain, heavy_rain_mobilyzation)


        if audience_mobilization != "0":
            mobilization_dict[team_number] = '{}戦の観客動員数は{}人だったわ。\nお天気は{}だったわ。\nこの時私はまだ生まれてないから動員数の予測はしていないの。'.format(name, audience_mobilization, cloudy)

        if star == "1":
            mobilization_dict[team_number]  = basic_message + "\nこの試合はスター選手が来るから、たくさんお客さんが来そうね。"  .format(name, sunny, sunny_mobilization, cloudy, cloudy_mobilization, rain, rain_mobilyzation, heavy_rain, heavy_rain_mobilyzation, star)

        if sannno_univ_special_day == "1":
            mobilization_dict[team_number] = basic_message + "\nこの日は産能大スペシャルデーだから、たくさんの学生さんが来てくれると思うわ。"

        if sunny_mobilization > 15380:
            mobilization_dict[team_number] = basic_message + "\nスタジアムの収容人数よりも人が多い？\nごめんなさい。そういうことはまだ教わっていないの。"

    response = mobilization_dict
    return response[number]
