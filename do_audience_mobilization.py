from bottle import route, run, template, request, static_file
import os
from pybot import pybot
from bottle import jinja2_template as template


# 必要に応じて、jinja2テンプレートがあるディレクトリを追加
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append("./path/to/templates")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# jinja2のfilterを設定
from bottle import BaseTemplate
BaseTemplate.settings.update({'filters': {'nl2br': lambda content: content.replace('\n', '<br>')}})


@route('/douinyosoku/1/')
def audience_mobilization():
    input_text = '観客動員予測や質問を入力してください'
    output_text='こんにちは！\n湘南ベルマーレ観客動員予測システムの\n「観客動員予測１号」です。\nよろしくお願いいたします！'
    return template('template', input_text=input_text, output_text=output_text, input_text_conversion='')


@route('/douinyosoku/1/', method='POST')
def do_audience_mobilization():
    input_text = request.forms.input_text
    output_text = pybot(input_text)
    input_text_conversion = ''
    if input_text == 'audience_mobilization_anaritics 1':
        input_text_conversion = 'コンサドーレ札幌戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 2':
        input_text_conversion = 'FC東京戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 3':
        input_text_conversion = 'ベガルタ仙台戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 4':
        input_text_conversion = 'ジュビロ磐田戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 5':
        input_text_conversion = '松本山雅FC戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 6':
        input_text_conversion = '名古屋グランパス戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 7':
        input_text_conversion = '大分トリニータ戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 8':
        input_text_conversion = '横浜・Fマリノス戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 9':
        input_text_conversion = 'セレッソ大阪戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 10':
        input_text_conversion = 'ヴィッセル神戸戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 11':
        input_text_conversion = '鹿島アントラーズ戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 12':
        input_text_conversion = 'サガン鳥栖戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 13':
        input_text_conversion = '浦和レッズ戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 14':
        input_text_conversion = '清水エスパルス戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 15':
        input_text_conversion = '川崎フロンターレ戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 16':
        input_text_conversion = 'ガンバ大阪戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'audience_mobilization_anaritics 17':
        input_text_conversion = 'サンフレッチェ広島戦の観客動員数を教えて'
        input_text = ''

    if input_text == 'What_is_the_bellmare_spectator_recruitment_number_forecast？':
        input_text_conversion = 'ベルマーレ観客動員予測１号ちゃんって何？'
        input_text = ''

    if input_text == 'tell_me_the_analytical_method':
        input_text_conversion = '分析手法を教えて'
        input_text = ''

    if input_text == 'tell_me_about_other_functions':
        input_text_conversion = 'その他の機能について教えて'
        input_text = ''


    return template('template', input_text=input_text, output_text=output_text, input_text_conversion=input_text_conversion)



@route('/static/css/<filename:path>')
def send_static(filename):
    """静的ファイルを返す
    """
    return static_file(filename, root=f'{STATIC_DIR}/css')


#run(host='localhost', port=8080, debug=True)
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
