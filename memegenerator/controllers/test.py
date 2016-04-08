import ctypes
import os.path
save_path = '/memegenerator/static/'
#image_name = request.vars.upload
img = os.path.join(save_path, "meme.jpg")
final_img = os.path.join(save_path, "meme1.jpg")
#text = request.vars.text
lib = ctypes.CDLL('./libmeme.so')
pfun = lib.makeMeme("img", "final_img", "text")
    #x = pfun("img", "final_img", "text")
#return dict(image = img)
