import sys
import os

arg = sys.argv
cmdList = arg
del cmdList[0]
cmd = " ".join(cmdList)

class Parking:
  def __init__(self):
    self.numberOfSlots =  0
    self.main_parking = []
    self.parkingLog = []
    self.freeIndex = 0

  def park(self, ticket):
    if int(self.numberOfSlots) > int(self.freeIndex):
      self.updateHistory(ticket)
      self.updateParking(ticket)
      print("Allocated slot number:",  ticket.tId)
    else:
      print("Sorry, parking lot is full")

  def updateHistory(self, ticket):
    self.parkingLog.append(ticket)

  def updateParking(self,ticket):
    parkInd =ParkingJob.findNearestSlot() - 1
    self.main_parking[parkInd] = ticket
    self.freeIndex = self.freeIndex + 1

  def removeSlot(self,slotNumber):
    slotNum = int(slotNumber) - 1
    self.main_parking[slotNum] = None
    self.freeIndex = self.freeIndex-1
    print("Slot number",slotNumber,"is free")

  def getTotalSlots(self):
    return self.main_parking

  def setSlots(self, n):
    self.numberOfSlots = int(n)
    self.main_parking = [None]* int(n)
    print("Created a parking lot with",str(n),"slots")

  def getStatus(self):
    header = "Slot No.    Registration No    Colour"
    print(header)
    for ticket in self.main_parking:
      if ticket != None:
        print(str(ticket.tId)+"           "+ticket.regNum+"      "+ticket.color)

  def getRegNumByColor(self, _color):
    result = []
    color = str(_color)
    for ticket in self.parkingLog:
      if(ticket.color == color):
        result.append(str(ticket.regNum))
    if len(result)== 0:
      print("Not found")
    else:
      print(", ".join(result))

  def getSlotNumByColor(self, _color):
    result = set()
    color = str(_color)
    for ticket in self.parkingLog:
      if(ticket.color == color):
        result.add(str(ticket.tId))
    if len(result)== 0:
      print("Not found")
    else:
      result = sorted(result)
      print(", ".join(result))

  def getSlotNumByRegNum(self, _regNum):
    result = set()
    regNum = str(_regNum)
    for ticket in self.parkingLog:
      if(ticket.regNum == regNum):
        result.add(str(ticket.tId))
    if len(result)== 0:
      print("Not found")
    else:
      result = sorted(result)
      print(", ".join(result))

  def findNearestSlot(self):
    p = self.main_parking
    freeSlot = None
    for n in p:
      if n == None:
        freeSlot = p.index(n) + 1
        break
    return freeSlot

class Ticket:
  def __init__(self):
    self.tId = 0
    self.regNum = 0
    self.color = 0

  def createTicket(self,slotNum, regNum, color ):
    self.tId = slotNum
    self.regNum = regNum
    self.color = color

def parkInSlot(cmdData):
  tic = Ticket()
  slotNum = ParkingJob.findNearestSlot()
  regNum =  cmdData[0]
  color = cmdData[1]
  tic.createTicket(slotNum, regNum, color)
  ParkingJob.park(tic)

def leaveSlot(cmd):
  ParkingJob.removeSlot(cmd[0])

def getStatus():
  ParkingJob.getStatus()

def createParkingLot(cmd):
  global ParkingJob
  ParkingJob = Parking()
  ParkingJob.setSlots(str(cmd[0]))
  return ParkingJob

def searchRegNumByColor(color):
  ParkingJob.getRegNumByColor(color)

def searchSlotNumByColor(color):
  ParkingJob.getSlotNumByColor(color)

def searchSlotNumByRegNum(regNum):
  ParkingJob.getSlotNumByRegNum(regNum)

def decide(cmd, loop):
  cmdData = cmd.strip().split(" ")
  cmdMain = cmdData[0]
  del cmdData[0]

  if (cmdMain == "status"):
    getStatus()
  if (cmdMain == "park"):
    if len(cmdData) != 0:
      parkInSlot(cmdData)
    else:
      print("Need details. Try again!")
  elif (cmdMain == "leave"):
    if len(cmdData) != 0:
      leaveSlot(cmdData)
    else:
      print("Need a slot number. Try again!")
  elif (cmdMain == "create_parking_lot"):
    if len(cmdData) != 0:
      createParkingLot(cmdData)
    else:
      print("Need the total slot number to create. Try again!")
  elif ("registration_numbers_for_cars_with_colour" in cmdMain):
    if len(cmdData[0]) != 0:
      searchRegNumByColor(cmdData[0])
    else:
      print("Need color to search. Try again!")
  elif ("slot_numbers_for_cars_with_colour" in cmdMain):
    if len(cmdData[0]) != 0:
      searchSlotNumByColor(cmdData[0])
    else:
      print("Need Color to search. Try again!")
  elif("slot_number_for_registration_number" in cmdMain):
    if len(cmdData[0]) != 0:
      searchSlotNumByRegNum(cmdData[0])
    else:
      print("Need registration number to search. Try again!")
  else:
     return
  if (loop!= None):
    loop()

def wLoop():
  while True:
    iCmd = input()
    if ("exit" in iCmd):
      exit()
    else:
      decide(iCmd,wLoop)

# Entry Point
if cmd == ".":
  wLoop()

if ".txt" in cmd:
  inputDir = "."
  fileToRead = ""
  entries = os.listdir(inputDir)
  fileToRead = ""
  for root, dirs, files in os.walk(inputDir):
    for file in files:
      if file == cmd:
        fileToRead = root+"/"+file
  f = open(fileToRead, "r")
  data = f.readlines()
  for d in data:
    decide(d, None)
else:
  decide(cmd, wLoop)