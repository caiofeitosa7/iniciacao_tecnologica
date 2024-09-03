from .pdfWritter import PDFWriter


def gerar_pdf_obt_fetal_inf(dict_especifico: dict, modelo_pdf: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    document.write_code(dict_especifico['numero_ficha'], (452, 43), space=3)
    if dict_especifico['op_obito_fetal_DO'] == '1':
        document.write_cross((375, 65))
    document.write_text(dict_especifico['nome_paciente'], (81, 81))
    #verificar sexo é M ou F
    match dict_especifico['sexo']:
        case 'op-sexo-m':
            document.write_cross((418, 78))
        case 'op-sexo-f':
            document.write_cross((436, 78))
    document.write_code(dict_especifico['semanas_gestacao'], (137, 96), space=2)
    document.write_code(dict_especifico['idade_obito'], (228, 96), space=2)
    #verificar tipo de idade
    match dict_especifico['tp_idade_obito']:
        case 'tp-idade-obito-meses':
            document.write_cross((260, 99))  #meses
        case 'tp-idade-obito-dias':
            document.write_cross((293, 99))  #dias
        case 'tp-idade-obito-horas':
            document.write_cross((318, 99))  #horas
        case 'tp-idade-obito-min':
            document.write_cross((350, 99))  #minutos
    document.write_code(dict_especifico['peso'], (422, 94), space=3)
    #verificar tipo de peso
    match dict_especifico['tp_peso']:
        case 'tp-peso-gr':
            document.write_cross((493, 96))  #gramas
        case 'tp-peso-kg':
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
    #verificar raça da mãe
    match dict_especifico['raca_mae']:
        case 'raca-branca':
            document.write_cross((98, 227))  #branca
        case 'raca-preta':
            document.write_cross((129, 227))  #preta
        case 'raca-indigena':
            document.write_cross((159, 227))  #indigena
        case 'raca-parda':
            document.write_cross((98, 242))  #parda
        case 'raca-amarela':
            document.write_cross((129, 242))  #amarela

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
    match dict_especifico['tipo_estab']:
        case 'tipo-estab-SUS':
            document.write_cross((442, 294))  #tipo SUS
        case 'tipo-estab-convenio-SUS':
            document.write_cross((464, 294))  #tipo CONVENIO SUS
        case 'tipo-estab-privado':
            document.write_cross((442, 303))  #tipo PRIVADO
        case 'tipo-estab-outro':
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
    match dict_especifico['tp_idade_gest']:
        case 'idade-gestacional-DUM':
            document.write_cross((220, 362))  # dum
        case 'idade-gestacional-exame-fisico':
            document.write_cross((390, 362))  # exam fisico
        case 'idade-gestacional-outro':
            document.write_cross((442, 362))  # outro
        case 'idade-gestacional-naoSeAplica':
            document.write_cross((478, 362))  # n se aplica
    document.write_date(dict_especifico['dt_dum'], (250, 360), spacing=3)  #dt dum
    #if preferencia de formato xxx/xxx if not '/' insert '/' in the middle
    if '/' not in dict_especifico['press_art_adm_mae']:
        dict_especifico['press_art_adm_mae'] = dict_especifico['press_art_adm_mae'][:3] + '/' + dict_especifico[
                                                                                                    'press_art_adm_mae'][
                                                                                                3:]
    document.write_code(dict_especifico['press_art_adm_mae'], (202, 382), space=2)  #pressao arterial item 23
    #verificar opcao de obito da mae na admissao caso true pular para 27
    if dict_especifico['op_mae_obito_admissao'] == '1':
        document.write_cross((393, 385))  #opca de chegou em obito
    #verificar tipo de parto campo 24
    match dict_especifico['parto_admissao']:
        case 'parto-admisso-antes':
            document.write_cross((233, 403))  #antes do inicio do trabalho
        case 'parto-admisso-periodo-naoExpulsivo':
            document.write_cross((335, 403))  #No periodo não expulsivo
        case 'parto-admisso-periodo-expulsivo':
            document.write_cross((446, 403))  #No periodo expulsivo
    #verificar opcao de registro clinico 25 se true pular
    if dict_especifico['op_reg_clinico_admiss'] == '1':
        document.write_cross((478, 416))  #opcao de registro clinico 25
    document.write_code(dict_especifico['contracoes_10min'], (148, 431), space=2)  #contracoes por 10 min
    #verificar apresentacao fetal
    match dict_especifico['apresentacao_fetal']:
        case 'apresentacao-fetal-cefalica':
            document.write_cross((141, 451))  #cefalica
        case 'apresentacao-fetal-pelvica':
            document.write_cross((179, 451))  #pelvica
        case 'apresentacao-fetal-outra':
            document.write_cross((214, 451))  #Outra
    #verificar bcf
    match dict_especifico['bcf']:
        case 'op-bcf-positivo':
            document.write_cross((121, 467))  #positivo
        case 'op-bcf-negativo':
            document.write_cross((221, 467))  #negativo
    document.write_code(dict_especifico['bcf_posit_descricao'], (163, 465), space=2)  #descricao do positivo
    document.write_code(dict_especifico['descida_apresent'], (168, 484), space=2)  #descida da apresentacao
    document.write_code(dict_especifico['dilatacao_colo'], (401, 431), space=2)  #dilatacao do colo
    #todo verificar membrana
    match dict_especifico['membrana']:
        case 'op-membrana-integra':
            document.write_cross((393, 451))  #integra
        case 'op-membrana-rota':
            document.write_cross((432, 451))  #rotas
    document.write_code(dict_especifico['rotas_tempo'], (400, 465), space=2)  #rotas e tempo
    #todo verificar liquido amniotico
    match dict_especifico['rotas_liqAmniotico']:
        case 'rotas-liqAmniotico-claro':
            document.write_cross((393, 488))  #claro
        case 'rotas-liqAmniotico-meconial':
            document.write_cross((420, 488))  #meconial
        case 'rotas-liqAmniotico-fetido':
            document.write_cross((461, 488))  #Fétido
        case 'rotas-liqAmniotico-outro':
            document.write_cross((491, 488))  #Outro
    #!campo 26
    #verificar motivo de internacao
    match dict_especifico['motivo_inter']:
        case 'op-motivo-internacao-prematuro':
            document.write_cross((55, 521))  #prematuridade
        case 'op-motivo-internacao-posDatismo':
            document.write_cross((160, 521))  #pós-datismo
        case 'op-motivo-internacao-ruptura':
            document.write_cross((213, 521))  #rupturas de membranas
        case 'op-motivo-internacao-preEclampsia':
            document.write_cross((335, 521))  #pré-eclampsia
        case 'op-motivo-internacao-eclampsia':
            document.write_cross((387, 521))  #eclampsia
        case 'op-motivo-internacao-sangTransvaginal':
            document.write_cross((437, 521))  #Sangramento Transvaginal
        case 'op-motivo-internacao-cesariaAgendada':
            document.write_cross((56, 536))  #cesarea agendada
        case 'op-motivo-internacao-febre':
            document.write_cross((160, 536))  #febre
        case 'op-motivo-internacao-dimMovFecais':
            document.write_cross((213, 536))  #diminuicao mov fetais
        case 'op-motivo-internacao-outros':
            document.write_cross((335, 536))  #outros
        case 'op-motivo-internacao-nenhum':
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
    match dict_especifico['doen_gest_anterior']:
        case 'doenca-gestacao-anterior-nao':
            document.write_cross((203, 643))  #doencas na gestacao anterior nao
        case 'doenca-gestacao-anterior-sim':
            document.write_cross((249, 645))  #doencas na gestacao anterior sim

    document.write_text(dict_especifico['doen_gest_ante_sim_desc'], (295, 645))  #descricao doencas na gestacao anterior
    #!campo 29
    match dict_especifico['doen_fora_gest']:
        case 'doenca-fora-gestacao-nao':
            document.write_cross((203, 660))  #doencas fora da gestacao nao
        case 'doenca-fora-gestacao-sim':
            document.write_cross((248, 662))  #doencas fora da gestacao sim
    document.write_text(dict_especifico['doen_fora_gest_sim_desc'], (295, 662))  #descricao doencas fora da gestacao
    #*parte VI internacao hospitalar da mae-gestante op N se aplica
    #todo verificar opcao de internacao hospitalar
    if dict_especifico['op_inter_mae_NSA'] == '1':
        document.write_cross((466, 677))  #opcao de internacao hospitalar
    #!campo 30
    document.write_date(dict_especifico['dt_internacao_mae'], (142, 691), spacing=3)  #dt internacao
    document.write_hrmin(dict_especifico['hora_internacao_mae'], (442, 691), space=3)  #casa da hora
    #!campo 31
    match dict_especifico['parto_internacao']:
        case 'parto-internacao-sim':
            document.write_cross((179, 709))  #parto na internacao sim
        case 'parto-internacao-nao':
            document.write_cross((234, 709))  #parto na internacao nao
    #!campo 32
    #verificar utilizacao de partograma
    match dict_especifico['util_partograma']:
        case 'utilizou-partograma-sim':
            document.write_cross((176, 725))  #utilizou partograma sim
        case 'utilizou-partograma-nao':
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
    match dict_especifico['inter_aval_materna']:
        case 'intervalo-avaliacoes-materna-sim':
            document.write_cross((315, 758))  #intercorrencia materna sim
        case 'intervalo-avaliacoes-materna-nao':
            document.write_cross((337, 758))  #intercorrencia materna nao
    #verificar intercorrencia fetal
    match dict_especifico['inter_aval_fetal']:
        case 'intervalo-avaliacoes-fetal-sim':
            document.write_cross((399, 758))  #intercorrencia fetal sim
        case 'intervalo-avaliacoes-fetal-nao':
            document.write_cross((421, 758))  #intercorrencia fetal nao

    #===================== FIM DA PRIMEIRA PAGINA =======================

    #!campo 35
    #verificar uso de ocitocina
    match dict_especifico['ocitocina_mae']:
        case 'ocitocina-mae-sim':
            document.write_cross((285, 41), pg=1)  #ocitocina sim
        case 'ocitocina-mae-nao':
            document.write_cross((381, 41), pg=1)  #ocitocina nao
        case 'ocitocina-mae-naoSeAplica':
            document.write_cross((467, 41), pg=1)  #ocitocina n se aplica
    #!campo 36
    #verificar uso de eperidina
    match dict_especifico['eperidina_mae']:
        case 'eperidina-mae-sim':
            document.write_cross((285, 57), pg=1)  #eperidina sim
        case 'eperidina-mae-nao':
            document.write_cross((381, 57), pg=1)  #eperidina nao
        case 'eperidina-mae-naoSeAplica':
            document.write_cross((467, 57), pg=1)  #eperidina n se aplica
    #!campo 37
    #verificar uso de corticoide
    match dict_especifico['corticoide_mae']:
        case 'corticoide-mae-sim':
            document.write_cross((142, 73), pg=1)  #corticoide sim
        case 'corticoide-mae-nao':
            document.write_cross((381, 73), pg=1)  #corticoide nao
        case 'corticoide-mae-naoSeAplica':
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
    match dict_especifico['tipo_parto']:
        case 'tipo-parto-vaginal-forceps':
            document.write_cross((157, 152), pg=1)  #vaginal c forceps
        case 'tipo-parto-vaginal':
            document.write_cross((318, 152), pg=1)  #vaginal
        case 'tipo-parto-cesaria':
            document.write_cross((468, 152), pg=1)  #cesarea
    #se cesarea true qual o motivo no prontuario:
    #verificar motivo de cesaria
    match dict_especifico['motivo_cesaria']:
        case 'motivo-cesaria-anomalia':
            document.write_cross((111, 167), pg=1)  #apres anomala
        case 'motivo-cesaria-anterior':
            document.write_cross((111, 182), pg=1)  #cesarea anterior
        case 'motivo-cesaria-desproporcao':
            document.write_cross((111, 197), pg=1)  #desproporcao cefalopelvica
        case 'motivo-cesaria-placenta':
            document.write_cross((211, 167), pg=1)  #descolamento prematuro
        case 'motivo-cesaria-falha':
            document.write_cross((211, 182), pg=1)  #falha inducao parto
        case 'motivo-cesaria-feto-morto':
            document.write_cross((211, 197), pg=1)  #feto morto
        case 'motivo-cesaria-hemorragia-vaginal':
            document.write_cross((318, 167), pg=1)  #hemorragia vaginal
        case 'motivo-cesaria-eclampsia':
            document.write_cross((318, 182), pg=1)  #pre/eclampsia
        case 'motivo-cesaria-ruptura-prematura':
            document.write_cross((318, 197), pg=1)  #ruptura prematura membrana
        case 'motivo-cesaria-sofirmento-fetal':
            document.write_cross((425, 167), pg=1)  #sofrimento fetal agudo
        case 'motivo-cesaria-parto-prolongado':
            document.write_cross((425, 182), pg=1)  #trab parto prolongado
        case 'motivo-cesaria-outro':
            document.write_cross((425, 197), pg=1)  #outra
    document.write_text(dict_especifico['motivo_cesaria_outro_descricao'], (425, 207),
                        pg=1)  #descricao do motivo de cesaria
    #!campo 41
    #todo verificar quem atendeu
    match dict_especifico['quem_atendeu']:
        case 'quem-atendeu-obstetra':
            document.write_cross((143, 227), pg=1)  #medico gineco-obstetra
        case 'quem-atendeu-parteira':
            document.write_cross((143, 242), pg=1)  #parteira
        case 'quem-atendeu-nao-obstetra':
            document.write_cross((238, 227), pg=1)  #medico nao gineco-obstetra
        case 'quem-atendeu-obstretriz':
            document.write_cross((346, 227), pg=1)  #enfermeira obstetriz
        case 'quem-atendeu-enfermeira':
            document.write_cross((428, 227), pg=1)  #enfermeira
        case 'quem-atendeu-sem-assistencia':
            document.write_cross((428, 242), pg=1)  #sem assistencia
        case 'quem-atendeu-outro':
            document.write_cross((238, 242), pg=1)  #outro
    document.write_text(dict_especifico['que_atendeu_outro'], (272, 242), pg=1)  #outro quem atendeu
    #!campo 42
    #TODO verificar liquido amniotico
    match dict_especifico['liq_amni']:
        case 'liq-amniotico-claro':
            document.write_cross((183, 258), pg=1)  #claro
        case 'liq-amniotico-meconio':
            document.write_cross((238, 258), pg=1)  #com meconio
        case 'liq-amniotico-sanguinolento':
            document.write_cross((292, 258), pg=1)  #sanguinolento
        case 'liq-amniotico-fetido':
            document.write_cross((346, 258), pg=1)  #fetido
        case 'liq-amniotico-outro':
            document.write_cross((428, 258), pg=1)  #outro
    document.write_text(dict_especifico['liq_amni_outro'], (458, 257), pg=1)  #outro liquido amniotico
    #!campo 43
    #TODO verificar anestesia
    match dict_especifico['anestesia_parto']:
        case 'anestesia-parto-nenhuma':
            document.write_cross((183, 274), pg=1)  #nenhuma
        case 'anestesia-parto-geral':
            document.write_cross((238, 274), pg=1)  #geral
        case 'anestesia-parto-raquidiana':
            document.write_cross((292, 274), pg=1)  #raquidiana
        case 'anestesia-parto-peridural':
            document.write_cross((346, 274), pg=1)  #peridural
        case 'anestesia-parto-local':
            document.write_cross((392, 274), pg=1)  #local
        case 'anestesia-parto-outro':
            document.write_cross((428, 274), pg=1)  #outra
    document.write_text(dict_especifico['anestesia_parto_outro'], (458, 274), pg=1)  #outra anestesia
    #!campo 44
    #TODO verificar intercorrencia parto
    match dict_especifico['intercorr_parto']:
        case 'intercorrencia-parto-nenhuma':
            document.write_cross((198, 290), pg=1)  #nenhuma
        case 'intercorrencia-parto-hipertensao':
            document.write_cross((238, 290), pg=1)  #hipertensão
        case 'intercorrencia-parto-hemorragia':
            document.write_cross((292, 290), pg=1)  #Hemorragia
        case 'intercorrencia-parto-outro':
            document.write_cross((346, 290), pg=1)  #outra
    document.write_text(dict_especifico['intercorr_parto_outro'], (376, 290), pg=1)  #outra intercorrencia
    #!campo 45
    document.write_box(dict_especifico['evolucao_inter_mae'], rect=(53, 308, 542, 365), pg=1)  #evolucao internacao mae
    #!campo 46
    #TODO verificar parto sifilis
    match dict_especifico['parto_sifilis']:
        case 'parto-sifilis-nao':
            document.write_cross((204, 382), pg=1)  #sifilis n reagente
        case 'parto-sifilis-sim':
            document.write_cross((265, 382), pg=1)  #sifilis reagente
        case 'parto-sifilis-naoRealizado':
            document.write_cross((318, 382), pg=1)  #sifilis n realizado
    #TODO verificar parto hiv
    match dict_especifico['parto_hiv']:
        case 'parto-hiv-nao':
            document.write_cross((204, 398), pg=1)  #hiv n reagente
        case 'parto-hiv-sim':
            document.write_cross((265, 398), pg=1)  #hiv reagente
        case 'parto-hiv-naoRealizado':
            document.write_cross((318, 398), pg=1)  #hiv n realizado
    #* Bloco VII Condições de nascimento op N se aplica
    if dict_especifico['op_cond_nasc_NSA'] == '1':
        document.write_cross((463, 413), pg=1)  #opcao de n se aplica
    #!campo 47
    #TODO verificar natimorto aval
    match dict_especifico['natimorto_aval']:
        case 'natimorto-avaliado-obstetra':
            document.write_cross((204, 429), pg=1)  #medico gineco-obstetra
        case 'natimorto-avaliado-pediatra':
            document.write_cross((292, 429), pg=1)  #medico pediatra/neonatologista
        case 'natimorto-avaliado-outro-medico':
            document.write_cross((471, 429), pg=1)  #outro medico
        case 'natimorto-avaliado-enfermeira':
            document.write_cross((92, 444), pg=1)  #enfermeira obstetriz
        case 'natimorto-avaliado-parteira':
            document.write_cross((204, 444), pg=1)  #parteira
        case 'natimorto-avaliado-ninguem':
            document.write_cross((471, 444), pg=1)  #Ninguem
        case 'natimorto-avaliado-outro':
            document.write_cross((292, 444), pg=1)  #outro
    document.write_text(dict_especifico['natimorto_aval_outro'], (320, 444), pg=1)  #outro natimorto aval
    #!campo 48
    document.write_code(dict_especifico['idade_gest_nasc'], (178, 456), pg=1, space=2)  #idade gestacional
    #!campo 49
    document.write_code(dict_especifico['peso_nascimento'], (174, 472), pg=1, space=3)  #peso de nascimento
    #!campo 50
    match dict_especifico['quando_obito_ocorr']:
        case 'obito-ocorreu-antes-parto':
            document.write_cross((170, 489), pg=1)  #antes do parto
        case 'obito-ocorreu-durante-parto':
            document.write_cross((292, 489), pg=1)  #durante parto
        case 'obito-ocorreu-apos-parto':
            document.write_cross((428, 489), pg=1)  #apos parto
    #TODO se antes do parto true, foi macerado?
    #!campo 50.1
    match dict_especifico['feto_macerado']:
        case 'feto-macerado-sim':
            document.write_cross((292, 504), pg=1)  #sim ir para o bloco X
        case 'feto-macerado-durante-nao':
            document.write_cross((318, 504), pg=1)  #nao
    #!campo 51
    document.write_code(dict_especifico['apgar_1min'], (166, 520), pg=1)  #?apgar 1 min verificar o que escrever
    document.write_code(dict_especifico['apgar_5min'], (242, 517), pg=1)  #?apgar 5 min
    if dict_especifico['op_apgar_natimorto'] == '1':
        document.write_cross((312, 523), pg=1)  #natimorto
    #!campo 52
    #TODO verificar classificacao RN
    match dict_especifico['classificacaoRN']:
        case 'classificacaoRN-adequado':
            document.write_cross((137, 540), pg=1)  #adequado para idade gestacional
        case 'classificacaoRN-pequeno':
            document.write_cross((264, 540), pg=1)  #pequeno para idade gestacional
        case 'classificacaoRN-grande':
            document.write_cross((398, 540), pg=1)  #grande para idade gestacional
    #!campo 53
    #TODO verificar reanimacao
    match dict_especifico['reanimacao']:
        case 'reanimacao-sim':
            document.write_cross((224, 555), pg=1)  #sim
        case 'reanimacao-nao':
            document.write_cross((264, 557), pg=1)  #nao
    #!campo 54
    #TODO verificar assistencia RN
    match dict_especifico['assistenciaRN']:
        case 'assistenciaRN-nenhum':
            document.write_cross((435, 573), pg=1)  #nenhum
        case 'assistenciaRN-aspiracao':
            document.write_cross((72, 588), pg=1)  #aspiração das vias aéreas
        case 'assistenciaRN-cateterismo':
            document.write_cross((177, 588), pg=1)  #Cateterismo umbilical
        case 'assistenciaRN-entubacao':
            document.write_cross((277, 588), pg=1)  #Entubação
        case 'assistenciaRN-oxigenio':
            document.write_cross((386, 588), pg=1)  #Oxigenio
        case 'assistenciaRN-sonda':
            document.write_cross((470, 588), pg=1)  #Sonda nasogástrica
        case 'assistenciaRN-outro-procedimento':
            document.write_cross((75, 603), pg=1)  #Outros procedimentos
        case 'assistenciaRN-medicamentos':
            document.write_cross((71, 618), pg=1)  #Medicamentos utilizados
    document.write_text(dict_especifico['assistRN_outro_proced'], (177, 602), pg=1)  #outros procedimentos
    document.write_text(dict_especifico['assistRN_outro_medicam'], (177, 617), pg=1)  #medicamentos utilizados
    #!campo 55
    #TODO verificar diagnostico RN hipoglicemia
    match dict_especifico['hipoglicemia']:
        case 'hipoglicemia-sim':
            document.write_cross((204, 633), pg=1)  #sim
        case 'hipoglicemia-nao':
            document.write_cross((249, 633), pg=1)  #nao
        case 'hipoglicemia-naoFez':
            document.write_cross((367, 633), pg=1)  #n fez exame
    #* Bloco VIII Atendimento após o nascimento op N se aplica
    if dict_especifico['op_atend_apos_nasc'] == '1':
        document.write_cross((330, 651), pg=1)  #opcao de n se aplica
    #!campo 56
    #TODO setor internacao RN
    match dict_especifico['setorRN']:
        case 'setorRN-aloj-conjunto':
            document.write_cross((175, 670), pg=1)  #alojamento conjunto
        case 'setorRN-UTI-neonatal':
            document.write_cross((256, 670), pg=1)  #UTI/CTI neonatal
        case 'setorRN-ICINCo':
            document.write_cross((354, 670), pg=1)  #cuidado intermediario neonatal UCINCo
        case 'setorRN-ICINCa':
            document.write_cross((72, 685), pg=1)  #Cuidado intermediario neonatal Canguru UCINCa
        case 'setorRN-outro':
            document.write_cross((256, 685), pg=1)  #Outro
    document.write_text(dict_especifico['setorRN_outro_descricao'], (286, 684), pg=1)  #outro setor RN
    #!campo 57
    #TODO if RN tinha baixo peso <2500g?
    match dict_especifico['RN_baixo_peso']:
        case 'RN-baixo-peso-sim':
            document.write_cross((175, 700), pg=1)  #sim
        case 'RN-baixo-peso-nao':
            document.write_cross((198, 700), pg=1)  #nao
    #!campo 58
    #TODO RN era prematuro? IG < 37 semanas
    match dict_especifico['RN_prematuro']:
        case 'RN-prematuro-sim':
            document.write_cross((455, 701), pg=1)  #sim
        case 'RN-prematuro-nao':
            document.write_cross((478, 701), pg=1)  #nao
    #!campo 59
    #TODO verificar intercorrencia apos o nascimento
    match dict_especifico['INASC']:
        case 'INASC-metabolico':
            document.write_cross((176, 717), pg=1)  #disturbio metabolico
        case 'INASC-membrana-hialina':
            document.write_cross((257, 717), pg=1)  #doenca membrana hialina
        case 'INASC-hemolitica':
            document.write_cross((358, 717), pg=1)  #doenca hemolitica
        case 'INASC-ictericia':
            document.write_cross((444, 717), pg=1)  #ictericia
        case 'INASC-infeccao-confirmada':
            document.write_cross((58, 732), pg=1)  #infeccao confirmada
        case 'INASC-infeccao-suspeita':
            document.write_cross((176, 732), pg=1)  #infeccao suspeita
        case 'INASC-malformacao':
            document.write_cross((257, 732), pg=1)  #malformação congenita
        case 'INASC-aspiracao-meconial':
            document.write_cross((358, 732), pg=1)  #sd. aspiracao meconial
        case 'INASC-taquipneia':
            document.write_cross((444, 732), pg=1)  #taquipneia transitoria do RN
        case 'INASC-tocotraumatismo':
            document.write_cross((58, 747), pg=1)  #Tocotraumatismo
        case 'INASC-outro':
            document.write_cross((176, 747), pg=1)  #outra
    document.write_text(dict_especifico['INASC_outro_descricao'], (206, 746), pg=1)  #outra intercorrencia
    #!campo 60
    #TODO verificar admissao UTI neonatal
    match dict_especifico['IAUN']:
        case 'IAUN-sim':
            document.write_cross((210, 763), pg=1)  #sim
        case 'IAUN-nao':
            document.write_cross((505, 762), pg=1)  #nao
    #se sim motivo
    document.write_text(dict_especifico['IAUN_motivo'], (260, 762), pg=1)  #motivo
    #*===========================FIM DA SEGUNDA PAGINA===========================
    #!campo 60.1
    match dict_especifico['IUN']:
        case 'IUN-sim':
            document.write_cross((203, 41), pg=2)  #sim
        case 'IUN-nao':
            document.write_cross((504, 41), pg=2)  #nao
    #se sim data
    document.write_date(dict_especifico['dt_IUN'], (243, 38), pg=2, spacing=3)  #data
    document.write_code(dict_especifico['hora_IUN'][:5], (407, 38), pg=2, space=3)  #casa da hora
    #!campo 60.1.1
    match dict_especifico['mais3horas_inter']:
        case 'mais3horas-internar-sim':
            document.write_cross((203, 57), pg=2)  #sim
        case 'mais3horas-internar-nao':
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
    match dict_especifico['MARNI']:
        case 'MARNI-sim-integral':
            document.write_cross((249, 278), pg=2)  #sim em tempo integral
        case 'MARNI-sim-parcial':
            document.write_cross((345, 278), pg=2)  #sim em tempo parcial
        case 'MARNI-nao':
            document.write_cross((434, 278), pg=2)  #nao
    #!campo 64
    #TODO verificar se a mae nao acompanhou rn, rn teve outro acompanhante
    match dict_especifico['RNOA']:
        case 'RNOA-sim-integral':
            document.write_cross((249, 294), pg=2)  #sim em tempo integral
        case 'RNOA-sim-parcial':
            document.write_cross((345, 294), pg=2)  #sim em tempo parcial
        case 'RNOA-nao':
            document.write_cross((434, 294), pg=2)  #nao
    #!campo 65
    #TODO verificar desfecho internação após nascimento
    match dict_especifico['DIAN']:
        case 'DIAN-alta':
            document.write_cross((244, 310), pg=2)  #alta
        case 'DIAN-transferencia':
            document.write_cross((320, 310), pg=2)  #transferencia
        case 'DIAN-obito':
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
    match dict_especifico['obito_RN']:
        case 'obito-RN-alojamento-conjunto':
            document.write_cross((196, 387), pg=2)  #alojamento conjunto
        case 'obito-RN-cuidado-intermediario':
            document.write_cross((276, 387), pg=2)  #cuidado intermediario
        case 'obito-RN-UTI-neonatal':
            document.write_cross((357, 387), pg=2)  #uti neonatal
        case 'obito-RN-centro-obstetrico':
            document.write_cross((414, 387), pg=2)  #centro obstetrico
        case 'obito-RN-outro':
            document.write_cross((483, 387), pg=2)  #outro
    #* Bloco IX - Assistencia hospitalar a crianca durante a situação que levou a obito op n se aplica
    if dict_especifico['op_AHCDSO_NSA'] == '1':
        document.write_cross((484, 402), pg=2)  #opcao de n se aplica
    #!campo 72 data da intervenção
    document.write_date(dict_especifico['dt_inter_crianca'], (135, 430), pg=2, spacing=3)  #data
    document.write_hrmin(dict_especifico['hr_inter_crianca'], (398, 430), pg=2, space=3)  #casa da hora
    #!campo 73 a criança veio transferida de outro hospital
    match dict_especifico['CVTH']:
        case 'CVTH-sim':
            document.write_cross((204, 448), pg=2)  #sim
        case 'CVTH-nao':
            document.write_cross((414, 448), pg=2)  #nao
    document.write_text(dict_especifico['CVTH_hospital'], (95, 463), pg=2)  #nome do hospital
    document.write_code(dict_especifico['tempo_inter_crianca'], (450, 462), pg=2, space=3)  #tempo internação
    match dict_especifico['tipo_tempo_inter']:
        case 'TIT-dias':
            document.write_cross((481, 465), pg=2)  #dias
        case 'TIT-meses':
            document.write_cross((503, 465), pg=2)  #horas
    #!campo 74 breve historia na admissao
    document.write_box(dict_especifico['historia_admissao'], rect=(54, 484, 550, 525), pg=2)  #breve historia
    #!campo 75 dados da criança na admissao
    #!campo 75.1 idade
    document.write_code(dict_especifico['ICA'], (392, 540), pg=2, space=2)  #idade
    match dict_especifico['ICAT']:
        case 'ICAT-dias':
            document.write_cross((424, 542), pg=2)  #dias
        case 'ICAT-meses':
            document.write_cross((446, 542), pg=2)  #meses
        case 'ICAT-anos':
            document.write_cross((476, 542), pg=2)  #anos
    #!campo 75.2 peso
    document.write_code(dict_especifico['peso_crianca_admiss'] + '9999', (134, 555), pg=2, space=3)  #peso
    #!campo 75.3 altura
    document.write_code(dict_especifico['ACA'], (390, 555), pg=2, space=3)  #altura
    #!campo 75.4 estado nutricional
    match dict_especifico['ENCAT']:
        case 'ENCAT-eutrofica':
            document.write_cross((131, 574), pg=2)  #eutrofica
        case 'ENCAT-desnutrida':
            document.write_cross((185, 574), pg=2)  #desnutrida
    #!campo 75.5 estado hidratação
    match dict_especifico['EHCAT']:
        case 'EHCAT-hidratada':
            document.write_cross((385, 574), pg=2)  #hidratada
        case 'EHCAT-desidratada':
            document.write_cross((449, 574), pg=2)  #desidratada
    #!campo 75.6 estado geral grave
    match dict_especifico['EGGCA']:
        case 'EGGCA-sim':
            document.write_cross((131, 590), pg=2)  #sim
        case 'EGGCA-nao':
            document.write_cross((185, 590), pg=2)  #nao
    #!campo 75.7 perfusão
    match dict_especifico['PCA']:
        case 'PCA-normal':
            document.write_cross((385, 590), pg=2)  #normal
        case 'PCA-diminuida':
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
    match dict_especifico['IA_UTIP']:
        case 'IA-UTIP-sim':
            document.write_cross((212, 761), pg=2)  #sim
        case 'IA-UTIP-nao':
            document.write_cross((504, 761), pg=2)  #nao
    document.write_text(dict_especifico['IA_UTIP_motivo'], (262, 760), pg=2)  #motivo
    #* ========================FIM DA TERCEIRA PAGINA===========================
    #!campo 78.1 se sim foi internado na UTI pediatrica
    match dict_especifico['INT_UTIP']:
        case 'INT-UTIP-sim':
            document.write_cross((205, 41), pg=3)  #sim
        case 'INT-UTIP-nao':
            document.write_cross((504, 41), pg=3)  #nao
    #se sim data
    document.write_date(dict_especifico['dt_INT_UTIP'], (245, 38), pg=3, spacing=3)  #data
    document.write_hrmin(dict_especifico['hora_INT_UTIP'], (410, 38), pg=3, space=3)  #hora
    #!campo 78.1.1 demorou >3 horas para ser internado
    match dict_especifico['DM3HPSIC']:
        case 'DM3HPSIC-sim':
            document.write_cross((205, 57), pg=3)  #sim
        case 'DM3HPSIC-nao':
            document.write_cross((504, 57), pg=3)  #nao
    #se sim motivo
    document.write_text(dict_especifico['DM3HPSIC_motivo'], (256, 56), pg=3)  #motivo
    #!campo 78.1.2 pq nao foi internado
    document.write_text(dict_especifico['crianca_nao_inter_motivo'], (205, 73), pg=3)  #motivo
    #!campo 79 desfecho da internacao apos o nascimento
    match dict_especifico['DIANC']:
        case 'DIANC-alta':
            document.write_cross((239, 90), pg=3)  #alta
        case 'DIANC-transferencia':
            document.write_cross((319, 90), pg=3)  #transferencia
        case 'DIANC-obito':
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
    match dict_especifico['SOC']:
        case 'SOC-UTIP':
            document.write_cross((204, 170), pg=3)  #UTI neonatal/pediatrica
        case 'SOC-outro':
            document.write_cross((305, 170), pg=3)  #outro
        case 'SOC-naoSeAplica':
            document.write_cross((475, 170), pg=3)  #n se aplica
    document.write_text(dict_especifico['SOC_outro_descricao'], (335, 169), pg=3)  #outro local
    #* Bloco X - informacoes complementares sobre o obito
    #! campo 86 - liste os diagnosticos ou hipoteses diagnosticas
    document.write_box(dict_especifico['diag_clinicos'], rect=(70, 205, 550, 262), pg=3)  #diagnostico
    #! campo 87 - se houve necropsia
    #todo verificar se houve necropsia
    match dict_especifico['corpo_env_necropsia']:
        case 'corpo-enviado-necropsia-sim':
            document.write_cross((197, 275), pg=3)  #sim
        case 'corpo-enviado-necropsia-nao':
            document.write_cross((300, 275), pg=3)  #nao
    #se sim qual o tipo da necropsia
    #todo verificar tipo de necropsia
    match dict_especifico['CENL']:
        case 'CENL-iml':
            document.write_cross((220, 275), pg=3)  #IML
        case 'CENL-svo':
            document.write_cross((242, 275), pg=3)  #SVO
        case 'CENL-outro':
            document.write_cross((266, 275), pg=3)  #Outro
    #! campo 87.1 - se sim foi realizada a necropsia
    #todo verificar sim e nao
    match dict_especifico['realiz_necropsia']:
        case 'realizada-necropsia-sim':
            document.write_cross((490, 275), pg=3)  #sim
        case 'realizada-necropsia-nao':
            document.write_cross((514, 275), pg=3)  #nao
    #! campo 88 - este caso foi analisado por alguma comissao/grupo do hospital
    #todo verificar se foi analisado
    match dict_especifico['caso_analisado']:
        case 'caso-analisado-sim':
            document.write_cross((261, 290), pg=3)  #sim
        case 'caso-analisado-nao':
            document.write_cross((315, 290), pg=3)  #nao
    #se sim qual a comissao e conclusoes
    document.write_box(dict_especifico['comissao_conclusao'], rect=(65, 311, 550, 374), pg=3)  #comissao
    #se nao porque
    #todo verificar motivo
    match dict_especifico['CNA']:
        case 'CNA-nao-encaminhado':
            document.write_cross((139, 388), pg=3)  #nao foi encaminhado
        case 'CNA-encaminhado-nao-analisado':
            document.write_cross((225, 388), pg=3)  #foi encaminhado mas nao analisado
        case 'CNA-sem-comissao':
            document.write_cross((366, 388), pg=3)  #n existe comissao
        case 'CNA-outro':
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
    match dict_especifico['funcionario_hosp']:
        case 'funcionario-hospital-sim':
            document.write_cross((272, 531), pg=3)  #sim
        case 'funcionario-hospital-nao':
            document.write_cross((297, 531), pg=3)  #nao
    #! campo 93 - data do encerramento
    document.write_date(dict_especifico['dt_encerramento'], (227, 546), pg=3, spacing=3)  #data
    #! campo 94 - info anexa
    #todo verificar se tem info anexa
    match dict_especifico['info_anexa']:
        case 'informacao-anexa-sim':
            document.write_cross((454, 551), pg=3)  #sim
        case 'informacao-anexa-nao':
            document.write_cross((478, 551), pg=3)  #nao

    document.save(nome_arquivo, path_pdf_gerado)
