{% extends "gis/admin/custom/custom.js" %}
{% block base_layer %}
    new ol.layer.Tile({
        source: new ol.source.OSM(),
    })
{% endblock %}
