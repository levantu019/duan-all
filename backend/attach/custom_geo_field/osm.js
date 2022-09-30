{% extends "gis/admin/custom_geo_field/custom.js" %}
{% block base_layer %}
    new ol.layer.Tile({
        source: new ol.source.OSM(),
    })
{% endblock %}
