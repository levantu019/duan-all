{% load l10n %}
{% block vars %}
    var {{ module }} = {};
    {{ module }}.map = null; 
    {{ module }}.snap = null; 
    {{ module }}.draw = null; 
    {{ module }}.sDrawControl = null; 
    {{ module }}.eDrawControl = null; 
    {{ module }}.modify = null; 
    {{ module }}.convert = null; 
    {{ module }}.mouse = null; 
    {{ module }}.re = new RegExp("^SRID=\\d+;(.+)", "i"); 
    {{ module }}.layers = {};
    {{ module }}.wkt_f = new ol.format.WKT();
    {{ module }}.source = new ol.source.Vector();
{% endblock %}


// Convert srs
{{ module }}.convert = function(coord, from, to) {
    if ('{{ geom_type }}' === 'Point'){
        return proj4(from, to, coord);
    }
    else if ('{{ geom_type }}' === 'LineString'){
        return coord.map(value => proj4(from, to, value));
    }
    else if ('{{ geom_type }}' === 'Polygon'){
        return [coord[0].map(value => proj4(from, to, value))];
    }
}

// Return geometry str such as SRID=3857;POLYGON((2275010.5002242 -777333.97288251,-855850.17790075 -1573746.7474552))
{{ module }}.get_ewkt = function(feat){
    var current_feat = null;
    if(feat instanceof ol.Feature){
        current_feat = feat;
    }
    else if(feat.feature instanceof ol.Feature){
        current_feat = feat.feature
    }
    else{
        current_feat = feat.features.getArray()[0];
    }

    current_feat.getGeometry().setCoordinates({{ module }}.convert(current_feat.getGeometry().getCoordinates(), 'EPSG:{{ display_srid }}', 'EPSG:{{ srid }}'));   
    return 'SRID={{ srid|unlocalize }};' + {{ module }}.wkt_f.writeFeature(current_feat);
};

// Return wkt
{{ module }}.read_wkt = function(wkt){
    // OpenLayers cannot handle EWKT -- we make sure to strip it out.
    // EWKT is only exposed to OL if there's a validation error in the admin.
    var match = {{ module }}.re.exec(wkt);
    if (match){wkt = match[1];}
    return {{ module }}.wkt_f.readFeature(wkt,{
        dataProjection: 'EPSG:{{ srid }}',
        featureProjection: 'EPSG:{{ display_srid }}',
    });
};

// Write geometry str into textarea
{{ module }}.write_wkt = function(feat){
    document.getElementById('{{ id }}').value = {{ module }}.get_ewkt(feat);
};

//
{{ module }}.modify_wkt = function(event){
    {{ module }}.write_wkt(event.feature);
};

// Function to clear vector features and purge wkt from div
{{ module }}.deleteFeatures = function(){
    {{ module }}.layers.vector.getSource().getFeatures().forEach(item => {{ module }}.layers.vector.getSource().removeFeature(item));
};

{{ module }}.clearFeatures = function (){
    {{ module }}.deleteFeatures();
    document.getElementById('{{ id }}').value = '';
};


//
{{ module }}.init = function(){
    // The admin map for this geometry field.
    {% block map_creation %}
        {{ module }}.projection = {% block map_projection %}
            new ol.proj.Projection({
                code: 'EPSG:{{ display_srid }}',
                units: '{{ units }}',
            })
        {% endblock %}

        {{ module }}.view = {% block map_view %}
            new ol.View({
                projection: {{ module }}.projection,
                minZoom: {{ min_zoom }},
            })
        {% endblock %}

        {{ module }}.map = new ol.Map({
            controls: ol.control.defaults(),
            layers: [],
            target: '{{ id }}_map',
            view: {{ module }}.view
        })

        
        {{ module }}.layers.base = {% block base_layer %}
            new ol.layer.Image({
                source: new ol.source.ImageWMS({
                    url: '{{ wms_url }}',
                    params: {
                        'VERSION': '1.1.1',
                        'FORMAT': 'image/png',
                        'LAYERS': '{{ wms_layer }}',
                    }
                }),
            })
        {% endblock %}

    {{ module }}.map.addLayer({{ module }}.layers.base);
    {% endblock %}

    {% block extra_layers %}{% endblock %}
    
    {{ module }}.layers.vector = {% block layer_vector %}
        new ol.layer.Vector({
            source: {{ module }}.source,
            zIndex: 10,
            style: new ol.style.Style({
                fill: new ol.style.Fill({
                    color: 'rgba(255, 255, 255, 0.2)',
                }),
                stroke: new ol.style.Stroke({
                    color: '#ffcc33',
                    width: 2,
                }),
                image: new ol.style.Circle({
                    radius: 7,
                    fill: new ol.style.Fill({
                        color: '#ffcc33',
                    }),
                }),
            }),
        });
    {% endblock %}

    {{ module }}.map.addLayer({{ module }}.layers.vector);

    // Read WKT from the text field.
    var wkt = document.getElementById('{{ id }}').value;
    if (wkt){
        // After reading into geometry, immediately write back to
        // WKT <textarea> as EWKT (so that SRID is included).
        var admin_geom = {{ module }}.read_wkt(wkt);
        {{ module }}.write_wkt(admin_geom);

        // Add feature
        {{ module }}.layers.vector.getSource().addFeature(admin_geom);

        // fit map
        {{ module }}.map.getView().fit(admin_geom.getGeometry().getExtent(), {{ module }}.map.getSize());
        
    } else {
        {% localize off %}
            {{ module }}.map.getView().setCenter([{{ default_lon }}, {{ default_lat }}]);
            {{ module }}.map.getView().setZoom({{ default_zoom }});
        {% endlocalize %}
    }

    // Create some custom controls
    {% block controls %}
        //
        {{ module }}.draw = new ol.interaction.Draw({
            source: {{ module }}.source,
            type: '{{ geom_type }}',
        })

        {{ module }}.snap = new ol.interaction.Snap({
            source: {{ module }}.source,
        })

        {{ module }}.modify = new ol.interaction.Modify({
            source: {{ module }}.source,
        })

        // when draw end, write textarea
        {{ module }}.draw.on('drawstart', function () {
            if ({{ module }}.layers.vector.getSource().getFeatures().length != 0){
                {{ module }}.clearFeatures();
            }
        })

        {{ module }}.draw.on('drawend', function (evt) {
            {{ module }}.write_wkt(evt);
        })

        {{ module }}.modify.on('modifyend', function (evt) {
            {{ module }}.write_wkt(evt);
        })

        
        // Mouse Control
        {{ module }}.mouse = new ol.control.MousePosition({
            coordinateFormat: ol.coordinate.createStringXY(3),
            projection: {{ module }}.map.getView().getProjection(),
            className: 'mouse-position',
            target: document.getElementById('position_mouse'),
            undefinedHTML: '&nbsp;',
        })

        {{ module }}.map.addControl({{ module }}.mouse)

        // controls
        document.getElementById('start-draw').addEventListener('click', function(){
            {{ module }}.map.addInteraction({{ module }}.draw);
            {{ module }}.map.addInteraction({{ module }}.snap);
            {{ module }}.map.addInteraction({{ module }}.modify);
        })
        document.getElementById('end-draw').addEventListener('click', function(){
            {{ module }}.map.removeInteraction({{ module }}.draw);
            {{ module }}.map.removeInteraction({{ module }}.snap);
            {{ module }}.map.removeInteraction({{ module }}.modify);
        })
    
    {% endblock %}
};