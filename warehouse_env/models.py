from pydantic import Field
from openenv.core.env_server import Action, Observation

class WarehouseAction(Action):
    action_type: int = Field(..., description="0:North, 1:South, 2:East, 3:West, 4:Pick-up")

class WarehouseObservation(Observation):
    current_position: list[int] = Field(default=[0,0], description="[x, y] coordinates")
    has_item: bool = Field(default=False, description="Whether the agent is carrying a package")