from pdfWritter import PDFWriter

pdf = 'Óbito Tuberculose1.pdf'
doc = PDFWriter(pdf)

data = {
    "numero_ficha": "15485",
    "foi_notif_sinan": "9",
    "num_notif_sinan": "9",
    "dt_ultima_notif": "15/02/2022",
    "num_ficha_sinan": "9",
    "sit_caso_sim": "9",
    "dt_obito": "15/02/2022",
    "num_declar_obito": "9",
    "nome_paciente": "observacao",
    "nome_mae": "observacao",
    "dt_nascimento": "15/02/2022",
    "idade": "25",
    "sexo": "1",
    "logradouro_residencia": "observacao",
    "bairro_residencia": "observacao",
    "municipio_residencia": "observacao",
    "uf_residencia": "PI",
    "nome_hospital": "observacao",
    "prontuario_hospit": "9",
    "dt_admissao": "15/02/2022",
    "motivo_intern": "observacao",
    "nome_contato": "observacao",
    "telefone_contato": "86999999999",
    "parentesco_contato": "observacao",
    "sint_tosse": "9",
    "tempo_tosse": "9",
    "sint_febre": "9",
    "sint_desnutricao": "9",
    "sint_sudorese": "9",
    "sint_catarro": "9",
    "sint_dispineia": "9",
    "sint_dor_toracica": "9",
    "sint_cat_sangue": "9",
    "sint_outro": "9",
    "sint_outro_descricao": "observacao",
    "doenca_aids": "9",
    "doenca_neopla": "9",
    "doenca_alcool": "9",
    "doenca_dpoc": "9",
    "doenca_diab": "9",
    "doenca_asma": "9",
    "doenca_mental": "9",
    "doenca_pneumo": "9",
    "doenca_tabag": "9",
    "doenca_nefro": "9",
    "doenca_droga": "9",
    "doenca_hepato": "9",
    "doenca_outro": "9",
    "doenca_outro_descricao": "observacao",
    "ex_bacilo": "9",
    "dt_res_bacilo": "15/02/2022",
    "teste_molec_tub": "9",
    "mat_util_ex_molec": "observacao",
    "dt_admissao_molec": "15/02/2022",
    "ex_bacilo_outro_mat": "9",
    "dt_res_bacilo_outro_mat": "15/02/2022",
    "mat_util_outro_molec": "observacao",
    "cult_escarro": "9",
    "dt_res_cult_escarro": "15/02/2022",
    "ident_especie": "9",
    "especie_microb": "observacao",
    "cult_outro_mat": "9",
    "mat_util_cult_outro_mat": "observacao",
    "dt_res_cult_outro_mat": "15/02/2022",
    "ident_espec_outra_cult": "9",
    "esp_microb_outra_cult": "observacao",
    "teste_sensi_antimicrob": "9",
    "dt_res_antimicrob": "15/02/2022",
    "raio_x_torax": "9",
    "raiox_outra_doenca": "observacao",
    "dt_res_raiox": "15/02/2022",
    "hispatologico": "9",
    "hispato_outra_doenca": "observacao",
    "dt_res_hispato": "15/02/2022",
    "teste_hiv": "9",
    "dt_res_hiv": "15/02/2022",
    "tomografia": "9",
    "op_lesoes_escav": "9",
    "op_nodulos": "9",
    "op_lesoes_cron": "9",
    "op_outro_laudo": "9",
    "laudo_outro_descricao": "observacao",
    "dt_tomografia": "15/02/2022",
    "broncoscopia": "9",
    "dt_broncos": "15/02/2022",
    "outros_exames": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "necropsia": "op-necropsia-sim",
    "necropsia_serv": "op-necropsia-servico-svo",
    "achados_necropsia": "op-achados-necropsia-nao",
    "momento_diag": "9",
    "ini_trat_tuberc": "9",
    "dt_ini_trat_tuberc": "15/02/2022",
    "forma_clinica": "9",
    "extrapulmonar": "9",
    "extrapul_outro": "observacao",
    "confirm_obt_tuberc": "9",
    "cont_investig": "9",
    "motiv_cont_invest": "op-motivo-continuacao-outro",
    "motiv_cont_invest_outro": "observacao",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "info_anexa": "op-info-anexa-sim",
    "dt_notificacao": "15/02/2022",
    "nome_notificante": "observacao",
    "telefone_investigador": "86999999999",
    "municipio_us_notificante": "observacao"
}

doc.write_code(data['numero_ficha'], (518, 153), space=3)  #numero
doc.write_text(data['foi_notif_sinan'], (259, 202))  #ntf sinan antes de morrer
doc.write_text(data['num_notif_sinan'], (531, 200))  #numero notif sinan-TB
doc.write_date(data['dt_ultima_notif'], (205, 234), spacing=3)  #data ultima notif
doc.write_code(data['num_ficha_sinan'], (445, 234), space=3)  #numero ficha sinan
doc.write_text(data['sit_caso_sim'], (196, 267))  #situacao do caso sim
doc.write_date(data['dt_obito'], (157, 304), spacing=3)  #data obito
doc.write_text(data['num_declar_obito'], (432, 304))  #numero declaracao obito
doc.write_text(data['nome_paciente'], (160, 330))  #nome paciente
doc.write_text(data['nome_mae'], (145, 355))  #nome mae
doc.write_date(data['dt_nascimento'], (179, 384), spacing=3)  #data nascimento
doc.write_code(data['idade'], (366, 384), space=3)  #idade
doc.write_text(data['sexo'], (438, 384))  #sexo
doc.write_text(data['logradouro_residencia'], (130, 410))  #logradouro
doc.write_text(data['bairro_residencia'], (85, 443))  #bairro
doc.write_text(data['municipio_residencia'], (262, 443))  #municipio
doc.write_text(data['uf_residencia'], (550, 443))  #uf

#################### parte B ####################
doc.write_text(data['nome_hospital'], (90, 490))  #nome hospital
doc.write_code(data['prontuario_hospit'], (90, 519), space=3)  #prontuario
doc.write_date(data['dt_admissao'], (382, 512), spacing=3)  #data admissao
doc.write_box(data['motivo_intern'], rect=(85, 539, 590, 568))  #motivo internacao
doc.write_text(data['nome_contato'], (90, 595))  #nome contato
doc.write_text(data['telefone_contato'], (90, 625))  #telefone contato
doc.write_text(data['parentesco_contato'], (300, 625))  #parentesco contato

doc.write_text(data['sint_tosse'], (92, 668))  #tosse
doc.write_code(data['tempo_tosse'], (255, 668), space=3)  #tempo tosse
doc.write_text(data['sint_febre'], (92, 691))  #febre
doc.write_text(data['sint_desnutricao'], (140, 691))  #desnutricao
doc.write_text(data['sint_sudorese'], (312, 691))  #sudorese
doc.write_text(data['sint_catarro'], (374, 691))  #catarro
doc.write_text(data['sint_dispineia'], (428, 691))  #dispineia
doc.write_text(data['sint_dor_toracica'], (487, 691))  #dor toracica
doc.write_text(data['sint_desnutricao'], (92, 713))  #catarro de sangue
doc.write_text(data['sint_outro'], (195, 713))  #outro
doc.write_text(data['sint_outro_descricao'], (335, 710))  #descricao outro

#doencas e agravos associados
doc.write_text(data['doenca_aids'], (92, 767))  #aids
doc.write_text(data['doenca_neopla'], (92, 789))  #neoplasia
doc.write_text(data['doenca_alcool'], (157, 767))  #alcool
doc.write_text(data['doenca_dpoc'], (157, 789))  #dpoc
doc.write_text(data['doenca_diab'], (233, 767))  #diabetes
doc.write_text(data['doenca_asma'], (233, 789))  #asma
doc.write_text(data['doenca_mental'], (305, 767))  #doenca mental
doc.write_text(data['doenca_pneumo'], (305, 789))  #pneumonia
doc.write_text(data['doenca_tabag'], (396, 767))  #tabagismo
doc.write_text(data['doenca_nefro'], (396, 789))  #doenca renal
doc.write_text(data['doenca_droga'], (480, 767))  #drogas
doc.write_text(data['doenca_hepato'], (480, 789))  #hepatite
doc.write_text(data['doenca_outro'], (92, 811))  #outro
doc.write_text(data['doenca_outro_descricao'], (204, 809))  #descricao outro

#*========================== fim da pagina 1 ==========================*#

doc.write_text(data['ex_bacilo'], (208, 110), pg=1)  #exame baciloscopico
doc.write_date(data['dt_res_bacilo'], (447, 122), spacing=3, pg=1)  #data resultado baciloscopico
doc.write_text(data['teste_molec_tub'], (76, 160), pg=1)  #teste molecular
doc.write_text(data['mat_util_ex_molec'], (145, 188), pg=1)  #material utilizado
doc.write_date(data['dt_admissao_molec'], (447, 163), spacing=3, pg=1)  #data admissao
doc.write_text(data['ex_bacilo_outro_mat'], (208, 220), pg=1)  #outro material
doc.write_date(data['dt_res_bacilo_outro_mat'], (447, 231), spacing=3, pg=1)  #data resultado outro material
doc.write_text(data['mat_util_outro_molec'], (145, 236), pg=1)  #outro material utilizado
doc.write_text(data['cult_escarro'], (208, 268), pg=1)  #cultura escarro
doc.write_date(data['dt_res_cult_escarro'], (447, 279), spacing=3, pg=1)  #data resultado cultura escarro
doc.write_text(data['ident_especie'], (208, 298), pg=1)  #identificacao especie
doc.write_text(data['especie_microb'], (438, 298), pg=1)  #especie microbiana
doc.write_text(data['cult_outro_mat'], (208, 330), pg=1)  #outro material
doc.write_text(data['mat_util_cult_outro_mat'], (145, 346), pg=1)  #material utilizado
doc.write_date(data['dt_res_cult_outro_mat'], (447, 341), spacing=3, pg=1)  #data resultado outro material
doc.write_text(data['ident_espec_outra_cult'], (208, 368), pg=1)  #identificacao especie
doc.write_text(data['esp_microb_outra_cult'], (438, 366), pg=1)  #especie microbiana
doc.write_text(data['teste_sensi_antimicrob'], (230, 393), pg=1)  #teste sensibilidade
doc.write_date(data['dt_res_antimicrob'], (447, 409), spacing=3, pg=1)  #data resultado teste sensibilidade
doc.write_text(data['raio_x_torax'], (142, 462), pg=1)  #raio x torax
doc.write_text(data['raiox_outra_doenca'], (230, 494), pg=1)  #outra doenca
doc.write_date(data['dt_res_raiox'], (447, 478), spacing=3, pg=1)  #data resultado raio x
doc.write_text(data['hispatologico'], (143, 535), pg=1)  #histopatologico
doc.write_text(data['hispato_outra_doenca'], (230, 564), pg=1)  #outra doenca
doc.write_date(data['dt_res_hispato'], (447, 550), spacing=3, pg=1)  #data resultado histopatologico
doc.write_text(data['teste_hiv'], (143, 606), pg=1)  #teste hiv
doc.write_date(data['dt_res_hiv'], (447, 616), spacing=3, pg=1)  #data resultado hiv
doc.write_text(data['tomografia'], (198, 648), pg=1)  #tomografia
doc.write_text(data['op_lesoes_escav'], (76, 686), pg=1)  #lesoes escavadas
doc.write_text(data['op_nodulos'], (76, 705), pg=1)  #nodulos
doc.write_text(data['op_lesoes_cron'], (257, 705), pg=1)  #lesoes cronicas
doc.write_text(data['op_outro_laudo'], (76, 724), pg=1)  #outros
doc.write_text(data['laudo_outro_descricao'], (147, 724), pg=1)  #descricao outro
doc.write_date(data['dt_tomografia'], (447, 660), spacing=3, pg=1)  #data tomografia
doc.write_text(data['broncoscopia'], (141, 773), pg=1)  #broncoscopia
doc.write_date(data['dt_broncos'], (447, 784), spacing=3, pg=1)  #data broncoscopia
#*========================== fim da pagina 2 ==========================*#

doc.write_box(data['outros_exames'], rect=(65, 83, 588, 180), pg=2, bord=True)  #outros exames
match data['necropsia']:
    case 'op-necropsia-sim':
        doc.write_cross((78, 212), pg=2)  #necropsia sim
    case 'op-necropsia-nao':
        doc.write_cross((112, 212), pg=2)  #necropsia nao

match data['necropsia_serv']:
    case "op-necropsia-servico-iml":
        doc.write_cross((357, 200), pg=2)  #servico IML
    case "op-necropsia-servico-svo":
        doc.write_cross((395, 200), pg=2)  #servico SVO
    case "op-necropsia-servico-hospital":
        doc.write_cross((433, 200), pg=2)  #servico hospital

match data['achados_necropsia']:
    case "op-achados-necropsia-sim":
        doc.write_cross((518, 218), pg=2)  #sim
    case "op-achados-necropsia-nao":
        doc.write_cross((553, 218), pg=2)  #nao

doc.write_text(data['momento_diag'], (299, 268), pg=2)  #momento diagnostico
doc.write_text(data['ini_trat_tuberc'], (236, 332), pg=2)  #inicio tratamento
doc.write_date(data['dt_ini_trat_tuberc'], (386, 352), spacing=3, pg=2)  #data inicio tratamento
doc.write_text(data['forma_clinica'], (156, 383), pg=2)  #forma clinica
doc.write_text(data['extrapulmonar'], (156, 407), pg=2)  #extrapulmonar
doc.write_text(data['extrapul_outro'], (345, 420), pg=2)  #outro
doc.write_text(data['confirm_obt_tuberc'], (330, 455), pg=2)  #confirmacao TB
doc.write_text(data['cont_investig'], (192, 475), pg=2)  #continuar investigacao

match data['motiv_cont_invest']:
    case 'op-tuberculose-outras-unidades':
        doc.write_cross((191, 493), pg=2)  #confirmar caso de tuberculose em outras unidades
    case 'op-investigacao-contatos':
        doc.write_cross((191, 514), pg=2)  #investigação de contatos
    case 'op-motivo-continuacao-outro':
        doc.write_cross((310, 514), pg=2)  #outros

doc.write_text(data['motiv_cont_invest_outro'], (383, 514), pg=2)  #outro motivo
doc.write_box(data['obs_adicionais'], rect=(65, 541, 588, 672), pg=2, bord=True)  #observacoes adicionais

match data['info_anexa']:
    case 'op-info-anexa-sim':
        doc.write_cross((205, 706), pg=2)  #sim
    case 'op-info-anexa-nao':
        doc.write_cross((240, 706), pg=2)  #nao

doc.write_date(data['dt_notificacao'], (401, 706), spacing=3, pg=2)  #data notificacao
doc.write_text(data['nome_notificante'], (70, 745), pg=2)  #nome notificante
doc.write_text(data['telefone_investigador'], (452, 745), pg=2)  #telefone investigador
doc.write_text(data['municipio_us_notificante'], (70, 780), pg=2)  #municipio

doc.save('obito_tuberculose.pdf')
