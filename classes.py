class MealList:
    #There will be one MealList ("recipe book") per user.
    def __init__(self, meals=[]):
        self.meals = meals
        self.meal_names = [i.name for i in self.meals]
    def add_meal(self, meal):
        self.meals.append(meal)
        mealname = meal.name
        print("{MEAL} added to recipe book".format(MEAL=mealname))
    def stringify_meals(self):
        str = ""
        for i in self.meals:
            str = str + i.name + "; "
        return str
    def __repr__(self):
        meals = self.stringify_meals()
        return "You have the following meals in your recipe book: " + meals

recipebook = MealList() #The recipebook is user specific. For now (haven't added multi-user functions) only one is required for the programme to run for a single user.

class Meal:
    def __init__(self, name, photo=None, description=None, instructions={}, ingredients=[]):
        self.name = name
        self.photo = photo
        self.description = description
        self.instructions = instructions
        self.ingredients = ingredients
        print("{MEAL} created successfully.".format(MEAL=self.name))
        # Creating a meal should automatically add it to the meal list per below.
        recipebook.add_meal(self)
    def add_ingredients(self, ingredients):
        for i in ingredients:
            self.ingredients.append(i)
    def stringify_ingredients(self):
        str = ""
        for i in self.ingredients:
            str = str + i
        return str
    def add_next_instruction(self, instruction):
        next_item = len(self.instructions) + 1
        self.instructions.update({next_item:instruction})
    def __repr__(self):
        return "{MEAL} consists of {INGREDIENTS}".format(MEAL=self.name, INGREDIENTS=self.stringify_ingredients())
    def add_ingredients(self, ings):
        for i in ings:
            self.ingredients.append(i + "; ")
        print('Updated ingredients! {MEAL} now consists of {INGREDIENTS}'.format(MEAL=self.name, INGREDIENTS=self.stringify_ingredients()))
    def get_instructions(self):
        print(self.instructions.items())



class Ingredient:
    def __init__(self, name, emoji=None):
        self.name = name
        #Emoji just an idea at this stage - would be nice to have visual representation for ingredients.
        #Would have to be pushed centrally
        self.emoji = emoji

class Pantry:
    def __init__(self, ingredients=[]):
        self.ingredients = ingredients
    def get_meals(self):
        available_meals = []
        for i in recipebook.meals:
            result = all(elem in i.ingredients for elem in self.ingredients)
            if result:
                available_meals.append(i.name + "; ")
        return "The following meals can be cooked with your ingredients:" + str(available_meals)

#Everything below this line is just for testing.

bolognese = Meal(name="Bolognese", description="Lentil Bolognese using Merchant Gourmet lentils and tawny port")


bolognese.add_ingredients(["Beluga Lentils", "Tawny Port", "Brown Onions", "Garlic"])
print(bolognese)

bolognese.add_next_instruction('First, chop an onion and two gloves of garlic')
bolognese.add_next_instruction('Next, sautée them for eight minutes on a low heat')
bolognese.get_instructions()



my_pantry = Pantry(["Beluga Lentils", "Tawny Port", "Brown Onions", "Garlic"])
print(my_pantry.get_meals())
print(recipebook)