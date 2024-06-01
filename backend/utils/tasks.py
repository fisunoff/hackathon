from celery import shared_task
from django.contrib.auth.models import User

from backend.celery import app
from updater.const import ERROR
from updater.models import Version
from updater.processing import process_data
import logging

from utils.mail_send import send_message


@app.task
def update_data_cron():
    version = Version.objects.create()
    logging.log(logging.INFO, 'Работает задача cron')
    update_data_job(version_id=version.id)
    logging.log(logging.INFO, 'Cron отработал')


@shared_task
def update_data_job(version_id):
    from utils.getfile import download_file, read_ods_to_dataframe
    url = 'https://reestr.fstec.ru/reg3?option=com_rajax&module=rfiles&method=download&format=file&mod=209&file=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    ods_file = 'downloaded_file.ods'
    print('job')
    status_code = download_file(url, headers, ods_file)
    if status_code == 200:
        data = read_ods_to_dataframe(ods_file)
        try:
            process_data(data, version_id)
        except:
            version = Version.objects.get(id=version_id)
            version.status = ERROR
            version.save()
            logging.error("Ошибка при обработке файла.")

    else:
        version = Version.objects.get(id=version_id)
        version.status = ERROR
        version.save()
        logging.error("Ошибка при скачивании файла.")
    send_mails_job.delay(version_id)


@shared_task
def send_mails_job(version_id):
    version = Version.objects.get(id=version_id)
    stats = version.get_statistics()
    if sum(stats) > 0:
        emails = [i for i in User.objects.values_list('email', flat=True) if i] + ['nneewday@mail.ru']
        send_message(emails, *stats, version)
