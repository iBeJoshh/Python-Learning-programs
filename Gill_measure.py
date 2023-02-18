def main():
    ounces = float(input("Enter the number of ounces of apple cider: "))
    drams = ounces * 8
    gills = ounces / 4

    if drams > 1024:
        print("The amount you want is large and you will need to buy in gallons.")
    elif drams < 100:
        print("The amount you want is too small, you should just order a pint.")
    else:
        print("Gills:", gills)
        print("Drams:", drams)

if __name__ == '__main__':
    main()

