import pygame
import pygwidgets

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")

WHITE = (255, 255, 255)

# Widgets
inputTemp = pygwidgets.InputText(window, (50, 40), width=120, backgroundColor=(255, 255, 180))

radioGroup = "tempScale"
radioCtoF = pygwidgets.TextRadioButton(window, (50, 90), "C → F", radioGroup, value="CtoF")
radioFtoC = pygwidgets.TextRadioButton(window, (150, 90), "F → C", radioGroup, value="FtoC")

radioCtoF.setValue(True)

convertButton = pygwidgets.TextButton(window, (50, 150), "Convert")

outputDisplay = pygwidgets.DisplayText(window, (50, 210), "", fontSize=28, textColor=(0, 0, 150))


# Conversion Logic
def doConversion():
    try:
        temp = float(inputTemp.getValue())
    except ValueError:
        outputDisplay.setValue("Enter a valid number")
        return

    if radioCtoF.getValue() == "CtoF":
        result = temp * 9/5 + 32
        outputDisplay.setValue(f"{temp:.2f} °C = {result:.2f} °F")
    else:
        result = (temp - 32) / (9/5)
        outputDisplay.setValue(f"{temp:.2f} °F = {result:.2f} °C")


# Main Loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if inputTemp.handleEvent(event):
            doConversion()

        if radioCtoF.handleEvent(event) or radioFtoC.handleEvent(event):
            doConversion()

        if convertButton.handleEvent(event):
            doConversion()

    window.fill(WHITE)
    inputTemp.draw()
    radioCtoF.draw()
    radioFtoC.draw()
    convertButton.draw()
    outputDisplay.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
