function news_message() {
    $.ajax({
        url:"/index/news_message/",
        type:"post",
        data:{
            page:1,
        },
        async:false,
        dataType:"json",
        success:function (data) {
            var html = '';
            var history = JSON.parse(data.history);
            var count = JSON.parse(data.count);
            var page_num = JSON.parse(data.page_num);

            $.each(history,function (i,obj) {
                var img = '/static/img/'+(Math.floor(Math.random()*462+1)).toString()+'.jpg';
                html += '<table class="content"><tr>';
                html += '<td rowspan="4"><a href="/details/news_message/?id='+obj._id['$oid']+'" target="_blank"><img src="'+img+'"></a></td>';
                html += '<td class="title" rowspan="3">';
                html += '<a href="/details/news_message/?id='+obj._id['$oid']+'" target="_blank">'+obj.newsname+'</a>';
                html += '</td></tr><tr></tr><tr></tr>';
                html += '<tr><td class="date">'+obj.newsdate+'</td></tr></table>';
            });
            $("#show").html(html);

            var html2 = '';
            html2 += '<span class="page-cur">1</span>';
            html2 += '<a class="page" href="/index/news_message/?page=2">2</a>';
            html2 += '<a class="page" href="/index/news_message/?page=3">3</a>';
            html2 += '<span class="page-split">...</span>';
            html2 += '<a class="page" href="/index/news_message/?page='+count+'">'+count+'</a>';
            html2 += '<a href="/index/news_message/?page=2" class="page-next">下一页</a>';
            html2 += '<span class="totalPage">共'+count+'页</span>';
            html2 += '<span class="text">去第</span>';
            html2 += '<input id="Jumper" value="1" name="page" type="text">';
            html2 += '<span class="text2">页</span>';
            html2 += '<a href="#" class="pageConfirm">确定</a>';
            $("#pagination-page").html(html2);

        }
    });
}