import math
import gym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
#%matplotlib inline

### 状態行動価値関数を状態変数の線形関数で近似する
def q_func(state, action, param):
    #norm = [2.4, 3.0, 1.0, 2.5]
    norm = [1000, 3.0, 0.3, 1.5]
    return np.sum([w*x/c for w,x,c in zip(param[action], state, norm)])

### パラメーターの更新
def update_param(state, action, param, reward, next_state):
    alpha = 0.0001
    gamma = 0.999
    q = q_func(state, action, param)
    q_n = max([q_func(next_state, a, param) for a in range(2)])
    delta = reward + gamma * q_n - q

    #norm = [2.4, 3.0, 1.0, 2.5]
    norm = [1000, 3.0, 0.3, 1.5]
    return [[param[a][i] + alpha*delta*state[i]/norm[i]*int(a==action) for i in range(4)] for a in range(2)]

### epsilon-greedy方策
def get_action(next_state, epsilon, param):
    if epsilon <= np.random.uniform(0, 1):
        ### 基本は状態行動価値の高い行動を選ぶ
        if q_func(next_state, 1, param) > q_func(next_state, 0, param):
            return 1
        else:
            return 0
    else:
        ### 一定の割合(epsilone)で乱択する
        return np.random.choice([0, 1])



### CartPole用Enviromentの作成
env = gym.make('CartPole-v0')
#env = gym.make('CartPole-v1')
env._max_episode_steps = 10000 # 最大試行回数を設定

### seedの設定
env.seed(0) # envのseed
np.random.seed(1) # numpyのseed

n_epi = 1000
n_step = 10000

### paramの初期値
#param = np.random.uniform(low=-0.00001, high=0.00001, size=(2, 4)) # ランダム
param = np.zeros(shape=(2,4)) # zero
# 特定の値
# param = [[-0.06643713334085179, -1.602993897172896, -0.02137015668456138, 0.1077168262194545],
#         [0.3464814174808494, -1.501606929237508, 0.07623286207376416, 0.23174167706001064]]

is_draw = True
res = []

for epi in range(n_epi):
    ### init
    ob = env.reset()

    for step in range(n_step): # 特定のステップ数で終わらせたい場合
    #while True: # 終状態までやる場合
        ### 状態の描画
        #env.render()

        ### Q関数に基づくepsilon-greedy方策に従い行動を決定する
        action = get_action(ob, 0.2, param)

        ### 実際に行動し，状態と報酬とdoneフラグを得る
        ob_n, reward, done, _ = env.step(action) # q-learning

        ### 独自の報酬の設定
        #reward = step / 100

        # if done:
        #     if step < 195:
        #         reward = -2  #こけたら罰則
        #     # elif step < 220:
        #     #     reward = -150
        #     else:
        #         reward = 2  #立ったまま終了時は罰則はなし
        # else:
        #     reward = 1  #各ステップで立ってたら報酬追加

        ### Q関数のパラメーター更新
        param = update_param(ob, action, param, reward, ob_n)

        ob = ob_n
        if done:
            ### 終状態になったら
            print('EPI{:4d} : done at t={:3d} (q={})'.format(epi, step, q_func(ob, action, param)))
            res.append(step)
            break


### グラフ出力
# plt.ylim(0,1000)
# #plt.plot(res)
# n_sample = 100
# plt.plot([np.mean(res[i:i+n_sample]) for i in range(len(res)-n_sample)])

print(param[0])
print(param[1])

if is_draw:
    ### 最終的なモデルによるエピソードの描画
    ob = env.reset()
    action_list = []

    for step in range(n_step):
        env.render()
        #print(ob)
        ### epsilon-greedy方策に従い行動を決定する
        action = get_action(ob, 0.0, param) # 乱択なし
        #action = get_action(ob, epi, 0.2, param) # 乱択あり
        action_list.append(action)
        ### 実際に行動する
        ob, reward, done, _ = env.step(action) # q-learning
        if done:
            ###
            print('DONE at t={}'.format(step))
            print(action_list[-20:])
            break

### 最後には環境を閉じる
env.close()
