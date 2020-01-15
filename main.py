from ISS import ISS
from maths import geometricToStandard
import pygame
import datetime
import csv


def closest(lst, k):
    if k in lst:
        return [i for i, x in enumerate(lst) if x == k]
    else:
        return 0


cities = []
roundedlats = []
roundedlongs = []
countries = []

with open('worldcities.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        cities.append(row[0])
        # lats.append(row[2])
        # longs.append(row[3])
        roundedlats.append(round(float(row[2])))
        roundedlongs.append(round(float(row[3])))
        countries.append(row[4])

pygame.init()
pygame.font.init()

iss = ISS()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("ISS Tracker")

font = pygame.font.SysFont("Arial", 32)
smallfont = pygame.font.SysFont("Arial", 20)
geometricFeet = [1, 1]
time = datetime.datetime.now()
origTime = datetime.datetime.now()

while True:

    iss.update()

    window.fill((255, 255, 255))

    # Text

    text = font.render("Latitude: " + str(iss.lat), True, (0, 0, 0))
    textRect = text.get_rect()
    text2 = font.render("Longitude: " + str(iss.long), True, (0, 0, 0))
    text2Rect = text2.get_rect()

    # Time Calculations

    pastTime = origTime
    time = datetime.datetime.now()
    origTime = time
    time = str(time)
    time = time[:len(time) - 4]
    timeDiff = origTime - pastTime
    timeDiffMs = timeDiff.microseconds

    # Time Text

    timetext = smallfont.render("Current Time: " + time, True, (0, 0, 0))
    timetextrect = timetext.get_rect()

    # Text Rect Maths and Blit

    textRect.center = (250, 100)
    text2Rect.center = (250, 200)
    timetextrect.center = (250, 400)

    window.blit(text, textRect)
    window.blit(text2, text2Rect)
    window.blit(timetext, timetextrect)

    # Lat And Long Stuff

    closestlats = closest(roundedlats, round(float(iss.lat)))
    closestlongs = closest(roundedlongs, round(float(iss.long)))

    pastFeet = geometricFeet

    geometricFeet = geometricToStandard(iss.lat, iss.long)

    latVel = abs(geometricFeet[0] - pastFeet[0] / timeDiffMs)
    longVel = abs(geometricFeet[1] - pastFeet[1] / timeDiffMs)

    currentSpeedMPH = [latVel / 5280, longVel / 5280]

    avg = sum(currentSpeedMPH) / len(currentSpeedMPH)

    # Speed Rect

    avgText = smallfont.render("Current MPH: " + str(avg), True, (0, 0, 0))
    avgTextRect = avgText.get_rect()
    avgTextRect.center = (250, 450)
    window.blit(avgText, avgTextRect)

    # Type Testing

    if isinstance(closestlats, int):
        closestlats = [closestlats]
    if isinstance(closestlongs, int):
        closestlongs = [closestlongs]

    # Print Cities

    closestCity = "Not Detected"

    for item in closestlats:
        for iitem in closestlongs:
            if item == iitem:
                closestCity = (cities[item], countries[item])
                print(closestCity)

    # City Text

    if not isinstance(closestCity, str):
        closestCity = closestCity[0] + ", " + closestCity[1]
    cityText = font.render("Looking at: " + closestCity, True, (0, 0, 0))
    cityTextRect = cityText.get_rect()
    cityTextRect.center = (250, 300)
    window.blit(cityText, cityTextRect)

    # Game Loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
