//main javascript

// adds items as onload
if (window.addEventListener) // W3C standard
{
  window.addEventListener('load', FindLabels, false); // NB **not** 'onload'
  window.addEventListener('load', ShowHideNewRulesForm, false);
  window.addEventListener('load', ElementsEvents, false);
}


// adds items to events
function ElementsEvents(){
    if (document.getElementById('id_times'))
    {
        document.getElementById('id_times').addEventListener("change", ShowHideNewRulesForm);
    }
    if (document.getElementById('id_output'))
    {
        document.getElementById('id_output').addEventListener("change", ShowHideNewRulesForm);
    }
}


//adds labeled items to the base item
function FindLabels(){
    var labels = document.getElementsByTagName('label');
    for (var i = 0; i < labels.length; i++) {
        if (labels[i].htmlFor != '') {
            var elem = document.getElementById(labels[i].htmlFor);
            if (elem)
                elem.label = labels[i];
        }
    }
}


//function to show, hide or toggle an element and its label
function ShowHideById(id, state = "toggle"){
    //document.getElementById(id).style.display = 'none';
    var current = document.getElementById(id);
    if (state == 'toggle'){
        if (current.style.display == 'none'){
            current.style.display = 'inline';
            current.label.style.display = 'inline';
        } else if (current.style.display == 'inline'){
            current.style.display = 'none';
            current.label.style.display = 'none';
        }
    } else if (state == 'hide') {
        current.style.display = 'none';
        current.label.style.display = 'none';
    } else if (state == 'show') {
        current.style.display = 'inline';
        current.label.style.display = 'inline';
    }
}


//looks for, checks and hides items inside the newrules form
function ShowHideNewRulesForm(){
    if (document.getElementById('id_times')){
        var out = document.getElementById('id_output');
        var outoption = out.options.item(out.options.selectedIndex).value;
        if (outoption != ''){
            ShowHideById('id_action', 'show');
            ShowHideById('id_times', 'show');
            var sel = document.getElementById('id_times');
            var optionSelected = sel.options.item(sel.options.selectedIndex).value;
            if (optionSelected == 'T') {
                //document.getElementById('id_length').style.display = 'block'
                ShowHideById("id_length", "show");
            }else {
                //document.getElementById('id_length').style.display = 'none'
                ShowHideById("id_length", "hide");
            }
        } else {
            ShowHideById('id_action', 'hide');
            ShowHideById('id_times', 'hide');
    }
}

//AJAX call
function httpGetAsync(url, callback){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function(){
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
        }
        xmlHttp.open("GET", url, true);
        xmlHttp.send(null);
}