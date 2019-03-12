import random

about_soccer_dict = {
    '1':'サッカーはみるだけじゃなくやってみたいわね。\n今はインターネット上の存在だからゲームくらいでしかできないけど。',
    '2':'DAZNはすごいわね。Jリーグからチャンピオンズリーグまで見られるから。\n何気にボクシングのビッグマッチがやってるわよね。',
    '3':'またぎフェイントやってみたいなぁ。',
    '4':'フットサルもやってみたいなあ。',
    '5':'ダッシュダ～ッシュダッシュ♪\n昔の有名なサッカー漫画なんでしょ？',
    '6':'スタジアムに行きたいわ！',
    '7':'好きなサッカー？\nそれはアグレッシブで最後まであきらめない「湘南スタイルよ」',
    '8':'svolmeは可愛いわよね。\nもちろんベルマーレのサプライヤーのpenaltyも。',
    '9':'えいっ！ヒールリフト！',

}

def about_soccer():
    key, soccer = random.choice(list(about_soccer_dict.items()))
    choiced = soccer
    response = choiced
    return response
