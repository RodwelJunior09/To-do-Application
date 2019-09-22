$(document).ready(function(){
    var listContents = document.querySelectorAll("#card-content li.list-content");
    listContents.forEach(element => {
        var match = /\r|\n/.exec(element.innerHTML);
        if (match) {
            var splittext = element.innerHTML.split(/\r|\n/);
            splittext.forEach(s => {
                $(element).parent().append(`<li class='list-group-item list-content'>${s}</li>`)
            })
            element.remove();
        }
    });
})
