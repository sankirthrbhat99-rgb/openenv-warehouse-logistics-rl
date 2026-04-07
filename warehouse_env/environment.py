import numpy as np
from openenv.core.env_server import Environment
from .models import WarehouseAction, WarehouseObservation

class WarehouseEnv(Environment):
    # 🔧 FIX: Global Class Variables! 
    # This prevents the server from wiping the state on every new HTTP request.
    agent_pos = [0, 0]
    package_pos = [9, 9]
    has_item = False
    steps = 0
    grid_size = 10

    def __init__(self):
        super().__init__()
        # 🔧 REMOVED self.reset() from here so it doesn't wipe state on every move!

    def reset(self):
        # This is only called when the inference script explicitly hits the /reset endpoint
        WarehouseEnv.agent_pos = [0, 0]
        WarehouseEnv.package_pos = [9, 9]
        WarehouseEnv.has_item = False
        WarehouseEnv.steps = 0
        return self._get_obs(reward=0.0, done=False)

    def state(self):
        return self._get_obs(reward=0.0, done=False)

    def _get_obs(self, reward: float = 0.0, done: bool = False):
        return WarehouseObservation(
            current_position=WarehouseEnv.agent_pos,
            has_item=WarehouseEnv.has_item,
            reward=reward,
            done=done
        )

    def step(self, action: WarehouseAction):
        WarehouseEnv.steps += 1
        x, y = WarehouseEnv.agent_pos

        if action.action_type == 0 and y < WarehouseEnv.grid_size - 1: y += 1 # North
        elif action.action_type == 1 and y > 0: y -= 1              # South
        elif action.action_type == 2 and x < WarehouseEnv.grid_size - 1: x += 1 # East
        elif action.action_type == 3 and x > 0: x -= 1              # West
        elif action.action_type == 4:                               # Pick-up
            if x == WarehouseEnv.package_pos[0] and y == WarehouseEnv.package_pos[1]:
                WarehouseEnv.has_item = True

        WarehouseEnv.agent_pos = [x, y]
        
        if WarehouseEnv.has_item:
            reward = 1.0
        else:
            distance = abs(x - WarehouseEnv.package_pos[0]) + abs(y - WarehouseEnv.package_pos[1])
            max_distance = (WarehouseEnv.grid_size - 1) * 2
            reward = round((1 - (distance / max_distance)) * 0.9, 2)
            
        done = bool(WarehouseEnv.has_item or WarehouseEnv.steps >= 20)
        
        return self._get_obs(reward=reward, done=done)