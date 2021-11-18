import cv2
import numpy as np
import matplotlib.pyplot as plt
a=cv2.imread('salt.jpg',0)
b=np.zeros((a.shape[0],1))
e=np.zeros((1,a.shape[1]+2))
c=np.append(a,b,axis=1)
d=np.append(b,c,axis=1)
f=np.append(d,e,axis=0)
padding=np.append(e,f,axis=0)
cikis = np.empty(a.shape)

def max(img):
    for i in range((img.shape[0])):
        for j in range((img.shape[1])):
            filtre = ([padding[i - 1, j - 1], padding[i - 1, j], padding[i - 1, j + 1]],[padding[i, j - 1], padding[i, j], padding[i, j + 1]],[padding[i + 1, j - 1], padding[i + 1, j], padding[i + 1, j + 1]])
            deger = np.max(filtre)
            cikis[i, j] = deger
    temp_image = np.float64(np.copy(cikis))
    temp_image = cv2.normalize(temp_image, temp_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    temp_image = temp_image.astype(np.uint8)
    plt.subplot(122), plt.imshow(temp_image, cmap='gray'), plt.title('cikis')
    plt.subplot(121), plt.imshow(a, cmap='gray'), plt.title('giris')
    plt.show()
def median(img):
    for i in range((img.shape[0])):
        for j in range((img.shape[1])):
            filtre = ([padding[i - 1, j - 1], padding[i - 1, j], padding[i - 1, j + 1]],[padding[i, j - 1], padding[i, j], padding[i, j + 1]],[padding[i + 1, j - 1], padding[i + 1, j], padding[i + 1, j + 1]])
            deger = np.median(filtre)
            cikis[i, j] = deger
    temp_image = np.float64(np.copy(cikis))
    temp_image = cv2.normalize(temp_image, temp_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    temp_image = temp_image.astype(np.uint8)
    plt.subplot(122), plt.imshow(temp_image, cmap='gray'), plt.title('cikis')
    plt.subplot(121), plt.imshow(a, cmap='gray'), plt.title('giris')
    plt.show()
def sobel(img):
    for i in range((img.shape[0])):
        for j in range((img.shape[1])):
            gx = (padding[i - 1][j - 1] + 2 * padding[i][j - 1] + padding[i + 1][j - 1]) - (padding[i - 1][j + 1] + 2 * padding[i][j + 1] + padding[i + 1][j + 1])
            gy = (padding[i - 1][j - 1] + 2 * padding[i - 1][j] + padding[i - 1][j + 1]) - (padding[i + 1][j - 1] + 2 * padding[i + 1][j] + padding[i + 1][j + 1])
            cikis[i][j] = min(255, np.sqrt(gx ** 2 + gy ** 2))
    temp_image = np.float64(np.copy(cikis))
    temp_image = cv2.normalize(temp_image, temp_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    temp_image = temp_image.astype(np.uint8)
    plt.subplot(122), plt.imshow(temp_image, cmap='gray'), plt.title('cikis')
    plt.subplot(121), plt.imshow(a, cmap='gray'), plt.title('giris')
    plt.show()
max(a)
#median(a)
#sobel(a)