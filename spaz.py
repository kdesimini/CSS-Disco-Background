import random

colors = ["Aqua","Aquamarine","Bisque","BlanchedAlmond","Blue","BlueViolet","Chartreuse","Coral","CornflowerBlue","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkMagenta","DarkOliveGreen","DarkOrange","DarkOrchid","DarkRed","DarkSlateBlue","DarkTurquoise","DarkViolet","DeepPink","DodgerBlue","FireBrick","ForestGreen","Fuchsia","Gold","GoldenRod","Green","GreenYellow","HotPink","IndianRed","Indigo","LawnGreen","LightBlue","LightCoral","LightGreen","LightSeaGreen","Lime","LimeGreen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","Navy","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGreen","PaleTurquoise","PaleVioletRed","Peru","Pink","Plum","PowderBlue","Purple","RebeccaPurple","Red","RosyBrown","RoyalBlue","SeaGreen","Sienna","SlateBlue","SlateGray","SpringGreen","SteelBlue","Teal","Thistle","Tomato","Turquoise","Violet","Yellow","YellowGreen"]

# Parameters
maxWidth = 1920 # in pixles
minWidth = 280 # in pixles
density = 20 # pixles before new color is generated
useTransition = False
useDelay = False # prevents color change until resizing stops
transitionString = "transition: background 0.1s linear; "
delayString = "transition-delay: .2s;"
saveToFile = True # make this false if you just want console output. 
fileName = "discojam.css"
reset = True


def outputToConsole(maxWidth):
    print("@media (max-width: " + str(maxWidth) + "px) and (max-height: " + str(maxWidth) + "px) {")
    print("    body {")
    if useTransition : print("        " + transitionString)
    if useDelay : print ("        " + delayString)
    print("        background: " + str(random.choice(colors)) +";")
    print("    }\n}")

    
def outputToFile(maxWidth):
    global reset
    if reset == True:
        reset = False
        open(fileName, 'w').close() # reset the file to clean slate
    file = open(fileName, "a+")
    file.write("@media (max-width: " + str(maxWidth) + "px) and (max-height: " + str(maxWidth) + "px) {\n")
    file.write("    body {\n")
    if useTransition : file.write("        " + transitionString + "\n")
    if useDelay : file.write ("        " + delayString + "\n")
    file.write("        background: " + str(random.choice(colors)) +";\n")
    file.write("    }\n}")
    file.close()

def generate():
    # The obsurdity
    global maxWidth
    while maxWidth >= minWidth:
        if saveToFile == True:
            outputToFile(maxWidth)
        else:
            outputToConsole(maxWidth)
        maxWidth -= density


if __name__ == "__main__":
    generate()
