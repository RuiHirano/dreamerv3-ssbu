from libultimate import Button, UltimateClient
from enum import Enum
import gym
import time
import threading
import cv2
import random
import numpy as np

class EnvAction(Enum):
    NONE = {"name": "NONE", "input": {"buttons": [], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    JAB = {"name": "JAB", "input": {"buttons": [Button.A], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    TILT_U = {"name": "TILT_U", "input": {"buttons": [Button.A], "main_stick": (0, 0.5), "c_stick": (0, 0), "hold": False}}
    TILT_L = {"name": "TILT_L", "input": {"buttons": [Button.A], "main_stick": (-0.5, 0), "c_stick": (0, 0), "hold": False}}
    TILT_D = {"name": "TILT_D", "input": {"buttons": [Button.A], "main_stick": (0, -0.5), "c_stick": (0, 0), "hold": False}}
    TILT_R = {"name": "TILT_R", "input": {"buttons": [Button.A], "main_stick": (0.5, 0), "c_stick": (0, 0), "hold": False}}
    SMASH_U = {"name": "SMASH_U", "input": {"buttons": [Button.A], "main_stick": (0, 1), "c_stick": (0, 0), "hold": False}}
    SMASH_L = {"name": "SMASH_L", "input": {"buttons": [Button.A], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    SMASH_D = {"name": "SMASH_D", "input": {"buttons": [Button.A], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    SMASH_R = {"name": "SMASH_R", "input": {"buttons": [Button.A], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_N = {"name": "SPECIAL_N", "input": {"buttons": [Button.B], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_UL = {"name": "SPECIAL_UL", "input": {"buttons": [Button.B], "main_stick": (-1, 1), "c_stick": (0, 0), "hold": True}}
    SPECIAL_UR = {"name": "SPECIAL_UR", "input": {"buttons": [Button.B], "main_stick": (1, 1), "c_stick": (0, 0), "hold": True}}
    SPECIAL_L = {"name": "SPECIAL_L", "input": {"buttons": [Button.B], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    SPECIAL_D = {"name": "SPECIAL_D", "input": {"buttons": [Button.B], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    SPECIAL_R = {"name": "SPECIAL_R", "input": {"buttons": [Button.B], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    SPOT_DODGE = {"name": "SPOT_DODGE", "input": {"buttons": [Button.ZR], "main_stick": (0, -1), "c_stick": (0, 0), "hold": False}}
    ROLL_L = {"name": "ROLL_L", "input": {"buttons": [Button.ZR], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": False}}
    ROLL_R = {"name": "ROLL_R", "input": {"buttons": [Button.ZR], "main_stick": (1, 0), "c_stick": (0, 0), "hold": False}}
    JUMP = {"name": "JUMP", "input": {"buttons": [Button.X], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    JUMP_L = {"name": "JUMP_L", "input": {"buttons": [Button.X], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    JUMP_R = {"name": "JUMP_R", "input": {"buttons": [Button.X], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP = {"name": "SHORT_HOP", "input": {"buttons": [Button.X, Button.Y], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP_L = {"name": "SHORT_HOP_L", "input": {"buttons": [Button.X, Button.Y], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    SHORT_HOP_R = {"name": "SHORT_HOP_R", "input": {"buttons": [Button.X, Button.Y], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    WALK_L = {"name": "WALK_L", "input": {"buttons": [], "main_stick": (-0.5, 0), "c_stick": (0, 0), "hold": True}}
    WALK_R = {"name": "WALK_R", "input": {"buttons": [], "main_stick": (0.5, 0), "c_stick": (0, 0), "hold": True}}
    DASH_L = {"name": "DASH_L", "input": {"buttons": [], "main_stick": (-1, 0), "c_stick": (0, 0), "hold": True}}
    DASH_R = {"name": "DASH_R", "input": {"buttons": [], "main_stick": (1, 0), "c_stick": (0, 0), "hold": True}}
    GUARD = {"name": "GUARD", "input": {"buttons": [Button.ZR], "main_stick": (0, 0), "c_stick": (0, 0), "hold": True}}
    GRAB = {"name": "GRAB", "input": {"buttons": [Button.L], "main_stick": (0, 0), "c_stick": (0, 0), "hold": False}}
    
    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

class UltimateEnv(gym.Env):
    def __init__(self, server_url="http://localhost:8008", fps=10, image_size=(256, 256), disable_percent_reset=False, obs_key='image'):
        super().__init__()
        self.action_space = gym.spaces.Discrete(len(EnvAction))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(image_size[1], image_size[0], 3), dtype=np.uint8)
        self.fps = fps
        self.image_size = image_size
        self.disable_percent_reset = disable_percent_reset
        self.client = UltimateClient(server_url)
        self.client.add_controller(0)
        self.obs_key = obs_key # 'image' or 'vector'
        self.gamestate = None
        self.prev_gamestate = None
        self.dead = {0: False, 1: False}
        self.reward = 0
        self.done = False

    def __enter__(self):
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._stream_gamestate)
        self.thread.start()
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("[libultimate] Stopping stream...")
        self.stop_event.set()
        cv2.destroyAllWindows()
        self.client.input(0)
        time.sleep(1)

    def _stream_gamestate(self):
        for gamestate in self.client.stream(fps=self.fps*2, include_image=self.obs_key=='image', image_size=self.image_size):
            self.prev_gamestate = self.gamestate
            self.gamestate = gamestate
            if self.gamestate.players[0].fighter_status_kind != 470 and self.prev_gamestate and self.prev_gamestate.players[0].fighter_status_kind == 470:
                self.dead[0] = True
            if self.gamestate.players[1].fighter_status_kind != 470 and self.prev_gamestate and self.prev_gamestate.players[1].fighter_status_kind == 470:
                self.dead[1] = True
            self.done = self._done()
            self.reward = self._reward(self.reward, self.done, self.gamestate, self.prev_gamestate)
            if self.stop_event.is_set():
                break
            
    def _convert_player_state_to_vector(self, player_state):
        return [
            player_state.position.x/242,
            player_state.position.y/146,
            player_state.lr,
            player_state.percent/150,
            player_state.speed.x/2.5,
            player_state.speed.y/2.5,
            player_state.controller_state.stick_x,
            player_state.controller_state.stick_y,
            int(player_state.situation_kind == 0), # on_ground
            int(player_state.situation_kind == 1), # on_cliff
            int(player_state.situation_kind == 2), # on_air
            int(player_state.fighter_status_kind == 0), # wait
            int(player_state.fighter_status_kind == 1), # walk
            int(player_state.fighter_status_kind == 3), # dash_start
            int(player_state.fighter_status_kind == 4), # dash
            int(player_state.fighter_status_kind == 5), # dash_end
            int(player_state.fighter_status_kind == 7), # turn
            int(player_state.fighter_status_kind == 8), # turn_dash
            int(player_state.fighter_status_kind == 11), # jump
            int(player_state.fighter_status_kind == 12), # jump_aer
            int(player_state.fighter_status_kind == 16), # cannot_action
            int(player_state.fighter_status_kind == 18), # crouch
            int(player_state.fighter_status_kind == 22), # landing
            int(player_state.fighter_status_kind == 23), # landing_short
            int(player_state.fighter_status_kind == 27), # guard_start
            int(player_state.fighter_status_kind == 28), # guard
            int(player_state.fighter_status_kind == 29), # guard_end
            int(player_state.fighter_status_kind == 31), # escape_neutral
            int(player_state.fighter_status_kind == 32), # escape_foward
            int(player_state.fighter_status_kind == 33), # escape_back
            int(player_state.fighter_status_kind == 34), # escape_air
            int(player_state.fighter_status_kind == 39), # attack_neutral
            int(player_state.fighter_status_kind == 41), # attack_dash
            int(player_state.fighter_status_kind == 42), # attack_side
            int(player_state.fighter_status_kind == 43), # attack_up
            int(player_state.fighter_status_kind == 44), # attack_down
            int(player_state.fighter_status_kind == 46), # smash_side_keep
            int(player_state.fighter_status_kind == 47), # smash_side
            int(player_state.fighter_status_kind == 49), # smash_down_keep
            int(player_state.fighter_status_kind == 50), # smash_down
            int(player_state.fighter_status_kind == 52), # smash_up_keep
            int(player_state.fighter_status_kind == 53), # smash_up
            int(player_state.fighter_status_kind == 54), # attack_air
            int(player_state.fighter_status_kind == 55), # grab
            int(player_state.fighter_status_kind == 60), # grab_wait
            int(player_state.fighter_status_kind == 61), # grab_attack
            int(player_state.fighter_status_kind == 62), # grab_cut
            int(player_state.fighter_status_kind == 64), # grab_throw
            int(player_state.fighter_status_kind == 66), # grabbed
            int(player_state.fighter_status_kind == 67), # grabbed_attack
            int(player_state.fighter_status_kind == 68), # grabbed_cut
            int(player_state.fighter_status_kind == 70), # grabbed_throw
            int(player_state.fighter_status_kind == 71), # damaged_not_fly
            int(player_state.fighter_status_kind == 72), # damaged_standing_fly
            int(player_state.fighter_status_kind == 73), # damaged_fall_fly
            int(player_state.fighter_status_kind == 80), # damaged_down_start
            int(player_state.fighter_status_kind == 83), # damaged_down
            int(player_state.fighter_status_kind == 87), # damaged_down_getup
            int(player_state.fighter_status_kind == 119), # cliff_catch
            int(player_state.fighter_status_kind == 120), # cliff_attack
            int(player_state.fighter_status_kind == 121), # cliff_climb
            int(player_state.fighter_status_kind == 122), # cliff_escape
            int(player_state.fighter_status_kind == 124), # cliff_jump
            int(player_state.fighter_status_kind == 127), # cliff_stegger
            int(player_state.fighter_status_kind == 476), # special_neutral
            int(player_state.fighter_status_kind == 477), # special_side
            int(player_state.fighter_status_kind == 478), # special_up
            int(player_state.fighter_status_kind == 481), # special_down
        ]

    def _gamestate_to_observation(self, gamestate):
        if self.obs_key == "vector":
            return np.array([
                self._convert_player_state_to_vector(gamestate.players[0]),
                self._convert_player_state_to_vector(gamestate.players[1]),
            ])
        return gamestate.image

    def reset(self):
        if not self.disable_percent_reset:
            self.client.input(0, [Button.L, Button.R, Button.A])
        observation = self._gamestate_to_observation(self.gamestate)
        self.client.input(0)
        time.sleep(1)
        self.dead = {0: False, 1: False}
        self.reward = 0
        self.done = False
        return observation

    def step(self, action_num: int):
        input = EnvAction[EnvAction.get_names()[action_num]].value["input"]
        self.client.input(0, input["buttons"], input["main_stick"], input["c_stick"], input["hold"])
        interval = 1/self.fps
        time.sleep(interval)
        observation = self._gamestate_to_observation(self.gamestate)
        info = {"state": self.gamestate}
        self.prev_gamestate = self.gamestate
        reward = self.reward
        self.reward = 0
        return observation, reward, self.done, info

    def render(self, mode='human', close=False):
        if self.obs_key == "image":
            cv2.imshow('camera' , self.gamestate.image)
            key =cv2.waitKey(10)
            if key == 27:
                raise KeyboardInterrupt
        elif self.obs_key == "vector":
            print(self.gamestate)

    def _done(self):
        return self.dead[0] or self.dead[1]

    def _reward(self, prev_reward, done, gamestate, prev_gamestate):
        if self.gamestate is None or self.prev_gamestate is None:
            return 0
        p1_diff_damage = gamestate.players[0].percent - prev_gamestate.players[0].percent
        p2_diff_damage = gamestate.players[1].percent - prev_gamestate.players[1].percent
        reward = prev_reward + (p2_diff_damage - p1_diff_damage)
        if done:
            if self.dead[0]:
                reward = -100
            if self.dead[1]:
                reward = 100
        return reward

if __name__ == "__main__":
    with UltimateEnv(server_url="http://localhost:8008", fps=10, obs_key="vector", image_size=(84, 84), disable_percent_reset=False) as env:
        episode = 1000
        for i in range(episode):
            print("episode: ", i)
            env.reset()
            done = False
            while not done:
                #env.render()
                random_action_num = np.random.randint(0, len(EnvAction))
                observation, reward, done, info = env.step(random_action_num)
                print(done, reward)