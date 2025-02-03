from fastapi import FastAPI
from api_middleware.downstream_auth import auth_required
from api_middleware.models import HealthCheckResponse, SensorStatus, SensorStatusResponse, SensorReadingsResponse, SensorReadingsRequest
from api_middleware.functions import get_status, get_status_by_id

app = FastAPI(
    title="API Middleware",
    description="API for retrieving sensor status and readings from AquaSensor.",
)

@app.get("/health")
async def get_health() -> HealthCheckResponse:
    """Health check endpoint."""
    return HealthCheckResponse(status="OK")

@app.get("/status", dependencies=[auth_required])
async def get_sensor_status() -> SensorStatusResponse:
    """Get sensor status."""

    return await get_status()

@app.get("/sensors/{sensorid}/status", dependencies=[auth_required])
async def get_sensor_status_by_id(sensorid: str) -> SensorStatus:
    """Get sensor status by ID."""

    return await get_status_by_id(sensorid)

@app.get("/sensors/{sensorid}/readings", dependencies=[auth_required])
async def get_sensor_readings_by_id(sensorid: str, request: SensorReadingsRequest) -> SensorReadingsResponse:
    """Get sensor readings by ID."""

@app.get("/sensors/{sensorid}/readings/latest", dependencies=[auth_required]) 
async def get_sensor_readings_latest_by_id(sensorid: str) -> SensorStatus:
    """Get latest sensor readings by ID."""

    return await get_status_by_id(sensorid)
