def short_date():
    """
        Example: 03/09/2022 -> 030922
    """
    import datetime
    now = datetime.datetime.now()

    short_day = now.strftime("%d")
    short_month = now.strftime("%m")
    short_year = now.strftime("%y")

    return short_day + short_month + short_year


def generate_MaNhanDang(model, prefix):
    """
        model:
        prefix: 
    """
    # NVDH030922
    prefix = prefix + short_date()

    id = 1
    items = model.objects.all()

    if len(items) != 0:
        # ma_last = items.last().maNhanDang
        # id = int(ma_last[len(prefix):]) + 1 
        id = len(items) + 1

    if id < 10:
        id = '0' + str(id)
    else:
        id = str(id)

    return prefix + id