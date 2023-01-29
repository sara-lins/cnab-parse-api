# CNAB Parse API

## Descrição do projeto (Project description)

Servidor elaborado para obter dados de parseamento de arquivos CNAB (Centro Nacional de Automação Bancária)

Server designed to obtain parsing data from CNAB files (National Banking Automation Center)

## Instalação dos pacotes (Installation of packages)

- Crie seu ambiente virtual (Create your virtual environment):

```bash
    python -m venv venv
```

- Ative a máquina virtual (Activate the virtual machine):

```shell
    source venv/bin/activate
```

- Rode o comando para instalar os pacotes que estão no arquivo requirements.txt (Run the command to install the packages that are in the requirements.txt file):

```shell
    pip install -r requirements.txt
```

## Testes (Tests):

- Rode os testes no diretório principal do projeto (Run the tests in the main project directory):

```shell
    pytest --testdox -vvs
```

- Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose** (If you want a more summarized log, just run with the tests without the flags **verbose**):

```shell
    pytest --testdox
```
