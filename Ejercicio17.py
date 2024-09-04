#Mi to Km

def convert_m_to_km(mi):
  km = mi * 1.60934
  return km

mi = float(input("Enter a distance in miles: "))

km = convert_m_to_km(mi)

print(f"{mi} mi is equal to {km} km")

