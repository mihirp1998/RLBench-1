import tasks
import ipdb
st = ipdb.set_trace
dict_val = {}
total_tasks = 0
tasks_class = dir(tasks)
for task_val in tasks_class:
    if '__' not in task_val and "fs" not in task_val[:2].lower() and "mt" not in task_val[:2].lower():
        # st()
        class_val = getattr(tasks,task_val)
        print(class_val)
        val_variations = class_val(None,None).variation_count()
        dict_val[task_val] = val_variations
        total_tasks += val_variations
print(total_tasks)
# 554

st()
# {'BasketballInHoop': 1, 'BeatTheBuzz': 1, 'BlockPyramid': 20, 'ChangeChannel': 2, 
#  'ChangeClock': 1, 'CloseBox': 1, 'CloseDoor': 1, 'CloseDrawer': 3, 'CloseFridge': 1, 
#  'CloseGrill': 1, 'CloseJar': 20, 'CloseLaptopLid': 1, 'CloseMicrowave': 1, 
#  'EmptyContainer': 20, 'EmptyDishwasher': 1, 'GetIceFromFridge': 1, 
#  'HangFrameOnHanger': 1, 'HitBallWithQueue': 1, 'Hockey': 1, 'InsertOntoSquarePeg': 20, 
#  'InsertUsbInComputer': 1, 'LampOff': 1, 'LampOn': 1, 'LightBulbIn': 20, 
#  'LightBulbOut': 20, 'MeatOffGrill': 2, 'MeatOnGrill': 2, 'MoveHanger': 1, 
#  'OpenBox': 1, 'OpenDoor': 1, 'OpenDrawer': 3, 'OpenFridge': 1, 'OpenGrill': 1, 
#  'OpenJar': 20, 'OpenMicrowave': 1, 'OpenOven': 1, 'OpenWindow': 1, 'OpenWineBottle': 1, 
#  'PhoneOnBase': 1, 'PickAndLift': 20, 'PickUpCup': 20, 'PlaceCups': 3, 
#  'PlaceHangerOnRack': 1, 'PlaceShapeInShapeSorter': 5, 'PlaceWineAtRackLocation': 3, 
#  'PlayJenga': 1, 'PlugChargerInPowerSupply': 1, 'PourFromCupToCup': 20, 'PressSwitch': 1, 
#  'PushButton': 18, 'PushButtons': 50, 'PutAllGroceriesInCupboard': 1, 
#  'PutBooksAtShelfLocation': 4, 'PutBooksOnBookshelf': 3, 'PutBottleInFridge': 1, 
#  'PutGroceriesInCupboard': 9, 'PutItemInDrawer': 3, 'PutKnifeInKnifeBlock': 1, 
#  'PutKnifeOnChoppingBoard': 1, 'PutMoneyInSafe': 3, 
#  'PutPlateInColoredDishRack': 20, 'PutRubbishInBin': 1, 'PutRubbishInColorBin': 2, 
#  'PutShoesInBox': 1, 'PutToiletRollOnStand': 1, 'PutTrayInOven': 1, 
#  'PutUmbrellaInUmbrellaStand': 1, 'ReachAndDrag': 20, 'ReachTarget': 20, 
#  'RemoveCups': 2, 'ScoopWithSpatula': 1, 'ScrewNail': 1, 'SetClockToTime': 3, 
#  'SetTheTable': 1, 'SetupCheckers': 3, 'SlideBlockToColorTarget': 4, 
#  'SlideBlockToTarget': 1, 'SlideCabinetOpen': 2, 
#  'SlideCabinetOpenAndPlaceCups': 2, 'SolvePuzzle': 1, 'StackBlocks': 60, 
#  'StackCups': 20, 'StackWine': 1, 'StraightenRope': 1, 
# 'SweepToDustpan': 1, 'SweepToDustpanOfSize': 2, 'TakeCupOutFromCabinet': 2, 'TakeFrameOffHanger': 1,
#  'TakeItemOutOfDrawer': 3, 'TakeLidOffSaucepan': 1, 'TakeMoneyOutSafe': 3, 'TakeOffWeighingScales': 3, 
#  'TakePlateOffColoredDishRack': 3, 'TakeShoesOutOfBox': 1, 'TakeToiletRollOffStand': 1, 
#  'TakeTrayOutOfOven': 1, 'TakeUmbrellaOutOfUmbrellaStand': 1, 'TakeUsbOutOfComputer': 1, 
#  'ToiletSeatDown': 1, 'ToiletSeatUp': 1, 'TurnOvenOn': 1, 
#  'TurnTap': 2, 'TvOn': 1, 'UnplugCharger': 1, 'WaterPlants': 1, 'WeighingScales': 3, 'WipeDesk': 1}