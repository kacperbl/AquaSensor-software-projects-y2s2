from fastapi import FastAPI
from api_middleware.downstream_auth import auth_required
from api_middleware.models import HealthCheckResponse, SensorStatus, SensorStatusResponse, SensorReadingsResponse, SensorReadingsRequest

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

@app.get("{sensorid}/status", dependencies=[auth_required])
async def get_sensor_status_by_id(sensorid: str) -> SensorStatus:
    """Get sensor status by ID."""

@app.get("{sensorid}/readings", dependencies=[auth_required])
async def get_sensor_readings_by_id(sensorid: str, request: SensorReadingsRequest) -> SensorReadingsResponse:
    """Get sensor readings by ID."""

@app.get("{sensorid}/readings/latest", dependencies=[auth_required]) 
async def get_sensor_readings_latest_by_id(sensorid: str) -> SensorReadingsResponse:
    """Get latest sensor readings by ID."""
