$("#edit-title").attr("v-model", "editModal.title");
$("#edit-objective").attr("v-model", "editModal.objective");
$("#edit-content").attr("v-model", "editModal.content");

var homePage = new Vue({
    el: "#app",
    data: {
        editModal: {},
        event_id: ""
    },
    methods: {
        editData: function(){
            this.$http.post(`/edit/${this.event_id}`).then(resp => {
                window.location.reload();
            })
        },
        deleteData: function(){
            this.$http.post(`/delete/${this.event_id}`).then(resp => {
                window.location.reload();
            });
        },
        apiData: function(event){
            $("#edit_form").attr("action", `/edit/${event.target.id}`);
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
        getID: function(event){
            this.event_id = event.target.id;
        }
    }
})
