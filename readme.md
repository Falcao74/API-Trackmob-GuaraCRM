# Consumo de dados API Trackmob - GuaraCRM
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Django?style=for-the-badge">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img alt="Mysql" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
<h1> </h1>

<h1> Descrição </h1>
<p>Implementação em Python do consumo dos dados, via API V1, disponibilizados pela Trackmob, para utilização dos recursos vindos do GuaraCRM</p>

<h1>Instalação e primeiro uso: </h1>

<ul>
<h2> Para instalar iniciar o projeto, digite os comandos abaixo: </h2>
        <li> python -m venv env </li>
        <li> source env/bin/activate (Linux) ou .\env\Scripts\activate (Windows) </li>
        <li> pip install -r requirements.txt </li>
</ul>

<h1> Criando as tabelas no seu banco de dados:</h1>
<ul>
    <li> Acesse o diretório SQL deste projeto </li>
    <li>Abra o arquivo <b>script.sql</b> que está dentro do diretório e copie o código.</li>
    <li>Crie um banco de dados MySQL com o nome que desejar na sua máquina ou na nuvem.</li>
    <li>Abra seu editor de SQL - Como o MySQL Workbench ou HeidiSQL ou outro.</li>
    <li>Crie uma nova consulta SQL, cole o código e execute.</li>
</ul>
    <br />

<h1> Setando o acesso ao banco de dados e inserindo o token: </h1>
<ul>
    <li> Renomeie o arquivo <b>settings_example.py </b>para <b>settings.py</b> </li>
    <li> Preencha os dados com o seu acesso. </li>
</ul>
<br />

<h1> Uso </h1>
<ul>
    <li>Com o banco de dados já criado;</li>
    <li>Ambiente virtual ativado (<b>env</b>);</li>
    <li>No terminal do VSCode, Sublime, ou prompt, digite: <b>python app.py</b></li>
</ul>

