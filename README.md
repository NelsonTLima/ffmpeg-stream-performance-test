# TESTE DE PERFORMANCE DO FFMPEG EM STREAM DE VIDEO

Esse repositório foi feito para a atividade de sistemas operacionais.
O objetivo da atividade é medir indices de performance do ffmpeg quando
está fazendo streaming de vídeo.

Para que isso seja possível, nós subiremos um servidor NGINX especialmente
compilado para para transmissão de vídeos no protocolo RTMP. Esse servidor
irá capturar a transmissão do stream de vídeo segmentado para HLS (HTTP Live
Streaming) com ffmpeg e redirecionar para uma página web que irá exibir o video.

Para garantir que o experimento seja reprodutível escrevemos um script em python
que irá iniciar os processos do servidor, do ffmpeg e acionar o gerador do relatório
que vai registrar as métricas do processo ffmpeg em períodos regulares de tempo.

## Dependencias

Para que o experimento funcione corretamente, será necessário utilizar na maquina do teste,
o docker-compose e, é claro, o próprio ffmpeg.

Pra instalar, caso esteja usando uma distribuição baseada em debian,
você pode tentar executar os seguintes comandos:

### Para instalar o ffmpeg

```bash
sudo apt install ffmpeg
```

### Para instalar o docker-compose

```bash
curl -SL https://github.com/docker/compose/releases/download/v2.29.6/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

Se o comando docker-compose não funcionar, talvez você deva criar um link simbólico para /usr/bin

```bash
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Os binários baixados da internet, por padrão não podem ser bicados, portanto, é necessário usar o comando chmod para aplicar
permissões de execução.

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

### Informações oficiais do docker-compose e do ffmpeg

Informações para baixar e instalar o docker-compose podem ser encontradas [aqui](https://docs.docker.com/compose/install/standalone/)<br>
Informações para baixar e instalar o FFMPEG podem ser encontradas [aqui](https://www.ffmpeg.org/download.html)

### plot charts

A função desse código é usar numpy, pandas e matplotlib para plotar as imagens dos gráficos, da mesma maneira, o script pip_install.py deve
funcionar nos sistemas baseados em debian para instalar essas 3 dependências pra gerar os gráficos. Você precisa instalar na sua máquina
se tiver intenção de gerar os graficos.

## Executando o experimento

Para iniciar o teste é basta executar o script em python usando permissão de superusuário
(root).

```bash
sudo python3 run-test.py
```
