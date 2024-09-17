import numpy as np
import cv2 as cv

def rotacao_matriz(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], 
                     [np.sin(theta),  np.cos(theta)]])

def cisalhamento_matriz(shx, shy):
    return np.array([[1, shx], 
                     [shy, 1]])

def aplicar_transformacao(image, matriz_transformacao):
    altura, largura = image.shape[:2]
    cx, cy = largura // 2, altura // 2

    y, x = np.mgrid[0:altura, 0:largura]
    coords = np.vstack([x.flatten() - cx, y.flatten() - cy])

    novas_coords = matriz_transformacao @ coords

    novas_coords[0, :] += cx
    novas_coords[1, :] += cy

    novas_coords = np.round(novas_coords).astype(int)

    x_novo, y_novo = novas_coords
    dentro_limite = (0 <= x_novo) & (x_novo < largura) & (0 <= y_novo) & (y_novo < altura)

    imagem_transformada = np.zeros_like(image)
    imagem_transformada[y.flatten()[dentro_limite], x.flatten()[dentro_limite]] = \
        image[y_novo[dentro_limite], x_novo[dentro_limite]]

    return imagem_transformada

def run():
    camera = cv.VideoCapture(0)
    width = 320*2
    height = 240*2

    if not camera.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    angulo_rotacao = 0
    velocidade_rotacao = 1  
    cisalhamento_x, cisalhamento_y = 0.5, 0.5
    rotacao_ativa = False
    cisalhamento_ativo = False

    while True:
        frame_ok, quadro = camera.read()

        if not frame_ok:
            print("Não consegui capturar quadro!")
            break

        quadro = cv.resize(quadro, (width, height), interpolation=cv.INTER_AREA)

        if rotacao_ativa and not cisalhamento_ativo:
            matriz_rotacao = rotacao_matriz(np.radians(angulo_rotacao))
            quadro_transformado = aplicar_transformacao(quadro, matriz_rotacao)
            angulo_rotacao += velocidade_rotacao
            if angulo_rotacao >= 360:
                angulo_rotacao = 0

        elif cisalhamento_ativo and not rotacao_ativa:
            matriz_cisalhamento = cisalhamento_matriz(cisalhamento_x, cisalhamento_y)
            quadro_transformado = aplicar_transformacao(quadro, matriz_cisalhamento)

        elif cisalhamento_ativo and rotacao_ativa:
            matriz_rotacao = rotacao_matriz(np.radians(angulo_rotacao))
            quadro_rotacionado = aplicar_transformacao(quadro, matriz_rotacao)
            matriz_cisalhamento = cisalhamento_matriz(cisalhamento_x, cisalhamento_y)
            quadro_transformado = aplicar_transformacao(quadro_rotacionado, matriz_cisalhamento)
            angulo_rotacao += velocidade_rotacao
            if angulo_rotacao >= 360:
                angulo_rotacao = 0

        else:
            quadro_transformado = np.array(quadro).astype(float) / 255

        cv.imshow('Minha Imagem!', quadro_transformado)

        key = cv.waitKey(1)

        if key == ord('s'):
            break

        if key == ord('c'):
            cisalhamento_ativo = not cisalhamento_ativo

        if key == ord('r'):
            rotacao_ativa = not rotacao_ativa

        if key == 27:
            rotacao_ativa = False
            cisalhamento_ativo = False

        if key == ord('a'):
            velocidade_rotacao = max(1, velocidade_rotacao - 1)

        if key == ord('d'):
            velocidade_rotacao += 1

    camera.release()
    cv.destroyAllWindows()

run()
