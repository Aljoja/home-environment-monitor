from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Measurement():

    device_id: str
    timestamp: datetime = field(
        default_factory=lambda: datetime.now().astimezone()
    )
    temperature_c: float = 21.5
    pressure_hpa: float = 1013.25
    humidity_pct: float = 47.0
    def __str__(self) -> str:
        time = self.timestamp.strftime("%Y-%m-%d %H:%M:%S %z")
        return (
            f"[{time}] {self.device_id}: "
            f"{self.temperature_c:.1f} °C, "
            f"{self.pressure_hpa:.2f} hPa, "
            f"{self.humidity_pct:.1f}% RH"
        )

    def __post_init__(self) -> None:
        if not isinstance(self.device_id, str) or not self.device_id.strip():
            raise ValueError("device_id must be a non-empty string")

        if not 0 <= self.humidity_pct <= 100:
            raise ValueError("humidity must be between 0 and 100%")

        if not isinstance(self.pressure_hpa, (int, float)):
            raise ValueError("pressure must be a number")

        if not -20 <= self.temperature_c <= 60:
            raise ValueError("temperature must be between -20 and 60 °C")