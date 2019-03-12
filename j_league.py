import random

about_j_league_dict = {
    '1':'Jリーグ。実力差が少ないリーグという評判よ',
    '2':'Jリーグが強くならなければ日本代表も強くならないわ。\n選手を海外に輸出だけすれば強くなるなんて幻想よ。',
    '3':'みんなはどのチームのサポーターなの？\n私はもちろんベルマーレよ。',
    '4':'Jリーグアプリ。あれ面白そうね。',
    '5':'チケット買った？',
    '6':'バージョンが上がれば他にも会話が増えるかもね。',
    '7':'Jリーグは女性や子どもでも楽しめる安全なスタジアムを目指しているわ。\n私のようなインターネット上の存在でもいつか観戦できるようになるかしら？',

}

def about_j_league():
    key, j_league = random.choice(list(about_j_league_dict .items()))
    choiced = j_league
    response = choiced
    return response
