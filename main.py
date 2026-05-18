import subprocess
import sys

steps = [
    "fetch_weather.py",
    "clean_weather.py",
    "load_to_mysql.py",
    "weather_analysis.py",
]

for script in steps:
    print(f"\n Running {script}...")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f" {script} failed. Stopping pipeline.")
        sys.exit(1)

print("\n Pipeline complete.")
