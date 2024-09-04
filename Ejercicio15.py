def convert_min_to_hr(minutes):
  hours = minutes // 60
  minutes_left = minutes % 60
  return hours, minutes_left

minutes = int(input("Enter minutes: "))
hours, minutes_left = convert_min_to_hr(minutes)

print(f"{minutes} is equal to {hours} hour(S) and {minutes_left} minute(s)")