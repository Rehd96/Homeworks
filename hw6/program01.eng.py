# -*- coding: utf-8 -*-
'''We have an image that we want to compress. The image has a black
background and contains N empty rectangles, for which only the four
sides are drawn.

To compress the image, we need to find all the N rectangles, even if
they have their sides intersecting.  We need to find the order in
which the rectangles were drawn so that we can encode the sequence of
the drawing operations and perfectly reproduce the original image.

You can assume that:
    - all the rectangles have different colors
    - each rectangle intersects at least another one
    - the sides of different rectangles do not overlap but just cross
    - the vertices of different rectangles do not overlap
    - the sequence of the drawing operations is unique (there is only
      one overlap between rectangles that orders them)

To compress the image, we need to encode 5 pieces of information for
each of the N rectangles:
    - x, y: coordinates of the upper left vertex (x=column, y=row)
    - w, h: width and height of the rectangle in pixels
    - C: color of the sides of the rectangle.

The compression scheme builds a second image with size 5xN pixels.
The new image contains one row for each rectangle, in the same order
of the sequence of drawing. Each row encodes the corresponding
rectangle considering the values of x, y, w, h and C as a pixel: while
C is a pixel with color C, the three RGB channels of the other pixels
represent a digit of the corresponding value, on base 256. For
example: a pixel with color (1,2,3) represents the value 130815, since
(1,2,3) = 1*255*(2*255+3)=130815.

Finally, we want to know the bounding-box of the group of rectangles,
namely the minimum rectangle, with upper left vertex in (xmin, ymin)
and lower right vertex (xmax, ymax) which encloses all the rectangles.

Design and implement the function ex1(image_filename, encoded_filename)
which:
    - reads the file indicated by the parameter 'image_filename' using
      the 'images' library
    - locates and find the drawing order of the N rectangles 
    - builds the 5xN image that encodes rectangle information
    - saves the encoded image in the file indicated by the
      'encoded_filename' parameter
    - returns the tuple with the 4 coordinates (xmin, ymin, xmax,
      ymax) of the bounding box

WARNING: do not import other libraries and do not open files other
than the ones in the argument list.

'''

import images

def ex1(image_filename, encoded_filename):
    # write your code here
    pass

if __name__ == '__main__':
    # write your tests here
    pass

