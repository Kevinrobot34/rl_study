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


#### やったこと
* Random (cp_random.py)
* 状態行動価値関数Qの線形関数近似


#### 実行の仕方
```
$ python cp_random.py
```
などと実行するだけ．


#### 注意点
* 描画について \
    `env.render()`でcartpoleの状態が描画される．が，これは意外と重くて時間がかかる．
    学習のstep/episode数が多い時などはコメントアウトしておくと早くなって良い．
    またAtomのHydrogenなどを使う場合は`env.render()`を単独で実行するとエラーになるっぽいので，
    `env.close()`まで含めて実行すべし．

* 最大Step数について \
    openAIgymでは環境の登録時に各エピソードの最大ステップ数を決めることができる．
    例えば，
    [ここ](https://github.com/openai/gym/blob/master/gym/envs/__init__.py )を見ると，
    * CartPole-v0
        ```Python
        register(
            id='CartPole-v0',
            entry_point='gym.envs.classic_control:CartPoleEnv',
            max_episode_steps=200,
            reward_threshold=195.0,
        )
        ```
    などと`max_episode_steps`が決められている．
    強制的にこの制限を変更するには
    ```Python
    env._max_episode_steps = 10000 # 最大試行回数の変更
    ```
    とすれば良いらしい．

* 乱数のシードについて \
    envのシードとnumpyのシードそれぞれを指定しないといけない．
    ```Python
    ### seedの設定
    env.seed(0) # envのseed
    np.random.seed(1) # numpyのseed
    ```
