import requests
import json
# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
# Save the JSON response to a file
with open('weather.json', 'w') as f:
    output_json = json.dumps(result.json(), indent=4, sort_keys=True)
    f.write(output_json)
result_dict = json.loads(result.text) #parse the json string into a dict object
print(result.status_code)
print(result_dict["humidity"])
#print(result_dict["humidity"]["data"][0])
#print(result_dict["humidity"]["data"][0]["value"])

# Print the humidity value
print(f"The humidity is {result_dict['humidity']['data'][0]['value']}%")
# 输出所有城市温度和湿度
for city in result_dict['temperature']['data']:
    print(f"City: {city['place']}, Temperature: {city['value']}°C") 