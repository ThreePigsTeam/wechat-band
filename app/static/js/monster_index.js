window.onscroll = function(){
    var ScrT = document.body.scrollTop;
    var CliH = document.body.clientHeight;
    var ScrH = document.body.scrollHeight;
    if(ScrT >=ScrH - CliH - 1000)
    {
        AddPhotoGrid("ul1");
        InsertPhotoGrid();
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

var maxPics = 700;
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
    number.style ="margin-top:0.5px;margin-bottom:0px;color:red;text-align:right;font-weight:bold;";
    var photo = document.createElement("img");
    if(order < 10){
    photo.src = "img/fetch_picture/00" + order +".png";
    photo.alt = "pic"+ order;
    }
    else if(order < 100){
    photo.src = "img/fetch_picture/0" + order +".png";
    photo.alt = "pic"+ order;
    }
    else{
        photo.src = "img/fetch_picture/" + order +".png";
        photo.alt = "pic"+ order;
    }
    var info = document.createElement("info");
    li.appendChild(photo);
    li.appendChild(info);
    document.getElementById(elem).appendChild(li);
}

//將圖片格插入Column中
function InsertPhotoGrid()
{
    var ulgrids= new Array();
    var containerHeight = 0;
    for(i = 0 ; i < 2 ; i++)
    {
        ulgrids[i] = document.getElementById("ul" + (i + 1));
        if(ulgrids[i].clientHeight > containerHeight)
            containerHeight = ulgrids[i].clientHeight;
    }
            for(i = 0 ; i < 2 ; i++)
            {
            while(ulgrids[i].clientHeight < containerHeight )
            {
                if(pics >= maxPics)
                    return;
                AddPhotoGrid("ul"+ (i + 1));
                }
            }
}


