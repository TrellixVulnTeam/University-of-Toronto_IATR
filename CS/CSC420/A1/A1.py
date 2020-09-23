import random
import cv2 as cv
import numpy as np
import scipy.ndimage.filters as fi

# Q4 (a)
def correlation_helper(I, h):
    image_h, image_w = I.shape[0], I.shape[1]

    filter_h, filter_w = h.shape[0], h.shape[1]

    res_h = image_h - filter_h + 1
    res_w = image_w - filter_w + 1
    res = np.zeros((res_h, res_w))

    for i in range(res_h):
        for j in range(res_w):
            value = (h * I[i: i + filter_h, j: j + filter_w]).sum()
            res[i, j] = value
    return res


def MyCorrelation(I, h, mode):
    """
    Own function MyCorrelation that implements the correlation operation.
    :param I: gray-scale image I.
    :param h: filter h.
    :param mode: one of 'valid', 'same' and 'full'
    :return: output filtering result.
    """
    image_h, image_w = I.shape[0], I.shape[1]

    filter_h, filter_w = h.shape[0], h.shape[1]

    if mode == 'valid':
        return correlation_helper(I, h)

    elif mode == 'same':
        padded_image = np.zeros((image_h + filter_h-1, image_w+filter_w-1))
        padded_image_h = padded_image.shape[0]
        padded_image_w = padded_image.shape[1]

        # fill the image pixel data to padded_image
        padded_image[(filter_h)//2: (filter_h)//2 + image_h, (filter_w)//2: (filter_w)//2 + image_w] \
            = I[0: image_h, 0:image_w]
        res = correlation_helper(padded_image, h)
        return res
    else:  # mode is full
        padded_image = np.zeros((image_h + 2*filter_h, image_w + 2*filter_w))
        padded_image_h = padded_image.shape[0]
        padded_image_w = padded_image.shape[1]

        padded_image[filter_h:padded_image_h - filter_h, filter_w:padded_image_w - filter_w] \
            = I[0: image_h, 0:image_w]
        res = correlation_helper(padded_image, h)
        return res

# Q4(b)
def MyConvolution(I, h, mode):
    """
    Own convolution calculation.
    :param I: input Image
    :param h: filter
    :param mode: string mode
    :return: image after convolution calculation
    """
    # flip the filter in both way
    h = np.flip(h, axis=0)
    h = np.flip(h, axis=1)
    return MyCorrelation(I, h, mode)

# Q4(c)
def generate_gaussian_kernel(size, sigma):
    inp = np.zeros((size, size))
    inp[size//2, size//2] = 1
    return fi.gaussian_filter(inp, sigma)

def portrait_mode(image):
    gaussian_kernel = generate_gaussian_kernel(51, 10)
    portrait = image[200:, 400:1100, :]

    img_1 = image[:,:,0]
    blur_image_1 = MyCorrelation(img_1, gaussian_kernel, 'same')

    img_2 = image[:, :, 1]
    blur_image_2 = MyCorrelation(img_2, gaussian_kernel, 'same')

    img_3 = image[:, :, 2]
    blur_image_3 = MyCorrelation(img_3, gaussian_kernel, 'same')

    blur_image = cv.merge((blur_image_1, blur_image_2, blur_image_3))

    blur_image[200:, 400:1100, :] = portrait
    cv.imwrite("q4_c_blur.jpg", blur_image)

# Q5(b)
def SeparableFilter(filter):
    """
    Given a filter, to find two seperable filters.
    :param filter:
    :return: 1 if true, otherwise 0.
    """
    u, d, v = np.linalg.svd(filter)

    index_lst = np.flatnonzero(d)
    if len(index_lst) == 1:
        sigma = d[index_lst[0]]
        vertical_filter = np.sqrt(sigma) * u[:,0]
        horizontal_filter = np.sqrt(sigma) * v.transpose()[0]
        print('vertical filter:')
        print(vertical_filter)
        print('horizontal filter')
        print(horizontal_filter)
        return 1
    else:
        return 0

#Q6(a)
def AddRandNoise(I, m):
    # rescale range of image to [0,1]
    img = I / 255

    img_w = I.shape[0]
    img_h = I.shape[1]
    img_color = I.shape[2]

    # create noise matrix
    noise = np.random.uniform(low=-m, high=m, size=(img_w, img_h, img_color))
    img = img + noise
    img = img * 255
    return img

#Q6(b)
def linear_remove_filter(I):
    I = cv.blur(I, (3,3))
    return I

#Q6 (c)
def AddSaltAndPepperNoise(I,d):
    w = I.shape[0]
    h = I.shape[1]
    count = 0

    while count < int(w*h*d/2):
        i = int(random.uniform(0,w-1))
        j = int(random.uniform(0,h-1))
        I[i, j] = d
        count +=1

    count_2 = 0
    while count < int(w*h*d/2):
        i = int(random.uniform(0,w-1))
        j = int(random.uniform(0,h-1))
        I[i, j] = d
        count_2 +=1
    return I






if __name__ == '__main__':
    img = cv.imread('source picture/gray.jpg')[:,:,0]
    img = AddSaltAndPepperNoise(img, 0.05)
    img = linear_remove_filter(img)
    cv.imwrite("q6_(b).jpg", img)

    # kernel = 3
    #
    # g, b, r = cv.split(img)
    #
    # g = AddSaltAndPepperNoise(g, 255)
    # g = AddSaltAndPepperNoise(g, 0)
    # g = cv.medianBlur(g, kernel)
    #
    # b = AddSaltAndPepperNoise(b, 255)
    # b = AddSaltAndPepperNoise(b, 0)
    # b = cv.medianBlur(b, kernel)
    #
    # r = AddSaltAndPepperNoise(r, 255)
    # r = AddSaltAndPepperNoise(r, 0)
    # r = cv.medianBlur(r, kernel)
    #
    # img = cv.merge((g, b, r))
    #
    # kernel_2 = 5
    # img = cv.medianBlur(img, kernel_2)
    #
    #
    # #img = cv.medianBlur(img, kernel)
    # #img = cv.bilateralFilter(img, 9, 75, 75)
    #
    # cv.imshow('salt and pepper removal', img)
    #
    # cv.waitKey()



    # print('original shape:')
    # print(img.shape)
    # filter = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    #
    # output_valid = MyConvolution(img, filter, 'valid')
    # print('valid mode:')
    # print(output_valid.shape)
    # cv.imwrite("q4_(b)_valid.jpg", output_valid)
    #
    # output_same = MyConvolution(img, filter, 'same')
    # print('same mode')
    # print(output_same.shape)
    # cv.imwrite("q4_(b)_same.jpg", output_same)
    #
    # output_full = MyConvolution(img, filter, 'full')
    # print('full mode')
    # print(output_full.shape)
    # cv.imwrite("q4_(b)_full.jpg", output_full)

    # output_valid = MyCorrelation(img, filter, 'valid')
    # print('valid mode:')
    # print(output_valid.shape)
    # cv.imwrite("q4_(a)_valid.jpg", output_valid)
    #
    # output_same = MyCorrelation(img, filter, 'same')
    # print('same mode:')
    # print(output_same.shape)
    # cv.imwrite("q4_(a)_same.jpg", output_same)
    #
    # output_full = MyCorrelation(img, filter, 'full')
    # print('full mode:')
    # print(output_full.shape)
    # cv.imwrite("q4_(a)full.jpg", output_full)
    # print('hello world')






    #
    # img = cv.merge((g,b,r))
    #
    # cv.imshow('shanwen', img)
    # cv.waitKey()



    # img = linear_remove_filter(img)
    # cv.imshow('Salt and Pepper', img_after_median_filter)
    # cv.waitKey(0)

    # img = AddRandNoise(img, m=0.05)
    # img = linear_remove_filter(img)
    # cv.imwrite("q6_b.jpg", img)

    # filter = np.array([[16, 0, 16], [0, 0, 0], [16, 0, 16]])
    # res = SeparableFilter(filter)
    # print(res)