import pandas as pd
import os


class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time

    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print(f"Warning: Flight {self.flight_num} is moderately delayed ({self.delay_time} mins)")
        elif self.delay_time > 60:
            print(f"SEVERE: Flight {self.flight_num} is heavily delayed ({self.delay_time} mins)")
        else:
            print(f"Flight {self.flight_num} is on time")



df = pd.read_csv("arrivals.csv")


df["Minutes_Delayed"] = df["Minutes_Delayed"].fillna(0)



delayed_df = df[df["Minutes_Delayed"] > 30]


most_delayed = delayed_df.sort_values(by="Minutes_Delayed", ascending=False).iloc[0]

flight_obj = Flight(
    most_delayed["Flight_Number"],
    most_delayed["Minutes_Delayed"]
)

flight_obj.check_severity()



new_log = pd.DataFrame([{
    "Flight_Number": most_delayed["Flight_Number"],
    "Airline": most_delayed["Airline"],
    "Minutes_Delayed": most_delayed["Minutes_Delayed"]
}])


if os.path.exists("severe_delays_log.csv"):
    old_log = pd.read_csv("severe_delays_log.csv")
    updated_log = pd.concat([old_log, new_log], ignore_index=True)
else:
    updated_log = new_log

updated_log.to_csv("severe_delays_log.csv", index=False)

print("Log updated successfully!")