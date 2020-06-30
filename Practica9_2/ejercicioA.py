import cv2
import numpy as np
import math

img = cv2.imread("perro.png")
rows, cols, ch = img.shape

print(img.shape)
print(cols)
print(rows)
cv2.circle(img, (round((cols-1)/2), round((rows-1)/2)), 5, (0, 0, 255), -1)
px = cols/2
py = rows/2

centro = np.array([px,py]).astype(np.float32)


print("centro: ", centro)

angle = math.degrees(math.pi)
print(angle)

def rotacion(file_img, angulo, centro):

    a = abs(math.cos(angulo))
    print("cos angulo: ", a)
    b = abs(math.sin(angulo))
    print("seno angulo", b)
    print("px: ", centro[0])
    print("py: ", centro[1])
    A = np.array([[a, b], [b*(-1), a]]).astype(np.float32)
    B = np.array([[((1-a)*centro[0]) - (b*centro[1])], [(b*centro[0]) + (1-a)*centro[1]]]).astype(np.float32)
    #B = np.array([[0], [0]]).astype(np.float32)
    print("array A: ", A)
    print("array B: ", B)
    matriz_m_rotate = np.append(A, B, axis=1)
    print(matriz_m_rotate)
    ncols = int((rows*b) + (cols*a))
    print("nuevas cols: ", ncols)
    nrows = int((rows*a) + (cols*b))
    print("nuevas filas: ", nrows)
    matriz_m_rotate[0, 2] += (ncols/2) - centro[0]
    matriz_m_rotate[1, 2] += (nrows/2) - centro[1]
    dst_rotation = cv2.warpAffine(file_img, matriz_m_rotate, (ncols, nrows))

    return dst_rotation

img_result = rotacion(img, angle, centro)
cv2.imshow("mi imgen", img)
cv2.imshow("resultado", img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
