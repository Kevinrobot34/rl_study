## Cartpole
open AI gymのCartpoleで強化学習してみた．


#### Reference
* https://gym.openai.com/envs/CartPole-v1/
  * オフィシャルなCartpoleのenvの説明．
* https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
  * Cartpoleのコード
* https://github.com/openai/gym/wiki/CartPole-v0
  * CartpoleのWiki
  * state(observation), action, rewardなどについて細かく書いてある．


#### 設定
`env.step()`で返される変数ob, reward, actionについて
* ob
    * [cart_pos, cart_v, pole_angle, pole_v]
* reward
    * 常に１
* done
    * 以下が成立した時，done=Trueとなる
        * Poleの角度が鉛直12度より倒れた時
        * Cartの位置が中止から2.4以上離れた時（画面外に出た時）
        * ('CartPole-v0'のデフォルト設定では)ステップ数が200を超えた時


#### やったこと
* Random (`cp_random.py`)
* Q-Learning
    * 離散化してテーブルを作る (`cp_ql.py`)
    * 線形関数近似 (`cp_lfa.py`)


#### 実行の仕方
```
$ python cp_random.py
```
などと実行するだけ．
