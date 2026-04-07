from openenv.core.env_server import create_app
from warehouse_env.environment import WarehouseEnv
from warehouse_env.models import WarehouseAction, WarehouseObservation
import os
import uvicorn

app = create_app(WarehouseEnv)

# This ensures the server uses the port Scaler assigns it during validation
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    # Note: the "app:app" part assumes your FastAPI variable is named 'app'
    # inside this app.py file.
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)