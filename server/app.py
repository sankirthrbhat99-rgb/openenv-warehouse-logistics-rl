from openenv.core.env_server import create_app
from warehouse_env.environment import WarehouseEnv
from warehouse_env.models import WarehouseAction, WarehouseObservation

app = create_app(WarehouseEnv, WarehouseAction, WarehouseObservation)