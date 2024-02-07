new Vue({
    el: '#weather_show',
    data: {
    weather: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/weather/')
        .then(function (response){
        console.log(response.data)
        })
    }
}
)