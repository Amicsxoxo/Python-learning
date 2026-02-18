capitals = {
  "France" : "Paris",
  "Germany" : "Berlin",
}

#Nesting a list in a dictionary

travel_log ={
  "France": {"cities_visited" : ["Paris" , "Lille" , "Dijon"], "totatl_visit" : 12,},
  "Germany" : {"cities_visited" : ["Berlin", "Hamburg" , "Stuttgart"] , "total_visit" : 23},
}

#Nesting a list in a list

letters = ["A" , "B" , ["C" , "D"]]

#Nesting a dictionary in a list

travel_log = [
  {
    "country" : "France",
    "cities_visited" : ["Paris" , "Lille" , "Dijon"],
    "totatl_visit" : 12
  },
  {
    "country" : "Germany",
    "cities_visited" : ["Berlin", "Hamburg" , "Stuttgart"] ,
    "total_visit" : 23
  },
]