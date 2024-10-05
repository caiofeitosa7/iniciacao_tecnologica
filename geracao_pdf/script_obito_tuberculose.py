from .pdfWritter import PDFWriter


def gerar_pdf_obt_tuberculose(dict_especifico: dict, modelo_pdf: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    document.write_code(dict_especifico['numero_ficha'], (518, 153), space=3)  #numero
    document.write_text(dict_especifico['foi_notif_sinan'], (259, 202))  #ntf sinan antes de morrer
    document.write_text(dict_especifico['num_notif_sinan'], (531, 200))  #numero notif sinan-TB
    document.write_date(dict_especifico['dt_ultima_notif'], (205, 234), spacing=3)  #data ultima notif
    document.write_code(dict_especifico['num_ficha_sinan'], (445, 234), space=3)  #numero ficha sinan
    document.write_text(dict_especifico['sit_caso_sim'], (196, 267))  #situacao do caso sim
    document.write_date(dict_especifico['dt_obito'], (157, 304), spacing=3)  #data obito
    document.write_text(dict_especifico['num_declar_obito'], (432, 304))  #numero declaracao obito
    document.write_text(dict_especifico['nome_paciente'], (160, 330))  #nome paciente
    document.write_text(dict_especifico['nome_mae'], (145, 355))  #nome mae
    document.write_date(dict_especifico['dt_nascimento'], (179, 384), spacing=3)  #data nascimento
    document.write_code(dict_especifico['idade'], (366, 384), space=3)  #idade
    document.write_text(dict_especifico['sexo'], (438, 384))  #sexo
    document.write_text(dict_especifico['logradouro_residencia'], (130, 410))  #logradouro
    document.write_text(dict_especifico['bairro_residencia'], (85, 443))  #bairro
    document.write_text(dict_especifico['municipio_residencia'], (262, 443))  #municipio
    document.write_text(dict_especifico['uf_residencia'], (550, 443))  #uf

    #################### parte B ####################
    document.write_text(dict_especifico['nome_hospital'], (90, 490))  #nome hospital
    document.write_code(dict_especifico['prontuario_hospit'], (90, 519), space=3)  #prontuario
    document.write_date(dict_especifico['dt_admissao'], (382, 512), spacing=3)  #data admissao
    document.write_box(dict_especifico['motivo_intern'], rect=(85, 539, 590, 568))  #motivo internacao
    document.write_text(dict_especifico['nome_contato'], (90, 595))  #nome contato
    document.write_text(dict_especifico['telefone_contato'], (90, 625))  #telefone contato
    document.write_text(dict_especifico['parentesco_contato'], (300, 625))  #parentesco contato

    document.write_text(dict_especifico['sint_tosse'], (92, 668))  #tosse
    document.write_code(dict_especifico['tempo_tosse'], (255, 668), space=3)  #tempo tosse
    document.write_text(dict_especifico['sint_febre'], (92, 691))  #febre
    document.write_text(dict_especifico['sint_desnutricao'], (140, 691))  #desnutricao
    document.write_text(dict_especifico['sint_sudorese'], (312, 691))  #sudorese
    document.write_text(dict_especifico['sint_catarro'], (374, 691))  #catarro
    document.write_text(dict_especifico['sint_dispineia'], (428, 691))  #dispineia
    document.write_text(dict_especifico['sint_dor_toracica'], (487, 691))  #dor toracica
    document.write_text(dict_especifico['sint_desnutricao'], (92, 713))  #catarro de sangue
    document.write_text(dict_especifico['sint_outro'], (195, 713))  #outro
    document.write_text(dict_especifico['sint_outro_descricao'], (335, 710))  #descricao outro

    #doencas e agravos associados
    document.write_text(dict_especifico['doenca_aids'], (92, 767))  #aids
    document.write_text(dict_especifico['doenca_neopla'], (92, 789))  #neoplasia
    document.write_text(dict_especifico['doenca_alcool'], (157, 767))  #alcool
    document.write_text(dict_especifico['doenca_dpoc'], (157, 789))  #dpoc
    document.write_text(dict_especifico['doenca_diab'], (233, 767))  #diabetes
    document.write_text(dict_especifico['doenca_asma'], (233, 789))  #asma
    document.write_text(dict_especifico['doenca_mental'], (305, 767))  #doenca mental
    document.write_text(dict_especifico['doenca_pneumo'], (305, 789))  #pneumonia
    document.write_text(dict_especifico['doenca_tabag'], (396, 767))  #tabagismo
    document.write_text(dict_especifico['doenca_nefro'], (396, 789))  #doenca renal
    document.write_text(dict_especifico['doenca_droga'], (480, 767))  #drogas
    document.write_text(dict_especifico['doenca_hepato'], (480, 789))  #hepatite
    document.write_text(dict_especifico['doenca_outro'], (92, 811))  #outro
    document.write_text(dict_especifico['doenca_outro_descricao'], (204, 809))  #descricao outro

    #*========================== fim da pagina 1 ==========================*#

    document.write_text(dict_especifico['ex_bacilo'], (208, 110), pg=1)  #exame baciloscopico
    document.write_date(dict_especifico['dt_res_bacilo'], (447, 122), spacing=3, pg=1)  #data resultado baciloscopico
    document.write_text(dict_especifico['teste_molec_tub'], (76, 160), pg=1)  #teste molecular
    document.write_text(dict_especifico['mat_util_ex_molec'], (145, 188), pg=1)  #material utilizado
    document.write_date(dict_especifico['dt_admissao_molec'], (447, 163), spacing=3, pg=1)  #data admissao
    document.write_text(dict_especifico['ex_bacilo_outro_mat'], (208, 220), pg=1)  #outro material
    document.write_date(dict_especifico['dt_res_bacilo_outro_mat'], (447, 231), spacing=3,
                        pg=1)  #data resultado outro material
    document.write_text(dict_especifico['mat_util_outro_molec'], (145, 236), pg=1)  #outro material utilizado
    document.write_text(dict_especifico['cult_escarro'], (208, 268), pg=1)  #cultura escarro
    document.write_date(dict_especifico['dt_res_cult_escarro'], (447, 279), spacing=3,
                        pg=1)  #data resultado cultura escarro
    document.write_text(dict_especifico['ident_especie'], (208, 298), pg=1)  #identificacao especie
    document.write_text(dict_especifico['especie_microb'], (438, 298), pg=1)  #especie microbiana
    document.write_text(dict_especifico['cult_outro_mat'], (208, 330), pg=1)  #outro material
    document.write_text(dict_especifico['mat_util_cult_outro_mat'], (145, 346), pg=1)  #material utilizado
    document.write_date(dict_especifico['dt_res_cult_outro_mat'], (447, 341), spacing=3,
                        pg=1)  #data resultado outro material
    document.write_text(dict_especifico['ident_espec_outra_cult'], (208, 368), pg=1)  #identificacao especie
    document.write_text(dict_especifico['esp_microb_outra_cult'], (438, 366), pg=1)  #especie microbiana
    document.write_text(dict_especifico['teste_sensi_antimicrob'], (230, 393), pg=1)  #teste sensibilidade
    document.write_date(dict_especifico['dt_res_antimicrob'], (447, 409), spacing=3,
                        pg=1)  #data resultado teste sensibilidade
    document.write_text(dict_especifico['raio_x_torax'], (142, 462), pg=1)  #raio x torax
    document.write_text(dict_especifico['raiox_outra_doenca'], (230, 494), pg=1)  #outra doenca
    document.write_date(dict_especifico['dt_res_raiox'], (447, 478), spacing=3, pg=1)  #data resultado raio x
    document.write_text(dict_especifico['hispatologico'], (143, 535), pg=1)  #histopatologico
    document.write_text(dict_especifico['hispato_outra_doenca'], (230, 564), pg=1)  #outra doenca
    document.write_date(dict_especifico['dt_res_hispato'], (447, 550), spacing=3, pg=1)  #data resultado histopatologico
    document.write_text(dict_especifico['teste_hiv'], (143, 606), pg=1)  #teste hiv
    document.write_date(dict_especifico['dt_res_hiv'], (447, 616), spacing=3, pg=1)  #data resultado hiv
    document.write_text(dict_especifico['tomografia'], (198, 648), pg=1)  #tomografia
    document.write_text(dict_especifico['op_lesoes_escav'], (76, 686), pg=1)  #lesoes escavadas
    document.write_text(dict_especifico['op_nodulos'], (76, 705), pg=1)  #nodulos
    document.write_text(dict_especifico['op_lesoes_cron'], (257, 705), pg=1)  #lesoes cronicas
    document.write_text(dict_especifico['op_outro_laudo'], (76, 724), pg=1)  #outros
    document.write_text(dict_especifico['laudo_outro_descricao'], (147, 724), pg=1)  #descricao outro
    document.write_date(dict_especifico['dt_tomografia'], (447, 660), spacing=3, pg=1)  #data tomografia
    document.write_text(dict_especifico['broncoscopia'], (141, 773), pg=1)  #broncoscopia
    document.write_date(dict_especifico['dt_broncos'], (447, 784), spacing=3, pg=1)  #data broncoscopia
    #*========================== fim da pagina 2 ==========================*#

    document.write_box(dict_especifico['outros_exames'], rect=(65, 83, 588, 180), pg=2, bord=True)  #outros exames
    if dict_especifico['necropsia'] == 'op-necropsia-sim':
        document.write_cross((78, 212), pg=2)  #necropsia sim
    elif dict_especifico['necropsia'] == 'op-necropsia-nao':
        document.write_cross((112, 212), pg=2)  #necropsia nao

    if dict_especifico['necropsia_serv'] == "op-necropsia-serv-iml":
        document.write_cross((357, 200), pg=2)  #servico IML
    elif dict_especifico['necropsia_serv'] == "op-necropsia-serv-svo":
        document.write_cross((395, 200), pg=2)  #servico SVO
    elif dict_especifico['necropsia_serv'] == "op-necropsia-serv-hospital":
        document.write_cross((433, 200), pg=2)  #servico hospital

    if dict_especifico['achados_necropsia'] == "op-achados-necropsia-sim":
        document.write_cross((518, 218), pg=2)  #sim
    elif dict_especifico['achados_necropsia'] == "op-achados-necropsia-nao":
        document.write_cross((553, 218), pg=2)  #nao

    document.write_text(dict_especifico['momento_diag'], (299, 268), pg=2)  #momento diagnostico
    document.write_text(dict_especifico['ini_trat_tuberc'], (236, 332), pg=2)  #inicio tratamento
    document.write_date(dict_especifico['dt_ini_trat_tuberc'], (386, 352), spacing=3, pg=2)  #data inicio tratamento
    document.write_text(dict_especifico['forma_clinica'], (156, 383), pg=2)  #forma clinica
    document.write_text(dict_especifico['extrapulmonar'], (156, 407), pg=2)  #extrapulmonar
    document.write_text(dict_especifico['extrapul_outro'], (345, 420), pg=2)  #outro
    document.write_text(dict_especifico['confirm_obt_tuberc'], (330, 455), pg=2)  #confirmacao TB
    document.write_text(dict_especifico['cont_investig'], (192, 475), pg=2)  #continuar investigacao

    if dict_especifico['motiv_cont_invest'] == 'op-tuberculose-outras-unidades':
        document.write_cross((191, 493), pg=2)  #confirmar caso de tuberculose em outras unidades
    elif dict_especifico['motiv_cont_invest'] == 'op-investigacao-contatos':
        document.write_cross((191, 514), pg=2)  #investigação de contatos
    elif dict_especifico['motiv_cont_invest'] == 'op-motivo-continuacao-outro':
        document.write_cross((310, 514), pg=2)  #outros

    document.write_text(dict_especifico['motiv_cont_invest_outro'], (383, 514), pg=2)  #outro motivo
    document.write_box(dict_especifico['obs_adicionais'], rect=(65, 541, 588, 672), pg=2,
                       bord=True)  #observacoes adicionais

    if dict_especifico['info_anexa'] == 'op-info-anexa-sim':
        document.write_cross((205, 706), pg=2)  #sim
    elif dict_especifico['info_anexa'] == 'op-info-anexa-nao':
        document.write_cross((240, 706), pg=2)  #nao

    document.write_date(dict_especifico['dt_notificacao'], (401, 706), spacing=3, pg=2)  #data notificacao
    document.write_text(dict_especifico['nome_notificante'], (70, 745), pg=2)  #nome notificante
    document.write_text(dict_especifico['telefone_investigador'], (452, 745), pg=2)  #telefone investigador
    document.write_text(dict_especifico['municipio_us_notificante'], (70, 780), pg=2)  #municipio

    document.save(nome_arquivo, path_pdf_gerado)
