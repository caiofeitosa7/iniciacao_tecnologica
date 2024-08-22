import pandas as pd
import pymysql


def criar_tabela_acesso(cursor):
	try:
		cursor.execute("""
			CREATE TABLE acesso (
			    codigo    INTEGER PRIMARY KEY AUTO_INCREMENT,
			    descricao VARCHAR(20)
			);
		""")
		print("Tabela 'acesso' criada...")
	except e:
		print('Erro na criação da tabela acesso:', e)


def criar_tabela_usuario(cursor):
	try:
		cursor.execute("""
			CREATE TABLE usuario
			(
			    codigo      INTEGER PRIMARY KEY AUTO_INCREMENT,
			    nome        VARCHAR(255),
			    funcao      VARCHAR(100),
			    usuario     VARCHAR(100),
			    senha       VARCHAR(50),
			    tipo_acesso INTEGER,
			    FOREIGN KEY (tipo_acesso) REFERENCES acesso (codigo)
			);
		""")
		print("Tabela 'usuario' criada...")
		
	except  e:
		print('Erro na criação da tabela usuario:', e)


def criar_tabela_estado_ficha(cursor):
	try:
		cursor.execute("""
			CREATE TABLE estado_ficha
			(
			    codigo    INTEGER PRIMARY KEY AUTO_INCREMENT,
			    descricao VARCHAR(25)
			);
		""")
		print("Tabela 'estado_ficha' criada...")
	except  e:
		print('Erro na criação da tabela estado_ficha:', e)
		
		
def criar_tabela_tipo_campo(cursor):
	try:
		cursor.execute("""
			CREATE TABLE tipo_campo
			(
			    codigo INTEGER PRIMARY KEY AUTO_INCREMENT,
			    nome   VARCHAR(25)
			);
		""")
		print("Tabela 'tipo_campo' criada...")
	except  e:
		print('Erro na criação da tabela tipo_campo:', e)


def criar_tabela_tipo_ficha(cursor):
	try:
		cursor.execute("""
			CREATE TABLE acesso (
			    codigo    INTEGER PRIMARY KEY AUTO_INCREMENT,
			    descricao VARCHAR(20)
			);
		""")
		print("Tabela 'tipo_ficha' criada...")
	except  e:
		print('Erro na criação da tabela tipo_ficha:', e)
		
		
def criar_tabela_campo(cursor):
	try:
		cursor.execute("""
			CREATE TABLE campo
			(
			    codigo         INTEGER PRIMARY KEY AUTO_INCREMENT,
			    nome           VARCHAR(150),
			    descricao      VARCHAR(255),
			    cod_tipo_campo INTEGER,
			    FOREIGN KEY (cod_tipo_campo) REFERENCES tipo_campo (codigo)
			);
		""")
		print("Tabela 'campo' criada...")
	except e:
		print('Erro na criação da tabela campo:', e)
		
		
def criar_tabela_campo_tipo_ficha(cursor):
	try:
		cursor.execute("""
			CREATE TABLE campo_tipo_ficha
			(
			    codigo         INTEGER PRIMARY KEY AUTO_INCREMENT,
			    cod_tipo_ficha INTEGER,
			    cod_campo      INTEGER,
			    FOREIGN KEY (cod_tipo_ficha) REFERENCES tipo_ficha (codigo),
			    FOREIGN KEY (cod_campo) REFERENCES campo (codigo)
			);
		""")
		print("Tabela 'campo_tipo_ficha' criada...")
	except e:
		print('Erro na criação da tabela campo_tipo_ficha:', e)
		
		
def criar_tabela_ficha(cursor):
	try:
		cursor.execute("""
			CREATE TABLE ficha
			(
			    codigo         INTEGER PRIMARY KEY AUTO_INCREMENT,
			    setor          VARCHAR(255),
			    prontuario     BIGINT,
			    cod_estado     INTEGER,
			    cod_tipo_ficha INTEGER,
			    FOREIGN KEY (cod_estado) REFERENCES estado_ficha (codigo),
			    FOREIGN KEY (cod_tipo_ficha) REFERENCES tipo_ficha (codigo)
			);
		""")
		print("Tabela 'ficha' criada...")
	except e:
		print('Erro na criação da tabela ficha:', e)


def criar_tabela_valorcampo(cursor):
	try:
		cursor.execute("""
			CREATE TABLE valorcampo
			(
			    codigo         INTEGER PRIMARY KEY AUTO_INCREMENT,
			    valor_string   TEXT   DEFAULT NULL,
			    valor_numerico BIGINT DEFAULT NULL,
			    valor_data     DATE   DEFAULT NULL,
			    cod_ficha      INTEGER,
			    cod_campo      INTEGER,
			    FOREIGN KEY (cod_campo) REFERENCES campo (codigo),
			    FOREIGN KEY (cod_ficha) REFERENCES ficha (codigo)
			);
		""")
		print("Tabela 'valorcampo' criada...")
	except e:
		print('Erro na criação da tabela valorcampo:', e)


def criar_tabela_arquivo(cursor):
	try:
		cursor.execute("""
			CREATE TABLE arquivo
			(
			    codigo          INTEGER PRIMARY KEY AUTO_INCREMENT,
			    nome_original   VARCHAR(255) DEFAULT NULL,
			    nome_armazenado VARCHAR(255) DEFAULT NULL,
			    extensao        VARCHAR(7)   DEFAULT '.geracao_pdf',
			    url             VARCHAR(500) DEFAULT NULL,
			    data_cadastro   DATE         DEFAULT NULL,
			    data_deletado   DATE         DEFAULT NULL,
			    deletado        TINYINT      DEFAULT 0,
			    cod_ficha       INTEGER,
			    FOREIGN KEY (cod_ficha) REFERENCES ficha (codigo)
			);
		""")
		print("Tabela 'arquivo' criada...")
	except e:
		print('Erro na criação da tabela arquivo:', e)


def criar_tabela_observacao(cursor):
	try:
		cursor.execute("""
			CREATE TABLE observacao
			(
			    codigo                 INTEGER PRIMARY KEY AUTO_INCREMENT,
			    descricao              VARCHAR(1200),
			    concluida              INTEGER,
			    cod_ficha              INTEGER,
			    cod_usuario_autor      INTEGER,
			    cod_usuario_concluinte INTEGER,
			    dataHora_cadastro      DATETIME,
			    dataHora_concluida     DATETIME,
			    FOREIGN KEY (cod_ficha) REFERENCES ficha (codigo),
			    FOREIGN KEY (cod_usuario_autor) REFERENCES usuario (codigo),
			    FOREIGN KEY (cod_usuario_concluinte) REFERENCES usuario (codigo)
			);
		""")
		print("Tabela 'observacao' criada...")
	except e:
		print('Erro na criação da tabela observacao:', e)


def descrever_tipo_ficha(cursor):
	cursor.execute("""
		DESCRIBE tipo_ficha;
	""")
	print(cursor.fetchall())


def preencher_tabela_acesso(cursor):
	acessos = pd.read_csv('acesso.csv', sep=',')

	for _, linha in acessos.iterrows():
		cursor.execute(f"""
			INSERT INTO acesso (descricao)
			VALUES ('{linha['descricao']}');
		""")


def preencher_tabela_usuario(cursor):
	usuarios = pd.read_csv('usuario.csv', sep=',')

	for _, linha in usuarios.iterrows():
		cursor.execute(f"""
			INSERT INTO usuario (nome, funcao, usuario, senha, tipo_acesso)
			VALUES ('{linha['nome']}', '{linha['funcao']}', '{linha['usuario']}', '{linha['senha']}', {linha['tipo_acesso']});
		""")


def preencher_tabela_estado_ficha(cursor):
	estados = pd.read_csv('estado_ficha.csv')

	for _, linha in estados.iterrows():
		cursor.execute(f"""
			INSERT INTO estado_ficha (descricao)
			VALUES ('{linha['descricao']}');
		""")


def preencher_tabela_tipo_campo(cursor):
	tipos = pd.read_csv('tipo_campo.csv')

	for _, linha in tipos.iterrows():
		cursor.execute(f"""
			INSERT INTO tipo_campo (nome)
			VALUES ('{linha['nome']}');
		""")


def preencher_tabela_tipo_ficha(cursor):
	tipos = pd.read_csv('tipo_ficha.csv')

	for _, linha in tipos.iterrows():
		cursor.execute(f"""
			INSERT INTO tipo_ficha (nome, arquivoHTML, ativo)
			VALUES ('{linha['nome']}', '{linha['arquivoHTML']}', {linha['ativo']});
		""")


def preencher_tabela_campo(cursor):
	campos = pd.read_csv('campo.csv')

	for _, linha in campos.iterrows():
		cursor.execute(f"""
			INSERT INTO campo (nome, descricao, cod_tipo_campo)
			VALUES ('{linha['nome']}', '{linha['descricao']}', {linha['cod_tipo_campo']});
		""")
		

def preencher_tabela_campo_tipo_ficha(cursor):
	campos = pd.read_csv('campo_tipo_ficha.csv')

	for _, linha in campos.iterrows():
		cursor.execute(f"""
			INSERT INTO campo_tipo_ficha (cod_tipo_ficha, cod_campo)
			VALUES ({linha['cod_tipo_ficha']}, {linha['cod_campo']});
		""")


def mostrar_tipos_ficha(cursor):
	cursor.execute("""
		SELECT * FROM tipo_ficha;
	""")

	print(cursor.fetchall())


if __name__ == '__main__':
	conexao = pymysql.connect(
		host='127.0.0.1',
		user='root',
		database='ana',
		cursorclass=pymysql.cursors.DictCursor,
		password='suc0_b0l4ch4'
	)
	
	cursor = conexao.cursor()
	
	criar_tabela_acesso(cursor)
	criar_tabela_usuario(cursor)
	criar_tabela_estado_ficha(cursor)		
	criar_tabela_tipo_campo(cursor)
	criar_tabela_tipo_ficha(cursor)		
	criar_tabela_campo(cursor)
	criar_tabela_campo_tipo_ficha(cursor)		
	criar_tabela_ficha(cursor)
	criar_tabela_valorcampo(cursor)
	criar_tabela_arquivo(cursor)
	criar_tabela_observacao(cursor)

	preencher_tabela_acesso(cursor)
	preencher_tabela_usuario(cursor)
	preencher_tabela_estado_ficha(cursor)
	preencher_tabela_tipo_ficha(cursor)
	preencher_tabela_tipo_campo(cursor)
	preencher_tabela_campo(cursor)
	preencher_tabela_campo_tipo_ficha(cursor)

	mostrar_tipos_ficha(cursor)
	
	conexao.commit()
	conexao.close()
