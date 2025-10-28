import random

random.seed(42)


class Environment:

    def __init__(self, steps_left: int = 10):
        self.steps_left = steps_left

    def get_observation(self) -> list[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> list[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")

        self.steps_left -= 1

        return random.random()


class Agent:

    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Environment):
        current_obs = env.get_observation()
        actions = env.get_actions()
        selected_action = random.choice(actions)
        reward = env.action(selected_action)

        self.total_reward += reward


if __name__ == '__main__':
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: {agent.total_reward:.4f}")
