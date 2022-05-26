# 最新更新时间: 2022-05-25
# 此dockerfile文件在m1 pro芯片的mac book pro上测试通过
# 本镜像支持arm架构的机器，未在x86架构上的机器测试
FROM ubuntu:22.04

LABEL MAINTAINER="fischl.j@protonmail.com"

# 设置工作目录
WORKDIR /root
ARG WORK_DIR=work
RUN mkdir ${WORK_DIR}

# 软件源更新
RUN apt update && apt -y upgrade

# 基础依赖
RUN apt -y install wget curl git zip

# 系统默认地区、时间
ENV TZ=Asia/Shanghai
# RUN apt -y install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# 常用依赖
RUN apt -y install nodejs npm mlocate
RUN apt -y install tree neofetch neovim
RUN apt -y install ranger
# 文件查找 updatedb  locate est.file   locate /root/work a.py

# zsh配置
RUN apt -y install zsh \
    && sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)" \
    && sed -i '11c ZSH_THEME="apple"' /root/.zshrc

# python 依赖
RUN apt -y install python3 python3-dev python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

# 对中文的显示
RUN apt -y install locales language-pack-zh-hans fonts-wqy-zenhei \
    && echo 'LANG="zh_CN.UTF-8"' >> /etc/environment \
    && echo 'LANGUAGE="zh_CN:zh:en_US:en"' >> /etc/environment \
    && echo 'en_US.UTF-8 UTF-8' >> /var/lib/locales/supported.d/local \
    && echo 'zh_CN.UTF-8 UTF-8' >> /var/lib/locales/supported.d/local \
    && echo 'zh_CN.GBK GBK' >> /var/lib/locales/supported.d/local \
    && echo 'zh_CN GB2312' >> /var/lib/locales/supported.d/local \
    && echo "export LANG=zh_CN.UTF-8" >> /root/.bashrc \
    && echo "export LANG=zh_CN.UTF-8" >> /root/.zshrc
RUN ["locale-gen"]

# neovim 配置
RUN sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# 删除无用的安装包，缩小体积
RUN apt clean

# 安装 .config
RUN git clone https://github.com/fischlj/.config.git \
    && echo "some change"
# :PlugInstall
# :CocInstall coc-pyright coc-markdownlint 
# coc-python

# copilot 安装
RUN git clone https://github.com/github/copilot.vim.git ~/.config/nvim/pack/github/start/copilot.vim
# :Copilot setup

# 需要添加的功能：
# 配置ranger，使其更加好用，预览文件啥的
