/**
 * Created by tarena on 18-10-17.
 */
function escapeChars(str) {
    str1 = str.replace(/&amp;/g, '&');
    str1 = str1.replace(/&lt;/g, '<');
    str1 = str1.replace(/&gt;/g, '>');
    str1 = str1.replace(/&acute;/g, "'");
    str1 = str1.replace(/&quot;/g, '"');
    str1 = str1.replace(/&brvbar;/g, '\|');
    return str1;
}

$(function(){
    var cont = $("#main").html();
    var cont1 = escapeChars(cont);
    $('#main').html(cont1);
});