function initMap(){
    // Pozicioni i FSHN
    var fshn ={lat:41.32815,lng:19.81306 };
    // Harta e qenderzuartek FSHN
    var map =new google.maps.Map(document.getElementById('map'),{zoom:20,center:fshn});
    // Markeri i pozicionuar tek FSHN
    var marker =new google.maps.Marker({position:fshn,map:map});
}