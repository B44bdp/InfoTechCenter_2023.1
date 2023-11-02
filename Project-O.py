print("********************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with list of GasStations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Meijer","Exxon","Cosco","Sam's","Marathon"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby





# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a Quarter Tank of gas left, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank,
              "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("You Car has Half a Tank of gas left of gas.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three Quarters Left!")
    else:
        print("Your gas tank is full!")


gasLevelAlert()