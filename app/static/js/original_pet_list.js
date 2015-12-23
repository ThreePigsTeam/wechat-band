window.onscroll = function(){
    var allHeight = document.documentElement.scrollHeight || document.body.scrollHeight;//body的高度 
    var hideHeight = document.body.scrollTop || document.documentElement.scrollTop;//卷上去的高度 
    var screenHeight = document.documentElement.clientHeight;//浏览器可见高度
    if(hideHeight+screenHeight>=allHeight-40)
    {
        AddPhotoGrid("ul1",u);
        AddPhotoGrid("ul2",u);
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
    $(document).on('click','.pic-grid :image',function()
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
    li.setAttribute("id", "pet"+order);
    var number = document.createElement("h5");
    var photo = document.createElement("img");
    if(order < 10){
    photo.src = u +"00"+ order +".png";
    photo.alt = "00" + order;
    number.innerHTML = "#00" + order;
    }
    else if(order < 100){
    photo.src = u +"0"+ order +".png";
    photo.alt = "0" + order;
    number.innerHTML = "#0" + order;
    }
    else{
        photo.src = u + order +".png";
        photo.alt = order;
        number.innerHTML = "#" + order;
    }
    var info = document.createElement("info");
    li.appendChild(number);
    li.appendChild(photo);
    li.appendChild(info);
    document.getElementById(elem).appendChild(li);
}

function showDetail()
{
    var detail_name = ("<p><h2>宝贝名称："+ pet['name'] +"</h2>");
    var n = 0;
    var detail_nature = ("<p><h2>属性： ");
    for(n = 0 ; n < pet['natures'] ; n++)
        detail_nature += (pet['nature'] + ' ');
    detail_nature += "</h2>"
    var detail_cost = ("<p><h2>日消耗："+ pet['basic_cost'] +"</h2>");
    var detail_text = detail_name + detail_nature + detail_cost;
    $(".detail-container").text(detail_text);
}