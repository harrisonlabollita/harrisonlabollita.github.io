function openTab(evt, tabname) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    homecontent = document.getElementsByClassName("homecontent");

    for (i=0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    for (i=0; i < homecontent.length; i++) {
        homecontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i=0; i < tablinks.length; i++){
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementById(tabname).style.display="block";
    evt.currentTarget.className += "active";
}

function openHome(evt) {
    var i, tabcontent, tablinks, homecontent;

    homecontent = document.getElementsByClassName("homecontent");
    tabcontent = document.getElementsByClassName("tabcontent");

    for (i=0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    for (i=0; i < homecontent.length; i++) {
        homecontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i=0; i < tablinks.length; i++){
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementById('home').style.display="block";
    evt.currentTarget.className += "active";
}
