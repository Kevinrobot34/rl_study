### Cartpole
open AI gymのCartpoleで強化学習してみた．


#### Reference
* https://gym.openai.com/envs/CartPole-v1/
  * オフィシャルなCartpoleのenvの説明．
* https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
  * Cartpoleのコード
* https://github.com/openai/gym/wiki/CartPole-v0
  * CartpoleのWiki
  * state(observation), action, rewardなどについて細かく書いてある．


#### やったこと
* Random (cp_random.py)


#### 注意点
openAIgymでは環境の登録時に各エピソードの最大ステップ数を決めることができる．
例えば， [ここ](https://github.com/openai/gym/blob/master/gym/envs/__init__.py )を見ると，
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
