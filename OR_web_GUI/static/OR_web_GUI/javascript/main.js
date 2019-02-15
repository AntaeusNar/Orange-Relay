//onload replacement js to allow for multiple functions

if (window.addEventListener) // W3C standard
{
  window.addEventListener('load', FindLabels, false); // NB **not** 'onload'
  window.addEventListener('load', ShowHideNewRulesForm, false);
  window.addEventListener('load', ElementsEvents, false);
}


function ElementsEvents(){
    if (document.getElementById('id_times'))
    {
        document.getElementById('id_times').addEventListener("change", ShowHideNewRulesForm);
    }
}

function ShowHideNewRulesForm(){
    if (document.getElementById('id_times')){
        var sel = document.getElementById('id_times');
        var optionSelected = sel.options.item(sel.options.selectedIndex).value;
        if (optionSelected == 'T') {
           ShowNewRulesForm();
        }else {
            HideNewRulesForm();
        }
    }
}

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

function HideNewRulesForm(){
    var length = document.getElementById('id_length');
    length.style.display = 'none';
    length.label.style.display = 'none';
}


function ShowNewRulesForm(){
    var length = document.getElementById('id_length');
    length.style.display = 'block';
    length.label.style.display = 'block';
}

