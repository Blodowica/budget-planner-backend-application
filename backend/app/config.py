import os


class Settings:
    app_name: str = os.getenv("APP_NAME", "Budget Planner API")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
