from .pdfWritter import PDFWriter


def gerar_pdf_obt_mulher_id_fertil(dict_especifico: dict, modelo_pdf: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    # ! campo 0 ao 6
    document.write_code(dict_especifico['ano'], (425, 46), space=3)  # ano
    document.write_text(dict_especifico['nome_paciente'], (118, 92))  # nome_paciente
    document.write_code(dict_especifico['num_DO'], (120, 108), space=3)  # num_DO
    document.write_code(dict_especifico['idade'], (378, 108), space=3)  # idade
    document.write_date(dict_especifico['dt_obito'], (122, 126), spacing=3)  # dt_obito
    document.write_hrmin(dict_especifico['hr_obito'], (378, 124), space=3)  # hr_obito
    document.write_date(dict_especifico['dt_nascimento'], (122, 144), spacing=3)  # dt_nascimento

    # !campo 7
    # todo validar cor da pele
    if dict_especifico['btn_raca'] == 'raca-branca':
        document.write_cross((372, 146))  # branca
    elif dict_especifico['btn_raca'] == 'raca-preta':
        document.write_cross((406, 146))  # preta
    elif dict_especifico['btn_raca'] == 'raca-amarela':
        document.write_cross((435, 146))  # amarela
    elif dict_especifico['btn_raca'] == 'raca-parda':
        document.write_cross((475, 146))  # parda
    elif dict_especifico['btn_raca'] == 'raca-indigena':
        document.write_cross((509, 146))  # indigena

    document.write_text(dict_especifico['etnia'], (164, 167))  # etnia
    document.write_text(dict_especifico['aldeia'], (164, 184))  # aldeia
    # * não aldeado
    if dict_especifico['nao_aldeado'] == '1':
        document.write_cross((500, 181))  # nao aldeado

    # ! campo 8
    document.write_text(dict_especifico['endereco_residencia'], (43, 213))  # endereço
    # ! campo 9
    document.write_text(dict_especifico['municipio_residencia'], (130, 230))  # municipio
    document.write_code(dict_especifico['uf_residencia'], (538, 227), space=3)  # uf

    # ! campo 10
    # todo verificar fontes de informação consultadas durante a investigação MIF
    if dict_especifico['fonte_entrev_domic'] == '1':
        document.write_cross((46, 277))  # entrevista domiciliar
    if dict_especifico['fonte_laudo_svo'] == '1':
        document.write_cross((46, 290))  # laudo do SVO
    if dict_especifico['fonte_pront_hosp'] == '1':
        document.write_cross((143, 277))  # prontuário hospitalar
    if dict_especifico['fonte_entrev_prof'] == '1':
        document.write_cross((143, 290))  # entrevista com profissional de saúde
    if dict_especifico['fonte_pront_ambul'] == '1':
        document.write_cross((285, 277))  # prontuário ambulatorial
    if dict_especifico['fonte_sisprenatal'] == '1':
        document.write_cross((285, 290))  # SISPRENATAL
    if dict_especifico['fonte_laudo_iml'] == '1':
        document.write_cross((405, 277))  # laudo do IML
    if dict_especifico['fonte_outro'] == '1':
        document.write_cross((405, 290))  # outro
    if dict_especifico['fonte_sinasc'] == '1':
        document.write_cross((511, 277))

    document.write_text(dict_especifico['fonte_outro_descricao'], (480, 290), font_size=11)  # fonte_outro_descricao

    # ! campo 11
    # todo verificar momento da morte
    if dict_especifico['momento_morte'] == 'op-gestacao':
        document.write_cross((43, 324))  # durante a gestação
    elif dict_especifico['momento_morte'] == 'op-abortamento':
        document.write_cross((43, 337))  # durante o abortamento
    elif dict_especifico['momento_morte'] == 'op-apos-abortamento':
        document.write_cross((142, 324))  # apos o abortamento
    elif dict_especifico['momento_morte'] == 'op-parto':
        document.write_cross((142, 337))  # no parto ou ate 1hora depois
    elif dict_especifico['momento_morte'] == 'op-42d-parto':
        document.write_cross((283, 324))  # ate 42 dias apos o parto
    elif dict_especifico['momento_morte'] == 'op-43d-1ano-parto':
        document.write_cross((283, 337))  # ate 43 dias a 1 ano apos o parto
    elif dict_especifico['momento_morte'] == 'op-NDA':
        document.write_cross((410, 324))  # nao ocorreu nesses periodos
    elif dict_especifico['momento_morte'] == 'op-nao-edentificado':
        document.write_cross((410, 337))  # momento nao identificado

    # ! campo 12
    # todo verificar morte devido causa externa
    if dict_especifico['morte_causa_ext'] == 'op-causa-externa-sim':
        document.write_cross((176, 353))  # sim
    elif dict_especifico['morte_causa_ext'] == 'op-causa-externa-nao':
        document.write_cross((347, 353))  # nao
    # 12.A
    # todo verificar cirscunstancia provavel
    if dict_especifico['circunst_morte'] == 'op-circuns-acidente':
        document.write_cross((176, 365))  # acidente
    elif dict_especifico['circunst_morte'] == 'op-circuns-suicidio':
        document.write_cross((222, 365))  # suicidio
    elif dict_especifico['circunst_morte'] == 'op-circuns-homicidio':
        document.write_cross((261, 365))  # homicidio
    elif dict_especifico['circunst_morte'] == 'op-circuns-outro':
        document.write_cross((307, 365))  # outro

    document.write_text(dict_especifico['circunst_morte_outro'], (350, 369))  # outra possibilidade

    # 12.B
    # todo verificar estado puerperal
    if dict_especifico['estado_puerperal'] == 'op-estado-puerperal-sim':
        document.write_cross((232, 384))  # sim
    elif dict_especifico['estado_puerperal'] == 'op-estado-puerperal-nao':
        document.write_cross((347, 384))  # nao

    # ! campo 13
    if dict_especifico['seq_eventos'] == '1':
        document.write_cross((46, 419))  # seq_eventos

    # * doença ou estado morbido que causou a morte
    document.write_text(dict_especifico['est_morbido'], (46, 450))  # est_morbido
    document.write_text(dict_especifico['est_morbido_cid10'], (512, 450), font_size=9)  # est_morbido_cid10
    # * consequencia 1
    document.write_text(dict_especifico['est_morbido_conseq1'], (46, 480))  # est_morbido_conseq1
    document.write_text(dict_especifico['est_morbido_cid1'], (512, 480), font_size=9)  # est_morbido_cid1
    # * consequencia 2
    document.write_text(dict_especifico['est_morbido_conseq2'], (46, 510))  # est_morbido_conseq2
    document.write_text(dict_especifico['est_morbido_cid2'], (512, 510), font_size=9)  # est_morbido_cid2
    # * consequencia 3
    document.write_text(dict_especifico['est_morbido_conseq3'], (46, 540))  # est_morbido_conseq3
    document.write_text(dict_especifico['est_morbido_cid3'], (512, 540), font_size=9)  # est_morbido_cid3
    # * outra condição
    document.write_text(dict_especifico['est_morb_outra_cond'], (46, 570))  # est_morb_outra_cond
    document.write_text(dict_especifico['est_morb_outra_cond_cid'], (512, 570), font_size=9)  # est_morb_outra_cond

    # ! campo 14
    # todo verificar modificação do DO
    if dict_especifico['modif_do'] == 'op-modif-DO-sim':
        document.write_cross((282, 587))  # sim
    elif dict_especifico['modif_do'] == 'op-modif-DO-nao':
        document.write_cross((399, 587))  # nao

    document.write_box(dict_especifico['num_campo1'], rect=(46, 603, 97, 618), bord=True)  # num_campo1
    document.write_box(dict_especifico['info_original1'], rect=(98, 603, 335, 618), bord=True)  # info_original1
    document.write_box(dict_especifico['info_nova1'], rect=(334, 603, 560, 618), bord=True)  # info_nova1
    # * campo 2
    document.write_box(dict_especifico['num_campo2'], rect=(46, 618, 97, 633), bord=True)  # num_campo2
    document.write_box(dict_especifico['info_original2'], rect=(98, 618, 335, 633), bord=True)  # info_original2
    document.write_box(dict_especifico['info_nova2'], rect=(334, 618, 560, 633), bord=True)  # info_nova2
    # * campo 3
    document.write_box(dict_especifico['num_campo3'], rect=(46, 633, 97, 648), bord=True)  # num_campo3
    document.write_box(dict_especifico['info_original3'], rect=(98, 633, 335, 648), bord=True)  # info_original3
    document.write_box(dict_especifico['info_nova3'], rect=(334, 633, 560, 648), bord=True)  # info_nova3
    # ! campo 15
    document.write_text(dict_especifico['nome_notificante'], (185, 695))  # nome_notificante
    # ! campo 16
    document.write_code(dict_especifico['telefone_notificante'], (472, 696), space=1,
                        font_size=10)  # telefone_notificante
    # ! campo 17
    document.write_date(dict_especifico['dt_notificacao'], (208, 716), spacing=3)  # dt_notificacao

    # ! campo 18
    if dict_especifico['info_anexa'] == 'op-info-anexa-sim':
        document.write_cross((482, 717))  # info_anexa sim
    elif dict_especifico['info_anexa'] == 'op-info-anexa-nao':
        document.write_cross((508, 717))  # info_anexa nao

    # ! campo 19
    if dict_especifico['destino_web'] == '1':
        document.write_cross((121, 737))  # Destino da ficha MIF - WEB

    if dict_especifico['destino_integ'] == '1':
        document.write_cross((286, 737))  # Destino da ficha MIF - INTEGRACAO

    document.save(nome_arquivo, path_pdf_gerado)
