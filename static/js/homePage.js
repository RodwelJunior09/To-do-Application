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

    // Add value to input when is editing pop up appears
    $("a[href='#edit']").click(function(){
        var idElement = this.id;
        $.ajax({
            url: "http://localhost:5000/api/todo_list",
            success: function(resp){
                resp.forEach(d => {
                    if (d.id == idElement) {
                        $("input#title").val(d.title);
                        $("input#objective").val(d.objective);
                        $("textarea#content").val(d.content);
                    }
                });
            }
        })
    });
})
