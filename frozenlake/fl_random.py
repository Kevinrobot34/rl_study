import gym

### FrozenLake用のenviromentを作る
env = gym.make('FrozenLake-v0')


n_epi = 10
n_step = 200

for epi in range(n_epi):
    ### init
    ob = env.reset()
    total_reward = 0

    #for step in range(n_step): # 特定のステップ数で終わらせたい場合
    while True: # 週状態までやる場合
        ### 毎回状態を表示する
        env.render()
        #print('ob = {}'.format(ob))

        ### 行動決定：ランダム
        action = env.action_space.sample()

        ### 実際に行動して，状態と報酬とdoneフラグを得る
        ob, reward, done, _ = env.step(action) # take a random action

        ### Reward
        total_reward += reward
        # print('reward: {}'.format(reward))
        # print('TOTreward: {}\n'.format(total_reward))

        if done:
            ### 終状態になったら
            print('EPI {}'.format(epi))
            print('total-reward = {}'.format(total_reward))
            #print('final-ob     = {}'.format(ob))
            #print('-'*80)
            env.render()
            break

### 最後には環境を閉じる
env.close()
