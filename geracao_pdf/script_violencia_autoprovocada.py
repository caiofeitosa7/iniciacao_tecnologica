from .pdfWritter import PDFWriter


def gerar_pdf_vio_autoprov(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'], (470, 47))
    document.write_date(dict_especifico['dt_notificacao2'], (446, 146), spacing=2)  # data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (56, 168))  # uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'],
                        (90, 168))  # municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (478, 166), space=2)  # cod_ibge
    document.write_mini(dict_especifico['unid_notif_num'], (149, 180))  # unidade_notificacao
    document.write_text(dict_especifico['nome_unid_notif'], (70, 210))  # nome_unidade_notificacao
    document.write_code(dict_especifico['cod_unid_notif'], (335, 210))  # cod_unidade_notificacao
    document.write_text(dict_especifico['unid_saude'], (70, 231))  # unidade_saude
    document.write_code(dict_especifico['cod_cnes_us'], (337, 231), space=2)  # cod_cnes
    document.write_date(dict_especifico['dt_violencia'], (446, 221), spacing=2)  # data_violencia
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (65, 253))  # nome
    document.write_date(dict_especifico['dt_nascimento2'], (450, 251), spacing=2)  # data_nascimento
    document.write_code(dict_especifico['idade2'], (65, 282), space=2)  # idade
    document.write_mini(dict_especifico['tipo_idade2'], (111, 274))  # tipo_idade
    document.write_mini(dict_especifico['sexo2'], (233, 267))  # sexo
    document.write_mini(dict_especifico['gestante2'], (420, 267))  # gestante
    document.write_mini(dict_especifico['raca2'], (553, 268))  # raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (554, 297))  # escolaridade
    document.write_code(dict_especifico['numero_sus2'], (51, 342), space=2, font_size=11)  # cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 341))  # nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (57, 370))  # uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (100, 372))  # municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (328, 371), space=2)  # cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (430, 371))  # endereco
    document.write_text(dict_especifico['bairro_residencia2'], (70, 396))  # bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 398))  # logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (481, 397), space=2)  # cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (66, 419))  # numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 420))  # complemento
    document.write_text(dict_especifico['geo_campo1_2'], (420, 421))  # geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (63, 445))  # geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (232, 447))  # ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (461, 448), space=2, font_size=12)  # cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (58, 472), space=2)  # telefone
    document.write_mini(dict_especifico['zona_residencia2'], (334, 460))  # zona
    document.write_text(dict_especifico['pais_residencia2'], (365, 473))  # pais
    ###################################################
    # Dados Complementares _ Ficha de Investigação    #
    ###################################################
    document.write_text(dict_especifico['nome_social'], (65, 515), font_size=9)  # nome_social
    document.write_text(dict_especifico['ocupacao'], (370, 515), font_size=9)  # ocupacao
    document.write_mini(dict_especifico['sit_conjugal'], (550, 537))  # situacao_conjugal
    document.write_mini(dict_especifico['orient_sexual'], (291, 565))  # orientacao_sexual
    document.write_mini(dict_especifico['ident_genero'], (552, 566))  # identidade_genero
    document.write_mini(dict_especifico['possui_def'], (170, 598))  # possui_deficiencia

    document.write_mini(dict_especifico['def_fisica'], (198, 607))
    document.write_mini(dict_especifico['def_intel'], (198, 619))
    document.write_mini(dict_especifico['def_visual'], (295, 608))
    document.write_mini(dict_especifico['def_audi'], (295, 619))
    document.write_mini(dict_especifico['def_mental'], (389, 608))
    document.write_mini(dict_especifico['def_comport'], (389, 620))
    document.write_mini(dict_especifico['def_outra'], (475, 609), font_size=7)

    document.write_text(dict_especifico['def_outra_descricao'], (510, 607))

    document.write_uf(dict_especifico['uf_ocorr'], (59, 650))  # uf_ocorrencia
    document.write_text(dict_especifico['municipio_ocorr'], (100, 650), font_size=9)  # municipio_ocorrencia
    document.write_code(dict_especifico['cod_ibge_ocorr'], (328, 650), space=2)  # cod_ibge_ocorrencia
    document.write_text(dict_especifico['distrito_ocorr'], (430, 650))  # distrito_ocorrencia
    document.write_text(dict_especifico['bairro_ocorr'], (70, 675))  # bairro_ocorrencia
    document.write_text(dict_especifico['logradouro_ocorr'], (210, 675), font_size=8)  # logradouro_ocorrencia
    document.write_code(dict_especifico['codigo_ocorr'], (483, 677), space=2)  # cod_logradouro_ocorrencia
    document.write_text(dict_especifico['numero_ocorr'], (66, 700))  # numero_ocorrencia
    document.write_text(dict_especifico['complemento_ocorr'], (120, 700), font_size=8)  # complemento_ocorrencia
    document.write_text(dict_especifico['geocampo3'], (310, 700))  # geo_campo_1_ocorrencia
    document.write_text(dict_especifico['geocampo4'], (430, 700))  # geo_campo_2_ocorrencia
    document.write_text(dict_especifico['ponto_ref_ocorr'], (63, 725), font_size=8)  # ponto_ref_ocorrencia
    document.write_mini(dict_especifico['zona_ocorr'], (334, 713))  # zona_ocorrencia
    document.write_hrmin(dict_especifico['hora_ocorr'], (494, 725), space=2)  # hora_ocorrencia
    document.write_code(dict_especifico['loc_ocorr_num'] + '9', (380, 740), space=2)  # local_ocorrencia
    document.write_text(dict_especifico['loc_ocorr_outro'], (317, 761), font_size=7)  # local_ocorrencia_outro
    document.write_mini(dict_especifico['ocorr_outras_vezes'], (555, 737))  # ocorrencia_outras_vezes
    document.write_mini(dict_especifico['lesao_autoprov'], (554, 764))  # lesao_autoprovocada

    # *=========================== fim pagina 1 ===========================*#
    document.write_code(dict_especifico['motiv_violencia'], (543, 62), space=2, pg=1)  # motivacao_violencia
    # ! campos 56
    document.write_mini(dict_especifico['viol_fisica'], (70, 95), pg=1)  # fisica
    document.write_mini(dict_especifico['viol_psico'], (70, 109), pg=1)  # psicologica
    document.write_mini(dict_especifico['viol_tort'], (70, 121), pg=1)  # tortura
    document.write_mini(dict_especifico['viol_sexual'], (70, 134), pg=1)  # sexual
    document.write_mini(dict_especifico['viol_traf'], (155, 95), pg=1)  # trafico
    document.write_mini(dict_especifico['viol_finan'], (155, 109), pg=1)  # financeira
    document.write_mini(dict_especifico['viol_negli'], (155, 121), pg=1)  # negligencia
    document.write_mini(dict_especifico['viol_trab'], (155, 134), pg=1)  # trabalho
    document.write_mini(dict_especifico['viol_inter'], (258, 107), pg=1)  # interfamiliar
    document.write_mini(dict_especifico['viol_outro'], (258, 122), pg=1)  # outros

    document.write_text(dict_especifico['viol_outro_descricao'], (270, 130), pg=1,
                        font_size=8)  # violencia_outro_descricao

    # ! campo 57
    document.write_mini(dict_especifico['agress_espanc'], (349, 102), pg=1)  # espancamento
    document.write_mini(dict_especifico['agress_enforc'], (349, 118), pg=1)  # enforcamento
    document.write_mini(dict_especifico['agress_contund'], (349, 134), pg=1)  # contundente
    document.write_mini(dict_especifico['agress_perfuro'], (425, 98), pg=1)  # perfurocortante
    document.write_mini(dict_especifico['agress_subst'], (425, 114), pg=1)  # substancia quente
    document.write_mini(dict_especifico['agress_intox'], (425, 130), pg=1)  # intoxicacao
    document.write_mini(dict_especifico['agress_arma'], (498, 99), pg=1)  # arma de fogo
    document.write_mini(dict_especifico['agress_ameaca'], (498, 112), pg=1)  # ameaca
    document.write_mini(dict_especifico['agress_outro'], (498, 124), pg=1)  # outros

    document.write_text(dict_especifico['agress_outro_descricao'], (531, 122), pg=1,
                        font_size=8)  # agressao_outro_descricao

    # ! campo 58
    document.write_mini(dict_especifico['vio_sex_assedio'], (69, 160), pg=1)  # assedio
    document.write_mini(dict_especifico['vio_sex_estupro'], (154, 160), pg=1)  # estupro
    document.write_mini(dict_especifico['vio_sex_porno'], (233, 159), pg=1)  # pornografia infantil
    document.write_mini(dict_especifico['vio_sex_explora'], (337, 159), pg=1)  # exploração sexual
    document.write_mini(dict_especifico['vio_sex_outros'], (440, 158), pg=1)  # exploração sexual

    document.write_text(dict_especifico['vio_sex_outros_descricao'], (478, 156), pg=1, font_size=8)

    # !campo 59
    document.write_mini(dict_especifico['proced_dst'], (70, 195), pg=1)  # profilaxia dst
    document.write_mini(dict_especifico['proced_hiv'], (70, 208), pg=1)  # profilaxia hiv
    document.write_mini(dict_especifico['proced_hepB'], (156, 195), pg=1)  # profilaxia hep b
    document.write_mini(dict_especifico['proced_sangue'], (156, 208), pg=1)  # coleta de sangue
    document.write_mini(dict_especifico['proced_semen'], (268, 194), pg=1)  # coleta de semen
    document.write_mini(dict_especifico['proced_vaginal'], (268, 207), pg=1)  # coleta de segrecao vaginal
    document.write_mini(dict_especifico['proced_contra'], (409, 195), pg=1)  # contracepção de emergencia
    document.write_mini(dict_especifico['proced_aborto'], (409, 208), pg=1)  # aborto previsto em lei

    # !campo 60
    document.write_mini(dict_especifico['num_envolvidos'], (94, 246), pg=1)  # num_envolvidos

    # !campo 61
    document.write_mini(dict_especifico['grau_pai'], (119, 238), pg=1)  # pai
    document.write_mini(dict_especifico['grau_mae'], (119, 251), pg=1)  # mae
    document.write_mini(dict_especifico['grau_padr'], (119, 264), pg=1)  # padrasto
    document.write_mini(dict_especifico['grau_madr'], (119, 275), pg=1)  # madrasta
    document.write_mini(dict_especifico['grau_conj'], (119, 288), pg=1)  # conjuge
    document.write_mini(dict_especifico['grau_ex_conj'], (173, 238), pg=1)  # ex_conjuge
    document.write_mini(dict_especifico['grau_namor'], (173, 251), pg=1)  # namorado
    document.write_mini(dict_especifico['grau_ex_namor'], (173, 264), pg=1)  # ex_namorado
    document.write_mini(dict_especifico['grau_filho'], (173, 275), pg=1)  # filho
    document.write_mini(dict_especifico['grau_irmao'], (173, 288), pg=1)  # irmao
    document.write_mini(dict_especifico['grau_amigos'], (252, 238), pg=1)  # amigos
    document.write_mini(dict_especifico['grau_desco'], (252, 251), pg=1)  # desconhecido
    document.write_mini(dict_especifico['grau_cuida'], (252, 264), pg=1)  # cuidador
    document.write_mini(dict_especifico['grau_chefe'], (252, 275), pg=1)  # chefe
    document.write_mini(dict_especifico['grau_pessoa'], (252, 288), pg=1)  # pessoa com relação institucional
    document.write_mini(dict_especifico['grau_policia'], (340, 238), pg=1)  # policia
    document.write_mini(dict_especifico['grau_proprio'], (340, 264), pg=1)  # proprio
    document.write_mini(dict_especifico['grau_outro'], (340, 276), pg=1)  # outro

    document.write_text(dict_especifico['grau_outro_descricao'], (378, 275), pg=1, font_size=7)  # grau_outro_descricao

    # !campo 62
    document.write_mini(dict_especifico['sexo_autor'], (482, 248), pg=1)  # sexo_autor
    # !campo 63
    document.write_mini(dict_especifico['uso_alcool'], (552, 245), pg=1)  # uso_alcool

    # !campo 64
    document.write_mini(dict_especifico['ciclo_autor'], (233, 308), pg=1)  # ciclo_violencia

    # !campo 65
    document.write_mini(dict_especifico['enca_saude'], (53, 368), pg=1)  # saude
    document.write_mini(dict_especifico['enca_social'], (53, 383), pg=1)  # social
    document.write_mini(dict_especifico['enca_educa'], (53, 398), pg=1)  # educacional
    document.write_mini(dict_especifico['enca_rede_mulher'], (53, 412), pg=1)  # rede de mulher
    document.write_mini(dict_especifico['enca_tutelar'], (53, 427), pg=1)  # conselho tutelar
    document.write_mini(dict_especifico['enca_cons_idoso'], (286, 363), pg=1)  # conselho do idoso
    document.write_mini(dict_especifico['enca_del_idoso'], (286, 378), pg=1)  # delegacia do idoso
    document.write_mini(dict_especifico['enca_dir_humano'], (286, 393), pg=1)  # direitos humanos
    document.write_mini(dict_especifico['enca_ministerio'], (286, 407), pg=1)  # ministerio publico
    document.write_mini(dict_especifico['enca_del_crianca'], (286, 424), pg=1)  # delegacia da criança
    document.write_mini(dict_especifico['enca_del_mulher'], (435, 360), pg=1)  # delegacia da mulher
    document.write_mini(dict_especifico['enca_outra_del'], (435, 378), pg=1)  # outra delegacia
    document.write_mini(dict_especifico['enca_jus_infancia'], (435, 393), pg=1)  # justiça da infancia
    document.write_mini(dict_especifico['enca_def_publica'], (435, 411), pg=1)  # defensoria publica

    # !campo 66
    document.write_mini(dict_especifico['doenca_rel_trab'], (166, 456), pg=1)  # doenca_relacionada_trabalho

    # !campo 67
    document.write_mini(dict_especifico['comun_acid_trab'], (356, 455), pg=1)  # comunicado_acidente_trabalho

    # !campo 68
    document.write_code(dict_especifico['circunst_lesao'], (508, 475), pg=1, space=2)  # circunstancia_lesao

    # !campo 69
    document.write_date(dict_especifico['dt_encerramento'], (57, 515), spacing=2, pg=1)  # data_encerramento

    document.write_text(dict_especifico['nome_acompanha'], (35, 560), pg=1, font_size=9)  # nome_acompanhante
    document.write_text(dict_especifico['vinculo_acompanha'], (240, 560), pg=1)  # vinculo_acompanhante
    document.write_telefone(dict_especifico['telefone_acompanha'], (422, 560), pg=1, space=2)  # telefone_acompanhante
    document.write_box(dict_especifico['obs_adicionais'], rect=(29, 575, 565, 636), pg=1)  # observacoes_adicionais
    document.write_text(dict_especifico['municipio_us_investigador'], (57, 706), pg=1, font_size=9)  # municipio_investigador,
    document.write_code(dict_especifico['cod_us_investigador'], (453, 706), pg=1, space=2)  # codigo_investigador
    document.write_text(dict_especifico['nome_investigador'], (57, 736), pg=1, font_size=9)  # nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (260, 736), pg=1, font_size=9)  # funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (465, 736), pg=1, font_size=9)  # assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)