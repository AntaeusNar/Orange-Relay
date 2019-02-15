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
            current.style.display = 'block';
            current.label.style.display = 'block';
        } else if (current.style.display == 'block'){
            current.style.display = 'none';
            current.label.style.display = 'none';
        }
    } else if (state == 'hide') {
        current.style.display = 'none';
        current.label.style.display = 'none';
    } else if (state == 'show') {
        current.style.display = 'block';
        current.label.style.display = 'block';
    }
}


//looks for, checks and hides items inside the newrules form
function ShowHideNewRulesForm(){
    if (document.getElementById('id_times')){
        var sel = document.getElementById('id_times');
        var optionSelected = sel.options.item(sel.options.selectedIndex).value;
        if (optionSelected == 'T') {
            //document.getElementById('id_length').style.display = 'block'
            ShowHideById("id_length", "show");
        }else {
            //document.getElementById('id_length').style.display = 'none'
            ShowHideById("id_length", "hide");
        }
    }
}

