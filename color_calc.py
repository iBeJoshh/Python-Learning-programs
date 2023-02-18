def main():
    color1 = input("Enter the first primary color: ").lower()
    color2 = input("Enter the second primary color: ").lower()

    if color1 == color2:
        print("Error: Both colors can't be the same.")
    elif color1 not in ["red", "blue", "yellow"] or color2 not in ["red", "blue", "yellow"]:
        print("Error: Invalid text entered, please try again.")
    else:
        if (color1 == "red" and color2 == "blue") or (color2 == "red" and color1 == "blue"):
            print("The secondary color is purple.")
        elif (color1 == "blue" and color2 == "yellow") or (color2 == "blue" and color1 == "yellow"):
            print("The secondary color is green.")
        elif (color1 == "yellow" and color2 == "red") or (color2 == "yellow" and color1 == "red"):
            print("The secondary color is orange.")

if __name__ == '__main__':
    main()
