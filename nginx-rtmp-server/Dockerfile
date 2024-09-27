# syntax=docker/dockerfile:1
FROM debian

ENV NGINX_VERSION=1.23.2

RUN apt-get update && \
    apt-get install -y wget \
    unzip \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    openssl \
    libssl-dev \
    zlib1g-dev \
    ffmpeg

# Download and install nginx and rtmp module source code
RUN \
    cd /tmp && \
    wget https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
    tar -zxf nginx-${NGINX_VERSION}.tar.gz && \
    wget -O rtmp_module.zip https://github.com/arut/nginx-rtmp-module/archive/refs/heads/master.zip && \
    unzip rtmp_module.zip

RUN \
    cd /tmp/nginx-${NGINX_VERSION} && \
    ./configure \
    --sbin-path=/usr/local/sbin/nginx \
    --conf-path=/etc/nginx/nginx-conf \
    --error-log-path=/var/log/nginx/error.log \
    --pid-path=/var/run/nginx/nginx.pid \
    --lock-path=/var/lock/nginx/nginx.lock \
    --http-log-path=/var/log/nginx/access.log \
    --http-client-body-temp-path=/tmp/nginx-client-body \
    --with-http_ssl_module \
    --with-threads \
    --with-ipv6 \
    --add-module=/tmp/nginx-rtmp-module-master \
    --with-debug && \
    make && make install

# Copy configuration files
COPY nginx.conf /etc/nginx/nginx-conf

# Copy website source code
COPY html/* /usr/local/nginx/html

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 1935 4000
CMD ["nginx", "-g", "daemon off;"]
