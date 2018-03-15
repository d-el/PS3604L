function nano(template, data) {
    return template.replace(/\{([\w\.]*)\}/g, function(str, key) {
      var keys = key.split("."), v = data[keys.shift()];
      for (var i = 0, l = keys.length; i < l; i++) v = v[keys[i]];
      return (typeof v !== "undefined" && v !== null) ? v : "";
    });
}

function updateInfo() {
    var oReq = new XMLHttpRequest();
    oReq.open('GET', '/statemeastask.bin', true);
    oReq.timeout = 2000;
    oReq.responseType = 'arraybuffer';
    oReq.onload = function (oEvent) {
        if (oReq.status != 200) {
            document.querySelector('main').innerHTML = oReq.status;
            return;
        }

        document.querySelector('main').innerHTML = '';  
        var arrayBuffer = oReq.response; // Note: not oReq.responseText
        var x = new DataView(arrayBuffer, 0);

        // State table
        var state = x.getUint32(0, true);
        var stateTable = {
            ovfCurrent: {name: 'current', val: (state & 1 << 0) ? 'ON' : 'OFF'},
            sw: {name: 'switch', val: (state & 1 << 1) ? 'ON' : 'OFF'},
            lim: {name: 'output', val: (state & 1 << 2) ? 'CC' : 'CV'}
        };
        for(var key in stateTable) {
            document.querySelector('main').innerHTML += nano('<div><div class="name">{name}</div><div class="info">{val}</div></div>', stateTable[key]);
        }

        document.querySelector('main').innerHTML += '<br>';
        
        // Measured table
        var measTable = {
            power: {name: 'power', val: x.getUint32(4, true) / 1000.0 + ' Wt'},
            resistens: {name: 'resistens', val: x.getUint32(8, true) / 1000.0 + ' Ohm'},
            time: {name: 'time', val: x.getUint32(12, true) + ' s'},
            capacity: {name: 'capacity', val: x.getUint32(16, true) / 1000.0 + ' Ah'},
            u: {name: 'u', val: x.getUint32(20, true) / 1000000.0 + ' V'},
            i: {name: 'i', val: x.getUint32(24, true) / 1000000.0 + ' A'},
            uin: {name: 'uin', val: x.getUint16(32, true) / 1000.0 + ' V'},
            temperature: {name: 'temperature', val: x.getUint16(34, true) / 10.0 + ' °C'},
        };
        for(var key in measTable) {
            document.querySelector('main').innerHTML += nano('<div><div class="name">{name}</div><div class="info">{val}</div></div>', measTable[key]);
        }

        document.querySelector('main').innerHTML += '<br>';

        // Task table
        var taskTable = {
            u: {name: 'u', val: x.getUint32(36, true) / 1000000.0 + ' V'},
            i: {name: 'i', val: x.getUint32(40, true) / 1000000.0 + ' A'},
        };
        for(var key in taskTable) {
            document.querySelector('main').innerHTML += nano('<div><div class="name">{name}</div><div class="info">{val}</div></div>', taskTable[key]);
        }
    };
    
    oReq.send(null);
}
updateInfo();
setInterval(updateInfo, 200); // Обновление каждые 200мс