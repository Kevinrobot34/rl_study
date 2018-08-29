import math
import gym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
#matplotlib inline

### binを作る
def create_bins(clip_min, clip_max, num):
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

### 各値を離散値に変換
def digitize_state(observation, num_digitized=6):
    cart_pos, cart_v, pole_angle, pole_v = observation
    digitized = [
        np.digitize(cart_pos, bins=create_bins(-2.4, 2.4, num_digitized)),
        np.digitize(cart_v, bins=create_bins(-3.0, 3.0, num_digitized)),
        np.digitize(pole_angle, bins=create_bins(-0.21, 0.21, num_digitized)),
        np.digitize(pole_v, bins=create_bins(-2.0, 2.0, num_digitized))
    ]
    return sum([x * (num_digitized**i) for i, x in enumerate(digitized)])

### 方策
def get_action(state, epsilon):
    if epsilon <= np.random.uniform(0, 1):
        action = np.argmax(q_table[state])
    else:
        action = np.random.choice([0, 1])
    return action

### Q-tableの更新
def update_Qtable(q_table, state, action, reward, next_state):
    alpha = 0.3
    gamma = 0.99
    next_Max_Q = max(q_table[next_state][0], q_table[next_state][1])
    q_table[state, action] = (1-alpha) * q_table[state, action] + alpha * (reward + gamma * next_Max_Q)

    return q_table


### CartPole用Enviromentの作成
#env = gym.make('CartPole-v0')
env = gym.make('CartPole-v1')
env._max_episode_steps = 10000 # 最大試行回数を設定

### seedの設定
env.seed(0) # envのseed
np.random.seed(1) # agentのseed

n_epi = 1000
n_step = 10000
n_dig = 6
q_table = np.random.uniform(low=-1, high=1, size=(n_dig**4, env.action_space.n))
#q_table = np.zeros((n_dig**4, env.action_space.n))

is_draw = True
res = []

for epi in range(n_epi):
    ### init
    ob = env.reset()

    for step in range(n_step): # 特定のステップ数で終わらせたい場合
    #while True: # 終状態までやる場合
        ### 状態の描画
        #env.render()

        ### 行動決定：Q-Learning
        ob_dig = digitize_state(ob, n_dig)
        action = get_action(ob_dig, 0.5* (1/(epi+1)))

        ### 実際に行動し，状態と報酬とdoneフラグを得る
        ob_n, reward, done, _ = env.step(action) # q-learning
        ob_n_dig = digitize_state(ob_n, n_dig)

        ### 報酬の設定
        # rewardはデフォルトで常に1
        if done:
            if step < 195:
                reward = -300  #失敗したら罰則
            # elif step < 220:
            #     reward = -150
        #print(ob, digitize_state(ob, 10), reward, done)

        ### Q-tableの更新
        q_table = update_Qtable(q_table, ob_dig, action, reward, ob_n_dig)

        ob = ob_n

        if done:
            ### 終状態になったら
            #print('EPI{} : done at t={} (state: {})'.format(epi, step, ob))
            print('EPI{} : done at t={}'.format(epi, step))
            res.append(step)
            break

#display_frames_as_gif(frames)

### グラフ出力
# plt.ylim(0,1000)
# #plt.plot(res)
# n_sample = 100
# plt.plot([np.mean(res[i:i+n_sample]) for i in range(len(res)-n_sample)])


if is_draw:
    ob = env.reset()

    for step in range(n_step):
        env.render()
        ### 方策に従い行動を決定
        action = get_action(digitize_state(ob, n_dig), 0.0)
        ### 実際に行動する
        ob_n, reward, done, _ = env.step(action) # q-learning

        ob = ob_n

        if done:
            ###
            print('DONE at t={}'.format(step))
            break


env.close()
