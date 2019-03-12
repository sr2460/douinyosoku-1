def about():
    """動員 keyをセレクトボックスのvalueにしてdouinyosoku.pyを作っていたがそうすると動員というワードを入れると変数を2つにしなくてはいけないのでエラーがでるので
    audience_mobilization_anaritics keyをセレクトボックスのvalueにする。"""

    response = 'ベルマーレ観客動員予測１号ちゃんは\n湘南ベルマーレの観客動員数の予測と、その他コミュニケーションがとれるツールとして生み出されました。'
    return response

def anaritics_method():
    response = '重回帰分析の手法を使って観客動員数を予測しているわ。\n\njupyter notebook上で解析後、出力したcsvをディレクトリに格納してそこから情報を引っ張り出しているわ。\n\nそこら辺は手作業なんだけれどバージョンが進めばプログラム上で予測したデータをそのまま抽出するなんてこともできるのかもね。'
    return response

def other_functions():
    response = 'wikipediaと入力した後に調べたい言葉を入れるとwikipediaから情報を引っ張り出せるわ。\n\n天気と入力すると現在の平塚の天気が分かる・・・と言いたいところだけどRSSが提供されていなかったから小田原の天気になっているわ。\nここら辺の機能は「いちばんやさしいPython教本」の機能の丸写しね。\n\nあいさつすればあいさつをするし、適当に話しかけてみたら思わぬことを喋るかもよ。'
    return response
