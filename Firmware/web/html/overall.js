function nano(template, data) {
	return template.replace(/\{([\w\.]*)\}/g, function(str, key) {
	  var keys = key.split("."), v = data[keys.shift()];
	  for (var i = 0, l = keys.length; i < l; i++) v = v[keys[i]];
	  return (typeof v !== "undefined" && v !== null) ? v : "";
	});
}

function updateTable(query, data) {
	var table = document.querySelector(query);
	table.innerHTML = '';
	for(var key in data) {
		table.innerHTML += nano('<tr><td>{name}</td><td>{val}</td></tr>', data[key]);
	}
}

function updateInfo() {
	var oReq = new XMLHttpRequest();
	oReq.open('GET', 'statemeastask.bin', true);
	oReq.timeout = 5000;
	oReq.responseType = 'arraybuffer';
	
	oReq.onerror = function (oEvent) {
		var errorbox = document.querySelector('.errorbox');
		errorbox.style.display = 'block';
		return errorbox.innerHTML = 'Error: ' + oReq.status;
	}
	
	oReq.onload = function (oEvent) {

		var errorbox = document.querySelector('.errorbox');
		if(oReq.status == 200) {
			errorbox.style.display = 'none';
		}else{
			errorbox.style.display = 'block';
			return errorbox.innerHTML = 'Error: ' + oReq.status;
		}

		var x = new DataView(oReq.response, 0);

		// State
		var state = x.getUint32(0, true);
		updateTable('.table1', [
			{name: 'overcurrent', val: (state & 1 << 0) ? '<p style="color:red;">YES</p>' : 'NO'},
			{name: 'switch', val: (state & 1 << 1) ? '<p style="color:red;">ON</p>' : 'OFF'},
			{name: 'output', val: (state & 1 << 2) ? 'CC' : 'CV'}
		]);

		// Meas
		updateTable('.table2', [
			{name: 'power', val: x.getUint32(4, true) / 1000.0 + ' Wt'},
			{name: 'resistance', val: x.getUint32(8, true) / 1000.0 + ' Ohm'},
			{name: 'time', val: x.getUint32(12, true) + ' s'},
			{name: 'capacity', val: x.getUint32(16, true) / 1000.0 + ' Ah'},
			{name: 'u', val: x.getUint32(20, true) / 1000000.0 + ' V'},
			{name: 'i', val: x.getUint32(24, true) / 1000000.0 + ' A'},
			{name: 'uin', val: x.getUint16(32, true) / 1000.0 + ' V'},
			{name: 'temperature', val: x.getUint16(34, true) / 10.0 + ' °C'}
		]);

		// Settings
		updateTable('.table3', [
			{name: 'u', val: x.getUint32(36, true) / 1000000.0 + ' V'},
			{name: 'i', val: x.getUint32(40, true) / 1000000.0 + ' A'},
		]);
	};
	oReq.send(null);
}
updateInfo();
setInterval(updateInfo, 2000);