import png
import random


width = 16
height = 16



def main(seed: int | None = None):
    if type(seed) == int:
       random.seed(seed)

    gradient = [117, 192]
    colors = [
        (gradient[0], gradient[0], gradient[0])
    ]


    color_ = gradient[0]
    for i in range(gradient[1] - color_):
        color_result_ = color_+i+1
        color_result_ = (color_result_, color_result_, color_result_)
        colors.append(color_result_)


    image_data = []


    for x in range(width):

        row = []

        for y in range(height):
            val = colors[ random.randint(0, len(colors)-1) ]
            row.extend(val)

        image_data.append(row)
    
    return image_data




def save( image_data: list[ list[int] ] ):
    filename = "image.png"

    # Open a file in binary write mode
    with open(filename, 'wb') as f:
        # Create a PNG writer instance
        w = png.Writer(width, height, greyscale=False, bitdepth=8)
        # Write the image data to the file
        w.write(f, image_data)


    print(f"Image {filename}  successfully.")




def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

def is_idx(list_: list, idx: int):
    try:
        list_[idx]
        return True
    except:
        return False



if __name__ == "__main__":
   from sys import argv

   seed = None

   if is_idx(argv, 1) and is_int( argv[1] ):
      seed = int(argv[1])

   save( main(seed) )
