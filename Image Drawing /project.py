import cv2 as cv 

img = cv.imread("people.jpg")

choices = input ("Line / Rectangle / Circle / Text: ")

if choices == "Line":
    coordinates = input ("Enter (x1, y1) and (x2, y2) for line:")

    x1, y1, x2, y2 = map(int, coordinates.split())

    cv.line (img, (x1, y1), (x2 , y2), (0, 0, 255), 4)

    cv.imshow("Line Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save = input ("Do you want to save the image? (yes/no): ")

    if save.lower() == "yes":
        filename = input("Enter filename: ")
        cv.imwrite(filename, img)
        print("Image saved successfully.")

elif choices == "Rectangle":
    coordinates = input ("Enter (x1 , y1) and (x2 , y2) for rectangle:")

    x1, y1, x2, y2 = map(int , coordinates.split())

    cv.rectangle (img, (x1, y1) , (x2, y2) , (0 ,0, 255), 4)
    cv.imshow("Rectangle Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save = input ("Do you want to save the image? (yes/no): ")

    if save.lower() == "yes":
        filename = input ("Enter Filesname: ")
        cv.imwrite(filename , img)
        print("Image Saved Successfully.")

elif choices == "Circle":
    coordinates = input ("Enter (x, y) for center and radius for circle:")

    x, y, radius = map(int , coordinates.split())

    cv.circle (img, (x, y) , radius , (0 ,0, 255), 4)
    cv.imshow("Circle Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save = input ("Do you want to save the image? (yes/no): ")
    if save.lower() == "yes":
        filename = input ("Enter Filename: ")
        cv.imwrite(filename , img)
        print("Image Saved Successfully.")

elif choices == "Text":
    text = input ("Enter text to display on image:")
    coordinates = input ("Enter (x, y) for text position:")

    x, y = map(int , coordinates.split())

    cv.putText (img, text , (x, y) , cv.FONT_HERSHEY_SIMPLEX , 1 , (0, 0, 255), 2)
    cv.imshow("Text Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save = input ("Do you want to save the image? (yes/no): ")
    if save.lower() == "yes":
        filename = input ("Enter Filename: ")
        cv.imwrite(filename , img)
        print("Image Saved Successfully.")

else:
    print("Oopsie! Invalid choice. Please choose Line, Rectangle, Circle, or Text.")
