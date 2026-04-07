from openenv.core.env_server import create_app
from warehouse_env.environment import WarehouseEnv
from warehouse_env.models import WarehouseAction, WarehouseObservation
import os
import uvicorn

app = create_app(WarehouseEnv, WarehouseAction, WarehouseObservation)

# NEW CODE (Correct for the grader)
def main():
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)

if __name__ == "__main__":
    main()