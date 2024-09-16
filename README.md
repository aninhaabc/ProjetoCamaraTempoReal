# Real-Time Video Effects Processor

**Versão:** 1.0  
**Desenvolvido por:** Ana Beatriz da Cunha e Manoela Saragoca

## 📝 Descrição

Este projeto consiste na criação de um processador de efeitos de vídeo em tempo real usando Python. O objetivo principal é aplicar transformações, como rotação e cisalhamento, no *streaming* de vídeo capturado diretamente da câmera, em tempo real. A implementação segue o estudo de transformações de imagens baseado em álgebra linear, utilizando a biblioteca NumPy para cálculos matriciais. O programa realiza a rotação da imagem ao redor do seu centro e permite ajustar a velocidade da rotação, além de incluir um efeito de cisalhamento controlado pelo usuário.

## Importante !!!

Para rodar o projeto tem que está dentro do arquivo **camera_tempo_real.py**.


## Funcionalidades

- Rotação em tempo real do vídeo capturado, ao redor do centro da imagem.
- Controle da velocidade de rotação por meio do teclado.
- Efeito de cisalhamento ajustável em tempo real.
- Integração dos efeitos de rotação e cisalhamento simultaneamente.

## 📚 Instruções de Instalação

### Pré-requisitos:

- **Python 3.11**  
  O jogo foi desenvolvido e testado usando o Python 3.11. Certifique-se de que essa versão esteja instalada no seu sistema.

  Para baixar e instalar o Python 3.11, acesse o site oficial através deste link: [Download Python 3.11](https://www.python.org/downloads/release/python-3110/)

### Como instalar

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/aninhaabc/projcameratemporeal.git
   cd projcameratemporeal

2. **Instalar o jogo com 'pip'**
    ```bash
    pip install git+https://github.com/aninhaabc/projcameratemporeal.git

3. **Executar o jogo**
    ```bash
    cameratemporeal 

## 💻 Estrutura do Código
A estrutura do código está organizada em módulos para facilitar a navegação e manutenção do projeto:

- projetocameratemporeal/: Diretório principal do projeto.

    - `requirements.txt`: Arquivo contendo as dependências necessárias para rodar o projeto.
    
    - `README.md`: Documentação do projeto, descrevendo seu funcionamento e como utilizar.

    - `setup.py`: Script para instalação do projeto.

    - aps/: Contém o código principal responsável pela captura e transformação do vídeo em tempo real.

        - `camera_tempo_real.py`: Arquivo que implementa as funcionalidades de rotação e cisalhamento no vídeo capturado da câmera.


