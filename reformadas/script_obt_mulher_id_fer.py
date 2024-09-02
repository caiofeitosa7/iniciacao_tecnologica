from pdfWritter import PDFWriter

pdf = 'Óbito Mulher em Idade Fértil1 - MIF.pdf'
doc = PDFWriter(pdf)

data = {
    "ano": "9",
    "nome_paciente": "observacao",
    "num_DO": "9",
    "idade": "25",
    "dt_obito": "15/02/2022",
    "hr_obito": "observacao",
    "dt_nascimento": "15/02/2022",
    "btn_raca": "raca-amarela",
    "etnia": "observacao",
    "aldeia": "observacao",
    "nao_aldeado": "1",
    "endereco_residencia": "observacao",
    "municipio_residencia": "observacao",
    "uf_residencia": "PI",
    "fonte_entrev_domic": "9",
    "fonte_laudo_svo": "1",
    "fonte_pront_hosp": "9",
    "fonte_entrev_prof": "9",
    "fonte_pront_ambul": "1",
    "fonte_sisprenatal": "9",
    "fonte_laudo_iml": "9",
    "fonte_outro": "9",
    "fonte_sinasc": "1",
    "fonte_outro_descricao": "observacao",
    "momento_morte": "op-42d-parto",
    "morte_causa_ext": "op-causa-externa-sim",
    "circunst_morte": "op-circuns-acidente",
    "circunst_morte_outro": "observacao",
    "estado_puerperal": "op-estado-puerperal-sim",
    "seq_eventos": "1",
    "est_morbido": "observacao",
    "est_morbido_cid10": "observacao",
    "est_morbido_conseq1": "observacao",
    "est_morbido_cid1": "observacao",
    "est_morbido_conseq2": "observacao",
    "est_morbido_cid2": "observacao",
    "est_morbido_conseq3": "observacao",
    "est_morbido_cid3": "observacao",
    "est_morb_outra_cond": "observacao",
    "est_morb_outra_cond_cid": "observacao",
    "modif_do": "op-modif-DO-sim",
    "num_campo1": "9",
    "info_original1": "observacao",
    "info_nova1": "observacao",
    "num_campo2": "9",
    "info_original2": "observacao",
    "info_nova2": "observacao",
    "num_campo3": "9",
    "info_original3": "observacao",
    "info_nova3": "observacao",
    "nome_notificante": "observacao",
    "telefone_notificante": "86999999999",
    "dt_notificacao": "15/02/2022",
    "info_anexa": "op-info-anexa-nao",
    "destino_web": "1",
    "destino_integ": "1"
}
#! campo 0 ao 6
doc.write_code(data['ano'], (425, 46), space=3)  # ano
doc.write_text(data['nome_paciente'], (118, 92))  # nome_paciente
doc.write_code(data['num_DO'], (120, 108), space=3)  # num_DO
doc.write_code(data['idade'], (378, 108), space=3)  # idade
doc.write_date(data['dt_obito'], (122, 126), spacing=3)  # dt_obito
doc.write_hrmin(data['hr_obito'], (378, 124), space=3)  # hr_obito
doc.write_date(data['dt_nascimento'], (122, 144), spacing=3)  # dt_nascimento

#!campo 7
#todo validar cor da pele
match data['btn_raca']:
    case 'raca-branca':
        doc.write_cross((372, 146))  # branca
    case 'raca-preta':
        doc.write_cross((406, 146))  # preta
    case 'raca-amarela':
        doc.write_cross((435, 146))  # amarela
    case 'raca-parda':
        doc.write_cross((475, 146))  # parda
    case 'raca-indigena':
        doc.write_cross((509, 146))  # indigena

doc.write_text(data['etnia'], (164, 167))  # etnia
doc.write_text(data['aldeia'], (164, 184))  # aldeia
#* não aldeado
if data['nao_aldeado'] == '1':
    doc.write_cross((500, 181))  # nao aldeado

#! campo 8
doc.write_text(data['endereco_residencia'], (43, 213))  # endereço
#! campo 9
doc.write_text(data['municipio_residencia'], (130, 230))  # municipio
doc.write_code(data['uf_residencia'], (538, 227), space=3)  # uf

#! campo 10
#todo verificar fontes de informação consultadas durante a investigação MIF
if data['fonte_entrev_domic'] == '1':
    doc.write_cross((46, 277))  # entrevista domiciliar
if data['fonte_laudo_svo'] == '1':
    doc.write_cross((46, 290))  # laudo do SVO
if data['fonte_pront_hosp'] == '1':
    doc.write_cross((143, 277))  # prontuário hospitalar
if data['fonte_entrev_prof'] == '1':
    doc.write_cross((143, 290))  # entrevista com profissional de saúde
if data['fonte_pront_ambul'] == '1':
    doc.write_cross((285, 277))  # prontuário ambulatorial
if data['fonte_sisprenatal'] == '1':
    doc.write_cross((285, 290))  # SISPRENATAL
if data['fonte_laudo_iml'] == '1':
    doc.write_cross((405, 277))  # laudo do IML
if data['fonte_outro'] == '1':
    doc.write_cross((405, 290))  # outro
if data['fonte_sinasc'] == '1':
    doc.write_cross((511, 277))

doc.write_text(data['fonte_outro_descricao'], (480, 290), font_size=11)  # fonte_outro_descricao

#! campo 11
#todo verificar momento da morte
match data['momento_morte']:
    case 'op-gestacao':
        doc.write_cross((43, 324))  # durante a gestação
    case 'op-abortamento':
        doc.write_cross((43, 337))  # durante o abortamento
    case 'op-apos-abortamento':
        doc.write_cross((142, 324))  # apos o abortamento
    case 'op-parto':
        doc.write_cross((142, 337))  # no parto ou ate 1hora depois
    case 'op-42d-parto':
        doc.write_cross((283, 324))  # ate 42 dias apos o parto
    case 'op-43d-1ano-parto':
        doc.write_cross((283, 337))  # ate 43 dias a 1 ano apos o parto
    case 'op-NDA':
        doc.write_cross((410, 324))  # nao ocorreu nesses periodos
    case 'op-nao-edentificado':
        doc.write_cross((410, 337))  # momento nao identificado

#! campo 12
#todo verificar morte devido causa externa
match data['morte_causa_ext']:
    case 'op-causa-externa-sim':
        doc.write_cross((176, 353))  # sim
    case 'op-causa-externa-nao':
        doc.write_cross((347, 353))  # nao
#12.A
#todo verificar cirscunstancia provavel
match data['circunst_morte']:
    case 'op-circuns-acidente':
        doc.write_cross((176, 365))  # acidente
    case 'op-circuns-suicidio':
        doc.write_cross((222, 365))  # suicidio
    case 'op-circuns-homicidio':
        doc.write_cross((261, 365))  # homicidio
    case 'op-circuns-outro':
        doc.write_cross((307, 365))  # outro

doc.write_text(data['circunst_morte_outro'], (350, 369))  # outro possibilidade

#12.B
#todo verificar estado puerperal
match data['estado_puerperal']:
    case 'op-estado-puerperal-sim':
        doc.write_cross((232, 384))  # sim
    case 'op-estado-puerperal-nao':
        doc.write_cross((347, 384))  # nao

#! campo 13
if data['seq_eventos'] == '1':
    doc.write_cross((46, 419))  # seq_eventos

#* doença ou estado morbido que causou a morte
doc.write_text(data['est_morbido'], (46, 450))  # est_morbido
doc.write_code(data['est_morbido_cid10'], (512, 450))  # est_morbido_cid10
#* consequencia 1
doc.write_text(data['est_morbido_conseq1'], (46, 480))  # est_morbido_conseq1
doc.write_code(data['est_morbido_cid1'], (512, 480))  # est_morbido_cid1
#* consequencia 2
doc.write_text(data['est_morbido_conseq2'], (46, 510))  # est_morbido_conseq2
doc.write_code(data['est_morbido_cid2'], (512, 510))  # est_morbido_cid2
#* consequencia 3
doc.write_text(data['est_morbido_conseq3'], (46, 540))  # est_morbido_conseq3
doc.write_code(data['est_morbido_cid3'], (512, 540))  # est_morbido_cid3
#* outra condição
doc.write_text(data['est_morb_outra_cond'], (46, 570))  # est_morb_outra_cond
doc.write_code(data['est_morb_outra_cond_cid'], (512, 570))  # est_morb_outra_cond

#! campo 14
#todo verificar modificação do DO
match data['modif_do']:
    case 'op-modif-DO-sim':
        doc.write_cross((282, 587))  # sim
    case 'op-modif-DO-nao':
        doc.write_cross((399, 587))  # nao

doc.write_box(data['num_campo1'], rect=(46, 603, 97, 618), bord=True)  # num_campo1
doc.write_box(data['info_original1'], rect=(98, 603, 335, 618), bord=True)  # info_original1
doc.write_box(data['info_nova1'], rect=(334, 603, 560, 618), bord=True)  # info_nova1
#* campo 2
doc.write_box(data['num_campo2'], rect=(46, 618, 97, 633), bord=True)  # num_campo2
doc.write_box(data['info_original2'], rect=(98, 618, 335, 633), bord=True)  # info_original2
doc.write_box(data['info_nova2'], rect=(334, 618, 560, 633), bord=True)  # info_nova2
#* campo 3
doc.write_box(data['num_campo3'], rect=(46, 633, 97, 648), bord=True)  # num_campo3
doc.write_box(data['info_original3'], rect=(98, 633, 335, 648), bord=True)  # info_original3
doc.write_box(data['info_nova3'], rect=(334, 633, 560, 648), bord=True)  # info_nova3
#! campo 15
doc.write_text(data['nome_notificante'], (185, 695))  # nome_notificante
#! campo 16
doc.write_code(data['telefone_notificante'], (472, 696), space=1, font_size=10)  # telefone_notificante
#! campo 17
doc.write_date(data['dt_notificacao'], (208, 716), spacing=3)  # dt_notificacao

#! campo 18
match data['info_anexa']:
    case 'op-info-anexa-sim':
        doc.write_cross((482, 717))  # info_anexa sim
    case 'op-info-anexa-nao':
        doc.write_cross((508, 717))  # info_anexa nao

#! campo 19
if data['destino_web'] == '1':
    doc.write_cross((121, 737))  # Destino da ficha MIF

if data['destino_integ'] == '1':
    doc.write_cross((286, 737))  # Destino da ficha MIF

doc.save('obito_mulher_age_fertil.pdf')
