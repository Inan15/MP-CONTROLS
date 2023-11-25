import time
import gym
env = gym.make('CartPole-v1')

a = 0
a_step = 0.01
num = 0
vTip = 0


obs = env.reset()
for j in range(600):
    # TODO SET ACTION

    obs, rew, done, info = env.step(0 if a > 0 else 1)  # REPLACE WITH ACTIONS
    env.render()
    # print(obs)
    vTip = obs[-1]
    pos = obs[0]
    theta = obs[2]

    print("V", vTip, "POS", pos, "ANG", theta)

    a = a - a_step if vTip > 0 else a + a_step

    if pos < -4 or pos > 4:
        break

    print("A", a)
    time.sleep(0.01)

env.close()
