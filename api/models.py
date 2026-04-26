from pydantic import BaseModel, Field

class HardwareSpecs(BaseModel):
    gpu_model:    str = Field("RTX 3060", description="Graphics card model", example="RTX 4090")
    vram_gb:      int = Field(12, description="GPU VRAM in GB", ge=0, example=24)
    ram_gb:       int = Field(16, description="System RAM in GB", ge=2, example=64)
    cpu_cores:    int = Field(8, description="CPU physical cores", ge=1, example=16)
    target_goal:  str = Field("AI", description="Target use case: AI | Gaming", example="AI")
