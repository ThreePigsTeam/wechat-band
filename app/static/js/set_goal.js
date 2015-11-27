function change(str) {
    var val = $(str).val();
    var opt = $('#option');
    if (val == "1" || val == "2" || val == "3") {
        opt.html("<label for='goal_distance'>目标完成距离(km)</label><input name='distance' id='goal_distance' class='form-control' type='number' value='0' min='0' style='width:100%;float:left;'/><label for='goal_time'>目标完成时间(min)</label><input name='duration' id='goal_time' class='form-control' type='number' value='0' min='0' style='width:100%;float:left;'>");
    }
    else {
        opt.html("<label for='goal_time'>目标完成时间(min)</label><input name='duration' id='goal_time' class='form-control' type='number' value='0' min='0' style='width:100%;float:left;'>");
    }
}