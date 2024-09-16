import numpy as np
import cv2 as cv

def rotacao_matriz(theta):
    x = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return x

def cisalhamento_matriz(shx, shy):
    cisalhar = np.array([[1, shx, 0],
                         [shy, 1, 0],
                         [0, 0, 1]])
    return cisalhar

def aplicar_rotacao(image, angulo_rotacao):
    altura, largura = image.shape[:2]
    cx, cy = largura // 2, altura // 2
    rotacao = rotacao_matriz(np.radians(angulo_rotacao))
    imagem_rotacionada = np.zeros_like(image)

    for y in range(altura):
        for x in range(largura):
            x_rel = x - cx
            y_rel = y - cy

            x_rot = rotacao[0, 0] * x_rel + rotacao[0, 1] * y_rel
            y_rot = rotacao[1, 0] * x_rel + rotacao[1, 1] * y_rel

            x_rot = int(x_rot + cx)
            y_rot = int(y_rot + cy)

            if 0 <= x_rot < largura and 0 <= y_rot < altura:
                imagem_rotacionada[y, x] = image[y_rot, x_rot]

    return imagem_rotacionada

def aplicar_cisalhamento(image, cisalhamento_x, cisalhamento_y):
    altura, largura = image.shape[:2]
    cx, cy = largura // 2, altura // 2
    cisalhamento = cisalhamento_matriz(cisalhamento_x, cisalhamento_y)
    imagem_cisalhada = np.zeros_like(image)

    for y in range(altura):
        for x in range(largura):
            x_rel = x - cx
            y_rel = y - cy

            x_cisalhado = cisalhamento[0, 0] * x_rel + cisalhamento[0, 1] * y_rel
            y_cisalhado = cisalhamento[1, 0] * x_rel + cisalhamento[1, 1] * y_rel

            x_cisalhado = int(x_cisalhado + cx)
            y_cisalhado = int(y_cisalhado + cy)

            if 0 <= x_cisalhado < largura and 0 <= y_cisalhado < altura:
                imagem_cisalhada[y, x] = image[y_cisalhado, x_cisalhado]

    return imagem_cisalhada

def run():
    camera = cv.VideoCapture(0)
    width = 320
    height = 240

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
            quadro_transformado = aplicar_rotacao(quadro, angulo_rotacao)
            angulo_rotacao += velocidade_rotacao
            if angulo_rotacao >= 360:
                angulo_rotacao = 0

        elif cisalhamento_ativo and not rotacao_ativa:
            quadro_transformado = aplicar_cisalhamento(quadro, cisalhamento_x, cisalhamento_y)

        elif cisalhamento_ativo and rotacao_ativa:
            quadro_transformado = aplicar_rotacao(quadro, angulo_rotacao)
            quadro_transformado = aplicar_cisalhamento(quadro_transformado, cisalhamento_x, cisalhamento_y)
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

        print(f"Velocidade: {velocidade_rotacao}")

    camera.release()
    cv.destroyAllWindows()

run()
