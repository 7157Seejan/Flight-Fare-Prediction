function predictFare(){
    var journey_date = document.getElementById("journey_date").value;
    var dep_time = document.getElementById("departure_time").value;
    var arr_time = document.getElementById("arrival_time").value;
    var source = document.getElementById("source").value;
    var destination = document.getElementById("destination").value;
    var stops = document.getElementById("stops").value;
    var airline = document.getElementById("airline").value;
    var estimated_price = document.getElementById("estimated_price");

    var fare_url = "http://127.0.0.1:5000/predict_price"

    $.post(fare_url, {
        journey_date: journey_date,
        departure_time: dep_time,
        arrival_time: arr_time,
        stops: stops,
        airline: airline,
        source: source,
        destination: destination
    }, function(data, status){
        estimated_price.innerHTML = "<h2> Estimated fare is: INR   " + "<span>" + data.estimated_fare + "</span>" + "</h2>";
    });
}

function onPageLoad(){
    var source_url = "http://127.0.0.1:5000/get_source_names"
    $.get(source_url, function(data, status){
        if(data){
            var sources = data.source;
            var source = document.getElementById("source");
            $("#source").empty();
            for(var i in sources){
                var option = new Option(sources[i]);
                $("#source").append(option);
            }
        }
    });

    var destination_url = "http://127.0.0.1:5000/get_destination_names"
    $.get(destination_url, function(data, status){
        if(data){
            var destinations = data.destination;
            var destination = document.getElementById("destination");
            $("#destination").empty();
            for(var i in destinations){
                var option = new Option(destinations[i]);
                $("#destination").append(option);
            }
        }
    });

    var airline_url = "http://127.0.0.1:5000/get_airline"
    $.get(airline_url, function(data, status){
        if(data){
            var airlines = data.airline;
            var airline = document.getElementById("airline");
            $("#airline").empty();
            for(var i in airlines){
                var option = new Option(airlines[i]);
                $("#airline").append(option);
            }
        }
    });
}

window.onload = onPageLoad;