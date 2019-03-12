from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command
from douinyosoku import douin_csv_open
from about import about, anaritics_method, other_functions
from bellmare import about_bellmare
from soccer import about_soccer
from stadium import about_stadium
from j_league import about_ｊ_league



command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(command):
    #command = input('pybot> ')
    response = ''
    try:
        for key in bot_dict:
            if key in command:
                response = bot_dict[key]
                break

            if '天気' in command:
                response = weather_command()
            if 'wikipedia' in command:
                response = wikipedia_command(command)
            if 'audience_mobilization_anaritics' in command:
                response = douin_csv_open(command)
            if 'What_is_the_bellmare_spectator_recruitment_number_forecast？' in command:
                response = about()
            if 'tell_me_the_analytical_method' in command:
                response = anaritics_method()
            if 'tell_me_about_other_functions' in command:
                response = other_functions()

            #サッカーのベルマーレとか打つと下のifの関数のみが適用されるのでいつか何かを考える

            if 'スタジアム' in command:
                response = about_stadium()

            if 'サッカー' in command:
                response  = about_soccer()

            if 'ベルマーレ' in command:
                response = about_bellmare()

            if 'Jリーグ' in command:
                response = about_j_league()



        if not response:
            response = 'ごめんなさい。その言葉はまだ教わっていないから分からないの。'
        return response



        #if 'さようなら' in command:
        #    break
    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ')
        print('* 種類：', type(e))
        print('* 内容', e)
