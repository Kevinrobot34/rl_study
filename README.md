## 強化学習勉強用レポジトリ
主にopen AI gymを利用して強化学習に関連したものを実装し置いておくレポジトリ．

gymの使い方などについては，
cartpoleフォルダのREADMEとcartpoleをランダムに動かすプログラム(`cartpole/cp_random.py`)を
見てください．
その他の手法は基本的にこのプログラムからactionやrewardの決め方を変えただけ．

### Reference
何はともあれオフィシャルページとコードを読むのが早い．
* https://gym.openai.com
  * open AI gymのページ
* https://github.com/openai/gym
  * open AI gymのgithub
  * wikiも併せて読むと分かりやすい


### 基本構造
```python
import gym
### CartPole用のenviromentを作る
env = gym.make('CartPole-v0')

### seedの設定
env.seed(0) # envのseed

n_epi = 1000
for epi in range(n_epi):
    ### init
    ob = env.reset()

    while True: # 終状態までやる場合
        ### 状態の描画
        env.render()

        ### 行動決定
        action = get_action(ob)

        ### 実際に行動し，状態と報酬とdoneフラグを得る
        ob_n, reward, done, _ = env.step(action) # take a random action

        ### Reward
        # reward = hoge() # rewardを自分で設定する場合
        ### parameterの更新など
        # param =  update_param(ob, action, param, reward, ob_n)
        ob = ob_n
        if done:
            ### 終状態になったら
            print('done')
            break

### 最後には環境を閉じる
env.close()
```
基本構造はこれだけ．\
環境に対する行動を決める->実際に行動する->Prameterなどを更新する->環境に対する行動を決める->...\
と繰り返すだけ．
環境に関する知識がない状況で実際に行動を繰り返し，
その情報から行動の選択を最適化して行くのが強化学習である．

設計しなければならないものは
* いかに取りうる行動の中から行動を選択するか
    * 上記のプログラムでは`get_action(ob)`という関数で書かれている．
    * Q-Learning, SARSA, DQN, 関数近似, などなど...
    * 付随するparameterの更新が必要な場合は適宜それも作る．
        * 例 : `param =  update_param(ob, action, param, reward, ob_n)`
* Rewardの設計
    * open ai gymでは環境に対する行動をする(`env.step()`)と適宜rewardをもらえるのでそれをそのまま利用するのでも良い．詳細は利用する環境のgithub wikiなどを確認しよう．
    * デフォルト以外のrewardを使う場合には`env.step()`の下などで，適宜設定．


### 注意点
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
