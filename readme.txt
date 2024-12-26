Trabajo realizado por Carolina Fernández, NIE:X5438988F

SISTEMA DE CONTROL DE VERSIONES

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

Añadimos un error en el software: no se añaden dígitos a pesar de que se deben añadir.
Hook: el script generado para hook hace que no se puedan hacer commit de aquellos archivos
que contengan error de sintaxis (como son paréntesis en funciones).