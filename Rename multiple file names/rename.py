# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir("with_mask")):
        dst ="mask" + str(count+1) + ".jpg"
        src ='with_mask/'+ filename
        dst ='with_mask/'+ dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()