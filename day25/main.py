import os
import csv
import pandas

script_dir = os.path.dirname(__file__)

with open(script_dir + "/data/weather_data.csv") as week_weather:
    print("DONE WITH I/O LIB:")
    for day_w in week_weather.readlines():
        day_deconstruted = day_w.split(",")
        if day_deconstruted[0] != "day":
            print(f"For {day_deconstruted[0]}, the temp will be around {day_deconstruted[1]} with {day_deconstruted[2]}")
        
    week_weather.seek(0)
    print("\nDONE WITH CSV LIB:")
    csv_week_weather = csv.reader(week_weather)
    for row in csv_week_weather:
        if row[0] != "day":
            print(f"For {row[0]}, the temp will be around {row[1]} with {row[2]}\n")
            
    
    
print("\nDONE WITH CSV PANDAS:")
csv_pandas_week_weather = pandas.read_csv(script_dir + "/data/squirrels.csv")
sq_b = csv_pandas_week_weather[csv_pandas_week_weather["Primary Fur Color"] == "Black"]
sq_c = csv_pandas_week_weather[csv_pandas_week_weather["Primary Fur Color"] == "Cinnamon"]
sq_g = csv_pandas_week_weather[csv_pandas_week_weather["Primary Fur Color"] == "Gray"]
final_sq_data = {
    "Fur Color": ["grey","red","black"],
    "Count": [len(sq_g), len(sq_c), len(sq_b)]
}

df = pandas.DataFrame(final_sq_data)
df.to_csv(script_dir + "/data/squirrels_counts.csv")

print(f"Black squirrels are: {len(sq_b)}\nCinnamon squirrels are: {len(sq_c)}\nGray squirrels are: {len(sq_g)}")
    
    
    