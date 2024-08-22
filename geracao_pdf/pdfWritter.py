import os
import fitz  # type: ignore
from .script_ficha_base import generateFicha
import datetime

from infocare import settings


class PDFWriter:
    def __init__(self, pdf_path:str):
        self.document = fitz.open(pdf_path) 
        self.default_font = 'helvetica'
        self.default_font_size = 13
        self.default_color = (1, 0, 0)
    
    def write_date(self, date: str, pos: tuple, pg: int = 0, font_size=None, spacing=0):
        if font_size is None: font_size = self.default_font_size
        """
        Escreve uma data no PDF na posição especificada.
        
        Args:
            date (str): A data a ser escrita.
            pos (tuple): A posição (x, y) onde a data será escrita.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
            font_size (int, opcional): O tamanho da fonte a ser usada. Padrão é 13.
            spacing (int, opcional): O espaçamento entre os caracteres. Padrão é 0.
        """

        try:
            data = float(date)
            timestamp = datetime.datetime.fromtimestamp(data)
            day = timestamp.day
            month = timestamp.month
            year = timestamp.year
            date = f'{day:02}/{month:02}/{year}'
        except:
            if not date:
                date = ''
            date = date.replace('/', '')
        finally:
            date = (' ' * spacing).join(date)
            self.document[pg].insert_text(pos, date, fontsize=font_size, fontname=self.default_font, color=self.default_color)
            
    def write_uf(self, uf: str, pos: tuple, pg: int = 0):
        """
        Escreve uma UF (sigla do estado) no PDF na posição especificada.
        
        Args:
            uf (str): A sigla do estado a ser escrita.
            pos (tuple): A posição (x, y) onde a sigla será escrita.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
        """
        uf = ' '.join(uf).upper()
        self.document[pg].insert_text(pos, uf, fontsize=self.default_font_size, fontname=self.default_font, color=self.default_color)
    
    def write_text(self, text:str, pos: tuple, pg: int = 0, color=(1, 0, 0), font_size=10):
        if font_size is None: font_size = self.default_font_size

        """
        Escreve um texto arbitrário no PDF na posição especificada.
        
        Args:
            text (str): O texto a ser escrito.
            pos (tuple): A posição (x, y) onde o texto será escrito.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
            color (tuple, opcional): A cor do texto. Padrão é (1, 0, 0).
            font_size (int, opcional): O tamanho da fonte a ser usada. Padrão é 13, que usa o tamanho de fonte padrão.
        """

        if text == "0":
            text = ""

        self.document[pg].insert_text(pos, text, fontsize=font_size, fontname=self.default_font, color=color)
    
    def write_cep(self, code: str, pos: tuple, pg: int = 0, space=0, font_size=None):
        if font_size is None: font_size = self.default_font_size

        """
        Escreve um CEP (código postal) no PDF na posição especificada.
        
        Args:
            code (str): O código postal a ser escrito.
            pos (tuple): A posição (x, y) onde o código postal será escrito.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
            space (int, opcional): O espaçamento entre os caracteres. Padrão é 0.
            font_size (int, opcional): O tamanho da fonte a ser usada. Padrão é 13.
        """
        code = (' ' * space).join(code)
        alvo = (' ' * space + '-' + ' ' * space)
        code = code.replace(alvo, ' - ')
        self.document[pg].insert_text(pos, code, fontsize=font_size, fontname=self.default_font, color=self.default_color)

    def write_code(self, code: str, pos: tuple, pg: int = 0, space=0, font_size=None):
        if font_size is None: font_size = self.default_font_size
        
        """
        Escreve um código no PDF na posição especificada.
        
        Args:
            code (str): O código a ser escrito.
            pos (tuple): A posição (x, y) onde o código será escrito.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
            space (int, opcional): O espaçamento entre os caracteres. Padrão é 0.
            font_size (int, opcional): O tamanho da fonte a ser usada. Padrão é 13.
        """

        if code == "0":
            code = ""

        code = (' ' * space).join(code)
        self.document[pg].insert_text(pos, code, fontsize=font_size, fontname=self.default_font, color=self.default_color)
    
    def write_telefone(self, telefone: str, pos: tuple, space=0, pg: int = 0, font_size=None):
        if font_size is None: font_size = self.default_font_size
        """
        Escreve um número de telefone no PDF na posição especificada.
        
        Args:
            telefone (str): O número de telefone a ser escrito.
            pos (tuple): A posição (x, y) onde o número de telefone será escrito.
            space (int, opcional): O espaçamento entre os caracteres. Padrão é 0.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
        """
        
        telefone = telefone.replace('(', '').replace(')', '').replace('-', '')
        mod = 0 if len(telefone) == 11 else 1
        telefone = telefone[:2] + telefone[(3-mod):]
        telefone = (' ' * space).join(telefone).strip()
        
        self.document[pg].insert_text(pos, telefone, fontsize=font_size, fontname=self.default_font, color=self.default_color)
    
    def write_mini(self, text: str, pos: tuple, pg: int = 0, font_size=10, spacing=0):
        if font_size is None: font_size = self.default_font_size

        """
        Escreve um texto em tamanho reduzido no PDF na posição especificada.
        
        Args:
            text (str): O texto a ser escrito.
            pos (tuple): A posição (x, y) onde o texto será escrito.
            pg (int, opcional): O número da página onde escrever. Padrão é 0.
            size (int, opcional): O tamanho da fonte a ser usada. Padrão é 10.
            spacing (int, opcional): O espaçamento entre os caracteres. Padrão é 0.
        """

        if text == "0":
            text = ""

        text = str(text)
        text = (' ' * spacing).join(text)
        self.document[pg].insert_text(pos, text, fontsize=font_size, fontname=self.default_font, color=self.default_color)
    
    def write_box(self, text: str, pg: int, rect: tuple, color='red'):
        """
        Escreve um texto em uma caixa no PDF na posição especificada.
        
        Args:
            text (str): O texto a ser escrito.
            pg (int): O número da página onde escrever.
            rect (tuple): A posição e tamanho da caixa (x, y, width, height).
            color (str, opcional): A cor do texto. Padrão é 'red'.
        """

        if text == "0":
            text = ""

        text = str(text)
        self.document[pg].insert_htmlbox(rect, text, css='* {font-size: 12pt; font-family: Helvetica; text-align: justify; color:' + color + '; background-color: #fff; text-decoration-color: black;}')
    
    def save(self, nome_arquivo: str, path_pdf_gerado: str, dictcsv: dict = None, path_pdf_base: str = '', close_doc=True):
        """
        Salva o documento PDF com o nome especificado.
        
        Args:
            file_name (str): O nome do arquivo PDF a ser salvo.
            dictcsv (dict): O dicionário contendo os dados para gerar a ficha.
        """
        
        if dictcsv:
            notificatoria = generateFicha(dictcsv, path_pdf_base, path_pdf_gerado, nome_arquivo, close_doc=False)
            self.document.insert_pdf(notificatoria.document, start_at=0)
            notificatoria.document.close()

        path_arquivo = os.path.join(path_pdf_gerado, nome_arquivo)

        print('função save')
        print('salvando o arquivo:', path_arquivo)

        self.document.save(path_arquivo)

        if close_doc:
            self.document.close()
    