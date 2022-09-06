# -*- coding: utf-8 -*-
"""
@author: Hugo Franco, Roberto Arias
"""
try:
    import os, sys
    from pathlib import Path as p
    from pandas_profiling import ProfileReport

except Exception as exc:
            print('Module(s) {} are missing.:'.format(str(exc)))

dir_root = p(__file__).parents[1]
sys.path.append(str(p(dir_root) /'source' / 'clases'))

from cls_extract_data_mf import extract_data_mf as data_extractor

#%%
''' Crear una instancia de la clase (objeto) '''
extractor = data_extractor()
extractor.path = dir_root

#%%
'''Autenticación en el api de Kaggle'''
path_auth = str(p(extractor.path) / 'kaggle')
extractor.set_kaggle_api(path_auth)

#%%
''' Existe el directorio destino '''
path_data = str(p(extractor.path) / 'Dataset' / 'nfl')
extractor.check_path(path_data)
print(extractor.dir_exist)

#%%
''' Espacio disponible en disco '''
path_data = str(p(extractor.path) / 'Dataset' / 'Finance')
extractor.check_free_space(path_data)
extractor.check_used_space(path_data)

#%%
''' Listar competencias'''
extractor.list_competition_kaggle(competition="nfl")

#%%
''' Listar archivos en una competencia. Ejemplo: 3'''
extractor.competition = str(extractor.lst_competition[3])
print("Competencia: ", extractor.competition)
extractor.list_files_competition_kaggle()

#%%
''' Descargar archivos de una competencia'''
path_data = str(p(extractor.path) / 'Dataset' / 'nfl')
extractor.dataset = str(extractor.lst_files_c[0])
extractor.get_data_from_kaggle_c(path_data)

#%%
''' Listar datasets'''
extractor.list_dataset_kaggle('youtube')
#extractor.list_dataset_kaggle('finance complaints')

extractor.show_kaggle_datasets()

#%%
''' Descargar todos los archivos de un dataset alojado kaggle '''

path_data = str(p(extractor.path) / 'Dataset' / 'youtube')
extractor.get_data_from_kaggle_d(path_data,'datasnaek/youtube-new')

#%%
''' Listar archivos según el tipo'''
path_data = str(p(extractor.path) / 'Dataset' / 'youtube')
extractor.get_lst_files(path_data,'csv')
print('{}Instancia kaggle:'.format(os.linesep))
extractor.show_files()

#%%
''' Cargar datos a memoria'''
extractor.get_data_csv(extractor.lst_files[9])

#%%
''' Mostrar datos'''
print(extractor.data)

#%%
''' Crear perfil de los datos '''
df = extractor.data
profile = ProfileReport(df, 
                        title="ESTADOS UNIDOS", 
                        explorative=True,
                        minimal=True)

profile.to_file("pandas_profiling_report.html")