#Dictionaries --to group together with jkey and value pair
#{key: value} --syntax


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
   
}
#how to retrive them:
print(programming_dictionary ["Bug"]) #the value will be printed

#add data
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create empty dictionary
empty_dictionary = {}

#wipe an existing dictionary 
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"]= "It is the name of sheep in amharic"
print(programming_dictionary["Bug"])

#Loop through a dictionary
#dictionaries acessed by their key
for key in programming_dictionary:
    print(key) #we only get the keys 
    print(programming_dictionary[key]) #to get the values

            #-----------------Exerise--------------#
student_scores = {
    "Harry": 81,
    "Selam": 78,
    "Ron": 99,
    "Dave": 74,
    "Nina": 62,
}
student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
         student_grades[key] = "Exceeds Expectations"#add to the dictionary
    elif score >= 71:
         student_grades[key] = "Acceptable"
    else:
         student_grades[key] = "Fail"

print(student_grades)

#nesting
#1 Nesting list in a dictionary 
travel_loggss = {
     "France": ["subcity1", "subcity2", "subcity3"]
}

#2 Nesting dictionary in a dictionary 
travel_logs = {
     "France": {
          "city_visited": ["city1","city2","city3"],
          "toatl_visit": 12,
     },

     "Ethiopia": {
          "city_visited": ["city1","city2","city3"],
          "toatl_visit": 4,
     }
}
#3 Nesting dictionary in a list
travels = [
     {
          "country": "Ethiopia", 
          "cities_visited": ["city1","city2","city3"],
           "toatl_visit": 4,
     },
      {
          "country": "Germany", 
          "cities_visited": ["city1","city2","city3"],
           "toatl_visit": 4,
     }
]
#-------------------Exerecise-----------------------#

travel_log = [
     {
          "country": "France", 
          "visitis": 12,
          "cities_visited": ["city1","city2","city3"],
           
     },
      {
          "country": "Germany", 
          "visitis": 5,
          "cities_visited": ["city1","city2","city3"],
          
      }
]
#so we need to add a new dictionary right so we need empty dictionary
def add_new_country(country, visitis,cities_visited):
     new_country = {}
     new_country["country"] = country
     new_country["visitis"] = visitis
     new_country["cities_visited"] = cities_visited
     travel_log.append(new_country)




add_new_country("Russia", 2 , ["Moscow", "Saint"])
print(travel_log)
   

