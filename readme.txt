SISTEMA DE CONTROL DE VERSIONES

Práctica de git:
$ ls -a -> mostrar archivos ocultos
- Los comandos globales no los puede ver, especificar en el archivo de texto el comando utilizado
y una lista de aquellos que tengamos que se pueden ver dentro del .git.
- Los alias tienen que ser de comandos.
- Hacer un commit al menos a cada rama, y hacer un merge a main.

Configuraciones de alias:
- Local:
    git config alias.ss "status"
    git config alias.ch "checkout"
    git config alias.br "branch"
    git config alias.com "commit"

- Global:
    git config --global alias.ss "status"
    git config --global alias.ch "checkout"
    git config --global alias.br "branch"
    git config --global alias.com "commit"