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
    li.setAttribute("id", "pet"+num);
    var number = document.createElement("h5");
    var inp =document.createElement("input");
    inp.setAttribute("type","hidden");
    inp.setAttribute("name","original_pet_id");
    inp.setAttribute("value", num);
    var photo = document.createElement("img");
    if(order < 10){
    photo.src = "{{ url_for('static', filename='img/pets/00" + order +".png') }}";
    photo.alt = "pic"+ order;
    number.innerHTML = "#00" + order;
    }
    else if(order < 100){
    photo.src = "{{ url_for('static', filename='img/pets/0" + order +".png') }}";
    photo.alt = "pic"+ order;
    number.innerHTML = "#0" + order;
    }
    else{
        photo.src = "{{ url_for('static', filename='img/pets/" + order +".png') }}";
        photo.alt = "pic"+ order;
        number.innerHTML = "#" + order;
    }
    li.appendChild(number);
    li.appendChild(photo);
    li.appendChild(inp);
    document.getElementById(elem).appendChild(li);
}

function showDetail()
{
    $(".detail-container").append(detailData);   
}