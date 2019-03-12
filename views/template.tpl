
<head>
  <!doctype html>
  <html lang="ja">
  <meta charset="UTF-8">
  <title>ベルマーレ観客動員予測１号ちゃん</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <link rel="stylesheet" href="/static/css/style.css" type="text/css" />

</head>

<html>
<body>

  <!-- Bootstrap CSS -->
  <!--<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">-->



<div class="line-top">
<strong>ベルマーレ観客動員予測１号ちゃん</strong>
</div>



<div class="line-bc"><!--①LINE会話全体を囲う-->



  <!--③右コメント始-->
  <div class="mycomment">
    <p>
      {{input_text|nl2br }}
      {{input_text_conversion|nl2br }}
    </p>
  </div>
  <!--/③右コメント終-->




  <!--②左コメント始-->
  <div class="balloon6">
    <div class="faceicon">
      <img src = /static/css/images/icon.png>
    </div>
    <div class="chatting">
      <div class="says">
           {{output_text|nl2br }}
      </div>
    </div>

  </div>
  <!--②/左コメント終-->

</div><!--/①LINE会話終了-->

<!--送信フォーム-->
<form method="post" action="/douinyosoku/1/">
  <input class = "input-form" name="input_text">
  <input class = "input-button" type="image" src="/static/css/images/submit_button.png" alt="送信する">
  <!--<input class = "input-button" type="submit" value="送信">-->
</form>



<strong class="douinyosokukiku">観客動員数の予測を聞く</strong>
<form class = "select-form" method="post" action="/douinyosoku/1/">
<select name="input_text">
<option value="audience_mobilization_anaritics 1">1節 北海道コンサドーレ札幌</option>
<option value="audience_mobilization_anaritics 2">2節:FC東京</option>
<option value="audience_mobilization_anaritics 3">4節:ベガルタ仙台</option>
<option value="audience_mobilization_anaritics 4">6節:ジュビロ磐田</option>
<option value="audience_mobilization_anaritics 5">7節:松本山雅FC</option>
<option value="audience_mobilization_anaritics 6">10節:名古屋グランパス</option>
<option value="audience_mobilization_anaritics 7">11節:大分トリニータ</option>
<option value="audience_mobilization_anaritics 8">14節:横浜F・マリノス</option>
<option value="audience_mobilization_anaritics 9">17節:セレッソ大阪戦</option>
<option value="audience_mobilization_anaritics 10">19節:ヴィッセル神戸</option>
<option value="audience_mobilization_anaritics 11">21節:鹿島アントラーズ</option>
<option value="audience_mobilization_anaritics 12">23節:サガン鳥栖</option>
<option value="audience_mobilization_anaritics 13">25節:浦和レッズ</option>
<option value="audience_mobilization_anaritics 14">27節:清水エスパルス</option>
<option value="audience_mobilization_anaritics 15">28節:	川崎フロンターレ</option>
<option value="audience_mobilization_anaritics 16">30節:ガンバ大阪</option>
<option value="audience_mobilization_anaritics 17">33節:サンフレッチェ広島</option>
</select></p>
<input type="submit" value="送信"><input type="reset" value="リセット">
</form>




<strong class="douinyosokukiku">ベルマーレ観客動員予測１号ちゃんについて</strong>
<form class = "select-form" method="post" action="/douinyosoku/1/">
<select name="input_text">
<option value="What_is_the_bellmare_spectator_recruitment_number_forecast？">ベルマーレ観客動員予測１号ちゃんって何</option>
<option value="tell_me_the_analytical_method">分析手法を教えて</option>
<option value="tell_me_about_other_functions">その他の機能について教えて</option>
</select></p>
<input type="submit" value="送信"><input type="reset" value="リセット">
</form>





<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>


</body>
</html>
