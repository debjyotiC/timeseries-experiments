import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data = pd.read_csv('data/temperature-sensor-data.csv')

time = data["Time"]
temperature = data["Temperature"]

model = ARIMA(temperature, order=(1, 1, 1))  # Change parameters based on your analysis

# Fit the model
model_fit = model.fit()

# Predict future values
future_periods = 10  # Change this to the number of periods to predict
future_predictions = model_fit.forecast(steps=future_periods)

# Print the predicted values
print(future_predictions)


plt.plot(time, temperature, label='Actual')
plt.plot(future_predictions, color='red', label='Predicted')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Prediction with ARIMA')
plt.legend()
plt.show()