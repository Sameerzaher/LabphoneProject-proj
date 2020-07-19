document.onload = () => {
console.log("sameer")
    $(document).ready(function() {
        $.getJSON("/repair/static/json/youtubeVideos.json", function(data){
            var htmlStr = "";
    
            $.each(data, function(key, val){
                console.log(val);
                htmlStr += `<iframe width="100%" height="230" src="${val['url']}" frameborder="0" allowfullscreen></iframe>
                <label class="form-control label-warning text-center">${val['name']}</label>`
            });
    

            console.log("htmlStr: " + htmlStr);
    
            $("#youtubevideo").append(htmlStr);
        });
    });
}


// {
//     "id": "1",
//     "name": "Samsung Galaxy A3 2017 Display Assembly Repair Guide",
//     "url": "https://www.youtube.com/embed/g1P5KBEaHUg?ecver=1"
   
// },