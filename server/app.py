from openenv.core.env_server import create_app
from warehouse_env.environment import WarehouseEnv
from warehouse_env.models import WarehouseAction, WarehouseObservation

# This creates your environment app
app = create_app(WarehouseEnv, WarehouseAction, WarehouseObservation)

# This is the specific function the validator is looking for
def main():
    import uvicorn
    # This tells uvicorn to run the 'app' object we created above
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
