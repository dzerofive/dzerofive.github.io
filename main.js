var map = L.map('map').setView([48.51632099978832, 32.2578105536212], 2);
let point_p = document.getElementById("points");

L.tileLayer('map/{z}/{x}-{y}.png', {
    maxZoom: 5,
    attribution: '<a href="http://t.me/dzerofive">dzerofive</a>',
}).addTo(map);

var marker = L.marker([24.521092, -52.04299]).addTo(map);
marker.bindPopup("Хаха я тут живу").openPopup();

L.circle([40, 25], {radius: 300000, color: '#55ee99'}).addTo(map);




let points = [];
let display_points = [];
var polyg = L.polygon(points).addTo(map);

function onMapClick(e) {
  map.removeLayer(polyg)
  points.push(e.latlng);
  polyg = L.polygon(points).addTo(map);

  display_points.push('[' + e.latlng.lng + ',' + e.latlng.lat + ']');
  point_p.innerText = display_points;
}
map.on('click', onMapClick);