# import cv2

# img = cv2.imread("Resources/download.png")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Output", gray)

# cv2.imwrite("Resources/gray.png", gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2

# Read image
img = cv2.imread("Resources/download.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ask user what to do
choice = input("Type 'show' to display image or 'save' to save image: ").lower()

if choice == "show":
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "save":
    path = input("Enter file path to save image (example: Resources/gray.png): ")

    success = cv2.imwrite(path, gray)

    if success:
        print(f"Image saved successfully at: {path}")
    else:
        print("Failed to save image.")

else:
    print("Invalid option. Please type 'show' or 'save'.")