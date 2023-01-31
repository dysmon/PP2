# Dictionary is a collection which is ordered** and changeable. No duplicate members.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# Mustang

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['year'] = 2020
#"year": 2020 overwrite "year": 1964

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red" 
#adding key/value

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
# empty 'car'

