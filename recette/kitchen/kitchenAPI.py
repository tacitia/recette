from kitchen.models import Ingredient,Kitchen,KitchenIngredientList
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
"""
We do not need userID here!! It SHOULD BE requested from Authentification system.
"""
def getCurrentUser():
    return User.objects.get(username='ron')
def createKitchen(currentUser):
    """
    initilize kitchen for the current user
    """
    createdKitchen = Kitchen(user = currentUser)
    createdKitchen.save()
    
def getKitchenIngredientList(currentUser):
    try:
        uKitchen = Kitchen.objects.get(user=currentUser.pk)
        return uKitchen.ingredients.all()
    except ObjectDoesNotExist:
        print("User doesn't exist.")

def getNonZeroAmountIngredients(currentUser):
    try:
        uKitchen = Kitchen.objects.get(user=currentUser.pk)
        return uKitchen.ingredients.filter(amount__gt=0)
    except ObjectDoesNotExist:
        print("User doesn't exist.")
 
"""
getNonZeroAmountIngredients(userID, minimumAmount)
 return [ingredient]
"""
def getAllIngredientNames():
    ingredients = Ingredient.objects.values("name").distinct()
    return [x[u'name'] for x in ingredients]
"""
We do not need userID here!! It SHOULD BE requested from Authentification system.
"""
def addIngredient(currentUser,ingredient,amount = 0):
    if amount == 0:
        amount = ingredient.defaultAmount
    kitchen = currentUser.kitchen_set
    myKitchen = kitchen[0]
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    if not kitchenIngredientListMy.get(ingredient__pk = ingredient.pk):
        """
        Create a new relation here!!!!!!
        """
        newKitchenIngredientList = KitchenIngredientList(ingredient = ingredient,kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        for x in kitchenIngredientListMy:
            x.amount = x.amount + amount
            x.save()
    
        
    
def ModifyIngredientAmount(currentUser, ingredient, amount):
    kitchen = currentUser.kitchen_set
    myKitchen = kitchen[0]
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    if not kitchenIngredientListMy.get(ingredient__pk = ingredient.pk):
        """
        Create a new relation here!!!!!!
        """
        newKitchenIngredientList = KitchenIngredientList(ingredient = ingredient,kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        for x in kitchenIngredientListMy:
            x.amount = amount
            x.save()

def createIngredient(ingredientName,basicMeasure,ingredientType,brand,dAmount):
    ingredientNew = Ingredient(name = ingredientName,
                               basic_measure = basicMeasure,
                               ingredientType = ingredientType,
                               brand = brand,
                               defaultAmount = dAmount)
    ingredientNew.save()
    
