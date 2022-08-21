import os
from django.contrib.gis import admin
from django.conf import settings


# Register your models here.
class CustomGeoAdmin(admin.GeoModelAdmin):
    # Toạ độ ban đầu
    default_lon = settings.GEOADMIN_SETTINGS['default_lon']
    default_lat = settings.GEOADMIN_SETTINGS['default_lat']
    default_zoom = settings.GEOADMIN_SETTINGS['default_zoom']
    display_wkt = settings.GEOADMIN_SETTINGS['display_wkt']
    # display_srid: Hệ toạ độ trên bản đồ tương tác
    display_srid = settings.GEOADMIN_SETTINGS['display_srid']   
    extra_js = settings.GEOADMIN_SETTINGS['extra_js']
    max_zoom = settings.GEOADMIN_SETTINGS['max_zoom']
    min_zoom = settings.GEOADMIN_SETTINGS['min_zoom']
    units = settings.GEOADMIN_SETTINGS['units']
    max_resolution = settings.GEOADMIN_SETTINGS['max_resolution']
    modifiable = settings.GEOADMIN_SETTINGS['modifiable']
    mouse_position = settings.GEOADMIN_SETTINGS['mouse_position']
    scale_text = settings.GEOADMIN_SETTINGS['scale_text']
    layerswitcher = settings.GEOADMIN_SETTINGS['layerswitcher']
    scrollable = settings.GEOADMIN_SETTINGS['scrollable']
    map_width = settings.GEOADMIN_SETTINGS['map_width']
    map_height = settings.GEOADMIN_SETTINGS['map_height']
    # map_srid: Hệ toạ độ lưu trong db
    map_srid = settings.GEOADMIN_SETTINGS['map_srid']
    map_template = settings.GEOADMIN_SETTINGS['map_template']
    openlayers_url = settings.GEOADMIN_SETTINGS['openlayers_url']
    wms_url = settings.GEOADMIN_SETTINGS['wms_url']
    wms_layer = settings.GEOADMIN_SETTINGS['wms_layer']
    wms_name = settings.GEOADMIN_SETTINGS['wms_name']
    wms_options = settings.GEOADMIN_SETTINGS['wms_options']
