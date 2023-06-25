class India:
    def capital(self):
        print("New Delhi is capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language in India.")
    def type(self):
        print("India is developing country.")

class USA:
    def capital(self):
        print("Washington, DC is capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is developed country.")

obj_Ind = India()
obj_Usa = USA()
for country in (obj_Ind, obj_Usa):
    country.capital()
    country.language()
    country.type()