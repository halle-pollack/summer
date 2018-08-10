from PIL import Image

im = Image.open("butterfly.jpg")
im.show()
im_data = im.getdata()
#print(list(im_data))

new_im = []



for (a,b,c) in im_data:
	new_im.append((a//2, 0 , c))
	
im.putdata(new_im)
im.show()