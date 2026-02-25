import png
import random
import os
from time import time


# Parameters
width = 16
height = 16


method = "pallete"



# Image generation main function
def main(seed: int | None = None):

    # Check seed parameter for existing
    if type(seed) == int:
       random.seed(seed)


    # Gradient method
    if method == "gradient":
        gradient = [117, 192] # Two colors for gradient
        colors = [
            (gradient[0], gradient[0], gradient[0]) # Convert to RGB
        ]

        
        color_ = gradient[0] # First color
        for i in range(gradient[1] - color_): # Iterages into first color and second color
            color_result_ = color_+i+1 # Color is depends to iterage
            color_result_ = (color_result_, color_result_, color_result_) # Convert to RGB
            colors.append(color_result_) # Append color

        colors_ = colors.copy()
        
        # Multiplying colors, while they not fill full image (see later)
        while len(colors) < width*height:
            colors.extend(colors_)


    # Minecraft grass pallete method
    elif method == "pallete":
        
        # Gray colors pallete
        colors_ = [112, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 179, 181, 182, 183, 186, 191, 192, 195]


        colors = []

        # Create colors, while they not fill full image (see later)
        while len(colors) < width*height:
              
            # Convert to rgb
            for color in colors_:
                colors.append((color, color, color))
    
    else:
        print(f"Incorrect method: {method}. Acceptable methods: gradient, pallete.")
        raise SystemExit(1)


    image_data = []


    for x in range(width):

        row = []

        for y in range(height):

            val_idx = random.randint(0, len(colors)-1) # Random color index
            val = colors[ val_idx ] # Get this color
            row.extend(val) # Append this color
            
            
            # Remove used color, for he is not repeats (for that colors needs to fill image)

            colors_ = colors.copy() # Copy colors
            i = 0 # Index

            colors = [] # Remove old colors
            
            for color in colors_:
                
                # Append color, if he is not used color
                if i != val_idx:
                   colors.append(color)
                
                i += 1 # Update index


        image_data.append(row)
    
    return image_data



# Save image
def save( image_data: list[ list[int] ], filename: str ):

    # Open a file in binary write mode
    with open(filename, 'wb') as f:
        # Create a PNG writer instance
        w = png.Writer(width, height, greyscale=False, bitdepth=8)
        # Write the image data to the file
        w.write(f, image_data)


    print(f"Image {filename} successfully saved.")



# Checks for arguments

# Check for integer type
def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

# Check index existing in list
def has_idx(list_: list, idx: int):
    try:
        list_[idx]
        return True
    except:
        return False




# File start
if __name__ == "__main__":
   from sys import argv

   seed = None
   seed_idx = 1

   filename = "image.png"


   if has_idx( argv, seed_idx ) and is_int( argv[seed_idx] ):
      seed = int( argv[seed_idx] )
   else:
      t = int(time())
      seed = int( t + (  int.from_bytes( os.urandom(16), 'big' ) % pow( 10, len(str(t)) )  ) )


   filename = f"seed{seed}_{ int( random.randint(0, 4999) + ( time() % 4999 ) ) }_{method}.png"

   save( main(seed), filename )
