# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:46:35 2022

@author: admin
"""
import pickle

list_words = {1 : "ALEATORIZACION", 2 : "ALHAJAR", 3 : "ALJOFIFAR", 4 : "ANEMOMETRO", 5 : "ANTEDATADO", 6 : "ANTIFLOGISTICO", 7 : "ANTROPOMORFISMO", 8 : "ASINTOTICAMENTE", 9 : "BENZOICO", 10 : "BIENQUISTAR", 11 : "BONHOMIA", 12 : "BRAQUIACION", 13 : "CARDENALATO", 14 : "CERNIDILLO", 15 : "CHAFARRINAR", 16 : "CHUNGUEARSE", 17 : "CIRENAICA", 18 : "CORIORRETINITIS", 19 : "COMEDOGENICO", 20 : "CRIPTOZOOLOGIA", 21 : "DEFLACIONISTA", 22 : "DEHISCENTE", 23 : "DENDROCRONOLOGIA", 24 : "DESENMASCARAMIENTO", 25 : "DESHEREDAMIENTO", 26 : "DESNACIONALIZACION", 27 : "DESPERSONALIZACION", 28 : "DESPOSORIOS", 29 : "DICROISMO", 30 : "DICOTILEDONEO", 31 : "DIPSOMANIACO", 32 : "DITIRAMBO", 33 : "DOSIMETRO", 34 : "DRAGAMINAS", 35 : "ECOTOXICOLOGIA", 36 : "ECUMENICO", 37 : "ELASTOMERO", 38 : "ELECTROCHAPAR", 39 : "ELECTROGALVANISMO", 40 : "ELECTROLUMINISCENCIA", 41 : "ELUVIACION", 42 : "EMPANTANAMIENTO", 43 : "EMPEDERNIRSE", 44 : "ENANTIOMERO", 45 : "ENCUMBRAMIENTO", 46 : "ENMARAÑAMIENTO", 47 : "ENMOHECER", 48 : "ENMUGRAR", 49 : "ENNOBLECIMIENTO", 50 : "ENTRONQUE", 51 : "ENVANECIMIENTO", 52 : "EPICUREISMO", 53 : "EPIGRAMATICO", 54 : "ESCOFINA", 55 : "ESCOLASTICO", 56 : "ESCOPOLAMINA", 57 : "ESCORRENTIA", 58 : "FEMTOGRAMO", 59 : "FERROMAGNETISMO", 60 : "FLOGISTO", 61 : "FOLKLORICO", 62 : "FLUORESCENCIA", 63 : "GONGORISMO", 64 : "GRAMOFONICO", 65 : "GRAVIMETRIA", 66 : "KINESIOLOGIA", 67 : "LICUEFACCION", 68 : "LIGNITO", 69 : "LILIPUTIENSE", 70 : "LOCOMOVIBLE", 71 : "MACADAMIZAR", 72 : "MAGNIFICENCIA", 73 : "MANIOBRABILIDAD", 74 : "MONOLINGÜE", 75 : "MOSCARDON", 76 : "YUXTAPOSICION", 77 : "ZASCANDIL", 78 : "ZIGZAGUEAR", 79 : "ZURCIDURA", 80 : "ZURRIAGAZO", 81 : "RECIPIENDARIO", 82 : "XEROFITICO", 83 : "ESPARADRAPO", 84 : "IDIOSINCRASIA", 85 : "DESENHEBRAR", 86 : "ALEBRESTARSE", 87 : "LOGICOMECANOFOBIA", 88 : "BURDEGANO", 89 : "PARAFRASTICO", 90 : "ESPASTICIDAD", 91 : "ATAXIA", 92 : "CHOQUEZUELA", 93 : "DELICUESCENCIA", 94 : "ABROGRACION", 95 : "ABUBILLA", 96 : "ACEPILLADURA", 97 : "AFILIGRANADO", 98 : "AHERROJAR", 99 : "AISLACIONISMO", 100 : "PERPENDICULAR"}

file_words = open('words.dat', 'wb')

pickle.dump(list_words, file_words)

file_words.close()