num = 0
num1 = 0
num3 = 0
while num <= 10800: # This is for a 3 hour video, change it to however long you want it to be
  
    num += 180 # this is for three minute intervals change it to however long you want the intervals
    
    clip = VideoFileClip("PASTE YOUR PATH TO THE VIDEO HERE")
    
    clip = clip.subclip(num1, num)
    
    clip.write_videofile(str(num3)+".mp4") #saves the video as a number (e.g. 1.mp4, 2.mp4), you can change it to whatever you want

    num1 = num
    
    num3 +=1 
