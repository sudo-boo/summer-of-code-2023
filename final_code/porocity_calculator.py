import cv2 as cv
import numpy as np

def calculate_porosity(image_path, blur_rate=10, threshold_value=125):

    # Load the image
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # Create a window to display the image
    cv.namedWindow("Image with Contours")

    # Create trackbars for blur rate and threshold
    cv.createTrackbar("Blur Rate", "Image with Contours", blur_rate, 50, lambda x: None)
    cv.createTrackbar("Threshold", "Image with Contours", threshold_value, 255, lambda x: None)

    while True:
        # Read the current trackbar positions
        blur_rate = cv.getTrackbarPos("Blur Rate", "Image with Contours")
        threshold_value = cv.getTrackbarPos("Threshold", "Image with Contours")

        # Apply Gaussian blur to the image
        blurred = cv.GaussianBlur(image, (blur_rate*2+1, blur_rate*2+1), 0)

        # Apply adaptive thresholding to obtain a binary image
        _, binary_image = cv.threshold(blurred, threshold_value, 255, cv.THRESH_BINARY)

        # Perform morphological operations to further refine the binary image
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
        opened_image = cv.morphologyEx(binary_image, cv.MORPH_OPEN, kernel, iterations=2)

        # Find contours in the binary image
        contours, _ = cv.findContours(opened_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Create a copy of the original image to draw contours on
        image_with_contours = cv.cvtColor(image.copy(), cv.COLOR_GRAY2BGR)

        # Calculate the contour area
        contour_area = sum(cv.contourArea(contour) for contour in contours)

        # Draw contours on the image
        cv.drawContours(image_with_contours, contours, -1, (0, 0, 255), 5)

        # Display the image with contours
        cv.imshow("Image with Contours", image_with_contours)

        # Check for key press
        key = cv.waitKey(1)
        if key == ord('q'):
            break

    # Calculate the porosity
    total_pixels = image.shape[0] * image.shape[1]
    porosity_pixels = np.sum(opened_image == 0)
    porosity = (contour_area / total_pixels) * 100

    return porosity

# Example usage
image_path = "sample.jpg"
porosity = calculate_porosity(image_path)
print("Porosity: {:.2f}%".format(porosity))
