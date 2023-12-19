# windows命令
1. 检查用户账户列表
   ```bash
   net user
   ```
2. 检查账户状态
   ```bash
   net user "用户名"
   ```
3. 启用管理员账户并设置密码
   ```bash
    net user Administrator admin123
    net user Administrator /active:yes
    shutdown /r
   ```
4. 禁用管理员账户
   ```bash
    net user Administrator /active:no
    shutdown /r
   ```
## 绕过账户进入系统
1. 按住 shift 键 不要放，然后点击屏幕上的 电源图标 菜单的重启键，重启进入 高级模式，选择 troubleshooting （疑难解答）—— Advanced options (高级选项) —— Command prompt (命令提示符 )
2. 使用命令行 修改 cmd.exe 程序的 名字 
   ```bash
    C:
    cd windows\system32
    ren Utilman.exe Utilman_temp.exe
    ren cmd.exe Utilman.exe
    shutdown /r
   ```
3. 使用命令行 修改密码 或者 启用 Administrator 登录，登录页面，点击电源按钮旁边的 【ease of acess】（轻松使用）图标 进入命令行
   ```bash
    net user
    net user test mima1234
    net user Administrator admin123
    net user Administrator /active:yes
    shutdown /r
   ```
4. 将 cmd.exe 命令的名字重新改回去。重启过程一直按住 shit 键，进入 高级模式 （仍然选择启用命令提示符 ）
   ```bash
    C:
    cd windows/system32
    ren Utilman.exe cmd.exe
    ren Utilman_temp.exe Utilman.exe
    shutdown /r
   ```
5. 禁用 Administrator 用户，切换到 Administrator 身份，登录后 按 win + R 组合键，输入 cmd 进入命令行模式，运行下面的命令
   ```bahs
    net user Administrator /active:no
    shutdown /r
   ```