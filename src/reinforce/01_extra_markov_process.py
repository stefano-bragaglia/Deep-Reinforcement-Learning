import random

random.seed(42)


class Environment:

    def __init__(self, steps_left: int = 10):
        self.current_state = 0
        self.transformation_matrix = [[0.8, 0.2], [0.1, 0.3]]
        self.steps_left = steps_left

    def get_observation(self) -> list[float]:
        return self.transformation_matrix[self.current_state]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self) -> float:
        if self.is_done():
            raise Exception("Game is over")

        self.steps_left -= 1

        return random.random()


class Agent:

    def __init__(self):
        self.total_reward = []

    def step(self, env: Environment):
        current_obs = env.get_observation()
        reward = env.action()

        self.total_reward.append(reward)


if __name__ == '__main__':
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: [{", ".join(f"{r:.4f}" for r in agent.total_reward)}] ({sum(agent.total_reward):.4f})")
