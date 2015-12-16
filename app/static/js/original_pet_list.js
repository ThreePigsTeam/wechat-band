window.onscroll = function(){
    var ScrT = document.body.scrollTop;
    var CliH = document.body.clientHeight;
    var ScrH = document.body.scrollHeight;
    if(ScrT >= ScrH - CliH)
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
    $(document).on('click','.pic-grid input[type="image"]',function()
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
    var inp =document.createElement("input");
    inp.setAttribute("type","hidden");
    inp.setAttribute("name","original_pet_id");
    inp.setAttribute("value", order);
    var photo = document.createElement("input");
    photo.setAttribute("type","image");
    if(order < 10){
    photo.src = u +"00"+ order +".png";
    photo.alt = "Submit";
    number.innerHTML = "#00" + order;
    }
    else if(order < 100){
    photo.src = u +"0"+ order +".png";
        photo.alt = "Submit";
    number.innerHTML = "#0" + order;
    }
    else{
        photo.src = u + order +".png";
        photo.alt = "Submit";
        number.innerHTML = "#" + order;
    }
    li.appendChild(number);
    li.appendChild(inp);
    li.appendChild(photo);
    document.getElementById(elem).appendChild(li);
}

function showDetail(pet, pet_stages, image_url)
{
    var detail_name = ("<p><h2>宝贝名称："+ pet['name'] +"</h2>");
    var n = 0;
    var detail_nature = ("<p><h2>属性： ");
    for(n = 0 ; n < pet['natures'] ; n++)
        detail_nature += (pet['nature'] + ' ');
    detail_nature += "</h2>"
    var detail_cost = ("<p><h2>日消耗："+ pet['basic_cost'] +"</h2>");
    var detail_stages = ("<p><h2>进化路线： ");
    for(n = 0 ; n < pet['pet_stages']; n++)
        detail_stages += "<h4>" +  pet['name'] + "</h4>"+"<img class='img-responsive' src='" +image_url+ pet['picture'] +">";

    $(".detail-container").append(detail_name);
    $(".detail-container").append(detail_nature);
    $(".detail-container").append(detail_cost);
    $(".detail-container").append(detail_stages);
}