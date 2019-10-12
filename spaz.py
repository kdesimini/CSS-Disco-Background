import random

colors = ["Aqua ","Aquamarine ","Bisque ","BlanchedAlmond ","Blue ","BlueViolet ","Chartreuse ","Coral ","CornflowerBlue ","Crimson ","Cyan ","DarkBlue ","DarkCyan ","DarkGoldenRod ","DarkMagenta ","DarkOliveGreen ","DarkOrange ","DarkOrchid ","DarkRed ","DarkSlateBlue ","DarkSlateGray ","DarkSlateGrey ","DarkTurquoise ","DarkViolet ","DeepPink ","DeepSkyBlue ","DodgerBlue ","FireBrick ","ForestGreen ","Fuchsia ","Gold ","GoldenRod ","Green ","GreenYellow ","HotPink ","IndianRed  ","Indigo  ","LawnGreen ","LightBlue ","LightCoral ","LightGreen ","LightPink ","LightSalmon ","LightSeaGreen ","LightSkyBlue ","Lime ","LimeGreen ","Magenta ","Maroon ","MediumAquaMarine ","MediumBlue ","MediumOrchid ","MediumPurple ","MediumSeaGreen ","MediumSlateBlue ","MediumSpringGreen ","MediumTurquoise ","MediumVioletRed ","MidnightBlue ","Navy ","Olive ","OliveDrab ","Orange ","OrangeRed ","Orchid ","PaleGreen ","PaleTurquoise ","PaleVioletRed ","Peru ","Pink ","Plum ","PowderBlue ","Purple ","RebeccaPurple ","Red ","RosyBrown ","RoyalBlue ","SaddleBrown ","Salmon ","SandyBrown ","SeaGreen ","SeaShell ","Sienna ","Silver ","SkyBlue ","SlateBlue ","SlateGray ","SlateGrey ","Snow ","SpringGreen ","SteelBlue ","Tan ","Teal ","Thistle ","Tomato ","Turquoise ","Violet ","Wheat ","White ","WhiteSmoke ","Yellow ","YellowGreen "]
def generate():

    # Parameters
    maxWidth = 1920 # in pixles
    minWidth = 280 # in pixles
    density = 10 # pixles before new color is generated
    useTransition = True
    useDelay = False # prevents color change until resizing stops
    transitionString = "transition: background 0.7s linear; "
    delayString = "transition-delay: .2s;"

    # The obsurdity
    while maxWidth >= minWidth:
        print("@media (max-width: " + str(maxWidth) + "px) and (max-height: " + str(maxWidth) + "px) {")
        print("    body {")
        if useTransition : print("        " + transitionString)
        if useDelay : print ("        " + delayString)
        print("        background: " + str(random.choice(colors)) +";")
        print("    }\n}")
        maxWidth -= density

if __name__ == "__main__":
    generate()
