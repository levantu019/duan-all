import pandas as pd
import json
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from . import handleString

# PostgreSQL
def dataFromPostgres(host, port, username, password, database, table, model):
    import psycopg2 as db

    # list json data result
    result = []
    
    # connect
    conn = db.connect(host=host, port=port, user=username, password=password, dbname=database)

    # query data
    query = "SELECT * FROM {}".format(table)
    data = pd.read_sql_query(query, conn)

    # lower columns data
    columns_data = [col.lower() for col in list(data)]
    data.columns = columns_data

    # columns of model
    columns_model = model._meta.fields

    for idx in data.index:
        row = data.iloc[idx]
        item_result = {}

        for col in columns_model:
            if col.name.lower() in columns_data:
                # Nếu là khoá chính, sinh ra phần index từ dữ liệu có sẵn (8 ký tự cuối cùng)
                # Ghép với phần đầu của dữ liệu được load
                if col.primary_key:
                    index = handleString.generate_ID_MaNhanDang(idx+1, model)
                    header = row[col.name.lower()][:-8]
                    item_result[col.name] = header + index
                    continue
                # Nếu cột không null trong model và None trong data thì bỏ qua bản ghi
                if row[col.name.lower()] is None:
                    if col.null:
                        continue
                    else:
                        break
                else:
                    if not hasattr(col, 'geom_type'):
                        if type(row[col.name.lower()]).__name__ == 'Timestamp':
                            item_result[col.name] = row[col.name.lower()].tz_convert(tz=settings.TIME_ZONE).isoformat()
                        else:
                            item_result[col.name] = row[col.name.lower()]
                    else:
                        col_name = ''
                        if col.name.lower() in columns_data:
                            col_name = col.name.lower()
                        elif 'geom' in columns_data:
                            col_name = 'geom'
                        elif 'shape' in columns_data:
                            col_name = 'shape'
                        if col_name != '':    
                            item_result[col.name] = json.loads(GEOSGeometry(row[col_name]).geojson)
            else:
                if col.null:
                    continue
                else:
                    break
        
        if len(item_result) > 0:
            result.append(item_result)

    return result

