// EPSG:4756
proj4.defs(
    'EPSG:4756',
    '+proj=longlat +ellps=WGS84 +towgs84=-191.90441429,-39.30318279,-111.45032835,0.00928836,-0.01975479,0.00427372,0.252906278 +no_defs '
  );
ol.proj.proj4.register(proj4);