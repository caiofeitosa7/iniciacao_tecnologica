from pdfWritter import PDFWriter

pdf = 'Óbito Fetal-Infantil1.pdf'
doc = PDFWriter(pdf)

data = {
    "num_casos": "9999",
    "op_obito_fetal_DO": "1",
    "nome_paciente": "observacao",
    "sexo": "observacao",
    "semanas_gestacao": "99",
    "idade_obito": "25",
    "tp_idade_obito": "25",
    "peso": "8888",
    "tp_peso": "observacao",
    "dt_obito": "15/02/2022",
    "num_DO": "999999999",
    "dt_nascimento": "15/02/2022",
    "num_DN": "99999999999",
    "ender_responsavel": "observacao",
    "telefone_responsavel": "86999999999",
    "municipio_responsavel": "observacao",
    "uf_responsavel": "PI",
    "num_cartao_sus_mae": "123456789012345",
    "nome_mae": "observacao",
    "idade_mae": "25",
    "raca_mae": "observacao",
    "etnia_indig_mae": "observacao",
    "aldeia_mae": "observacao",
    "nao_aldeada_mae": "9",
    "nome_hospital2": "observacao",
    "cod_cnes_us": "1234567",
    "municipio_hospital2": "observacao",
    "uf_hospital2": "PI",
    "tipo_estab": "observacao",
    "pront_crianca": "observacao",
    "pront_mae": "observacao",
    "op_admiss_mae_NSA": "9",
    "dt_admiss_mae": "15/02/2022",
    "hora_admiss_mae": "12:50",
    "idade_gestacional": "25",
    "idade gestacional_dum": "9",
    "tp_idade_gest": "25",
    "dt_dum": "15/02/2022",
    "press_art_adm_mae": "130/800",
    "op_mae_obito_admissao": "9",
    "parto_admissao": "observacao",
    "op_reg_clinico_admiss": "9",
    "contracoes_10min": "99",
    "apresentacao_fetal": "observacao",
    "bcf": "observacao",
    "bcf_posit_descricao": "999",
    "descida_apresent": "99",
    "dilatacao_colo": "99",
    "membrana": "observacao",
    "rotas_tempo": "99",
    "rotas_liqAmniotico": "observacao",
    "motivo_inter": "observacao",
    "motivo_inter_descricao": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "op_hist_obstet_NSA": "9",
    "num_gest_anteriores": "99",
    "quant_abortos": "99",
    "quant_partos": "99",
    "quant_vaginais": "99",
    "quant_cesarias": "99",
    "quant_vivos": "99",
    "ano_ult_parto": "2024",
    "doen_gest_anterior": "observacao",
    "doen_gest_ante_sim_desc": "observacao",
    "doen_fora_gest": "observacao",
    "doen_fora_gest_sim_desc": "observacao",
    "op_inter_mae_NSA": "9",
    "dt_internacao_mae": "15/02/2022",
    "hora_internacao_mae": "observacao",
    "parto_internacao": "observacao",
    "util_partograma": "observacao",
    "util_partograma_obs": "observacao",
    "quant_maternas": "99",
    "quant_fetais": "99",
    "op_av_parto_NSA": "9",
    "inter_aval_materna": "observacao",
    "inter_aval_fetal": "observacao",
    "op_inter_aval_NSA": "9",
    "ocitocina_mae": "observacao",
    "eperidina_mae": "observacao",
    "corticoide_mae": "observacao",
    "dt_corticoide": "15/02/2022",
    "op_outra_med_internacao": "observacao",
    "outra_med_internacao": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "dt_parto": "15/02/2022",
    "hora_parto": "observacao",
    "tipo_parto": "observacao",
    "motivo_cesaria": "observacao",
    "motivo_cesaria_outro_descricao": "observacao",
    "quem_atendeu": "observacao",
    "que_atendeu_outro": "observacao",
    "liq_amni": "observacao",
    "liq_amni_outro": "observacao",
    "anestesia_parto": "observacao",
    "anestesia_parto_outro": "observacao",
    "intercorr_parto": "observacao",
    "intercorr_parto_outro": "observacao",
    "evolucao_inter_mae": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "parto_sifilis": "observacao",
    "parto_hiv": "observacao",
    "op_cond_nasc_NSA": "9",
    "natimorto_aval": "observacao",
    "natimorto_aval_outro": "observacao",
    "idade_gest_nasc": "25",
    "peso_nascimento": "5699",
    "quando_obito_ocorr": "observacao",
    "feto_macerado": "observacao",
    "apgar_1min": "9",
    "apgar_5min": "9",
    "op_apgar_natimorto": "9",
    "classificacaoRN": "observacao",
    "reanimacao": "observacao",
    "assistenciaRN": "observacao",
    "assistRN_outro_proced": "observacao",
    "assistRN_outro_medicam": "observacao",
    "hipoglicemia": "observacao",
    "op_atend_apos_nasc": "9",
    "setorRN": "observacao",
    "setorRN_outro_descricao": "observacao",
    "RN_baixo_peso": "observacao",
    "RN_prematuro": "observacao",
    "INASC": "observacao",
    "INASC_outro_descricao": "observacao",
    "IAUN": "observacao",
    "IAUN_motivo": "observacao",
    "IUN": "observacao",
    "dt_IUN": "15/02/2022",
    "hora_IUN": "22:22",
    "mais3horas_inter": "observacao",
    "mais3horas_inter_motivo": "observacao",
    "motivo_nao_inter": "observacao",
    "evolucao_inter_RN": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "PRDIRN": "observacao",
    "PRDIRN_outro_descricao": "observacao",
    "MARNI": "observacao",
    "RNOA": "observacao",
    "DIAN": "observacao",
    "dt_altaRN": "15/02/2022",
    "peso_altaRN": "9999",
    "motivo_transfRN": "observacao",
    "hosp_transfRN": "observacao",
    "hora_obitoRN": "observacao",
    "op_hora_obitoRN_NSA": "9",
    "obito_RN": "observacao",
    "op_AHCDSO_NSA": "9",
    "dt_inter_crianca": "15/02/2022",
    "hr_inter_crianca": "observacao",
    "CVTH": "observacao",
    "CVTH_hospital": "observacao",
    "tempo_inter_crianca": "9",
    "tipo_tempo_inter": "observacao",
    "historia_admissao": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "ICA": "9",
    "ICAT": "observacao",
    "peso_crianca_admiss": "9",
    "ACA": "9",
    "ENCAT": "observacao",
    "EHCAT": "observacao",
    "EGGCA": "observacao",
    "PCA": "observacao",
    "BCCA": "9",
    "RCA": "9",
    "TCA": "36.9",
    "diag_crianca_admissao": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "REIC": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "IA_UTIP": "observacao",
    "IA_UTIP_motivo": "observacao",
    "INT_UTIP": "observacao",
    "dt_INT_UTIP": "15/02/2022",
    "hora_INT_UTIP": "observacao",
    "DM3HPSIC": "observacao",
    "DM3HPSIC_motivo": "observacao",
    "crianca_nao_inter_motivo": "observacao",
    "DIANC": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "dt_alta_crianca": "15/02/2022",
    "peso_alta_crianca": "observacao",
    "CRIANCAT_motivo": "observacao",
    "op_CRIANCAT_motivo_NSA": "9",
    "CRIANCAT_nome_hosp": "observacao",
    "op_CRIANCAT_hosp_NSA": "9",
    "hora_obito_crianca": "observacao",
    "op_HOC_NSA": "9",
    "SOC": "observacao",
    "SOC_outro_descricao": "observacao",
    "diag_clinicos": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "corpo_env_necropsia": "observacao",
    "CENL": "observacao",
    "realiz_necropsia": "observacao",
    "caso_analisado": "observacao",
    "comissao_conclusao": "lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. lore ipsilum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "CNA": "observacao",
    "CNA_outro_descricao": "observacao",
    "outras_informacoes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "nome_notificante": "observacao",
    "telefone_investigador": "86999999999",
    "funcionario_hosp": "funcionario-hospital-nao",
    "dt_encerramento": "15/02/2022",
    "info_anexa": "informacao-anexa-sim",
    "PRDIRN_nenhum": "9",
    "PRDIRN_antibioti": "9",
    "PRDIRN_berco": "9",
    "PRDIRN_canguru": "9",
    "PRDIRN_cateter": "9",
    "PRDIRN_cpap": "9",
    "PRDIRN_disseccao": "9",
    "PRDIRN_entubacao": "9",
    "PRDIRN_fototera": "9",
    "PRDIRN_exsang": "9",
    "PRDIRN_hemotrans": "9",
    "PRDIRN_incuba": "9",
    "PRDIRN_nutri_par": "9",
    "PRDIRN_oxig_capacete": "9",
    "PRDIRN_oxig_inala": "9",
    "PRDIRN_puncao": "9",
    "PRDIRN_surf": "9",
    "PRDIRN_ventila": "9",
    "PRDIRN_outros": "9"
}

doc.write_code(data['num_casos'], (452, 43), space=3)
if data['op_obito_fetal_DO'] == '1':
    doc.write_cross((375, 65))
doc.write_text(data['nome_paciente'], (81, 81))
#verificar sexo é M ou F
match data['sexo']:
    case 'op-sexo-m':
        doc.write_cross((418, 78))
    case 'op-sexo-f':
        doc.write_cross((436, 78))
doc.write_code(data['semanas_gestacao'], (137, 96), space=2)
doc.write_code(data['idade_obito'], (228, 96), space=2)
#verificar tipo de idade
match data['tp_idade_obito']:
    case 'tp-idade-obito-meses':
        doc.write_cross((260, 99))  #meses
    case 'tp-idade-obito-dias':
        doc.write_cross((293, 99))  #dias
    case 'tp-idade-obito-horas':
        doc.write_cross((318, 99))  #horas
    case 'tp-idade-obito-min':
        doc.write_cross((350, 99))  #minutos
doc.write_code(data['peso'], (422, 94), space=3)
#verificar tipo de peso
match data['tp_peso']:
    case 'tp-peso-gr':
        doc.write_cross((493, 96))  #gramas
    case 'tp-peso-kg':
        doc.write_cross((514, 96))  #quilogramas
doc.write_date(data['dt_obito'], (124, 117), spacing=3)
doc.write_code(data['num_DO'], (350, 115), space=3, font_size=12)
doc.write_date(data['dt_nascimento'], (124, 137), spacing=3)
doc.write_code(data['num_DN'], (352, 134), space=3, font_size=12)
doc.write_text(data['ender_responsavel'], (195, 158))
doc.write_telefone(data['telefone_responsavel'][:2], (464, 156), font_size=11)
doc.write_telefone(data['telefone_responsavel'][2:], (479, 156), font_size=11)
doc.write_text(data['municipio_responsavel'], (195, 173))
doc.write_code(data['uf_responsavel'], (468, 171), space=2)
doc.write_code(data['num_cartao_sus_mae'], (431, 192))
doc.write_text(data['nome_mae'], (108, 212))
doc.write_code(data['idade_mae'], (465, 205), space=2)
#verificar raça da mãe
match data['raca_mae']:
    case 'raca-branca':
        doc.write_cross((98, 227))  #branca
    case 'raca-preta':
        doc.write_cross((129, 227))  #preta
    case 'raca-indigena':
        doc.write_cross((159, 227))  #indigena
    case 'raca-parda':
        doc.write_cross((98, 242))  #parda
    case 'raca-amarela':
        doc.write_cross((129, 242))  #amarela

doc.write_text(data['etnia_indig_mae'], (325, 227))  #se indigena etnia
doc.write_text(data['aldeia_mae'], (325, 242))  #se indigena aldeia
#se nao aldeada
if data['nao_aldeada_mae'] == '1':
    doc.write_cross((477, 243))

doc.write_text(data['nome_hospital2'], (109, 279))  #nome do hospital
doc.write_code(data['cod_cnes_us'], (425, 273), space=4, font_size=10)  #cnes
doc.write_text(data['municipio_hospital2'], (110, 301))  #municipio
doc.write_code(data['uf_hospital2'], (348, 296), space=2)  #uf
#verificar tipo de estabelecimento
match data['tipo_estab']:
    case 'tipo-estab-SUS':
        doc.write_cross((442, 294))  #tipo SUS
    case 'tipo-estab-convenio-SUS':
        doc.write_cross((464, 294))  #tipo CONVENIO SUS
    case 'tipo-estab-privado':
        doc.write_cross((442, 303))  #tipo PRIVADO
    case 'tipo-estab-outro':
        doc.write_cross((476, 303))  #tipo OUTRO
doc.write_code(data['pront_crianca'], (132, 315))  #prontuario criança
doc.write_code(data['pront_mae'], (450, 315))  #prontuario mae

# IV admissao da mae gestante no hospital/maternindade opt nao se aplica pular tudo IV
if data['op_admiss_mae_NSA'] == '1':
    doc.write_cross((478, 331))  #op de nao se aplica
doc.write_date(data['dt_admiss_mae'], (125, 342), spacing=3)  #dt_admiss_mae
doc.write_hrmin(data['hora_admiss_mae'], (364, 342), space=3)  # hora
doc.write_code(data['idade_gestacional'], (142, 360), space=2)  #idade gestacional
#verificar tipo dum / exam fisico / outro / n se aplica
match data['tp_idade_gest']:
    case 'idade-gestacional-DUM':
        doc.write_cross((220, 362))  # dum
    case 'idade-gestacional-exame-fisico':
        doc.write_cross((390, 362))  # exam fisico
    case 'idade-gestacional-outro':
        doc.write_cross((442, 362))  # outro
    case 'idade-gestacional-naoSeAplica':
        doc.write_cross((478, 362))  # n se aplica
doc.write_date(data['dt_dum'], (250, 360), spacing=3)  #dt dum
#if preferencia de formato xxx/xxx if not '/' insert '/' in the middle
if '/' not in data['press_art_adm_mae']:
    data['press_art_adm_mae'] = data['press_art_adm_mae'][:3] + '/' + data['press_art_adm_mae'][3:]
doc.write_code(data['press_art_adm_mae'], (202, 382), space=2)  #pressao arterial item 23
#verificar opcao de obito da mae na admissao caso true pular para 27
if data['op_mae_obito_admissao'] == '1':
    doc.write_cross((393, 385))  #opca de chegou em obito
#verificar tipo de parto campo 24
match data['parto_admissao']:
    case 'parto-admisso-antes':
        doc.write_cross((233, 403))  #antes do inicio do trabalho
    case 'parto-admisso-periodo-naoExpulsivo':
        doc.write_cross((335, 403))  #No periodo não expulsivo
    case 'parto-admisso-periodo-expulsivo':
        doc.write_cross((446, 403))  #No periodo expulsivo
#verificar opcao de registro clinico 25 se true pular
if data['op_reg_clinico_admiss'] == '1':
    doc.write_cross((478, 416))  #opcao de registro clinico 25
doc.write_code(data['contracoes_10min'], (148, 431), space=2)  #contracoes por 10 min
#verificar apresentacao fetal
match data['apresentacao_fetal']:
    case 'apresentacao-fetal-cefalica':
        doc.write_cross((141, 451))  #cefalica
    case 'apresentacao-fetal-pelvica':
        doc.write_cross((179, 451))  #pelvica
    case 'apresentacao-fetal-outra':
        doc.write_cross((214, 451))  #Outra
#verificar bcf
match data['bcf']:
    case 'op-bcf-positivo':
        doc.write_cross((121, 467))  #positivo
    case 'op-bcf-negativo':
        doc.write_cross((221, 467))  #negativo
doc.write_code(data['bcf_posit_descricao'], (163, 465), space=2)  #descricao do positivo
doc.write_code(data['descida_apresent'], (168, 484), space=2)  #descida da apresentacao
doc.write_code(data['dilatacao_colo'], (401, 431), space=2)  #dilatacao do colo
#todo verificar membrana
match data['membrana']:
    case 'op-membrana-integra':
        doc.write_cross((393, 451))  #integra
    case 'op-membrana-rota':
        doc.write_cross((432, 451))  #rotas
doc.write_code(data['rotas_tempo'], (400, 465), space=2)  #rotas e tempo
#todo verificar liquido amniotico
match data['rotas_liqAmniotico']:
    case 'rotas-liqAmniotico-claro':
        doc.write_cross((393, 488))  #claro
    case 'rotas-liqAmniotico-meconial':
        doc.write_cross((420, 488))  #meconial
    case 'rotas-liqAmniotico-fetido':
        doc.write_cross((461, 488))  #Fétido
    case 'rotas-liqAmniotico-outro':
        doc.write_cross((491, 488))  #Outro
#!campo 26
#verificar motivo de internacao
match data['motivo_inter']:
    case 'op-motivo-internacao-prematuro':
        doc.write_cross((55, 521))  #prematuridade
    case 'op-motivo-internacao-posDatismo':
        doc.write_cross((160, 521))  #pós-datismo
    case 'op-motivo-internacao-ruptura':
        doc.write_cross((213, 521))  #rupturas de membranas
    case 'op-motivo-internacao-preEclampsia':
        doc.write_cross((335, 521))  #pré-eclampsia
    case 'op-motivo-internacao-eclampsia':
        doc.write_cross((387, 521))  #eclampsia
    case 'op-motivo-internacao-sangTransvaginal':
        doc.write_cross((437, 521))  #Sangramento Transvaginal
    case 'op-motivo-internacao-cesariaAgendada':
        doc.write_cross((56, 536))  #cesarea agendada
    case 'op-motivo-internacao-febre':
        doc.write_cross((160, 536))  #febre
    case 'op-motivo-internacao-dimMovFecais':
        doc.write_cross((213, 536))  #diminuicao mov fetais
    case 'op-motivo-internacao-outros':
        doc.write_cross((335, 536))  #outros
    case 'op-motivo-internacao-nenhum':
        doc.write_cross((437, 536))  #nenhum dos anteriores
doc.write_box(data['motivo_inter_descricao'], rect=(55, 544, 550, 585))  #descricao do motivo de internacao
#*parte V historia obstetrica op N se aplica
#verificar opcao de historia obstetrica
if data['op_hist_obstet_NSA'] == '1':
    doc.write_cross((474, 600))  #opcao de historia obstetrica
#!campo 27
doc.write_code(data['num_gest_anteriores'], (73, 627), space=2)  #numero de gestacoes anteriores se 00 go to campo 29
doc.write_code(data['quant_abortos'], (203, 627), space=2)  #numero de abortos
doc.write_code(data['quant_partos'], (259, 627), space=2)  #numero de partos
doc.write_code(data['quant_vaginais'], (308, 627), space=2)  #numero de partos vaginais
doc.write_code(data['quant_cesarias'], (358, 627), space=2)  #numero de cesarias
doc.write_code(data['quant_vivos'], (413, 627), space=2)  #numero de vivos
doc.write_code(data['ano_ult_parto'], (471, 627), space=2)  #ano do ultimo parto
#!campo 28
match data['doen_gest_anterior']:
    case 'doenca-gestacao-anterior-nao':
        doc.write_cross((203, 643))  #doencas na gestacao anterior nao
    case 'doenca-gestacao-anterior-sim':
        doc.write_cross((249, 645))  #doencas na gestacao anterior sim

doc.write_text(data['doen_gest_ante_sim_desc'], (295, 645))  #descricao doencas na gestacao anterior
#!campo 29
match data['doen_fora_gest']:
    case 'doenca-fora-gestacao-nao':
        doc.write_cross((203, 660))  #doencas fora da gestacao nao
    case 'doenca-fora-gestacao-sim':
        doc.write_cross((248, 662))  #doencas fora da gestacao sim
doc.write_text(data['doen_fora_gest_sim_desc'], (295, 662))  #descricao doencas fora da gestacao
#*parte VI internacao hospitalar da mae-gestante op N se aplica
#todo verificar opcao de internacao hospitalar
if data['op_inter_mae_NSA'] == '1':
    doc.write_cross((466, 677))  #opcao de internacao hospitalar
#!campo 30
doc.write_date(data['dt_internacao_mae'], (142, 691), spacing=3)  #dt internacao
doc.write_hrmin(data['hora_internacao_mae'], (442, 691), space=3)  #casa da hora
#!campo 31
match data['parto_internacao']:
    case 'parto-internacao-sim':
        doc.write_cross((179, 709))  #parto na internacao sim
    case 'parto-internacao-nao':
        doc.write_cross((234, 709))  #parto na internacao nao
#!campo 32
#verificar utilizacao de partograma
match data['util_partograma']:
    case 'utilizou-partograma-sim':
        doc.write_cross((176, 725))  #utilizou partograma sim
    case 'utilizou-partograma-nao':
        doc.write_cross((200, 725))  #utilizou partograma nao
doc.write_text(data['util_partograma_obs'], (288, 725))  #descricao partograma
#!campo 33
#verificar opcao de avaliacao do parto
if data['op_av_parto_NSA'] == '1':
    doc.write_cross((467, 741))  #opcao de avaliacao do parto
doc.write_code(data['quant_maternas'], (326, 740), space=2)  #quantidade de maternas
doc.write_code(data['quant_fetais'], (411, 740), space=2)  #quantidade de fetais
#!campo 34
#verificar intercorrencia materna
if data['op_inter_aval_NSA'] == '1':
    doc.write_cross((467, 758))  #opcao de intercorrencia
match data['inter_aval_materna']:
    case 'intervalo-avaliacoes-materna-sim':
        doc.write_cross((315, 758))  #intercorrencia materna sim
    case 'intervalo-avaliacoes-materna-nao':
        doc.write_cross((337, 758))  #intercorrencia materna nao
#verificar intercorrencia fetal
match data['inter_aval_fetal']:
    case 'intervalo-avaliacoes-fetal-sim':
        doc.write_cross((399, 758))  #intercorrencia fetal sim
    case 'intervalo-avaliacoes-fetal-nao':
        doc.write_cross((421, 758))  #intercorrencia fetal nao
#===================== FIM DA PRIMEIRA PAGINA =======================
#!campo 35
#verificar uso de ocitocina
match data['ocitocina_mae']:
    case 'ocitocina-mae-sim':
        doc.write_cross((285, 41))  #ocitocina sim
    case 'ocitocina-mae-nao':
        doc.write_cross((381, 41))  #ocitocina nao
    case 'ocitocina-mae-naoSeAplica':
        doc.write_cross((467, 41))  #ocitocina n se aplica
#!campo 36
#verificar uso de eperidina
match data['eperidina_mae']:
    case 'eperidina-mae-sim':
        doc.write_cross((285, 57))  #eperidina sim
    case 'eperidina-mae-nao':
        doc.write_cross((381, 57))  #eperidina nao
    case 'eperidina-mae-naoSeAplica':
        doc.write_cross((467, 57))  #eperidina n se aplica
#!campo 37
#verificar uso de corticoide
match data['corticoide_mae']:
    case 'corticoide-mae-sim':
        doc.write_cross((142, 73))  #corticoide sim
    case 'corticoide-mae-nao':
        doc.write_cross((381, 73))  #corticoide nao
    case 'corticoide-mae-naoSeAplica':
        doc.write_cross((468, 73))  #corticoide n se aplica
doc.write_date(data['dt_corticoide'], (214, 71), pg=1, spacing=3)  #corticoide NAO
#!campo 38
if data['op_outra_med_internacao'] == '1':
    doc.write_cross((468, 90), pg=1)  #nenhuma
doc.write_box(data['outra_med_internacao'], rect=(53, 90, 542, 125), pg=1)  #outra medicação
#!campo 39
doc.write_date(data['dt_parto'], (149, 133), pg=1, spacing=3)  #dt parto
doc.write_hrmin(data['hora_parto'], (436, 133), pg=1, space=3)  #casa da hora
#!campo 40
#verificar tipo de parto
match data['tipo_parto']:
    case 'tipo-parto-vaginal-forceps':
        doc.write_cross((157, 152), pg=1)  #vaginal c forceps
    case 'tipo-parto-vaginal':
        doc.write_cross((318, 152), pg=1)  #vaginal
    case 'tipo-parto-cesaria':
        doc.write_cross((468, 152), pg=1)  #cesarea
#se cesarea true qual o motivo no prontuario:
#verificar motivo de cesaria
match data['motivo_cesaria']:
    case 'motivo-cesaria-anomalia':
        doc.write_cross((111, 167), pg=1)  #apres anomala
    case 'motivo-cesaria-anterior':
        doc.write_cross((111, 182), pg=1)  #cesarea anterior
    case 'motivo-cesaria-desproporcao':
        doc.write_cross((111, 197), pg=1)  #desproporcao cefalopelvica
    case 'motivo-cesaria-placenta':
        doc.write_cross((211, 167), pg=1)  #descolamento prematuro
    case 'motivo-cesaria-falha':
        doc.write_cross((211, 182), pg=1)  #falha inducao parto
    case 'motivo-cesaria-feto-morto':
        doc.write_cross((211, 197), pg=1)  #feto morto
    case 'motivo-cesaria-hemorragia-vaginal':
        doc.write_cross((318, 167), pg=1)  #hemorragia vaginal
    case 'motivo-cesaria-eclampsia':
        doc.write_cross((318, 182), pg=1)  #pre/eclampsia
    case 'motivo-cesaria-ruptura-prematura':
        doc.write_cross((318, 197), pg=1)  #ruptura prematura membrana
    case 'motivo-cesaria-sofirmento-fetal':
        doc.write_cross((425, 167), pg=1)  #sofrimento fetal agudo
    case 'motivo-cesaria-parto-prolongado':
        doc.write_cross((425, 182), pg=1)  #trab parto prolongado
    case 'motivo-cesaria-outro':
        doc.write_cross((425, 197), pg=1)  #outra
doc.write_text(data['motivo_cesaria_outro_descricao'], (425, 207), pg=1)  #descricao do motivo de cesaria
#!campo 41
#todo verificar quem atendeu
match data['quem_atendeu']:
    case 'quem-atendeu-obstetra':
        doc.write_cross((143, 227), pg=1)  #medico gineco-obstetra
    case 'quem-atendeu-parteira':
        doc.write_cross((143, 242), pg=1)  #parteira
    case 'quem-atendeu-nao-obstetra':
        doc.write_cross((238, 227), pg=1)  #medico nao gineco-obstetra
    case 'quem-atendeu-obstretriz':
        doc.write_cross((346, 227), pg=1)  #enfermeira obstetriz
    case 'quem-atendeu-enfermeira':
        doc.write_cross((428, 227), pg=1)  #enfermeira
    case 'quem-atendeu-sem-assistencia':
        doc.write_cross((428, 242), pg=1)  #sem assistencia
    case 'quem-atendeu-outro':
        doc.write_cross((238, 242), pg=1)  #outro
doc.write_text(data['que_atendeu_outro'], (272, 242), pg=1)  #outro quem atendeu
#!campo 42
#TODO verificar liquido amniotico
match data['liq_amni']:
    case 'liq-amniotico-claro':
        doc.write_cross((183, 258), pg=1)  #claro
    case 'liq-amniotico-meconio':
        doc.write_cross((238, 258), pg=1)  #com meconio
    case 'liq-amniotico-sanguinolento':
        doc.write_cross((292, 258), pg=1)  #sanguinolento
    case 'liq-amniotico-fetido':
        doc.write_cross((346, 258), pg=1)  #fetido
    case 'liq-amniotico-outro':
        doc.write_cross((428, 258), pg=1)  #outro
doc.write_text(data['liq_amni_outro'], (458, 257), pg=1)  #outro liquido amniotico
#!campo 43
#TODO verificar anestesia
match data['anestesia_parto']:
    case 'anestesia-parto-nenhuma':
        doc.write_cross((183, 274), pg=1)  #nenhuma
    case 'anestesia-parto-geral':
        doc.write_cross((238, 274), pg=1)  #geral
    case 'anestesia-parto-raquidiana':
        doc.write_cross((292, 274), pg=1)  #raquidiana
    case 'anestesia-parto-peridural':
        doc.write_cross((346, 274), pg=1)  #peridural
    case 'anestesia-parto-local':
        doc.write_cross((392, 274), pg=1)  #local
    case 'anestesia-parto-outro':
        doc.write_cross((428, 274), pg=1)  #outra
doc.write_text(data['anestesia_parto_outro'], (458, 274), pg=1)  #outra anestesia
#!campo 44
#TODO verificar intercorrencia parto
match data['intercorr_parto']:
    case 'intercorrencia-parto-nenhuma':
        doc.write_cross((198, 290), pg=1)  #nenhuma
    case 'intercorrencia-parto-hipertensao':
        doc.write_cross((238, 290), pg=1)  #hipertensão
    case 'intercorrencia-parto-hemorragia':
        doc.write_cross((292, 290), pg=1)  #Hemorragia
    case 'intercorrencia-parto-outro':
        doc.write_cross((346, 290), pg=1)  #outra
doc.write_text(data['intercorr_parto_outro'], (376, 290), pg=1)  #outra intercorrencia
#!campo 45
doc.write_box(data['evolucao_inter_mae'], rect=(53, 308, 542, 365), pg=1)  #evolucao internacao mae
#!campo 46
#TODO verificar parto sifilis
match data['parto_sifilis']:
    case 'parto-sifilis-nao':
        doc.write_cross((204, 382), pg=1)  #sifilis n reagente
    case 'parto-sifilis-sim':
        doc.write_cross((265, 382), pg=1)  #sifilis reagente
    case 'parto-sifilis-naoRealizado':
        doc.write_cross((318, 382), pg=1)  #sifilis n realizado
#TODO verificar parto hiv
match data['parto_hiv']:
    case 'parto-hiv-nao':
        doc.write_cross((204, 398), pg=1)  #hiv n reagente
    case 'parto-hiv-sim':
        doc.write_cross((265, 398), pg=1)  #hiv reagente
    case 'parto-hiv-naoRealizado':
        doc.write_cross((318, 398), pg=1)  #hiv n realizado
#* Bloco VII Condições de nascimento op N se aplica
if data['op_cond_nasc_NSA'] == '1':
    doc.write_cross((463, 413), pg=1)  #opcao de n se aplica
#!campo 47
#TODO verificar natimorto aval
match data['natimorto_aval']:
    case 'natimorto-avaliado-obstetra':
        doc.write_cross((204, 429), pg=1)  #medico gineco-obstetra
    case 'natimorto-avaliado-pediatra':
        doc.write_cross((292, 429), pg=1)  #medico pediatra/neonatologista
    case 'natimorto-avaliado-outro-medico':
        doc.write_cross((471, 429), pg=1)  #outro medico
    case 'natimorto-avaliado-enfermeira':
        doc.write_cross((92, 444), pg=1)  #enfermeira obstetriz
    case 'natimorto-avaliado-parteira':
        doc.write_cross((204, 444), pg=1)  #parteira
    case 'natimorto-avaliado-ninguem':
        doc.write_cross((471, 444), pg=1)  #Ninguem
    case 'natimorto-avaliado-outro':
        doc.write_cross((292, 444), pg=1)  #outro
doc.write_text(data['natimorto_aval_outro'], (320, 444), pg=1)  #outro natimorto aval
#!campo 48
doc.write_code(data['idade_gest_nasc'], (178, 456), pg=1, space=2)  #idade gestacional
#!campo 49
doc.write_code(data['peso_nascimento'], (174, 472), pg=1, space=3)  #peso de nascimento
#!campo 50
match data['quando_obito_ocorr']:
    case 'obito-ocorreu-antes-parto':
        doc.write_cross((170, 489), pg=1)  #antes do parto
    case 'obito-ocorreu-durante-parto':
        doc.write_cross((292, 489), pg=1)  #durante parto
    case 'obito-ocorreu-apos-parto':
        doc.write_cross((428, 489), pg=1)  #apos parto
#TODO se antes do parto true, foi macerado?
#!campo 50.1
match data['feto_macerado']:
    case 'feto-macerado-sim':
        doc.write_cross((292, 504), pg=1)  #sim ir para o bloco X
    case 'feto-macerado-durante-nao':
        doc.write_cross((318, 504), pg=1)  #nao
#!campo 51
doc.write_code(data['apgar_1min'], (166, 520), pg=1)  #?apgar 1 min verificar o que escrever
doc.write_code(data['apgar_5min'], (242, 517), pg=1)  #?apgar 5 min
if data['op_apgar_natimorto'] == '1':
    doc.write_cross((312, 523), pg=1)  #natimorto
#!campo 52
#TODO verificar classificacao RN
match data['classificacaoRN']:
    case 'classificacaoRN-adequado':
        doc.write_cross((137, 540), pg=1)  #adequado para idade gestacional
    case 'classificacaoRN-pequeno':
        doc.write_cross((264, 540), pg=1)  #pequeno para idade gestacional
    case 'classificacaoRN-grande':
        doc.write_cross((398, 540), pg=1)  #grande para idade gestacional
#!campo 53
#TODO verificar reanimacao
match data['reanimacao']:
    case 'reanimacao-sim':
        doc.write_cross((224, 555), pg=1)  #sim
    case 'reanimacao-nao':
        doc.write_cross((264, 557), pg=1)  #nao
#!campo 54
#TODO verificar assistencia RN
match data['assistenciaRN']:
    case 'assistenciaRN-nenhum':
        doc.write_cross((435, 573), pg=1)  #nenhum
    case 'assistenciaRN-aspiracao':
        doc.write_cross((72, 588), pg=1)  #aspiração das vias aéreas
    case 'assistenciaRN-cateterismo':
        doc.write_cross((177, 588), pg=1)  #Cateterismo umbilical
    case 'assistenciaRN-entubacao':
        doc.write_cross((277, 588), pg=1)  #Entubação
    case 'assistenciaRN-oxigenio':
        doc.write_cross((386, 588), pg=1)  #Oxigenio
    case 'assistenciaRN-sonda':
        doc.write_cross((470, 588), pg=1)  #Sonda nasogástrica
    case 'assistenciaRN-outro-procedimento':
        doc.write_cross((75, 603), pg=1)  #Outros procedimentos
    case 'assistenciaRN-medicamentos':
        doc.write_cross((71, 618), pg=1)  #Medicamentos utilizados
doc.write_text(data['assistRN_outro_proced'], (177, 602), pg=1)  #outros procedimentos
doc.write_text(data['assistRN_outro_medicam'], (177, 617), pg=1)  #medicamentos utilizados
#!campo 55
#TODO verificar diagnostico RN hipoglicemia
match data['hipoglicemia']:
    case 'hipoglicemia-sim':
        doc.write_cross((204, 633), pg=1)  #sim
    case 'hipoglicemia-nao':
        doc.write_cross((249, 633), pg=1)  #nao
    case 'hipoglicemia-naoFez':
        doc.write_cross((367, 633), pg=1)  #n fez exame
#* Bloco VIII Atendimento após o nascimento op N se aplica
if data['op_atend_apos_nasc'] == '1':
    doc.write_cross((330, 651), pg=1)  #opcao de n se aplica
#!campo 56
#TODO setor internacao RN
match data['setorRN']:
    case 'setorRN-aloj-conjunto':
        doc.write_cross((175, 670), pg=1)  #alojamento conjunto
    case 'setorRN-UTI-neonatal':
        doc.write_cross((256, 670), pg=1)  #UTI/CTI neonatal
    case 'setorRN-ICINCo':
        doc.write_cross((354, 670), pg=1)  #cuidado intermediario neonatal UCINCo
    case 'setorRN-ICINCa':
        doc.write_cross((72, 685), pg=1)  #Cuidado intermediario neonatal Canguru UCINCa
    case 'setorRN-outro':
        doc.write_cross((256, 685), pg=1)  #Outro
doc.write_text(data['setorRN_outro_descricao'], (286, 684), pg=1)  #outro setor RN
#!campo 57
#TODO if RN tinha baixo peso <2500g?
match data['RN_baixo_peso']:
    case 'RN-baixo-peso-sim':
        doc.write_cross((175, 700), pg=1)  #sim
    case 'RN-baixo-peso-nao':
        doc.write_cross((198, 700), pg=1)  #nao
#!campo 58
#TODO RN era prematuro? IG < 37 semanas
match data['RN_prematuro']:
    case 'RN-prematuro-sim':
        doc.write_cross((455, 701), pg=1)  #sim
    case 'RN-prematuro-nao':
        doc.write_cross((478, 701), pg=1)  #nao
#!campo 59
#TODO verificar intercorrencia apos o nascimento
match data['INASC']:
    case 'INASC-metabolico':
        doc.write_cross((176, 717), pg=1)  #disturbio metabolico
    case 'INASC-membrana-hialina':
        doc.write_cross((257, 717), pg=1)  #doenca membrana hialina
    case 'INASC-hemolitica':
        doc.write_cross((358, 717), pg=1)  #doenca hemolitica
    case 'INASC-ictericia':
        doc.write_cross((444, 717), pg=1)  #ictericia
    case 'INASC-infeccao-confirmada':
        doc.write_cross((58, 732), pg=1)  #infeccao confirmada
    case 'INASC-infeccao-suspeita':
        doc.write_cross((176, 732), pg=1)  #infeccao suspeita
    case 'INASC-malformacao':
        doc.write_cross((257, 732), pg=1)  #malformação congenita
    case 'INASC-aspiracao-meconial':
        doc.write_cross((358, 732), pg=1)  #sd. aspiracao meconial
    case 'INASC-taquipneia':
        doc.write_cross((444, 732), pg=1)  #taquipneia transitoria do RN
    case 'INASC-tocotraumatismo':
        doc.write_cross((58, 747), pg=1)  #Tocotraumatismo
    case 'INASC-outro':
        doc.write_cross((176, 747), pg=1)  #outra
doc.write_text(data['INASC_outro_descricao'], (206, 746), pg=1)  #outra intercorrencia
#!campo 60
#TODO verificar admissao UTI neonatal
match data['IAUN']:
    case 'IAUN-sim':
        doc.write_cross((210, 763), pg=1)  #sim
    case 'IAUN-nao':
        doc.write_cross((505, 762), pg=1)  #nao
#se sim motivo
doc.write_text(data['IAUN_motivo'], (260, 762), pg=1)  #motivo
#*===========================FIM DA SEGUNDA PAGINA===========================
#!campo 60.1
match data['IUN']:
    case 'IUN-sim':
        doc.write_cross((203, 41), pg=2)  #sim
    case 'IUN-nao':
        doc.write_cross((504, 41), pg=2)  #nao
#se sim data
doc.write_date(data['dt_IUN'], (243, 38), pg=2, spacing=3)  #data
doc.write_code(data['hora_IUN'][:5], (407, 38), pg=2, space=3)  #casa da hora
#!campo 60.1.1
match data['mais3horas_inter']:
    case 'mais3horas-internar-sim':
        doc.write_cross((203, 57), pg=2)  #sim
    case 'mais3horas-internar-nao':
        doc.write_cross((504, 57), pg=2)  #nao
#se sim motivo
doc.write_text(data['mais3horas_inter_motivo'], (255, 56), pg=2)  #motivo
#!campo 60.1.2
doc.write_text(data['motivo_nao_inter'], (203, 73), pg=2)  #pq nao foi internado
#!campo 61
doc.write_box(data['evolucao_inter_RN'], rect=(58, 95, 550, 175), pg=2)  #evolucao RN
#!campo 62
#TODO verificar procedimentos realizados no RN
if data['PRDIRN_nenhum'] == '1': doc.write_cross((462, 188), pg=2)  #nenhum
if data['PRDIRN_antibioti'] == '1': doc.write_cross((71, 204), pg=2)  #Antibioticoterapia
if data['PRDIRN_berco'] == '1': doc.write_cross((146, 204), pg=2)  #Berço aquecido
if data['PRDIRN_canguru'] == '1': doc.write_cross((257, 204), pg=2)  #Método canguru
if data['PRDIRN_cateter'] == '1': doc.write_cross((355, 204), pg=2)  #Cateterismo umbilical
if data['PRDIRN_cpap'] == '1': doc.write_cross((462, 204), pg=2)  #CPAP
if data['PRDIRN_disseccao'] == '1': doc.write_cross((71, 219), pg=2)  #Disecção venosa
if data['PRDIRN_entubacao'] == '1': doc.write_cross((146, 219), pg=2)  #Entubação
if data['PRDIRN_fototera'] == '1': doc.write_cross((257, 219), pg=2)  #Fototerapia
if data['PRDIRN_exsang'] == '1': doc.write_cross((355, 219), pg=2)  #Exsanguineo-transfusão
if data['PRDIRN_hemotrans'] == '1': doc.write_cross((462, 219), pg=2)  #Hemotransfusão
if data['PRDIRN_incuba'] == '1': doc.write_cross((71, 233), pg=2)  #Incubadora
if data['PRDIRN_nutri_par'] == '1': doc.write_cross((146, 233), pg=2)  #Nutrição parenteral
if data['PRDIRN_oxig_capacete'] == '1': doc.write_cross((257, 233), pg=2)  #Oxigenio em capacete
if data['PRDIRN_oxig_inala'] == '1': doc.write_cross((355, 233), pg=2)  #Oxigenio inalatorio
if data['PRDIRN_puncao'] == '1': doc.write_cross((462, 233), pg=2)  #punção venosa central
if data['PRDIRN_surf'] == '1': doc.write_cross((71, 248), pg=2)  #Surfactante
if data['PRDIRN_ventila'] == '1': doc.write_cross((146, 248), pg=2)  #Ventilação mecanica
if data['PRDIRN_outros'] == '1': doc.write_cross((257, 248), pg=2)  #Outros
doc.write_text(data['PRDIRN_outro_descricao'], (355, 247), pg=2)  #outros procedimentos
#!campo 63
#TODO verificar mae acompanhou rn internacao
match data['MARNI']:
    case 'MARNI-sim-integral':
        doc.write_cross((249, 278), pg=2)  #sim em tempo integral
    case 'MARNI-sim-parcial':
        doc.write_cross((345, 278), pg=2)  #sim em tempo parcial
    case 'MARNI-nao':
        doc.write_cross((434, 278), pg=2)  #nao
#!campo 64
#TODO verificar se a mae nao acompanhou rn, rn teve outro acompanhante
match data['RNOA']:
    case 'RNOA-sim-integral':
        doc.write_cross((249, 294), pg=2)  #sim em tempo integral
    case 'RNOA-sim-parcial':
        doc.write_cross((345, 294), pg=2)  #sim em tempo parcial
    case 'RNOA-nao':
        doc.write_cross((434, 294), pg=2)  #nao
#!campo 65
#TODO verificar desfecho internação após nascimento
match data['DIAN']:
    case 'DIAN-alta':
        doc.write_cross((244, 310), pg=2)  #alta
    case 'DIAN-transferencia':
        doc.write_cross((320, 310), pg=2)  #transferencia
    case 'DIAN-obito':
        doc.write_cross((434, 310), pg=2)  #obito
#!campo 66 Data alta/transferencia
doc.write_date(data['dt_altaRN'], (181, 324), pg=2, spacing=3)  #data
#! campo 67 peso alta/transferencia
doc.write_code(data['peso_altaRN'], (437, 324), pg=2, space=3)  #peso
#!campo 68 se foi transferido qual o motivo
doc.write_text(data['motivo_transfRN'], (181, 340), pg=2)  #motivo
#!campo 69 se foi transferido qual o hospital
doc.write_text(data['hosp_transfRN'], (181, 355), pg=2)  #hospital
#!campo 70 se foi a obito indique a hora
doc.write_hrmin(data['hora_obitoRN'], (203, 368), pg=2, space=3)  #casa da hora
if data['op_hora_obitoRN_NSA'] == '1':
    doc.write_cross((483, 371), pg=2)  #n se aplica
#!campo 71 se foi a obito onde ocorreu
match data['obito_RN']:
    case 'obito-RN-alojamento-conjunto':
        doc.write_cross((196, 387), pg=2)  #alojamento conjunto
    case 'obito-RN-cuidado-intermediario':
        doc.write_cross((276, 387), pg=2)  #cuidado intermediario
    case 'obito-RN-UTI-neonatal':
        doc.write_cross((357, 387), pg=2)  #uti neonatal
    case 'obito-RN-centro-obstetrico':
        doc.write_cross((414, 387), pg=2)  #centro obstetrico
    case 'obito-RN-outro':
        doc.write_cross((483, 387), pg=2)  #outro
#* Bloco IX - Assistencia hospitalar a crianca durante a situação que levou a obito op n se aplica
if data['op_AHCDSO_NSA'] == '1':
    doc.write_cross((484, 402), pg=2)  #opcao de n se aplica
#!campo 72 data da intervenção
doc.write_date(data['dt_inter_crianca'], (135, 430), pg=2, spacing=3)  #data
doc.write_hrmin(data['hr_inter_crianca'], (398, 430), pg=2, space=3)  #casa da hora
#!campo 73 a criança veio transferida de outro hospital
match data['CVTH']:
    case 'CVTH-sim':
        doc.write_cross((204, 448), pg=2)  #sim
    case 'CVTH-nao':
        doc.write_cross((414, 448), pg=2)  #nao
doc.write_text(data['CVTH_hospital'], (95, 463), pg=2)  #nome do hospital
doc.write_code(data['tempo_inter_crianca'], (450, 462), pg=2, space=3)  #tempo internação
match data['tipo_tempo_inter']:
    case 'TIT-dias':
        doc.write_cross((481, 465), pg=2)  #dias
    case 'TIT-meses':
        doc.write_cross((503, 465), pg=2)  #horas
#!campo 74 breve historia na admissao
doc.write_box(data['historia_admissao'], rect=(54, 484, 550, 525), pg=2)  #breve historia
#!campo 75 dados da criança na admissao
#!campo 75.1 idade
doc.write_code(data['ICA'], (392, 540), pg=2, space=2)  #idade
match data['ICAT']:
    case 'ICAT-dias':
        doc.write_cross((424, 542), pg=2)  #dias
    case 'ICAT-meses':
        doc.write_cross((446, 542), pg=2)  #meses
    case 'ICAT-anos':
        doc.write_cross((476, 542), pg=2)  #anos
#!campo 75.2 peso
doc.write_code(data['peso_crianca_admiss'] + '9999', (134, 555), pg=2, space=3)  #peso
#!campo 75.3 altura
doc.write_code(data['ACA'], (390, 555), pg=2, space=3)  #altura
#!campo 75.4 estado nutricional
match data['ENCAT']:
    case 'ENCAT-eutrofica':
        doc.write_cross((131, 574), pg=2)  #eutrofica
    case 'ENCAT-desnutrida':
        doc.write_cross((185, 574), pg=2)  #desnutrida
#!campo 75.5 estado hidratação
match data['EHCAT']:
    case 'EHCAT-hidratada':
        doc.write_cross((385, 574), pg=2)  #hidratada
    case 'EHCAT-desidratada':
        doc.write_cross((449, 574), pg=2)  #desidratada
#!campo 75.6 estado geral grave
match data['EGGCA']:
    case 'EGGCA-sim':
        doc.write_cross((131, 590), pg=2)  #sim
    case 'EGGCA-nao':
        doc.write_cross((185, 590), pg=2)  #nao
#!campo 75.7 perfusão
match data['PCA']:
    case 'PCA-normal':
        doc.write_cross((385, 590), pg=2)  #normal
    case 'PCA-diminuida':
        doc.write_cross((449, 590), pg=2)  #diminuida
#!campo 75.8 sinais vitais
doc.write_code(data['BCCA'] + '99', (226, 603), pg=2, space=2)  #freq cardiaca
doc.write_code(data['RCA'] + '9', (359, 603), pg=2, space=2)  #freq respiratoria
doc.write_code(data['TCA'], (469, 604), pg=2, space=2)  #temperatura
#!campo 76 diagnostico admissao e conduta inicial
doc.write_box(data['diag_crianca_admissao'], rect=(53, 622, 550, 658), pg=2)  #diagnostico
#!campo 77 evolucao durante a internação
doc.write_box(data['REIC'], rect=(53, 674, 550, 747), pg=2)  #evolucao dur internacao
#!campo 78 admissao na UTI pediatrica
#todo verificar admissao na UTI pediatrica
match data['IA_UTIP']:
    case 'IA-UTIP-sim':
        doc.write_cross((212, 761), pg=2)  #sim
    case 'IA-UTIP-nao':
        doc.write_cross((504, 761), pg=2)  #nao
doc.write_text(data['IA_UTIP_motivo'], (262, 760), pg=2)  #motivo
#* ========================FIM DA TERCEIRA PAGINA===========================
#!campo 78.1 se sim foi internado na UTI pediatrica
match data['INT_UTIP']:
    case 'INT-UTIP-sim':
        doc.write_cross((205, 41), pg=3)  #sim
    case 'INT-UTIP-nao':
        doc.write_cross((504, 41), pg=3)  #nao
#se sim data
doc.write_date(data['dt_INT_UTIP'], (245, 38), pg=3, spacing=3)  #data
doc.write_hrmin(data['hora_INT_UTIP'], (410, 38), pg=3, space=3)  #hora
#!campo 78.1.1 demorou >3 horas para ser internado
match data['DM3HPSIC']:
    case 'DM3HPSIC-sim':
        doc.write_cross((205, 57), pg=3)  #sim
    case 'DM3HPSIC-nao':
        doc.write_cross((504, 57), pg=3)  #nao
#se sim motivo
doc.write_text(data['DM3HPSIC_motivo'], (256, 56), pg=3)  #motivo
#!campo 78.1.2 pq nao foi internado
doc.write_text(data['crianca_nao_inter_motivo'], (205, 73), pg=3)  #motivo
#!campo 79 desfecho da internacao apos o nascimento
match data['DIANC']:
    case 'DIANC-alta':
        doc.write_cross((239, 90), pg=3)  #alta
    case 'DIANC-transferencia':
        doc.write_cross((319, 90), pg=3)  #transferencia
    case 'DIANC-obito':
        doc.write_cross((433, 90), pg=3)  #obito go to 84
#!campo 80 data alta/transferencia
doc.write_date(data['dt_alta_crianca'], (173, 103), pg=3, spacing=3)  #data
#!campo 81 peso alta/transferencia
doc.write_code(data['peso_alta_crianca'], (438, 103), pg=3, space=3)  #peso
#!campo 82 se foi transferido qual o motivo
doc.write_text(data['CRIANCAT_motivo'], (173, 121), pg=3)  #motivo
if data['op_CRIANCAT_motivo_NSA'] == '1':
    doc.write_cross((475, 121), pg=3)  #nao se aplica
#!campo 83 se foi transferido qual o hospital
doc.write_text(data['CRIANCAT_nome_hosp'], (208, 137), pg=3)  #hospital
if data['op_CRIANCAT_hosp_NSA'] == '1':
    doc.write_cross((475, 137), pg=3)  #nao se aplica
#!campo 84 se foi a obito indique a hora
doc.write_hrmin(data['hora_obito_crianca'], (210, 151), pg=3, space=3)  #hora
if data['op_HOC_NSA'] == '1':
    doc.write_cross((475, 154), pg=3)  #nao se aplica
#!campo 85 se foi a obito onde ocorreu
#todo verificar onde ocorreu o obito
match data['SOC']:
    case 'SOC-UTIP':
        doc.write_cross((204, 170), pg=3)  #UTI neonatal/pediatrica
    case 'SOC-outro':
        doc.write_cross((305, 170), pg=3)  #outro
    case 'SOC-naoSeAplica':
        doc.write_cross((475, 170), pg=3)  #n se aplica
doc.write_text(data['SOC_outro_descricao'], (335, 169), pg=3)  #outro local
#* Bloco X - informacoes complementares sobre o obito
#! campo 86 - liste os diagnosticos ou hipoteses diagnosticas
doc.write_box(data['diag_clinicos'], rect=(70, 205, 550, 262), pg=3)  #diagnostico
#! campo 87 - se houve necropsia
#todo verificar se houve necropsia
match data['corpo_env_necropsia']:
    case 'corpo-enviado-necropsia-sim':
        doc.write_cross((197, 275), pg=3)  #sim
    case 'corpo-enviado-necropsia-nao':
        doc.write_cross((300, 275), pg=3)  #nao
#se sim qual o tipo da necropsia
#todo verificar tipo de necropsia
match data['CENL']:
    case 'CENL-iml':
        doc.write_cross((220, 275), pg=3)  #IML
    case 'CENL-svo':
        doc.write_cross((242, 275), pg=3)  #SVO
    case 'CENL-outro':
        doc.write_cross((266, 275), pg=3)  #Outro
#! campo 87.1 - se sim foi realizada a necropsia
#todo verificar sim e nao
match data['realiz_necropsia']:
    case 'realizada-necropsia-sim':
        doc.write_cross((490, 275), pg=3)  #sim
    case 'realizada-necropsia-nao':
        doc.write_cross((514, 275), pg=3)  #nao
#! campo 88 - este caso foi analisado por alguma comissao/grupo do hospital
#todo verificar se foi analisado
match data['caso_analisado']:
    case 'caso-analisado-sim':
        doc.write_cross((261, 290), pg=3)  #sim
    case 'caso-analisado-nao':
        doc.write_cross((315, 290), pg=3)  #nao
#se sim qual a comissao e conclusoes
doc.write_box(data['comissao_conclusao'], rect=(65, 311, 550, 374), pg=3)  #comissao
#se nao porque
#todo verificar motivo
match data['CNA']:
    case 'CNA-nao-encaminhado':
        doc.write_cross((139, 388), pg=3)  #nao foi encaminhado
    case 'CNA-encaminhado-nao-analisado':
        doc.write_cross((225, 388), pg=3)  #foi encaminhado mas nao analisado
    case 'CNA-sem-comissao':
        doc.write_cross((366, 388), pg=3)  #n existe comissao
    case 'CNA-outro':
        doc.write_cross((474, 388), pg=3)  #outro
doc.write_text(data['CNA_outro_descricao'], (65, 403), pg=3)  #outro motivo
#! campo 89 - info complementares ou esclarecimentos do investigador, algo que deixou de ser feito
doc.write_box(data['outras_informacoes'], rect=(65, 420, 550, 485), pg=3)  #info complementares
#* Bloco XI - Encerramento da investigacao hospitalar
#! campo 90 - responsavel pelo preenchimento
doc.write_text(data['nome_notificante'], (180, 516), pg=3)  #responsavel
#! campo 91 - telefone de contato
doc.write_text(data['telefone_investigador'][:2], (466, 514), pg=3, font_size=11)  #telefone
doc.write_text(data['telefone_investigador'][2:], (482, 514), pg=3, font_size=11)  #telefone
#! campo 92 - o responsavel é do hospital
#todo verificar se o responsavel é do hospital
match data['funcionario_hosp']:
    case 'funcionario-hospital-sim':
        doc.write_cross((272, 531), pg=3)  #sim
    case 'funcionario-hospital-nao':
        doc.write_cross((297, 531), pg=3)  #nao
#! campo 93 - data do encerramento
doc.write_date(data['dt_encerramento'], (227, 546), pg=3, spacing=3)  #data
#! campo 94 - info anexa
#todo verificar se tem info anexa
match data['info_anexa']:
    case 'informacao-anexa-sim':
        doc.write_cross((454, 551), pg=3)  #sim
    case 'informacao-anexa-nao':
        doc.write_cross((478, 551), pg=3)  #nao

doc.save("obito_fetal_inf.pdf")  #especial sem notificação
