(function() {
	var table;
	var output = [["State","City","Area Code"]];
	
	function addRow(state, city, code) {
		output.push([state,city,code]);
		var row = document.createElement("row");
		row.innerHTML += "<td>" + state + "</td>";
		row.innerHTML += "<td>" + city + "</td>";
		row.innerHTML += "<td>" + code + "</td>";
		table.append(row);
	}
	
	function scrapeStatePage(url) {
		
	}
	
	function scrapeAllStates(url) {
		$.get({
			url:url,
			success: function( data ) {
				$( ".result" ).html( data );
				alert( "Load was performed." );
			},
			headers: {"Access-Control-Allow-Origin": "*"}
		});
	}

	function start() {
		table = $("#results")
		scrapeAllStates("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States");
	}
	
	start();
})();