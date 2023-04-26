function button() {
    var x = document.getElementById("sidenav");
    var a = document.getElementById("navclick1options");
    var b = document.getElementById("navclick2options");
    var c = document.getElementById("navclick3options");
    if (x.style.display === "block") {
        x.style.display = "none";
        document.getElementById("2").style.width = "100%";
        document.getElementById("3").style.width = "100%";
        a.style.display = "none";
        b.style.display = "none";
        c.style.display = "none";
        document.getElementById("navclick1").style.height = "50px";
        document.getElementById("navclick2").style.height = "50px";
        document.getElementById("navclick3").style.height = "50px";
        document.getElementById("body").style.overflow = "unset";
    } else {
        x.style.animationName = "sidenav";
        x.style.animationDuration = "0.1s"
        x.style.display = "block";
        document.getElementById("body").style.overflow = "hidden";
        document.getElementById("2").style.width = "75%";
        document.getElementById("3").style.width = "50%";
    }
}

function navclick1() {
    var a = document.getElementById("navclick1options");
    var b = document.getElementById("navclick2options");
    var c = document.getElementById("navclick3options");
    if (a.style.display === "block") {
        a.style.display = "none";
        document.getElementById("navclick1").style.height = "50px";
    } else {
        b.style.display = "none";
        c.style.display = "none";
        document.getElementById("navclick2").style.height = "50px";
        document.getElementById("navclick3").style.height = "50px";
        a.style.display = "block";
        document.getElementById("navclick1").style.height = "100px";
    }
}

function navclick2() {
    var a = document.getElementById("navclick1options");
    var b = document.getElementById("navclick2options");
    var c = document.getElementById("navclick3options");
    if (b.style.display === "block") {
        b.style.display = "none";
        document.getElementById("navclick2").style.height = "50px";
    } else {
        a.style.display = "none";
        c.style.display = "none";
        document.getElementById("navclick1").style.height = "50px";
        document.getElementById("navclick3").style.height = "50px";
        b.style.display = "block";
        document.getElementById("navclick2").style.height = "100px";
    }
}

function navclick3() {
    var a = document.getElementById("navclick1options");
    var b = document.getElementById("navclick2options");
    var c = document.getElementById("navclick3options");
    if (c.style.display === "block") {
        c.style.display = "none";
        document.getElementById("navclick3").style.height = "50px";
    } else {
        a.style.display = "none";
        b.style.display = "none";
        document.getElementById("navclick1").style.height = "50px";
        document.getElementById("navclick2").style.height = "50px";
        c.style.display = "block";
        document.getElementById("navclick3").style.height = "100px";
    }
}
