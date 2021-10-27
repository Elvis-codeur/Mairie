function change_table()
{
    //alert("klk")
    v = document.getElementById("catego").value
    link = "http://127.0.0.1:8070/fr/clients/get/" + v
    
    var xhr = new XMLHttpRequest()
    xhr.open("GET",link)
    xhr.onreadystatechange = function() {
        if (xhr.readyState == xhr.DONE) { 
            xhr.send(null)
            alert("done")
        }
        };
}