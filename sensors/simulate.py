import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Create folder if not exists
os.makedirs('data/sensor_data', exist_ok=True)

print("🌱 Generating Brinjal Farm Sensor Data...")

# Generate 30 days of hourly data
dates = []
soil_moisture = []
temperature = []
humidity = []
rainfall = []

start_date = datetime(2026, 1, 1)

for i in range(30 * 24):  # 30 days x 24 hours
    current_time = start_date + timedelta(hours=i)
    hour = current_time.hour
    dates.append(current_time)

    # Soil moisture — drops during day, rises after rain
    moisture = round(random.uniform(25, 85), 2)
    soil_moisture.append(moisture)

    # Temperature — higher during day, lower at night
    if 6 <= hour <= 18:
        temp = round(random.uniform(28, 38), 2)
    else:
        temp = round(random.uniform(18, 27), 2)
    temperature.append(temp)

    # Humidity — higher at night
    if 6 <= hour <= 18:
        hum = round(random.uniform(45, 70), 2)
    else:
        hum = round(random.uniform(65, 90), 2)
    humidity.append(hum)

    # Rainfall — random occasional rain
    rain = round(random.uniform(0, 20), 2) if random.random() < 0.1 else 0
    rainfall.append(rain)

# Save to CSV
df = pd.DataFrame({
    'timestamp': dates,
    'soil_moisture_%': soil_moisture,
    'temperature_C': temperature,
    'humidity_%': humidity,
    'rainfall_mm': rainfall
})

df.to_csv('data/sensor_data/farm_readings.csv', index=False)

print("=" * 45)
print("  ✅ Sensor Data Generated Successfully!")
print("=" * 45)
print(f"📊 Total rows     : {len(df)}")
print(f"📅 Days covered   : 30 days")
print(f"⏰ Readings/day   : 24 per hour")
print(f"💧 Avg moisture   : {df['soil_moisture_%'].mean():.1f}%")
print(f"🌡️ Avg temperature: {df['temperature_C'].mean():.1f}°C")
print(f"💦 Avg humidity   : {df['humidity_%'].mean():.1f}%")
print("=" * 45)
print(df.head(5))