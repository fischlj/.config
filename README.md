# .config

- neovim 的配置

```sh
# 在vim里面输入，安装
:PlugInstall
:CocInstall coc-pyright coc-markdownlint
:Copilot setup
```

- ranger 的配置

- git 配置

```bash
git config --global credential.helper store
git config --global user.email "name@email.com"
git config --global user.name "name"

# my git
git config --global credential.helper store
git config --global user.email "fischl.j@protonmail.com"
git config --global user.name "fischlj"
```

- 自动更新git项目的功能
```
在 ~/.zshrc 文件中加上 alias auto_git="python3 ~/git/.config/fischl/auto_git.py"
然后 source ~/.zshrc
先store设置密码保存，然后手动git push 一下，保存密码
最后测试一下在命令行输入: auto_git 体验
```

