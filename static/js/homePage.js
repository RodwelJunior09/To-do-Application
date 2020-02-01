$("#edit-title").attr("v-model", "editModal.title");
$("#edit-objective").attr("v-model", "editModal.objective");
$("#edit-content").attr("v-model", "editModal.content");

$("#searchButton").click(function(){
    var value = $("#search-bar").val().toLowerCase();
    if (value != "") {
        $("#card-content div.card").filter(`:not([title*='${value.replace(" ", "_")}'])`).removeClass("d-flex").addClass("d-none");
        $("#card-content div.card").filter(`[title*='${value.replace(" ", "_")}']`).removeClass("d-none").addClass("d-flex");
    } else {
        $("#card-content div.card").each(function(){
            $(this).removeClass("d-none").addClass("d-flex");
        });
    }
});

var homePage = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        editModal: {},
        event_id: "",
    },
    methods: {
        apiData: function(event){
            this.$http.get('/api/todo_list').then(resp => {
                let data = resp.body;
                data.forEach(element => {
                    if (event.target.id == element.id) {
                        this.editModal = element;
                    }
                });
            }, resp => {
                console.log(`An error has ocurred get in the API. ${resp}`)
            })
        },
        editPost: function(event){
            $("#edit_form").attr("action", `/edit/${event.target.id}`);
        },
        deletePost: function(event){
            $("#delete_form").attr("action", `/delete/${event.target.id}`);
        },
        getID: function(event){
            this.event_id = event.target.id;
        }
    }
})
