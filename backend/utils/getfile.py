import requests
import warnings
import pandas as pd

from updater.models import Version
from .tasks import update_data_job


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
    version = Version.objects.create()
    print('sync')
    update_data_job.delay(version.id)
