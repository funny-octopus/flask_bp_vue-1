var app = new Vue({
    el: '#appp',
    delimiters: ['[[', ']]'],
    data: {
        message:"Hi!",
        tags:null,
        changetags_flag:false,
    },
    methods:{
        remove_element:function(item, index){
            this.tags[item].splice(index, 1);
            this.changetags_flag = true;
        },
        add_element:function(item){
            var inp = document.getElementById(item);
            if(inp.value && this.tags[item].indexOf(inp.value)==-1){
                this.tags[item].push(inp.value);
                this.changetags_flag = true;
            inp.value='';
            };
        },
        save_tags:function(){
            if(this.tags != null){
                axios
                    .post('/api/tags', this.tags)
                    .then(response => (
                        response.data.status==="ok" ? this.changetags_flag=false : console.log("alert")
                    ));
            };
        },
    },
    mounted(){
        axios.get('/api/tags').then(response => (this.tags = response.data));
    },
});