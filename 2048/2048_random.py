#%%
import os, sys, math
import gym
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

# rl_studyのpathを適宜ROOT_DIRに設定してください
ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
ENV_DIR = os.path.join(ROOT_DIR, '2048', 'gym-2048') # 2048用envのためのsubmoduleへのpath
sys.path.append(ENV_DIR)

from gym_2048 import envs
#list(gym.envs.registry.all())
#%%

### 2048用のEnviromentを作る
env = gym.make('2048-v0')
#env.action_space.n # とりうる行動の数

n_epi = 100
res = []

for epi in tqdm(range(n_epi)):
    ### init
    ob = env.reset()
    total_reward = 0

    #for j in range(200): # 特定のステップ数で終わらせたい場合
    while True: # 週状態までやる場合
        ### 毎回状態を表示する
        env.render()
        #print(ob, env.action_space.n)

        ### 行動決定：ランダム
        action = env.action_space.sample()

        ### 実際に行動して，状態と報酬とdoneフラグを得る
        ob_n, reward, done, _ = env.step(action) # take a random action

        ### Reward
        total_reward += reward
        # print('reward: {}'.format(reward))
        # print('TOTreward: {}\n'.format(total_reward))

        ob = ob_n
        if done:
            ### 終状態になったら
            res.append(max(ob)) # 盤面にできた最大の数を保存しておく
            # print('EPI {}'.format(epi))
            # print('total-score = {}'.format(total_reward))
            # print('final-ob    = {}'.format(ob))
            # env.render() # 最終盤面を表示しておく
            # print('-'*80)
            break

### 結果のHistgram(text)
print(pd.Series(np.log2(res)).value_counts().sort_index())
print(np.mean(np.log2(res)))

### 最後には環境を閉じる
env.close()
