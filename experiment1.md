## Stage
- Pict chat (Final destination)

## Charactor
- 1p: Mario
- 2p(cpu): Mario (Lv.9)

## Input Paramater
66 Paramater

| Index | Name                        | Num       | Category       | Description |
| ----- | --------------------------- | --------- | -------------- | ----------- |
| 0     | position_x                  | -242~+242 | location       |             |
| 1     | position_y                  | -146~+146 | location       |             |
| 2     | lr                          | -1,1      | location       |             |
| 3     | percent                     | 0~150     | damage         |             |
| 4     | speed_x                     | -2.5~+2.5 | speed          |             |
| 5     | speed_y                     | -2.5~+2.5 | speed          |             |
| 4     | stick_x                     | -1~1      | stick          |             |
| 5     | stick_y                     | -1~1      | stick          |             |
| 6     | situation_ground            | 0         | situation_kind |             |
| 7     | situation_cliff             | 1         | situation_kind |             |
| 8     | situation_air               | 2         | situation_kind |             |
| 9     | status_wait                 | 0         | status_kind    |             |
| 10    | status_walk                 | 1         | status_kind    |             |
| 11    | status_dash_start           | 3         | status_kind    |             |
| 12    | status_dash                 | 4         | status_kind    |             |
| 13    | status_dash_end             | 5         | status_kind    |             |
| 14    | status_turn                 | 7         | status_kind    |             |
| 15    | status_turn_dash            | 8         | status_kind    |             |
| 16    | status_jump                 | 11        | status_kind    |             |
| 17    | status_jump_aer             | 12        | status_kind    |             |
| 18    | status_cannot_action        | 16        | status_kind    |             |
| 19    | status_crouch               | 18        | status_kind    |             |
| 20    | status_landing              | 22        | status_kind    |             |
| 21    | status_landing_short        | 23        | status_kind    |             |
| 22    | status_guard_start          | 27        | status_kind    |             |
| 23    | status_guard                | 28        | status_kind    |             |
| 24    | status_guard_end            | 29        | status_kind    |             |
| 25    | status_escape_neutral       | 31        | status_kind    |             |
| 26    | status_escape_foward        | 32        | status_kind    |             |
| 26    | status_escape_back          | 33        | status_kind    |             |
| 28    | status_escape_air           | 34        | status_kind    |             |
| 29    | status_attack_neutral       | 39        | status_kind    |             |
| 30    | status_attack_dash          | 41        | status_kind    |             |
| 31    | status_attack_side          | 42        | status_kind    |             |
| 32    | status_attack_up            | 43        | status_kind    |             |
| 33    | status_attack_down          | 44        | status_kind    |             |
| 34    | status_smash_side_keep      | 46        | status_kind    |             |
| 35    | status_smash_side           | 47        | status_kind    |             |
| 36    | status_smash_down_keep      | 49        | status_kind    |             |
| 37    | status_smash_down           | 50        | status_kind    |             |
| 38    | status_smash_up_keep        | 52        | status_kind    |             |
| 39    | status_smash_up             | 53        | status_kind    |             |
| 40    | status_attack_air           | 54        | status_kind    |             |
| 41    | status_grab                 | 55        | status_kind    |             |
| 42    | status_grab_wait            | 60        | status_kind    |             |
| 43    | status_grab_attack          | 61        | status_kind    |             |
| 44    | status_grab_cut             | 62        | status_kind    |             |
| 45    | status_grab_throw           | 64        | status_kind    |             |
| 46    | status_grabbed              | 66        | status_kind    |             |
| 47    | status_grabbed_attack       | 67        | status_kind    |             |
| 48    | status_grabbed_cut          | 68        | status_kind    |             |
| 49    | status_grabbed_throw        | 70        | status_kind    |             |
| 50    | status_damaged_not_fly      | 71        | status_kind    |             |
| 51    | status_damaged_standing_fly | 72        | status_kind    |             |
| 52    | status_damaged_fall_fly     | 73        | status_kind    |             |
| 53    | status_damaged_down_start   | 80        | status_kind    |             |
| 54    | status_damaged_down         | 83        | status_kind    |             |
| 55    | status_damaged_down_getup   | 87        | status_kind    |             |
| 56    | status_cliff_catch          | 119       | status_kind    |             |
| 57    | status_cliff_attack         | 120       | status_kind    |             |
| 58    | status_cliff_climb          | 121       | status_kind    |             |
| 59    | status_cliff_escape         | 122       | status_kind    |             |
| 60    | status_cliff_jump           | 124       | status_kind    |             |
| 61    | status_cliff_stegger        | 127       | status_kind    |             |
| 62    | status_special_neutral      | 476       | status_kind    |             |
| 63    | status_special_side         | 477       | status_kind    |             |
| 64    | status_special_up           | 478       | status_kind    |             |
| 65    | status_special_down         | 481       | status_kind    |             |

## Output Actions
31 Output

| Index | Name             | Description |
| ----- | ---------------- | ----------- |
| 0     | none             |             |
| 1     | jab              |             |
| 2     | tilt_up          |             |
| 3     | tilt_left        |             |
| 4     | tilt_down        |             |
| 5     | tilt_right       |             |
| 6     | smash_up         |             |
| 7     | smash_left       |             |
| 8     | smash_down       |             |
| 9     | smash_right      |             |
| 10    | special_n        |             |
| 11    | special_up_left  |             |
| 12    | special_up_right |             |
| 13    | special_left     |             |
| 14    | special_down     |             |
| 15    | special_right    |             |
| 16    | spot_dodge       |             |
| 17    | roll_left        |             |
| 18    | roll_right       |             |
| 19    | jump             |             |
| 20    | jump_left        |             |
| 21    | jump_right       |             |
| 22    | short_jump       |             |
| 23    | short_jump_left  |             |
| 24    | short_jump_right |             |
| 25    | walk_left        |             |
| 26    | walk_right       |             |
| 27    | dash_left        |             |
| 28    | dash_right       |             |
| 29    | guard            |             |
| 30    | grab             |             |

```
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
    
```