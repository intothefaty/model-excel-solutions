import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import models_excels.models.take_dataframe as td

def take_reg_pred():
    # Load the newly uploaded Excel file
    data = td.take_ronaldo()
    
    # Assuming the dataset structure is similar, remove non-relevant columns if present
    # If the structure has changed, adjust the column names to be removed or the logic accordingly
    # For example, if "Genel Toplam" and "(boş)" are still present and need to be excluded
    data = data.drop(columns=[col for col in data.columns if 'Genel Toplam' in col or '(boş)' in col], errors='ignore')
    
    # Creating a new DataFrame to hold all the forecasts
    combined_forecasts = pd.DataFrame(columns=data.columns)  # Initialize as DataFrame
    
    # Iterate over each row
    for i, row in data.iterrows():
        material_code = row['Row Labels']  # Ensure this column name matches the unique identifier in your dataset
        
        # Prepare the demand data (features) and dummy variables for all months
        all_months_columns = [col for col in data.columns if col != 'Row Labels']  # Adjust if the identifier has changed
        
        # Forecasting for each month separately in the next year
        for forecast_month in range(1, 13):  # Forecasting for all 12 months
            # Filter columns for the training data (excluding the last 12 months, adjust as needed)
            training_months_columns = all_months_columns[:-12]  # Adjust based on the forecasting needs
            
            # Prepare dummy variables for each month
            dummy_variables = np.array([1 if int(col[-2:]) == forecast_month else 0 for col in training_months_columns])
            
            demand_data = row[training_months_columns].values  # Get the demand data values for training
            
            # Fit the model
            model = LinearRegression()
            model.fit(dummy_variables.reshape(-1, 1), demand_data)
            
            # Forecast demand for the corresponding month
            forecast = model.predict(np.array([[1]]))
            
            # Format the month correctly for the forecast column name
            forecast_month_str = f'Ay_{forecast_month:02d}'  # Adjust the year if necessary
            
            # Add the regression results to the combined DataFrame
            combined_forecasts.loc[i, forecast_month_str] = forecast[0]
    
    return combined_forecasts


