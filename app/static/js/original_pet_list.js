window.onscroll = function(){
    var ScrT = document.body.scrollTop;
    var CliH = document.body.clientHeight;
    var ScrH = document.body.scrollHeight;
    if(ScrT >= ScrH - CliH)
    {
        AddPhotoGrid("ul1");
        AddPhotoGrid("ul2");
    }
}




//放大

    $(document).on('click','#Close',function(){
        $(".big").hide();
        $(this).hide();
        $("#Close").hide();
        $(".popup").hide();
        $(".detail-container").hide();
    })
    $(document).on('click','.pic-grid img',function()
    {   
        bigImg='';
        $(".popup").show();
        $(".big").show();
        $("#Close").show();
        $(".detail-container").show();
        bigImg = $(this).attr("src");
        $(".show img.big").attr("src",bigImg);
    })

//返回頁頂
$(function(){
    $("#BackToTop").click(function(){
        jQuery('html,body').animate({
            scrollTop:0
        },300);
    });
    $(window).scroll(function() {
        if ( $(this).scrollTop() > 150){
            $('#BackToTop').fadeIn("fast");
        } else {
            $('#BackToTop').stop().fadeOut("fast");
        }
    });
 });

var maxPics = 718;
var pics = 6;

//載入圖片格
function AddPhotoGrid(elem)
{
    if(pics >= maxPics)
        return;
    var order = ++pics;
    var li = document.createElement("li");
    li.setAttribute("class","pic-grid");
    var number = document.createElement("h5");
    var photo = document.createElement("img");
    if(order < 10){
    photo.src = "url({{ url_for('static', filename='img/pets/00" + order +".png') }}";
    photo.alt = "pic"+ order;
    number.innerHTML = "#00" + order;
    }
    else if(order < 100){
    photo.src = "url({{ url_for('static', filename='img/pets/0" + order +".png') }}";
    photo.alt = "pic"+ order;
    number.innerHTML = "#0" + order;
    }
    else{
        photo.src = "url({{ url_for('static', filename='img/pets/" + order +".png') }}";
        photo.alt = "pic"+ order;
        number.innerHTML = "#" + order;
    }
    var info = document.createElement("info");
    li.appendChild(photo);
    li.appendChild(info);
    document.getElementById(elem).appendChild(li);
}

function showDetail()
{
    var detailData = ("<p><h2>宝贝名称："+{{monster.name}}+"</h2><p>属性："+{{monster.type}}+"</p>");
    $(".detail-container").append(detailData);   
}