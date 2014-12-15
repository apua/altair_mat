gen_api = (function (method, URI, payload) {
        var xmlHttp = null;
        xmlHttp = new XMLHttpRequest();
        xmlHttp.open( method, URI, false );
        xmlHttp.setRequestHeader("Auth",AUTH);
        xmlHttp.send(payload);
        return JSON.parse(xmlHttp.responseText);
        })

/* Example */
// rep = gen_api('GET', '/rest/os-deployment-servers/30001')
