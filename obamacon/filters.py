from PIL import Image
def load_img(image):
    img = Image.open(image)
    return img
def show_img(image):
    img = Image.open(image)
    img.show()
def save_img(image, save_name):
    image.save(save_name)
load_img("obama.jpg")
show_img("obama.jpg")
img = load_img("obama.jpg")
save_img(img, "stitch.jpg")
#should return a new Image object with filter applied
# def obamicon(img_object):
    #create new empty list which you will put all new pixel values into (HINT: USE APPEND)
    # original_pixels = img_object.getdata()
    #use for loop to iterate through every single pixel 
        #at every pixel, sum up the RGB values
        #use conditionals and boolean checks to determine which new color to change to
    for i in (original_pixels):