import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA


def get_temperature_from_time(data_set_path, time_arg):
    data = pd.read_csv(data_set_path)
    time = data["Time"]
    temperature = data["Temperature"]
    time_format = " %I:%M:%S %p"  # Format for hours:minutes:seconds AM/PM

    dt1 = datetime.strptime(time[1], time_format)
    dt2 = datetime.strptime(time[0], time_format)

    time_difference = dt2-dt1

    last_time_stamp = datetime.strptime(data["Time"].iloc[-1], time_format)
    time_arg = datetime.strptime(time_arg, time_format)

    print(last_time_stamp-time_arg)

    model = ARIMA(temperature, order=(1, 1, 1))  # Change parameters based on your analysis

    model_fit = model.fit()
    future_periods = 10
    future_predictions = model_fit.forecast(steps=future_periods)


get_temperature_from_time("data/temperature-sensor-data.csv", " 1:50:00 PM")

