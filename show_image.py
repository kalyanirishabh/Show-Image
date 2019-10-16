import cv2

def show_image(image):
    cv2.imshow('image', image)
    while(1):
        if cv2.waitKey(10)&0xFF==27: # If it is 64 bit processor, then only use 0xFF otherwise don't
            break
    cv2.destroyAllWindows()
