from PIL import Image
import numpy as np


def convolve2D(image, kernel, padding=0, strides=1):
    # Do convolution instead of Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    kernel_x_shape = kernel.shape[0]
    kernel_left = kernel_x_shape // 2
    # since slicing end is exclusive, uneven kernel shapes would be too small
    kernel_right = int(np.around(kernel_x_shape / 2.))

    kernel_y_shape = kernel.shape[1]
    kernel_up = kernel_y_shape // 2
    kernel_down = int(np.around(kernel_y_shape / 2.))

    image_x_shape = image.shape[1]
    image_y_shape = image.shape[0]

    # Shape of Output Convolution
    # START TODO ###################
    # xOutput =
    # yOutput = 
    # raise NotImplementedError
    output_x_shape = int(np.around((image_x_shape - kernel_x_shape + 2 * padding) / strides + 1))
    output_y_shape = int(np.around((image_y_shape - kernel_y_shape + 2 * padding) / strides + 1))
    # END TODO ###################
    output = np.zeros((output_y_shape, output_x_shape))

    # Apply Equal Padding to All Sides
    if padding != 0:
        # START TODO ###################
        # imagePadded = 
        # raise NotImplementedError
        image_padded = np.zeros((image_y_shape + 2 * padding, image_x_shape + 2 * padding))
        image_padded[padding:-padding, padding:-padding] = image        
        # END TODO ###################
    else:
        image_padded = image

    # Indices for output image
    x_out = y_out = -1
    # Iterate through image
    for y in range(kernel_up, image_padded.shape[0], strides):
        # START TODO ###################
        # Exit Convolution before y is out of bounds
        # raise NotImplementedError
        if y > image_padded.shape[0] - kernel_down:
            break
        # END TODO ###################

        # START TODO ###################
        # iterate over columns and perform convolution
        # position the center of the kernel at x,y
        # and save the sum of the elementwise multiplication
        # to the corresponding pixel in the output image
        # raise NotImplementedError
        y_out += 1
        x_out = -1
        for x in range(kernel_left, image_padded.shape[1], strides):
            if x > image_padded.shape[1] - kernel_right:
                break
            x_out += 1
            output[y_out, x_out] = np.sum(image_padded[y - kernel_up:y + kernel_down, x - kernel_left:x + kernel_right] * kernel)
        # END TODO ###################
    return output


def main():
    # Grayscale Image
    image = np.array(Image.open("image.png").convert('L'))

    # Edge Detection Kernel
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Convolve and Save Output
    output = convolve2D(image, kernel, padding=2, strides=2)
    Image.fromarray(output).convert('L').save("convolution_output.png")


if __name__ == '__main__':
    main()
