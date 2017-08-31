
import os
from django.db import transaction
import pandas as pd
from conf import ROOT_DIR
from core.models import IMDB


def run(file_path):
    with transaction.atomic():
        xl = pd.ExcelFile(file_path)

        df = xl.parse('Sheet1')
        df = df.fillna('')
        for index, row in df.iterrows():
            IMDB.objects.get_or_create(imdb_id=row['imdb_id'])
    return True


run(os.path.join(ROOT_DIR, 'imdb_ids.xlsx'))