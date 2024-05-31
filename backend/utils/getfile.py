import requests
import warnings
import pandas as pd

from updater.processing import process_data


def download_file(url, headers, filename):
    """Метод для скачивания файла по урлу."""
    warnings.filterwarnings("ignore")

    r = requests.get(url, headers=headers, verify=False)

    if r.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(r.content)
    else:
        print(f"Failed to download file. Status code: {r.status_code}")
    return r.status_code


def read_ods_to_dataframe(filename):
    """Метод для считывания данных с файла."""
    data = pd.read_excel(filename, engine='odf')
    return data


def save_dataframe_to_excel(data, filename):
    """Метод для сохранения данных в xlsx."""
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        data.to_excel(writer, index=False)


def update_data():
    url = 'https://reestr.fstec.ru/reg3?option=com_rajax&module=rfiles&method=download&format=file&mod=209&file=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    xlsx_file = 'output_file.xlsx'
    ods_file = 'downloaded_file.ods'

    status_code = download_file(url, headers, ods_file)
    if status_code == 200:
        data = read_ods_to_dataframe(ods_file)
        process_data(data)
        # save_dataframe_to_excel(data, xlsx_file)

        # data_list = data.values.tolist()
        # print(data_list)

        print(data.iloc[0])
    else:
        print("Failed to download the file.")
