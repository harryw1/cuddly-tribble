import pandas as pd
import numpy as np
import datetime

def create_sample_weather_dataset(num_samples=20):
    """
    Generates a sample weather dataset mimicking the structure of weather_honolulu.csv.

    Args:
        num_samples (int): The number of sample data points to generate.

    Returns:
        pandas.DataFrame: A DataFrame containing the sample weather dataset.
    """
    # Set a seed for reproducibility
    np.random.seed(42)

    # Generate dates for a sample period
    start_date = datetime.date(2023, 1, 1)
    dates = [start_date + datetime.timedelta(days=i) for i in range(num_samples)]

    # Honolulu approximate latitude and longitude
    honolulu_latitude = 21.3069
    honolulu_longitude = -157.8583

    # Generate data for each field
    data = {
        "date": dates,
        "latitude": np.random.uniform(honolulu_latitude - 0.1, honolulu_latitude + 0.1, num_samples), # Latitude around Honolulu
        "longitude": np.random.uniform(honolulu_longitude - 0.1, honolulu_longitude + 0.1, num_samples), # Longitude around Honolulu
        "zipcode": [f"968{np.random.randint(10, 100)}" for _ in range(num_samples)], # Honolulu zip codes start with 968
        "average_precipitation": np.random.uniform(0, 0.5, num_samples), # Average precipitation in inches (example range)
        "average_temperature": np.random.uniform(70, 85, num_samples), # Average temperature in Fahrenheit (example range for Honolulu)
        "minimum_temperature": np.random.uniform(65, 75, num_samples), # Minimum temperature in Fahrenheit
        "maximum_temperature": np.random.uniform(80, 90, num_samples)  # Maximum temperature in Fahrenheit
    }

    # Ensure minimum <= average <= maximum temperature
    for i in range(num_samples):
        min_temp = data["minimum_temperature"][i]
        max_temp = data["maximum_temperature"][i]
        if data["average_temperature"][i] < min_temp:
            data["average_temperature"][i] = min_temp + np.random.uniform(0, 5)
        if data["average_temperature"][i] > max_temp:
            data["average_temperature"][i] = max_temp - np.random.uniform(0, 5)
        if data["minimum_temperature"][i] > data["average_temperature"][i]:
            data["minimum_temperature"][i] = data["average_temperature"][i] - np.random.uniform(0, 5)
        if data["maximum_temperature"][i] < data["average_temperature"][i]:
            data["maximum_temperature"][i] = data["average_temperature"][i] + np.random.uniform(0, 5)


    df_sample = pd.DataFrame(data)
    return df_sample

# Create the sample dataset
sample_df = create_sample_weather_dataset()
print(sample_df.head())

# To save to CSV (optional)
sample_df.to_csv("weather_maui.csv", index=False)