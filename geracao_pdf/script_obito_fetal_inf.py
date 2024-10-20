from .pdfWritter import PDFWriter


def gerar_pdf_obt_fetal_inf(dict_especifico: dict, modelo_pdf: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    document.write_code(dict_especifico['numero_ficha'], (452, 43), space=3)
    if dict_especifico['op_obito_fetal_DO'] == '1':
        document.write_cross((375, 65))
    document.write_text(dict_especifico['nome_paciente'], (81, 81))
    #verificar sexo é M ou F
    if dict_especifico['sexo'] == 'op-sexo-m':
        document.write_cross((418, 78))
    elif dict_especifico['sexo'] == 'op-sexo-f':
        document.write_cross((436, 78))
    document.write_code(dict_especifico['semanas_gestacao'], (137, 96), space=2)
    document.write_code(dict_especifico['idade_obito'], (228, 96), space=2)
    #verificar tipo de idade
    if dict_especifico['tp_idade_obito'] == 'tp-idade-obito-meses':
        document.write_cross((260, 99))  #meses
    elif dict_especifico['tp_idade_obito'] == 'tp-idade-obito-dias':
        document.write_cross((293, 99))  #dias
    elif dict_especifico['tp_idade_obito'] == 'tp-idade-obito-horas':
        document.write_cross((318, 99))  #horas
    elif dict_especifico['tp_idade_obito'] == 'tp-idade-obito-min':
        document.write_cross((350, 99))  #minutos
    document.write_code(dict_especifico['peso'], (422, 94), space=3)
    #verificar tipo de peso
    if dict_especifico['tp_peso'] == 'tp-peso-gr':
        document.write_cross((493, 96))  #gramas
    elif dict_especifico['tp_peso'] == 'tp-peso-kg':
        document.write_cross((514, 96))  #quilogramas
    document.write_date(dict_especifico['dt_obito'], (124, 117), spacing=3)
    document.write_code(dict_especifico['num_DO'], (350, 115), space=3, font_size=12)
    document.write_date(dict_especifico['dt_nascimento'], (124, 137), spacing=3)
    document.write_code(dict_especifico['num_DN'], (352, 134), space=3, font_size=12)
    document.write_text(dict_especifico['ender_responsavel'], (195, 158), font_size=9)
    document.write_telefone(dict_especifico['telefone_responsavel'][:2], (464, 156), font_size=11)
    document.write_telefone(dict_especifico['telefone_responsavel'][2:], (479, 156), font_size=11)
    document.write_text(dict_especifico['municipio_responsavel'], (195, 173))
    document.write_code(dict_especifico['uf_responsavel'], (468, 171), space=2)
    document.write_code(dict_especifico['num_cartao_sus_mae'], (431, 192))
    document.write_text(dict_especifico['nome_mae'], (108, 212))
    document.write_code(dict_especifico['idade_mae'], (465, 205), space=2)
    # verificar raça da mãe
    if dict_especifico['raca_mae'] == 'raca-branca':
        document.write_cross((98, 227))  # branca
    elif dict_especifico['raca_mae'] == 'raca-preta':
        document.write_cross((129, 227))  # preta
    elif dict_especifico['raca_mae'] == 'raca-indigena':
        document.write_cross((159, 227))  # indigena
    elif dict_especifico['raca_mae'] == 'raca-parda':
        document.write_cross((98, 242))  # parda
    elif dict_especifico['raca_mae'] == 'raca-amarela':
        document.write_cross((129, 242))  # amarela

    document.write_text(dict_especifico['etnia_indig_mae'], (325, 227))  #se indigena etnia
    document.write_text(dict_especifico['aldeia_mae'], (325, 242))  #se indigena aldeia
    #se nao aldeada
    if dict_especifico['nao_aldeada_mae'] == '1':
        document.write_cross((477, 243))

    document.write_text(dict_especifico['nome_hospital2'], (109, 279))  #nome do hospital
    document.write_code(dict_especifico['cod_cnes_us'], (425, 273), space=4, font_size=10)  #cnes
    document.write_text(dict_especifico['municipio_hospital2'], (110, 301))  #municipio
    document.write_code(dict_especifico['uf_hospital2'], (348, 296), space=2)  #uf
    #verificar tipo de estabelecimento
    if dict_especifico['tipo_estab'] == 'tipo-estab-SUS':
        document.write_cross((442, 294))  #tipo SUS
    elif dict_especifico['tipo_estab'] == 'tipo-estab-convenio-SUS':
        document.write_cross((464, 294))  #tipo CONVENIO SUS
    elif dict_especifico['tipo_estab'] == 'tipo-estab-privado':
        document.write_cross((442, 303))  #tipo PRIVADO
    elif dict_especifico['tipo_estab'] == 'tipo-estab-outro':
        document.write_cross((476, 303))  #tipo OUTRO
    document.write_code(dict_especifico['pront_crianca'], (132, 315))  #prontuario criança
    document.write_code(dict_especifico['pront_mae'], (450, 315))  #prontuario mae

    # IV admissao da mae gestante no hospital/maternindade opt nao se aplica pular tudo IV
    if dict_especifico['op_admiss_mae_NSA'] == '1':
        document.write_cross((478, 331))  #op de nao se aplica
    document.write_date(dict_especifico['dt_admiss_mae'], (125, 342), spacing=3)  #dt_admiss_mae
    document.write_hrmin(dict_especifico['hora_admiss_mae'], (364, 342), space=3)  # hora
    document.write_code(dict_especifico['idade_gestacional'], (142, 360), space=2)  #idade gestacional
    #verificar tipo dum / exam fisico / outro / n se aplica
    if dict_especifico['tp_idade_gest'] == 'idade-gestacional-DUM':
        document.write_cross((220, 362))  # dum
    elif dict_especifico['tp_idade_gest'] == 'idade-gestacional-exame-fisico':
        document.write_cross((390, 362))  # exam fisico
    elif dict_especifico['tp_idade_gest'] == 'idade-gestacional-outro':
        document.write_cross((442, 362))  # outro
    elif dict_especifico['tp_idade_gest'] == 'idade-gestacional-naoSeAplica':
        document.write_cross((478, 362))  # n se aplica
    document.write_date(dict_especifico['dt_dum'], (250, 360), spacing=3)  #dt dum
    #if preferencia de formato xxx/xxx if not '/' insert '/' in the middle
    if '/' not in dict_especifico['press_art_adm_mae']:
        dict_especifico['press_art_adm_mae'] = (dict_especifico['press_art_adm_mae'][:3]
                                                + '/' + dict_especifico['press_art_adm_mae'][3:])
    document.write_code(dict_especifico['press_art_adm_mae'], (202, 382), space=2)  #pressao arterial item 23
    #verificar opcao de obito da mae na admissao caso true pular para 27
    if dict_especifico['op_mae_obito_admissao'] == '1':
        document.write_cross((393, 385))  #opca de chegou em obito
    #verificar tipo de parto campo 24
    if dict_especifico['parto_admissao'] == 'parto-admisso-antes':
        document.write_cross((233, 403))  #antes do inicio do trabalho
    elif dict_especifico['parto_admissao'] == 'parto-admisso-periodo-naoExpulsivo':
        document.write_cross((335, 403))  #No periodo não expulsivo
    elif dict_especifico['parto_admissao'] == 'parto-admisso-periodo-expulsivo':
        document.write_cross((446, 403))  #No periodo expulsivo
    #verificar opcao de registro clinico 25 se true pular
    if dict_especifico['op_reg_clinico_admiss'] == '1':
        document.write_cross((478, 416))  #opcao de registro clinico 25
    document.write_code(dict_especifico['contracoes_10min'], (148, 431), space=2)  #contracoes por 10 min
    #verificar apresentacao fetal
    if dict_especifico['apresentacao_fetal'] == 'apresentacao-fetal-cefalica':
        document.write_cross((141, 451))  #cefalica
    elif dict_especifico['apresentacao_fetal'] == 'apresentacao-fetal-pelvica':
        document.write_cross((179, 451))  #pelvica
    elif dict_especifico['apresentacao_fetal'] == 'apresentacao-fetal-outra':
        document.write_cross((214, 451))  #Outra
    #verificar bcf
    if dict_especifico['bcf'] == 'op-bcf-positivo':
        document.write_cross((121, 467))  #positivo
    elif dict_especifico['bcf'] == 'op-bcf-negativo':
        document.write_cross((221, 467))  #negativo
    document.write_code(dict_especifico['bcf_posit_descricao'], (163, 465), space=2)  #descricao do positivo
    document.write_code(dict_especifico['descida_apresent'], (168, 484), space=2)  #descida da apresentacao
    document.write_code(dict_especifico['dilatacao_colo'], (401, 431), space=2)  #dilatacao do colo
    #verificar membrana
    if dict_especifico['membrana'] == 'op-membrana-integra':
        document.write_cross((393, 451))  #integra
    elif dict_especifico['membrana'] == 'op-membrana-rota':
        document.write_cross((432, 451))  #rotas
    document.write_code(dict_especifico['rotas_tempo'], (400, 465), space=2)  #rotas e tempo
    #verificar liquido amniotico
    if dict_especifico['rotas_liqAmniotico'] == 'rotas-liqAmniotico-claro':
        document.write_cross((393, 488))  #claro
    elif dict_especifico['rotas_liqAmniotico'] == 'rotas-liqAmniotico-meconial':
        document.write_cross((420, 488))  #meconial
    elif dict_especifico['rotas_liqAmniotico'] == 'rotas-liqAmniotico-fetido':
        document.write_cross((461, 488))  #Fétido
    elif dict_especifico['rotas_liqAmniotico'] == 'rotas-liqAmniotico-outro':
        document.write_cross((491, 488))  #Outro
    #!campo 26
    #verificar motivo de internacao
    if dict_especifico['motivo_inter'] == 'op-motivo-internacao-prematuro':
        document.write_cross((55, 521))  #prematuridade
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-posDatismo':
        document.write_cross((160, 521))  #pós-datismo
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-ruptura':
        document.write_cross((213, 521))  #rupturas de membranas
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-preEclampsia':
        document.write_cross((335, 521))  #pré-eclampsia
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-eclampsia':
        document.write_cross((387, 521))  #eclampsia
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-sangTransvaginal':
        document.write_cross((437, 521))  #Sangramento Transvaginal
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-cesariaAgendada':
        document.write_cross((56, 536))  #cesarea agendada
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-febre':
        document.write_cross((160, 536))  #febre
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-dimMovFecais':
        document.write_cross((213, 536))  #diminuicao mov fetais
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-outros':
        document.write_cross((335, 536))  #outros
    elif dict_especifico['motivo_inter'] == 'op-motivo-internacao-nenhum':
        document.write_cross((437, 536))  #nenhum dos anteriores
    document.write_box(dict_especifico['motivo_inter_descricao'],
                       rect=(55, 544, 550, 585))  #descricao do motivo de internacao
    #*parte V historia obstetrica op N se aplica
    #verificar opcao de historia obstetrica
    if dict_especifico['op_hist_obstet_NSA'] == '1':
        document.write_cross((474, 600))  #opcao de historia obstetrica
    #!campo 27
    document.write_code(dict_especifico['num_gest_anteriores'], (73, 627),
                        space=2)  #numero de gestacoes anteriores se 00 go to campo 29
    document.write_code(dict_especifico['quant_abortos'], (203, 627), space=2)  #numero de abortos
    document.write_code(dict_especifico['quant_partos'], (259, 627), space=2)  #numero de partos
    document.write_code(dict_especifico['quant_vaginais'], (308, 627), space=2)  #numero de partos vaginais
    document.write_code(dict_especifico['quant_cesarias'], (358, 627), space=2)  #numero de cesarias
    document.write_code(dict_especifico['quant_vivos'], (413, 627), space=2)  #numero de vivos
    document.write_code(dict_especifico['ano_ult_parto'], (471, 627), space=2)  #ano do ultimo parto
    #!campo 28
    if dict_especifico['doen_gest_anterior'] == 'doenca-gestacao-anterior-nao':
        document.write_cross((203, 643))  #doencas na gestacao anterior nao
    elif dict_especifico['doen_gest_anterior'] == 'doenca-gestacao-anterior-sim':
        document.write_cross((249, 645))  #doencas na gestacao anterior sim

    document.write_text(dict_especifico['doen_gest_ante_sim_desc'], (295, 645))  #descricao doencas na gestacao anterior
    #!campo 29
    if dict_especifico['doen_fora_gest'] == 'doenca-fora-gestacao-nao':
        document.write_cross((203, 660))  #doencas fora da gestacao nao
    elif dict_especifico['doen_fora_gest'] == 'doenca-fora-gestacao-sim':
        document.write_cross((248, 662))  #doencas fora da gestacao sim
    document.write_text(dict_especifico['doen_fora_gest_sim_desc'], (295, 662))  #descricao doencas fora da gestacao
    #*parte VI internacao hospitalar da mae-gestante op N se aplica
    #verificar opcao de internacao hospitalar
    if dict_especifico['op_inter_mae_NSA'] == '1':
        document.write_cross((466, 677))  #opcao de internacao hospitalar
    #!campo 30
    document.write_date(dict_especifico['dt_internacao_mae'], (142, 691), spacing=3)  #dt internacao
    document.write_hrmin(dict_especifico['hora_internacao_mae'], (442, 691), space=3)  #casa da hora
    #!campo 31
    if dict_especifico['parto_internacao'] == 'parto-internacao-sim':
        document.write_cross((179, 709))  #parto na internacao sim
    elif dict_especifico['parto_internacao'] == 'parto-internacao-nao':
        document.write_cross((234, 709))  #parto na internacao nao
    #!campo 32
    #verificar utilizacao de partograma
    if dict_especifico['util_partograma'] == 'utilizou-partograma-sim':
        document.write_cross((176, 725))  #utilizou partograma sim
    elif dict_especifico['util_partograma'] == 'utilizou-partograma-nao':
        document.write_cross((200, 725))  #utilizou partograma nao
    document.write_text(dict_especifico['util_partograma_obs'], (288, 725))  #descricao partograma
    #!campo 33
    #verificar opcao de avaliacao do parto
    if dict_especifico['op_av_parto_NSA'] == '1':
        document.write_cross((467, 741))  #opcao de avaliacao do parto
    document.write_code(dict_especifico['quant_maternas'], (326, 740), space=2)  #quantidade de maternas
    document.write_code(dict_especifico['quant_fetais'], (411, 740), space=2)  #quantidade de fetais
    #!campo 34
    #verificar intercorrencia materna
    if dict_especifico['op_inter_aval_NSA'] == '1':
        document.write_cross((467, 758))  #opcao de intercorrencia
    if dict_especifico['inter_aval_materna'] == 'intervalo-avaliacoes-materna-sim':
        document.write_cross((315, 758))  #intercorrencia materna sim
    elif dict_especifico['inter_aval_materna'] == 'intervalo-avaliacoes-materna-nao':
        document.write_cross((337, 758))  #intercorrencia materna nao
    #verificar intercorrencia fetal
    if dict_especifico['inter_aval_fetal'] == 'intervalo-avaliacoes-fetal-sim':
        document.write_cross((399, 758))  #intercorrencia fetal sim
    elif dict_especifico['inter_aval_fetal'] == 'intervalo-avaliacoes-fetal-nao':
        document.write_cross((421, 758))  #intercorrencia fetal nao

    #===================== FIM DA PRIMEIRA PAGINA =======================

    #!campo 35
    #verificar uso de ocitocina
    if dict_especifico['ocitocina_mae'] == 'ocitocina-mae-sim':
        document.write_cross((285, 41), pg=1)  #ocitocina sim
    elif dict_especifico['ocitocina_mae'] == 'ocitocina-mae-nao':
        document.write_cross((381, 41), pg=1)  #ocitocina nao
    elif dict_especifico['ocitocina_mae'] == 'ocitocina-mae-naoSeAplica':
        document.write_cross((467, 41), pg=1)  #ocitocina n se aplica
    #!campo 36
    #verificar uso de eperidina
    if dict_especifico['eperidina_mae'] == 'eperidina-mae-sim':
        document.write_cross((285, 57), pg=1)  #eperidina sim
    elif dict_especifico['eperidina_mae'] == 'eperidina-mae-nao':
        document.write_cross((381, 57), pg=1)  #eperidina nao
    elif dict_especifico['eperidina_mae'] == 'eperidina-mae-naoSeAplica':
        document.write_cross((467, 57), pg=1)  #eperidina n se aplica
    #!campo 37
    #verificar uso de corticoide
    if dict_especifico['corticoide_mae'] == 'corticoide-mae-sim':
        document.write_cross((142, 73), pg=1)  #corticoide sim
    elif dict_especifico['corticoide_mae'] == 'corticoide-mae-nao':
        document.write_cross((381, 73), pg=1)  #corticoide nao
    elif dict_especifico['corticoide_mae'] == 'corticoide-mae-naoSeAplica':
        document.write_cross((468, 73), pg=1)  #corticoide n se aplica
    document.write_date(dict_especifico['dt_corticoide'], (214, 71), pg=1, spacing=3)  #data corticoide SIM

    #!campo 38
    if dict_especifico['nenhuma_outra_med_intern'] == '1':
        document.write_cross((468, 90), pg=1)  #nenhuma

    document.write_box(dict_especifico['outra_med_internacao'], rect=(53, 90, 542, 125), pg=1)  #outra medicação
    #!campo 39
    document.write_date(dict_especifico['dt_parto'], (149, 133), pg=1, spacing=3)  #dt parto
    document.write_hrmin(dict_especifico['hora_parto'], (436, 133), pg=1, space=3)  #casa da hora
    #!campo 40
    #verificar tipo de parto
    if dict_especifico['tipo_parto'] == 'tipo-parto-vaginal-forceps':
        document.write_cross((157, 152), pg=1)  #vaginal c forceps
    elif dict_especifico['tipo_parto'] == 'tipo-parto-vaginal':
        document.write_cross((318, 152), pg=1)  #vaginal
    elif dict_especifico['tipo_parto'] == 'tipo-parto-cesaria':
        document.write_cross((468, 152), pg=1)  #cesarea
    #se cesarea true qual o motivo no prontuario:
    #verificar motivo de cesaria
    if dict_especifico['motivo_cesaria'] == 'motivo-cesaria-anomalia':
        document.write_cross((111, 167), pg=1)  #apres anomala
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-anterior':
        document.write_cross((111, 182), pg=1)  #cesarea anterior
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-desproporcao':
        document.write_cross((111, 197), pg=1)  #desproporcao cefalopelvica
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-placenta':
        document.write_cross((211, 167), pg=1)  #descolamento prematuro
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-falha':
        document.write_cross((211, 182), pg=1)  #falha inducao parto
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-feto-morto':
        document.write_cross((211, 197), pg=1)  #feto morto
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-hemorragia-vaginal':
        document.write_cross((318, 167), pg=1)  #hemorragia vaginal
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-eclampsia':
        document.write_cross((318, 182), pg=1)  #pre/eclampsia
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-ruptura-prematura':
        document.write_cross((318, 197), pg=1)  #ruptura prematura membrana
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-sofirmento-fetal':
        document.write_cross((425, 167), pg=1)  #sofrimento fetal agudo
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-parto-prolongado':
        document.write_cross((425, 182), pg=1)  #trab parto prolongado
    elif dict_especifico['motivo_cesaria'] == 'motivo-cesaria-outro':
        document.write_cross((425, 197), pg=1)  #outra
    document.write_text(dict_especifico['motivo_cesaria_outro_descricao'], (425, 207),
                        pg=1)  #descricao do motivo de cesaria
    #!campo 41
    #todo verificar quem atendeu
    if dict_especifico['quem_atendeu'] == 'quem-atendeu-obstetra':
        document.write_cross((143, 227), pg=1)  #medico gineco-obstetra
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-parteira':
        document.write_cross((143, 242), pg=1)  #parteira
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-nao-obstetra':
        document.write_cross((238, 227), pg=1)  #medico nao gineco-obstetra
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-obstretriz':
        document.write_cross((346, 227), pg=1)  #enfermeira obstetriz
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-enfermeira':
        document.write_cross((428, 227), pg=1)  #enfermeira
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-sem-assistencia':
        document.write_cross((428, 242), pg=1)  #sem assistencia
    elif dict_especifico['quem_atendeu'] == 'quem-atendeu-outro':
        document.write_cross((238, 242), pg=1)  #outro
    document.write_text(dict_especifico['que_atendeu_outro'], (272, 242), pg=1)  #outro quem atendeu
    #!campo 42
    #TODO verificar liquido amniotico
    if dict_especifico['liq_amni'] == 'liq-amniotico-claro':
        document.write_cross((183, 258), pg=1)  #claro
    elif dict_especifico['liq_amni'] == 'liq-amniotico-meconio':
        document.write_cross((238, 258), pg=1)  #com meconio
    elif dict_especifico['liq_amni'] == 'liq-amniotico-sanguinolento':
        document.write_cross((292, 258), pg=1)  #sanguinolento
    elif dict_especifico['liq_amni'] == 'liq-amniotico-fetido':
        document.write_cross((346, 258), pg=1)  #fetido
    elif dict_especifico['liq_amni'] == 'liq-amniotico-outro':
        document.write_cross((428, 258), pg=1)  #outro
    document.write_text(dict_especifico['liq_amni_outro'], (458, 257), pg=1)  #outro liquido amniotico
    #!campo 43
    #verificar anestesia
    if dict_especifico['anestesia_parto'] == 'anestesia-parto-nenhuma':
        document.write_cross((183, 274), pg=1)  #nenhuma
    elif dict_especifico['anestesia_parto'] == 'anestesia-parto-geral':
        document.write_cross((238, 274), pg=1)  #geral
    elif dict_especifico['anestesia_parto'] == 'anestesia-parto-raquidiana':
        document.write_cross((292, 274), pg=1)  #raquidiana
    elif dict_especifico['anestesia_parto'] == 'anestesia-parto-peridural':
        document.write_cross((346, 274), pg=1)  #peridural
    elif dict_especifico['anestesia_parto'] == 'anestesia-parto-local':
        document.write_cross((392, 274), pg=1)  #local
    elif dict_especifico['anestesia_parto'] == 'anestesia-parto-outro':
        document.write_cross((428, 274), pg=1)  #outra
    document.write_text(dict_especifico['anestesia_parto_outro'], (458, 274), pg=1)  #outra anestesia
    #!campo 44
    #TODO verificar intercorrencia parto
    if dict_especifico['intercorr_parto'] == 'intercorrencia-parto-nenhuma':
        document.write_cross((198, 290), pg=1)  #nenhuma
    elif dict_especifico['intercorr_parto'] == 'intercorrencia-parto-hipertensao':
        document.write_cross((238, 290), pg=1)  #hipertensão
    elif dict_especifico['intercorr_parto'] == 'intercorrencia-parto-hemorragia':
        document.write_cross((292, 290), pg=1)  #Hemorragia
    elif dict_especifico['intercorr_parto'] == 'intercorrencia-parto-outro':
        document.write_cross((346, 290), pg=1)  #outra
    document.write_text(dict_especifico['intercorr_parto_outro'], (376, 290), pg=1)  #outra intercorrencia
    #!campo 45
    document.write_box(dict_especifico['evolucao_inter_mae'], rect=(53, 308, 542, 365), pg=1)  #evolucao internacao mae
    #!campo 46
    #TODO verificar parto sifilis
    if dict_especifico['parto_sifilis'] == 'parto-sifilis-nao':
        document.write_cross((204, 382), pg=1)  #sifilis n reagente
    elif dict_especifico['parto_sifilis'] == 'parto-sifilis-sim':
        document.write_cross((265, 382), pg=1)  #sifilis reagente
    elif dict_especifico['parto_sifilis'] == 'parto-sifilis-naoRealizado':
        document.write_cross((318, 382), pg=1)  #sifilis n realizado
    #TODO verificar parto hiv
    if dict_especifico['parto_hiv'] == 'parto-hiv-nao':
        document.write_cross((204, 398), pg=1)  #hiv n reagente
    elif dict_especifico['parto_hiv'] == 'parto-hiv-sim':
        document.write_cross((265, 398), pg=1)  #hiv reagente
    elif dict_especifico['parto_hiv'] == 'parto-hiv-naoRealizado':
        document.write_cross((318, 398), pg=1)  #hiv n realizado
    #* Bloco VII Condições de nascimento op N se aplica
    if dict_especifico['op_cond_nasc_NSA'] == '1':
        document.write_cross((463, 413), pg=1)  #opcao de n se aplica
    #!campo 47
    #TODO verificar natimorto aval
    if dict_especifico['natimorto_aval'] == 'natimorto-avaliado-obstetra':
        document.write_cross((204, 429), pg=1)  #medico gineco-obstetra
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-pediatra':
        document.write_cross((292, 429), pg=1)  #medico pediatra/neonatologista
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-outro-medico':
        document.write_cross((471, 429), pg=1)  #outro medico
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-enfermeira':
        document.write_cross((92, 444), pg=1)  #enfermeira obstetriz
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-parteira':
        document.write_cross((204, 444), pg=1)  #parteira
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-ninguem':
        document.write_cross((471, 444), pg=1)  #Ninguem
    elif dict_especifico['natimorto_aval'] == 'natimorto-avaliado-outro':
        document.write_cross((292, 444), pg=1)  #outro
    document.write_text(dict_especifico['natimorto_aval_outro'], (320, 444), pg=1)  #outro natimorto aval
    #!campo 48
    document.write_code(dict_especifico['idade_gest_nasc'], (178, 456), pg=1, space=2)  #idade gestacional
    #!campo 49
    document.write_code(dict_especifico['peso_nascimento'], (174, 472), pg=1, space=3)  #peso de nascimento
    #!campo 50
    if dict_especifico['quando_obito_ocorr'] == 'obito-ocorreu-antes-parto':
        document.write_cross((170, 489), pg=1)  #antes do parto
    elif dict_especifico['quando_obito_ocorr'] == 'obito-ocorreu-durante-parto':
        document.write_cross((292, 489), pg=1)  #durante parto
    elif dict_especifico['quando_obito_ocorr'] == 'obito-ocorreu-apos-parto':
        document.write_cross((428, 489), pg=1)  #apos parto
    #TODO se antes do parto true, foi macerado?
    #!campo 50.1
    if dict_especifico['feto_macerado'] == 'feto-macerado-sim':
        document.write_cross((292, 504), pg=1)  #sim ir para o bloco X
    elif dict_especifico['feto_macerado'] == 'feto-macerado-durante-nao':
        document.write_cross((318, 504), pg=1)  #nao
    #!campo 51
    document.write_code(dict_especifico['apgar_1min'], (166, 520), pg=1)  #?apgar 1 min verificar o que escrever
    document.write_code(dict_especifico['apgar_5min'], (242, 517), pg=1)  #?apgar 5 min
    if dict_especifico['op_apgar_natimorto'] == '1':
        document.write_cross((312, 523), pg=1)  #natimorto
    #!campo 52
    #TODO verificar classificacao RN
    if dict_especifico['classificacaoRN'] == 'classificacaoRN-adequado':
        document.write_cross((137, 540), pg=1)  #adequado para idade gestacional
    elif dict_especifico['classificacaoRN'] == 'classificacaoRN-pequeno':
        document.write_cross((264, 540), pg=1)  #pequeno para idade gestacional
    elif dict_especifico['classificacaoRN'] == 'classificacaoRN-grande':
        document.write_cross((398, 540), pg=1)  #grande para idade gestacional
    #!campo 53
    #TODO verificar reanimacao
    if dict_especifico['reanimacao'] == 'reanimacao-sim':
        document.write_cross((224, 555), pg=1)  #sim
    elif dict_especifico['reanimacao'] == 'reanimacao-nao':
        document.write_cross((264, 557), pg=1)  #nao
    #!campo 54
    #TODO verificar assistencia RN
    if dict_especifico['assistenciaRN'] == 'assistenciaRN-nenhum':
        document.write_cross((435, 573), pg=1)  #nenhum
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-aspiracao':
        document.write_cross((72, 588), pg=1)  #aspiração das vias aéreas
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-cateterismo':
        document.write_cross((177, 588), pg=1)  #Cateterismo umbilical
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-entubacao':
        document.write_cross((277, 588), pg=1)  #Entubação
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-oxigenio':
        document.write_cross((386, 588), pg=1)  #Oxigenio
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-sonda':
        document.write_cross((470, 588), pg=1)  #Sonda nasogástrica
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-outro-procedimento':
        document.write_cross((75, 603), pg=1)  #Outros procedimentos
    elif dict_especifico['assistenciaRN'] == 'assistenciaRN-medicamentos':
        document.write_cross((71, 618), pg=1)  #Medicamentos utilizados
    document.write_text(dict_especifico['assistRN_outro_proced'], (177, 602), pg=1)  #outros procedimentos
    document.write_text(dict_especifico['assistRN_outro_medicam'], (177, 617), pg=1)  #medicamentos utilizados
    #!campo 55
    #TODO verificar diagnostico RN hipoglicemia
    if dict_especifico['hipoglicemia'] == 'hipoglicemia-sim':
        document.write_cross((204, 633), pg=1)  #sim
    elif dict_especifico['hipoglicemia'] == 'hipoglicemia-nao':
        document.write_cross((249, 633), pg=1)  #nao
    elif dict_especifico['hipoglicemia'] == 'hipoglicemia-naoFez':
        document.write_cross((367, 633), pg=1)  #n fez exame
    #* Bloco VIII Atendimento após o nascimento op N se aplica
    if dict_especifico['op_atend_apos_nasc'] == '1':
        document.write_cross((330, 651), pg=1)  #opcao de n se aplica
    #!campo 56
    #TODO setor internacao RN
    if dict_especifico['setorRN'] == 'setorRN-aloj-conjunto':
        document.write_cross((175, 670), pg=1)  #alojamento conjunto
    elif dict_especifico['setorRN'] == 'setorRN-UTI-neonatal':
        document.write_cross((256, 670), pg=1)  #UTI/CTI neonatal
    elif dict_especifico['setorRN'] == 'setorRN-ICINCo':
        document.write_cross((354, 670), pg=1)  #cuidado intermediario neonatal UCINCo
    elif dict_especifico['setorRN'] == 'setorRN-ICINCa':
        document.write_cross((72, 685), pg=1)  #Cuidado intermediario neonatal Canguru UCINCa
    elif dict_especifico['setorRN'] == 'setorRN-outro':
        document.write_cross((256, 685), pg=1)  #Outro
    document.write_text(dict_especifico['setorRN_outro_descricao'], (286, 684), pg=1)  #outro setor RN
    #!campo 57
    #TODO if RN tinha baixo peso <2500g?
    if dict_especifico['RN_baixo_peso'] == 'RN-baixo-peso-sim':
        document.write_cross((175, 700), pg=1)  #sim
    elif dict_especifico['RN_baixo_peso'] == 'RN-baixo-peso-nao':
        document.write_cross((198, 700), pg=1)  #nao
    #!campo 58
    #TODO RN era prematuro? IG < 37 semanas
    if dict_especifico['RN_prematuro'] == 'RN-prematuro-sim':
        document.write_cross((455, 701), pg=1)  #sim
    elif dict_especifico['RN_prematuro'] == 'RN-prematuro-nao':
        document.write_cross((478, 701), pg=1)  #nao
    #!campo 59
    #TODO verificar intercorrencia apos o nascimento
    if dict_especifico['INASC'] == 'INASC-metabolico':
        document.write_cross((176, 717), pg=1)  #disturbio metabolico
    elif dict_especifico['INASC'] == 'INASC-membrana-hialina':
        document.write_cross((257, 717), pg=1)  #doenca membrana hialina
    elif dict_especifico['INASC'] == 'INASC-hemolitica':
        document.write_cross((358, 717), pg=1)  #doenca hemolitica
    elif dict_especifico['INASC'] == 'INASC-ictericia':
        document.write_cross((444, 717), pg=1)  #ictericia
    elif dict_especifico['INASC'] == 'INASC-infeccao-confirmada':
        document.write_cross((58, 732), pg=1)  #infeccao confirmada
    elif dict_especifico['INASC'] == 'INASC-infeccao-suspeita':
        document.write_cross((176, 732), pg=1)  #infeccao suspeita
    elif dict_especifico['INASC'] == 'INASC-malformacao':
        document.write_cross((257, 732), pg=1)  #malformação congenita
    elif dict_especifico['INASC'] == 'INASC-aspiracao-meconial':
        document.write_cross((358, 732), pg=1)  #sd. aspiracao meconial
    elif dict_especifico['INASC'] == 'INASC-taquipneia':
        document.write_cross((444, 732), pg=1)  #taquipneia transitoria do RN
    elif dict_especifico['INASC'] == 'INASC-tocotraumatismo':
        document.write_cross((58, 747), pg=1)  #Tocotraumatismo
    elif dict_especifico['INASC'] == 'INASC-outro':
        document.write_cross((176, 747), pg=1)  #outra
    document.write_text(dict_especifico['INASC_outro_descricao'], (206, 746), pg=1)  #outra intercorrencia
    #!campo 60
    #TODO verificar admissao UTI neonatal
    if dict_especifico['IAUN'] == 'IAUN-sim':
        document.write_cross((210, 763), pg=1)  #sim
    elif dict_especifico['IAUN'] == 'IAUN-nao':
        document.write_cross((505, 762), pg=1)  #nao
    #se sim motivo
    document.write_text(dict_especifico['IAUN_motivo'], (260, 762), pg=1)  #motivo
    #*===========================FIM DA SEGUNDA PAGINA===========================
    #!campo 60.1
    if dict_especifico['IUN'] == 'IUN-sim':
        document.write_cross((203, 41), pg=2)  #sim
    elif dict_especifico['IUN'] == 'IUN-nao':
        document.write_cross((504, 41), pg=2)  #nao
    #se sim data
    document.write_date(dict_especifico['dt_IUN'], (243, 38), pg=2, spacing=3)  #data
    document.write_code(dict_especifico['hora_IUN'][:5], (407, 38), pg=2, space=3)  #casa da hora
    #!campo 60.1.1
    if dict_especifico['mais3horas_inter'] == 'mais3horas-internar-sim':
        document.write_cross((203, 57), pg=2)  #sim
    elif dict_especifico['mais3horas_inter'] == 'mais3horas-internar-nao':
        document.write_cross((504, 57), pg=2)  #nao
    #se sim motivo
    document.write_text(dict_especifico['mais3horas_inter_motivo'], (255, 56), pg=2)  #motivo
    #!campo 60.1.2
    document.write_text(dict_especifico['motivo_nao_inter'], (203, 73), pg=2)  #pq nao foi internado
    #!campo 61
    document.write_box(dict_especifico['evolucao_inter_RN'], rect=(58, 95, 550, 175), pg=2)  #evolucao RN
    #!campo 62
    #TODO verificar procedimentos realizados no RN
    if dict_especifico['PRDIRN_nenhum'] == '1': document.write_cross((462, 188), pg=2)  #nenhum
    if dict_especifico['PRDIRN_antibioti'] == '1': document.write_cross((71, 204), pg=2)  #Antibioticoterapia
    if dict_especifico['PRDIRN_berco'] == '1': document.write_cross((146, 204), pg=2)  #Berço aquecido
    if dict_especifico['PRDIRN_canguru'] == '1': document.write_cross((257, 204), pg=2)  #Método canguru
    if dict_especifico['PRDIRN_cateter'] == '1': document.write_cross((355, 204), pg=2)  #Cateterismo umbilical
    if dict_especifico['PRDIRN_cpap'] == '1': document.write_cross((462, 204), pg=2)  #CPAP
    if dict_especifico['PRDIRN_disseccao'] == '1': document.write_cross((71, 219), pg=2)  #Disecção venosa
    if dict_especifico['PRDIRN_entubacao'] == '1': document.write_cross((146, 219), pg=2)  #Entubação
    if dict_especifico['PRDIRN_fototera'] == '1': document.write_cross((257, 219), pg=2)  #Fototerapia
    if dict_especifico['PRDIRN_exsang'] == '1': document.write_cross((355, 219), pg=2)  #Exsanguineo-transfusão
    if dict_especifico['PRDIRN_hemotrans'] == '1': document.write_cross((462, 219), pg=2)  #Hemotransfusão
    if dict_especifico['PRDIRN_incuba'] == '1': document.write_cross((71, 233), pg=2)  #Incubadora
    if dict_especifico['PRDIRN_nutri_par'] == '1': document.write_cross((146, 233), pg=2)  #Nutrição parenteral
    if dict_especifico['PRDIRN_oxig_capacete'] == '1': document.write_cross((257, 233), pg=2)  #Oxigenio em capacete
    if dict_especifico['PRDIRN_oxig_inala'] == '1': document.write_cross((355, 233), pg=2)  #Oxigenio inalatorio
    if dict_especifico['PRDIRN_puncao'] == '1': document.write_cross((462, 233), pg=2)  #punção venosa central
    if dict_especifico['PRDIRN_surf'] == '1': document.write_cross((71, 248), pg=2)  #Surfactante
    if dict_especifico['PRDIRN_ventila'] == '1': document.write_cross((146, 248), pg=2)  #Ventilação mecanica
    if dict_especifico['PRDIRN_outros'] == '1': document.write_cross((257, 248), pg=2)  #Outros
    document.write_text(dict_especifico['PRDIRN_outro_descricao'], (355, 247), pg=2)  #outros procedimentos
    #!campo 63
    #TODO verificar mae acompanhou rn internacao
    if dict_especifico['MARNI'] == 'MARNI-sim-integral':
        document.write_cross((249, 278), pg=2)  #sim em tempo integral
    elif dict_especifico['MARNI'] == 'MARNI-sim-parcial':
        document.write_cross((345, 278), pg=2)  #sim em tempo parcial
    elif dict_especifico['MARNI'] == 'MARNI-nao':
        document.write_cross((434, 278), pg=2)  #nao
    #!campo 64
    #TODO verificar se a mae nao acompanhou rn, rn teve outro acompanhante
    if dict_especifico['RNOA'] == 'RNOA-sim-integral':
        document.write_cross((249, 294), pg=2)  #sim em tempo integral
    elif dict_especifico['RNOA'] == 'RNOA-sim-parcial':
        document.write_cross((345, 294), pg=2)  #sim em tempo parcial
    elif dict_especifico['RNOA'] == 'RNOA-nao':
        document.write_cross((434, 294), pg=2)  #nao
    #!campo 65
    #TODO verificar desfecho internação após nascimento
    if dict_especifico['DIAN'] == 'DIAN-alta':
        document.write_cross((244, 310), pg=2)  #alta
    elif dict_especifico['DIAN'] == 'DIAN-transferencia':
        document.write_cross((320, 310), pg=2)  #transferencia
    elif dict_especifico['DIAN'] == 'DIAN-obito':
        document.write_cross((434, 310), pg=2)  #obito
    #!campo 66 Data alta/transferencia
    document.write_date(dict_especifico['dt_altaRN'], (181, 324), pg=2, spacing=3)  #data
    #! campo 67 peso alta/transferencia
    document.write_code(dict_especifico['peso_altaRN'], (437, 324), pg=2, space=3)  #peso
    #!campo 68 se foi transferido qual o motivo
    document.write_text(dict_especifico['motivo_transfRN'], (181, 340), pg=2)  #motivo
    #!campo 69 se foi transferido qual o hospital
    document.write_text(dict_especifico['hosp_transfRN'], (181, 355), pg=2)  #hospital
    #!campo 70 se foi a obito indique a hora
    document.write_hrmin(dict_especifico['hora_obitoRN'], (203, 368), pg=2, space=3)  #casa da hora
    if dict_especifico['op_hora_obitoRN_NSA'] == '1':
        document.write_cross((483, 371), pg=2)  #n se aplica
    #!campo 71 se foi a obito onde ocorreu
    if dict_especifico['obito_RN'] == 'obito-RN-alojamento-conjunto':
        document.write_cross((196, 387), pg=2)  #alojamento conjunto
    elif dict_especifico['obito_RN'] == 'obito-RN-cuidado-intermediario':
        document.write_cross((276, 387), pg=2)  #cuidado intermediario
    elif dict_especifico['obito_RN'] == 'obito-RN-UTI-neonatal':
        document.write_cross((357, 387), pg=2)  #uti neonatal
    elif dict_especifico['obito_RN'] == 'obito-RN-centro-obstetrico':
        document.write_cross((414, 387), pg=2)  #centro obstetrico
    elif dict_especifico['obito_RN'] == 'obito-RN-outro':
        document.write_cross((483, 387), pg=2)  #outro
    #* Bloco IX - Assistencia hospitalar a crianca durante a situação que levou a obito op n se aplica
    if dict_especifico['op_AHCDSO_NSA'] == '1':
        document.write_cross((484, 402), pg=2)  #opcao de n se aplica
    #!campo 72 data da intervenção
    document.write_date(dict_especifico['dt_inter_crianca'], (135, 430), pg=2, spacing=3)  #data
    document.write_hrmin(dict_especifico['hr_inter_crianca'], (398, 430), pg=2, space=3)  #casa da hora
    #!campo 73 a criança veio transferida de outro hospital
    if dict_especifico['CVTH'] == 'CVTH-sim':
        document.write_cross((204, 448), pg=2)  #sim
    elif dict_especifico['CVTH'] == 'CVTH-nao':
        document.write_cross((414, 448), pg=2)  #nao
    document.write_text(dict_especifico['CVTH_hospital'], (95, 463), pg=2)  #nome do hospital
    document.write_code(dict_especifico['tempo_inter_crianca'], (450, 462), pg=2, space=3)  #tempo internação

    if dict_especifico['tipo_tempo_inter'] == 'TIT-dias':
        document.write_cross((481, 465), pg=2)  #dias
    elif dict_especifico['tipo_tempo_inter'] == 'TIT-meses':
        document.write_cross((503, 465), pg=2)  #horas
    #!campo 74 breve historia na admissao
    document.write_box(dict_especifico['historia_admissao'], rect=(54, 484, 550, 525), pg=2)  #breve historia
    #!campo 75 dados da criança na admissao
    #!campo 75.1 idade
    document.write_code(dict_especifico['ICA'], (392, 540), pg=2, space=2)  #idade

    if dict_especifico['ICAT'] == 'ICAT-dias':
        document.write_cross((424, 542), pg=2)  #dias
    elif dict_especifico['ICAT'] == 'ICAT-meses':
        document.write_cross((446, 542), pg=2)  #meses
    elif dict_especifico['ICAT'] == 'ICAT-anos':
        document.write_cross((476, 542), pg=2)  #anos
    #!campo 75.2 peso
    document.write_code(dict_especifico['peso_crianca_admiss'], (134, 555), pg=2, space=3)  #peso
    #!campo 75.3 altura
    document.write_code(dict_especifico['ACA'], (390, 555), pg=2, space=3)  #altura
    #!campo 75.4 estado nutricional
    if dict_especifico['ENCAT'] == 'ENCAT-eutrofica':
        document.write_cross((131, 574), pg=2)  #eutrofica
    elif dict_especifico['ENCAT'] == 'ENCAT-desnutrida':
        document.write_cross((185, 574), pg=2)  #desnutrida
    #!campo 75.5 estado hidratação
    if dict_especifico['EHCAT'] == 'EHCAT-hidratada':
        document.write_cross((385, 574), pg=2)  #hidratada
    elif dict_especifico['EHCAT'] == 'EHCAT-desidratada':
        document.write_cross((449, 574), pg=2)  #desidratada
    #!campo 75.6 estado geral grave
    if dict_especifico['EGGCA'] == 'EGGCA-sim':
        document.write_cross((131, 590), pg=2)  #sim
    elif dict_especifico['EGGCA'] == 'EGGCA-nao':
        document.write_cross((185, 590), pg=2)  #nao
    #!campo 75.7 perfusão
    if dict_especifico['PCA'] == 'PCA-normal':
        document.write_cross((385, 590), pg=2)  #normal
    elif dict_especifico['PCA'] == 'PCA-diminuida':
        document.write_cross((449, 590), pg=2)  #diminuida
    #!campo 75.8 sinais vitais
    document.write_code(dict_especifico['BCCA'], (226, 603), pg=2, space=2)  #freq cardiaca
    document.write_code(dict_especifico['RCA'], (359, 603), pg=2, space=2)  #freq respiratoria
    document.write_code(dict_especifico['TCA'], (469, 604), pg=2, space=2)  #temperatura
    #!campo 76 diagnostico admissao e conduta inicial
    document.write_box(dict_especifico['diag_crianca_admissao'], rect=(53, 622, 550, 658), pg=2)  #diagnostico
    #!campo 77 evolucao durante a internação
    document.write_box(dict_especifico['REIC'], rect=(53, 674, 550, 747), pg=2)  #evolucao dur internacao
    #!campo 78 admissao na UTI pediatrica
    #todo verificar admissao na UTI pediatrica
    if dict_especifico['IA_UTIP'] == 'IA-UTIP-sim':
        document.write_cross((212, 761), pg=2)  #sim
    elif dict_especifico['IA_UTIP'] == 'IA-UTIP-nao':
        document.write_cross((504, 761), pg=2)  #nao
    document.write_text(dict_especifico['IA_UTIP_motivo'], (262, 760), pg=2)  #motivo
    #* ========================FIM DA TERCEIRA PAGINA===========================
    #!campo 78.1 se sim foi internado na UTI pediatrica
    if dict_especifico['INT_UTIP'] == 'INT-UTIP-sim':
        document.write_cross((205, 41), pg=3)  #sim
    elif dict_especifico['INT_UTIP'] == 'INT-UTIP-nao':
        document.write_cross((504, 41), pg=3)  #nao
    #se sim data
    document.write_date(dict_especifico['dt_INT_UTIP'], (245, 38), pg=3, spacing=3)  #data
    document.write_hrmin(dict_especifico['hora_INT_UTIP'], (410, 38), pg=3, space=3)  #hora
    #!campo 78.1.1 demorou >3 horas para ser internado
    if dict_especifico['DM3HPSIC'] == 'DM3HPSIC-sim':
        document.write_cross((205, 57), pg=3)  #sim
    elif dict_especifico['DM3HPSIC'] == 'DM3HPSIC-nao':
        document.write_cross((504, 57), pg=3)  #nao
    #se sim motivo
    document.write_text(dict_especifico['DM3HPSIC_motivo'], (256, 56), pg=3)  #motivo
    #!campo 78.1.2 pq nao foi internado
    document.write_text(dict_especifico['crianca_nao_inter_motivo'], (205, 73), pg=3)  #motivo
    #!campo 79 desfecho da internacao apos o nascimento
    if dict_especifico['DIANC'] == 'DIANC-alta':
        document.write_cross((239, 90), pg=3)  #alta
    elif dict_especifico['DIANC'] == 'DIANC-transferencia':
        document.write_cross((319, 90), pg=3)  #transferencia
    elif dict_especifico['DIANC'] == 'DIANC-obito':
        document.write_cross((433, 90), pg=3)  #obito go to 84
    #!campo 80 data alta/transferencia
    document.write_date(dict_especifico['dt_alta_crianca'], (173, 103), pg=3, spacing=3)  #data
    #!campo 81 peso alta/transferencia
    document.write_code(dict_especifico['peso_alta_crianca'], (438, 103), pg=3, space=3)  #peso
    #!campo 82 se foi transferido qual o motivo
    document.write_text(dict_especifico['CRIANCAT_motivo'], (173, 121), pg=3)  #motivo
    if dict_especifico['op_CRIANCAT_motivo_NSA'] == '1':
        document.write_cross((475, 121), pg=3)  #nao se aplica
    #!campo 83 se foi transferido qual o hospital
    document.write_text(dict_especifico['CRIANCAT_nome_hosp'], (208, 137), pg=3)  #hospital
    if dict_especifico['op_CRIANCAT_hosp_NSA'] == '1':
        document.write_cross((475, 137), pg=3)  #nao se aplica
    #!campo 84 se foi a obito indique a hora
    document.write_hrmin(dict_especifico['hora_obito_crianca'], (210, 151), pg=3, space=3)  #hora
    if dict_especifico['op_HOC_NSA'] == '1':
        document.write_cross((475, 154), pg=3)  #nao se aplica
    #!campo 85 se foi a obito onde ocorreu
    #todo verificar onde ocorreu o obito
    if dict_especifico['SOC'] == 'SOC-UTIP':
        document.write_cross((204, 170), pg=3)  #UTI neonatal/pediatrica
    elif dict_especifico['SOC'] == 'SOC-outro':
        document.write_cross((305, 170), pg=3)  #outro
    elif dict_especifico['SOC'] == 'SOC-naoSeAplica':
        document.write_cross((475, 170), pg=3)  #n se aplica
    document.write_text(dict_especifico['SOC_outro_descricao'], (335, 169), pg=3)  #outro local
    #* Bloco X - informacoes complementares sobre o obito
    #! campo 86 - liste os diagnosticos ou hipoteses diagnosticas
    document.write_box(dict_especifico['diag_clinicos'], rect=(70, 205, 550, 262), pg=3)  #diagnostico
    #! campo 87 - se houve necropsia
    #todo verificar se houve necropsia
    if dict_especifico['corpo_env_necropsia'] == 'corpo-enviado-necropsia-sim':
        document.write_cross((197, 275), pg=3)  #sim
    elif dict_especifico['corpo_env_necropsia'] == 'corpo-enviado-necropsia-nao':
        document.write_cross((300, 275), pg=3)  #nao
    #se sim qual o tipo da necropsia
    #todo verificar tipo de necropsia
    if dict_especifico['CENL'] == 'CENL-iml':
        document.write_cross((220, 275), pg=3)  #IML
    elif dict_especifico['CENL'] == 'CENL-svo':
        document.write_cross((242, 275), pg=3)  #SVO
    elif dict_especifico['CENL'] == 'CENL-outro':
        document.write_cross((266, 275), pg=3)  #Outro
    #! campo 87.1 - se sim foi realizada a necropsia
    #todo verificar sim e nao
    if dict_especifico['realiz_necropsia'] == 'realizada-necropsia-sim':
        document.write_cross((490, 275), pg=3)  #sim
    elif dict_especifico['realiz_necropsia'] == 'realizada-necropsia-nao':
        document.write_cross((514, 275), pg=3)  #nao
    #! campo 88 - este caso foi analisado por alguma comissao/grupo do hospital
    #todo verificar se foi analisado
    if dict_especifico['caso_analisado'] == 'caso-analisado-sim':
        document.write_cross((261, 290), pg=3)  #sim
    elif dict_especifico['caso_analisado'] == 'caso-analisado-nao':
        document.write_cross((315, 290), pg=3)  #nao
    #se sim qual a comissao e conclusoes
    document.write_box(dict_especifico['comissao_conclusao'], rect=(65, 311, 550, 374), pg=3)  #comissao
    #se nao porque
    #todo verificar motivo
    if dict_especifico['CNA'] == 'CNA-nao-encaminhado':
        document.write_cross((139, 388), pg=3)  #nao foi encaminhado
    elif dict_especifico['CNA'] == 'CNA-encaminhado-nao-analisado':
        document.write_cross((225, 388), pg=3)  #foi encaminhado mas nao analisado
    elif dict_especifico['CNA'] == 'CNA-sem-comissao':
        document.write_cross((366, 388), pg=3)  #n existe comissao
    elif dict_especifico['CNA'] == 'CNA-outro':
        document.write_cross((474, 388), pg=3)  #outro
    document.write_text(dict_especifico['CNA_outro_descricao'], (65, 403), pg=3)  #outro motivo
    #! campo 89 - info complementares ou esclarecimentos do investigador, algo que deixou de ser feito
    document.write_box(dict_especifico['outras_informacoes'], rect=(65, 420, 550, 485), pg=3)  #info complementares
    #* Bloco XI - Encerramento da investigacao hospitalar
    #! campo 90 - responsavel pelo preenchimento
    document.write_text(dict_especifico['nome_notificante'], (180, 516), pg=3)  #responsavel
    #! campo 91 - telefone de contato
    document.write_text(dict_especifico['telefone_investigador'][:2], (466, 514), pg=3, font_size=11)  #telefone
    document.write_text(dict_especifico['telefone_investigador'][2:], (482, 514), pg=3, font_size=11)  #telefone
    #! campo 92 - o responsavel é do hospital
    #todo verificar se o responsavel é do hospital
    if dict_especifico['funcionario_hosp'] == 'funcionario-hospital-sim':
        document.write_cross((272, 531), pg=3)  #sim
    elif dict_especifico['funcionario_hosp'] == 'funcionario-hospital-nao':
        document.write_cross((297, 531), pg=3)  #nao
    #! campo 93 - data do encerramento
    document.write_date(dict_especifico['dt_encerramento'], (227, 546), pg=3, spacing=3)  #data
    #! campo 94 - info anexa
    # verificar se tem info anexa
    if dict_especifico['info_anexa'] == 'informacao-anexa-sim':
        document.write_cross((454, 551), pg=3)  #sim
    elif dict_especifico['info_anexa'] == 'informacao-anexa-nao':
        document.write_cross((478, 551), pg=3)  #nao

    document.save(nome_arquivo, path_pdf_gerado)
