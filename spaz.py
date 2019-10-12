import random

colors = ["AliceBlue ","AntiqueWhite ","Aqua ","Aquamarine ","Azure ","Beige ","Bisque ","Black ","BlanchedAlmond ","Blue ","BlueViolet ","Brown ","BurlyWood ","CadetBlue ","Chartreuse ","Chocolate ","Coral ","CornflowerBlue ","Cornsilk ","Crimson ","Cyan ","DarkBlue ","DarkCyan ","DarkGoldenRod ","DarkGray ","DarkGrey ","DarkGreen ","DarkKhaki ","DarkMagenta ","DarkOliveGreen ","DarkOrange ","DarkOrchid ","DarkRed ","DarkSalmon ","DarkSeaGreen ","DarkSlateBlue ","DarkSlateGray ","DarkSlateGrey ","DarkTurquoise ","DarkViolet ","DeepPink ","DeepSkyBlue ","DimGray ","DimGrey ","DodgerBlue ","FireBrick ","FloralWhite ","ForestGreen ","Fuchsia ","Gainsboro ","GhostWhite ","Gold ","GoldenRod ","Gray ","Grey ","Green ","GreenYellow ","HoneyDew ","HotPink ","IndianRed  ","Indigo  ","Ivory ","Khaki ","Lavender ","LavenderBlush ","LawnGreen ","LemonChiffon ","LightBlue ","LightCoral ","LightCyan ","LightGoldenRodYellow ","LightGray ","LightGrey ","LightGreen ","LightPink ","LightSalmon ","LightSeaGreen ","LightSkyBlue ","LightSlateGray ","LightSlateGrey ","LightSteelBlue ","LightYellow ","Lime ","LimeGreen ","Linen ","Magenta ","Maroon ","MediumAquaMarine ","MediumBlue ","MediumOrchid ","MediumPurple ","MediumSeaGreen ","MediumSlateBlue ","MediumSpringGreen ","MediumTurquoise ","MediumVioletRed ","MidnightBlue ","MintCream ","MistyRose ","Moccasin ","NavajoWhite ","Navy ","OldLace ","Olive ","OliveDrab ","Orange ","OrangeRed ","Orchid ","PaleGoldenRod ","PaleGreen ","PaleTurquoise ","PaleVioletRed ","PapayaWhip ","PeachPuff ","Peru ","Pink ","Plum ","PowderBlue ","Purple ","RebeccaPurple ","Red ","RosyBrown ","RoyalBlue ","SaddleBrown ","Salmon ","SandyBrown ","SeaGreen ","SeaShell ","Sienna ","Silver ","SkyBlue ","SlateBlue ","SlateGray ","SlateGrey ","Snow ","SpringGreen ","SteelBlue ","Tan ","Teal ","Thistle ","Tomato ","Turquoise ","Violet ","Wheat ","White ","WhiteSmoke ","Yellow ","YellowGreen "]
def generate():

    # Parameters
    maxWidth = 1920 # in pixles
    minWidth = 280 # in pixles
    density = 20 # pixles before new color is generated
    useTransition = True
    transitionString = "transition: background 0.7s linear;"

    # The obsurdity
    while maxWidth >= minWidth:
        print("@media (max-width: " + str(maxWidth) + "px) {")
        print("body {")
        if useTransition : print("  " + transitionString)
        print("  background: " + str(random.choice(colors)) +";")
        print("  }\n}")
        maxWidth -= density

if __name__ == "__main__":
    generate()
