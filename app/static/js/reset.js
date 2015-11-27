function reset()
{
    $("input").each(function () {
        $(this).val("value", "");
    });
}