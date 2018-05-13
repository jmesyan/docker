FROM php:7.1-fpm

# 安装 git curl vim zip
RUN apt-get update && apt-get install -y git curl vim libfreetype6-dev \
    && rm -rf /var/lib/apt/list* \
    && pecl install zip \
    && docker-php-ext-enable zip

# 安装 composer
RUN curl -o composer.phar https://getcomposer.org/download/1.4.1/composer.phar \
    && chmod +x composer.phar

# 配置 composer ，将镜像源改为中国国内
RUN mv composer.phar /usr/local/bin/composer \
     && echo 'export PATH="$PATH:$HOME/.composer/vendor/bin"' >> ~/.bashrc \
     && . ~/.bashrc \
     && composer config -g repo.packagist composer https://packagist.phpcomposer.com

# 设置 Git 的身份
RUN git config --global user.name "jieqiang1017@qq.com" \
    && git config --global user.email "yan172168"