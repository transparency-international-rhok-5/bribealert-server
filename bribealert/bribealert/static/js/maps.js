
var map, layer;

jQuery.fn.geoMap = function(){
    var lon = this.data('lon');
    var lat = this.data('lat');
    var zoom = 2;

    this.css("height", this.width());

    map = new OpenLayers.Map({
        div: this[0],
        controls: [
            new OpenLayers.Control.Navigation(),
            // new OpenLayers.Control.PanZoom()
        ]
    });
    layer = new OpenLayers.Layer.OSM();
    var context = {
      country_transparency: function(feature) {
        if (feature.attributes["gcb"] != undefined) {
          return (feature.attributes["gcb"]-(feature.attributes["gcb"]%20))/100+0.1
        } else {
          return 0
        }
      }
    }
    var template = {
        fillOpacity: "${country_transparency}",
        strokeWidth: 0,
        fillColor: "#FF1F13"
    };

    var style = new OpenLayers.Style(template, {context: context});
    var styleMap = new OpenLayers.StyleMap({'default': style});
    map.addLayer(layer);
    map.zoomToExtent(new OpenLayers.Bounds(-3.922119,44.335327,4.866943,49.553833));
    map.addLayer(new OpenLayers.Layer.GML( "Internet Users", "js/gcbCountries.json",
                                        { format: OpenLayers.Format.GeoJSON,
                                          styleMap: styleMap,
                                          isBaseLayer: false,
                                          projection: new OpenLayers.Projection("EPSG:4326")} ));
    var markers = new OpenLayers.Layer.Markers( "Markers" );
    map.addLayer(markers);

    var size = new OpenLayers.Size(21,25);
    var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
    var icon = new OpenLayers.Icon('openlayers/img/marker.png',size,offset);

    var position = new OpenLayers.LonLat(lon,lat).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913"));
    myMarker  = new OpenLayers.Marker(position, icon)
    myMarker.events.register("click", myMarker, function() {
        location.hash = 'foo'
    });
    markers.addMarker(myMarker);
    map.setCenter(position, zoom);
};


$(function(){
    $("div[data-lon]").geoMap();
});