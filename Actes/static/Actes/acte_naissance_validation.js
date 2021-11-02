
function get_child_class(element)
{

}
function send_info()
{
    /*
    datas = document.getElementsByTagName("p")
    for(i = 0; i < datas.length;i++)
    {
        
        
    }
    */

    //alert("done")
    
    
    //alert("done")
    
    datas = document.getElementsByTagName("input")
    for(var i = 0;i<datas.length;i++)
    {
        if(datas[i].type != "hidden" && datas[i].type != 'submit')
        {
            datas[i].value = 1
        }
    }
    
    
    /*
    datas = document.getElementsByTagName("input")
    result = ""
    for(var i = 0;i<datas.length;i++)
    {
        result = result + "µ"+datas[i].getAttribute("id")+"Œ"+datas[i].value
    }
    //alert("in")
    send_xhr = new XMLHttpRequest()
    //token = document.getElementByName()
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value
    //alert(token)
    //send_xhr.setRequestHeader("Content-Type", "application/x-www-formurlencoded");
    l = document.URL.split("/")
    send_url = "http://127.0.0.1:8070/actes/m?csrfmiddlewaretoken="+token //["/",l[2],l[3],"m?"].join("/") + ""+token
    send_xhr.open("GET",send_url)
    send_xhr.send(result)
    //alert(["/",l[2],l[3],"m?"].join("/") + ""+token)
    //alert(result)
    */
}