from kitchen.models import Ingredient,Kitchen,KitchenIngredientList
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def createKitchen(currentUser):
    """
    initilize kitchen for the current user
    """
    createdKitchen = Kitchen(user = currentUser)
    createdKitchen.save()
    
def getKitchenIngredientList(currentUser):
    try:
        uKitchen = Kitchen.objects.get(user=currentUser.pk)
        return zip(uKitchen.ingredients.all(),[float(temp.amount/100.0) for temp in uKitchen.kitcheningredientlist_set.all()])
    except ObjectDoesNotExist:
        createKitchen(currentUser)
        uKitchen = Kitchen.objects.get(user=currentUser.pk)
        return (uKitchen.ingredients.all(),[temp.amout for temp in uKitchen.kitcheningredientlist_set.all()])   

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
"""
def addIngredient(currentUser,ingredientID,amount = 0):
    if amount == 0:
        amount = ingredient.defaultAmount
    myKitchen = Kitchen.objects.get(user = currentUser)
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    if not kitchenIngredientListMy.get(ingredient__pk = ingredientID):
        newKitchenIngredientList = KitchenIngredientList(ingredient = Ingredient.objects.get(pk = ingredientID),kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        x = kitchenIngredientListMy.get(ingredient__pk = ingredientID)
        x.amount = amount
        x.save()
"""
def addIngredient(currentUser,ingredientName,amount = 0,ingredientID = -1):
    if amount == 0:
        amount = ingredient.defaultAmount
    myKitchen = Kitchen.objects.get(user = currentUser)
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    theIngredient = Ingredient.objects.get(name = ingredientName)
    if not kitchenIngredientListMy.filter(ingredient__pk = theIngredient.pk):
        newKitchenIngredientList = KitchenIngredientList(ingredient = theIngredient,kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        x = kitchenIngredientListMy.get(ingredient__pk = theIngredient.pk)
        x.amount = x.amount + amount
        x.save()

    
def increaseIngredientAmount(currentUser, ingredientID, amount = 0):
    myKitchen = Kitchen.objects.get(user = currentUser)
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    if not kitchenIngredientListMy.filter(ingredient__pk = ingredientID):
        """
        Create a new relation here!!!!!!
        """
        newKitchenIngredientList = KitchenIngredientList(ingredient = Ingredient.object.get(pk = ingredientID),kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        print "Add amount"
        x = kitchenIngredientListMy.get(ingredient__pk = ingredientID)
        x.amount = x.amount + amount
        x.save()

def modifyIngredientAmount(currentUser, ingredient, amount):
    myKitchen = Kitchen.objects.get(user = currentUser)
    kitchenIngredientListMy = myKitchen.kitcheningredientlist_set
    if not kitchenIngredientListMy.filter(ingredient__pk = ingredient.pk):
        """
        Create a new relation here!!!!!!
        """
        newKitchenIngredientList = KitchenIngredientList(ingredient = ingredient,kitchen = myKitchen,amount = amount)
        newKitchenIngredientList.save()
    else:
        x = kitchenIngredientListMy.get(ingredient__pk = ingredient.pk)
        x.amount = amount
        x.save()

def createIngredient(ingredientName,basicMeasure,ingredientType,brand,dAmount):
    ingredientNew = Ingredient(name = ingredientName,
                               basic_measure = basicMeasure,
                               ingredientType = ingredientType,
                               brand = brand,
                               defaultAmount = dAmount)
    ingredientNew.save()
    
