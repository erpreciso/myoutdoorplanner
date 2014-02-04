$(window).ready(function () {
    create_map();
    $("#create_map").on("click", center_map);
});

var map;

function create_map() {
    var center = new google.maps.LatLng(45.6, 8.85);
    var mapOptions = {
        center: center,
        zoom: 12
    };
    map = new google.maps.Map($("#map-canvas")[0], mapOptions);
    
}

function center_map(){
	var new_center = $("#trip_destination").val();
	var geocoder = new google.maps.Geocoder();
	geocoder.geocode({"address": new_center}, function(results, status){
		if (status == google.maps.GeocoderStatus.OK){
			map.setCenter(results[0].geometry.location);
			map.setZoom(10);
		}
		else {
			alert("Geocode not successful: " + status);
		}
	});
}
