(function (theUrl){
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.setRequestHeader("Auth","VYilMkTj_EWsPH03DKoEC5jnaIivJrMc");
    xmlHttp.send( null );
    return JSON.parse(xmlHttp.responseText);
})("/rest/os-deployment-facility/1")
