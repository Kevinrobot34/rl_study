import gym

### CartPole用のenviromentを作る
env = gym.make('CartPole-v0')
#env = gym.make('CartPole-v1') # max_episode_stepsが異なる．
#env._max_episode_steps = 10000 # 最大試行回数の変更

### seedの設定
env.seed(0) # envのseed
np.random.seed(1) # numpyのseed


n_epi = 10
for epi in range(n_epi):
    ### init
    ob = env.reset()
    total_reward = 0

    #for j in range(200): # 特定のステップ数で終わらせたい場合
    while True: # 終状態までやる場合
        ### 状態の描画
        env.render()

        ### 行動決定：ランダム
        action = env.action_space.sample()

        ### 実際に行動し，状態と報酬とdoneフラグを得る
        ob, reward, done, _ = env.step(action) # take a random action

        ### Reward
        total_reward += reward
        # print('reward: {}'.format(reward))
        # print('TOTreward: {}\n'.format(total_reward))

        if done:
            ### 終状態になったら
            print('-'*80)
            print('EPI {}'.format(epi))
            print('total-reward = {}'.format(total_reward))
            print('final-ob     = {}'.format(ob))

            break

### 最後には環境を閉じる
env.close()
