import pandas as pd
def process_weather_data(raw_data):
    if 'error' in raw_data:
      return raw_data
    
    processed_data= {
       'City':raw_data['name'],
       'Temperature':raw_data['main']['temp'],
       'Humidity':raw_data['main']['humidity'],
       'Weather':raw_data['weather'][0]['description']

    }
    df =pd.DataFrame([processed_data])
    df.fillna('unknown',inplace=True)
    
    df.to_csv("output.csv", index=False)

    return df.to_dict(orient='records')  # Returns a list of dictionaries
    