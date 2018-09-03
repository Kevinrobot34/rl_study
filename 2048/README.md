## 2048
https://github.com/rgal/gym-2048 を使って2048の強化学習をしよう！


#### Reference
* https://github.com/rgal/gym-2048
  * opan AI gym向けに作られた2048のenv．世界は広い．


### 設定
`env.step()`で返される変数ob, reward, actionについて．
詳細は `gym-2048/gym_2048/envs/game2048_env.py` を参照．
* ob
    * 以下のような盤面に対応するリストが返される．
    * [0 1 2 3 4 5 6 7 8 9 a b c d e f]
        * 0 1 2 3 \
          4 5 6 7 \
          8 9 a b \
          c d e f
    * 数字が無いときは0, 他は数字がそのまま入ってる．
* reward
    * ゲームやってる時のスコア
* done
    * 以下が成立した時，done=Trueとなる
        * 2048のタイルができる
        * うごかせなくなる


### やったこと
* Random (`2048_random.py`)


### 実行の仕方
```
$ python 2048_random.py
```
などと実行するだけ．
