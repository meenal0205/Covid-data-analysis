const layerList = document.getElementById('menu');

$('.sidebar').addClass('close');
$('.sidebar h3').hide();



$('#menu_btn').on('click',function()
{
    $('.sidebar h3').show();
    $('.sidebar').addClass('open');
    $('main .analytics').css('left','250px');
    $('#menu_btn').hide();
    $('#close_btn').show();

});

$('#close_btn').on('click',function()
{
    $('.sidebar').removeClass('open');
    $('main .analytics').css('left','140px');
    $('.sidebar h3').hide();
    $('#close_btn').hide();
    $('#menu_btn').show();
})

function updateMap()
{
    fetch('latest.json')
    .then(Response => Response.json())
    .then(rsp => {
        console.log(rsp.data.regional)
        rsp.data.regional.forEach(element => {
            
        });

        new mapboxgl.Marker({
            draggable: true
            })
            .setLngLat([18.5204, 73.8567])
            .addTo(map);
    })
    const inputs = layerList.getElementsByTagName('input');
    for (const input of inputs) {
        input.onclick = (layer) => {
        const layerId = layer.target.id;
        map.setStyle('mapbox://styles/mapbox/' + layerId);
        };
        }
    
}

mapboxgl.accessToken = 'pk.eyJ1IjoiZnVnZ3MxMzQ3IiwiYSI6ImNsMTF3aDgwdjA1dTEzY3A0YmxxYzZudGYifQ.kgWahH-A5V9y4xzSHzzkSQ';
const mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });
mapboxClient.geocoding
.forwardGeocode({
query: 'Wellington, New Zealand',
autocomplete: false,
limit: 1
})
.send()
.then((response) => {
if (
!response ||
!response.body ||
!response.body.features ||
!response.body.features.length
) {
console.error('Invalid response:');
console.error(response);
return;
}
const feature = response.body.features[0];
 
const map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: feature.center,
zoom: 10
});
 
// Create a marker and add it to the map.
new mapboxgl.Marker().setLngLat(feature.center).addTo(map);
});




updateMap();